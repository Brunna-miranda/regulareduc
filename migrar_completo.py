"""
Migração completa: SQLite → Supabase (usa service_role key para bypasear RLS).
Execute: python -X utf8 migrar_completo.py
"""
import sqlite3, json, sys, time
from pathlib import Path

SUPABASE_URL     = "https://ruirdarbiftvnducmfxt.supabase.co"
SUPABASE_SRV_KEY = "COLE_AQUI_A_SERVICE_ROLE_KEY"   # Settings → API → service_role

def main():
    if "COLE_AQUI" in SUPABASE_SRV_KEY:
        print("❌  Configure SUPABASE_SRV_KEY antes de rodar!")
        return

    try:
        from supabase import create_client
    except ImportError:
        import subprocess; subprocess.run([sys.executable,"-m","pip","install","supabase","-q"])
        from supabase import create_client

    sb  = create_client(SUPABASE_URL, SUPABASE_SRV_KEY)
    db  = sqlite3.connect("regulatorio.db")
    db.row_factory = sqlite3.Row

    def insert(table, data, label=""):
        if not data: return []
        r = sb.table(table).upsert(data).execute()
        print(f"  ✓ {table}: {len(data)} registros  {label}")
        return r.data or []

    def clear(table):
        sb.table(table).delete().neq("id", 0).execute()

    print("=" * 55)
    print("  Migração SQLite → Supabase")
    print("=" * 55)

    # ── 1. Redes ──────────────────────────────────────────────
    print("\n[1/7] Redes")
    clear("redes")
    redes_rows = db.execute("SELECT id, nome FROM redes ORDER BY id").fetchall()
    redes_data = [{"id": r["id"], "nome": r["nome"]} for r in redes_rows]
    redes_ins  = insert("redes", redes_data)
    # mapa id_old → id_new (se Supabase mantiver BIGSERIAL pode ser diferente)
    redes_map  = {r["id"]: r["id"] for r in redes_rows}  # assume ids iguais no upsert

    # ── 2. Escolas ────────────────────────────────────────────
    print("\n[2/7] Escolas")
    clear("escolas")
    escolas_rows = db.execute("""
        SELECT e.id, e.nome, e.rede_id, e.cnpj, e.inscricao_municipal,
               COALESCE(e.estado,'RJ') AS estado, e.o_que_funciona,
               e.observacoes, e.ativa
        FROM escolas e WHERE e.ativa = 1 ORDER BY e.id
    """).fetchall()
    escolas_data = [{
        "id": e["id"], "nome": e["nome"],
        "rede_id": redes_map.get(e["rede_id"]),
        "cnpj": e["cnpj"], "inscricao_municipal": e["inscricao_municipal"],
        "estado": e["estado"], "o_que_funciona": e["o_que_funciona"],
        "observacoes": e["observacoes"], "ativa": bool(e["ativa"]),
        "status_unidade": "em_funcionamento",
    } for e in escolas_rows]
    insert("escolas", escolas_data)
    escola_map = {e["id"]: e["id"] for e in escolas_rows}

    # ── 3. Tipos de documento ─────────────────────────────────
    print("\n[3/7] Tipos de documento")
    clear("tipos_documentos")
    tipos_rows = db.execute(
        "SELECT id, nome, alerta_dias FROM tipos_documentos ORDER BY id"
    ).fetchall()
    insert("tipos_documentos", [
        {"id": t["id"], "nome": t["nome"], "alerta_dias": t["alerta_dias"] or 60}
        for t in tipos_rows
    ])
    tipo_map = {t["id"]: t["nome"] for t in tipos_rows}

    # ── 4. Documentos ─────────────────────────────────────────
    print("\n[4/7] Documentos")
    clear("documentos")
    docs_rows = db.execute("""
        SELECT d.id, d.escola_id, d.tipo_id, d.status,
               d.data_vencimento, d.observacoes
        FROM documentos d
        JOIN escolas e ON e.id = d.escola_id WHERE e.ativa = 1
        ORDER BY d.id
    """).fetchall()
    docs_data = [{
        "id": d["id"],
        "escola_id": escola_map.get(d["escola_id"]),
        "tipo": tipo_map.get(d["tipo_id"], "Desconhecido"),
        "status": d["status"] or "desconhecido",
        "data_vencimento": d["data_vencimento"],
        "observacoes": d["observacoes"],
    } for d in docs_rows if escola_map.get(d["escola_id"])]
    insert("documentos", docs_data)

    # ── 5. Processos SEI ──────────────────────────────────────
    print("\n[5/7] Processos SEI")
    clear("processos_sei")

    # Criar escola-placeholder para processos sem escola vinculada
    rede_geral = sb.table("redes").upsert({"nome": "Geral"}).execute().data[0]
    escola_placeholder = sb.table("escolas").upsert({
        "nome": "— Sem escola vinculada —",
        "rede_id": rede_geral["id"], "estado": "RJ",
        "ativa": True, "status_unidade": "em_funcionamento"
    }).execute().data[0]
    placeholder_id = escola_placeholder["id"]
    procs_rows = db.execute("""
        SELECT p.id, p.escola_id, p.numero, p.forma_exigencia,
               p.data_recebimento, p.prazo, p.status, p.observacoes
        FROM processos_sei p ORDER BY p.id
    """).fetchall()
    import re
    def extrai_data(texto):
        """Extrai data ISO de texto livre como 'recebido por email em 14/04/2025'."""
        if not texto: return None
        m = re.search(r'(\d{2})/(\d{2})/(\d{4})', str(texto))
        if m: return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
        m2 = re.search(r'(\d{4})-(\d{2})-(\d{2})', str(texto))
        if m2: return m2.group(0)
        return None

    procs_data = [{
        "id": p["id"],
        "escola_id": escola_map.get(p["escola_id"]) if p["escola_id"] else placeholder_id,
        "numero": p["numero"],
        "forma_exigencia": p["forma_exigencia"],
        "data_recebimento": extrai_data(p["data_recebimento"]),
        "prazo": extrai_data(p["prazo"]),
        "status": p["status"] or "aberto",
        "observacoes": "\n".join(filter(None, [
            p["observacoes"],
            f"Recebimento original: {p['data_recebimento']}" if p["data_recebimento"] and not extrai_data(p["data_recebimento"]) else None,
            f"Prazo original: {p['prazo']}" if p["prazo"] and not extrai_data(p["prazo"]) else None,
        ])) or None,
    } for p in procs_rows]
    insert("processos_sei", procs_data)

    # ── 6. Tipos de processo ──────────────────────────────────
    print("\n[6/7] Tipos de processo")
    clear("tipos_processo")
    tipos_proc = [
        ("Autorização de Funcionamento", 1), ("Renovação de Autorização", 2),
        ("Renovação de Alvará", 3), ("Renovação — Licença Sanitária", 4),
        ("AVCB — Corpo de Bombeiros", 5), ("Laudo Técnico CREA", 6),
        ("Habite-se", 7), ("Transferência de Mantenedora", 8),
        ("Recredenciamento MEC", 9), ("Censo Escolar INEP", 10),
        ("Regularização Fiscal", 11), ("Processo Administrativo", 12), ("Outro", 13),
    ]
    insert("tipos_processo", [{"nome": n, "ordem": o} for n, o in tipos_proc])

    # ── 7. Usuário padrão ─────────────────────────────────────
    # usuarios_app requer auth.users — será criado automaticamente no primeiro login
    print("\n[7/7] Usuário padrão")
    print("  → Será criado automaticamente no primeiro login na plataforma")

    db.close()

    print("\n" + "=" * 55)
    print("  ✅ Migração concluída!")
    print(f"  {len(redes_data)} redes | {len(escolas_data)} escolas")
    print(f"  {len(docs_data)} documentos | {len(procs_data)} processos SEI")
    print("=" * 55)
    print("\nAcesse a plataforma e faça login:")
    print("  https://regulareduc.vercel.app")

if __name__ == "__main__":
    main()
