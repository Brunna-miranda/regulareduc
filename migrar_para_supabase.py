"""
Migra dados do SQLite (regulatorio.db) para o Supabase.
Execute APÓS criar o schema no SQL Editor do Supabase.

Uso:
  pip install supabase
  python migrar_para_supabase.py
"""
import sqlite3, json, os

# ── CONFIGURAR ANTES DE RODAR ─────────────────────────────────────────────────
SUPABASE_URL = "https://ruirdarbiftvnducmfxt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1aXJkYXJiaWZ0dm5kdWNtZnh0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODEyODk0MzcsImV4cCI6MjA5Njg2NTQzN30.XznYUuv30VAW6jtH3leuaFFlOZC_ViMOCU1wGZnUJd8"
# ─────────────────────────────────────────────────────────────────────────────

def main():
    try:
        from supabase import create_client
    except ImportError:
        print("Instalando supabase...")
        os.system("pip install supabase -q")
        from supabase import create_client

    if "COLE_AQUI" in SUPABASE_URL:
        print("❌ Configure SUPABASE_URL e SUPABASE_KEY no arquivo antes de rodar!")
        return

    sb = create_client(SUPABASE_URL, SUPABASE_KEY)
    conn = sqlite3.connect("regulatorio.db")
    conn.row_factory = sqlite3.Row

    print("Conectado ao Supabase e SQLite.")

    # 1. Redes
    print("\n[1/6] Migrando redes...")
    redes = conn.execute("SELECT id, nome FROM redes ORDER BY id").fetchall()
    redes_map = {}
    for r in redes:
        res = sb.table("redes").upsert({"nome": r["nome"]}).execute()
        redes_map[r["id"]] = res.data[0]["id"]
        print(f"  ✓ {r['nome']}")

    # 2. Escolas
    print("\n[2/6] Migrando escolas...")
    escolas = conn.execute("SELECT * FROM escolas WHERE ativa=1").fetchall()
    escola_map = {}
    for e in escolas:
        rede_id_novo = redes_map.get(e["rede_id"])
        data = {
            "nome": e["nome"], "rede_id": rede_id_novo,
            "cnpj": e["cnpj"], "inscricao_municipal": e["inscricao_municipal"],
            "estado": e["estado"] or "RJ", "o_que_funciona": e["o_que_funciona"],
            "ativa": True,
        }
        res = sb.table("escolas").upsert(data).execute()
        escola_map[e["id"]] = res.data[0]["id"]
    print(f"  ✓ {len(escola_map)} escolas migradas")

    # 3. Tipos de documentos
    print("\n[3/6] Migrando tipos de documentos...")
    tipos = conn.execute("SELECT id, nome, alerta_dias FROM tipos_documentos").fetchall()
    tipo_map = {}
    for t in tipos:
        res = sb.table("tipos_documentos").upsert({"nome": t["nome"], "alerta_dias": t["alerta_dias"] or 60}).execute()
        tipo_map[t["id"]] = res.data[0]["id"]
    print(f"  ✓ {len(tipo_map)} tipos migrados")

    # 4. Documentos
    print("\n[4/6] Migrando documentos...")
    docs = conn.execute("SELECT * FROM documentos").fetchall()
    count = 0
    for d in docs:
        escola_id_novo = escola_map.get(d["escola_id"])
        if not escola_id_novo:
            continue
        data = {
            "escola_id": escola_id_novo,
            "tipo": conn.execute("SELECT nome FROM tipos_documentos WHERE id=?", (d["tipo_id"],)).fetchone()["nome"],
            "status": d["status"] or "desconhecido",
            "data_vencimento": d["data_vencimento"],
            "observacoes": d["observacoes"],
        }
        sb.table("documentos").insert(data).execute()
        count += 1
    print(f"  ✓ {count} documentos migrados")

    # 5. Processos SEI
    print("\n[5/6] Migrando processos SEI...")
    procs = conn.execute("SELECT * FROM processos_sei").fetchall()
    proc_map = {}
    for p in procs:
        escola_id_novo = escola_map.get(p["escola_id"]) if p["escola_id"] else None
        data = {
            "escola_id": escola_id_novo,
            "numero": p["numero"],
            "forma_exigencia": p["forma_exigencia"],
            "data_recebimento": p["data_recebimento"],
            "prazo": p["prazo"],
            "status": p["status"] or "aberto",
            "observacoes": p["observacoes"],
        }
        res = sb.table("processos_sei").insert(data).execute()
        proc_map[p["id"]] = res.data[0]["id"]
    print(f"  ✓ {len(proc_map)} processos migrados")

    # 6. Tipos de processo
    print("\n[6/6] Migrando tipos de processo...")
    tipos_proc = ["Autorização de Funcionamento","Renovação de Autorização","Renovação de Alvará",
        "Renovação — Licença Sanitária","AVCB — Corpo de Bombeiros","Laudo Técnico CREA",
        "Habite-se","Transferência de Mantenedora","Recredenciamento MEC",
        "Censo Escolar INEP","Regularização Fiscal","Processo Administrativo","Outro"]
    for i, t in enumerate(tipos_proc, 1):
        sb.table("tipos_processo").upsert({"nome": t, "ordem": i}).execute()
    print(f"  ✓ {len(tipos_proc)} tipos de processo")

    conn.close()
    print("\n✅ Migração concluída com sucesso!")
    print("\nPróximo passo: configure as credenciais no regulareduc.html e faça o deploy.")

if __name__ == "__main__":
    main()
