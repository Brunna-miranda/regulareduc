"""
Gera um arquivo SQL com todos os dados do SQLite para importar no Supabase SQL Editor.
Execute: python -X utf8 gerar_sql_migracao.py
Depois cole o conteúdo de 'migracao_dados.sql' no SQL Editor do Supabase e clique Run.
"""
import sqlite3, json
from pathlib import Path

conn = sqlite3.connect("regulatorio.db")
conn.row_factory = sqlite3.Row

def esc(val):
    if val is None:
        return "NULL"
    if isinstance(val, bool):
        return "TRUE" if val else "FALSE"
    if isinstance(val, (int, float)):
        return str(val)
    return "'" + str(val).replace("'", "''") + "'"

lines = []
lines.append("-- =============================================")
lines.append("-- MIGRAÇÃO: SQLite → Supabase")
lines.append("-- Execute no SQL Editor do Supabase (Dashboard > SQL Editor)")
lines.append("-- =============================================")
lines.append("")

# 1. Redes
lines.append("-- 1. REDES")
redes = conn.execute("SELECT id, nome FROM redes ORDER BY id").fetchall()
redes_map = {}
if redes:
    lines.append("INSERT INTO redes (nome) VALUES")
    vals = [f"  ({esc(r['nome'])})" for r in redes]
    lines.append(",\n".join(vals))
    lines.append("ON CONFLICT DO NOTHING RETURNING id, nome;")
lines.append("")

# 2. Escolas — via subquery de rede
lines.append("-- 2. ESCOLAS")
escolas = conn.execute("""
    SELECT e.nome, r.nome AS rede_nome, e.cnpj, e.inscricao_municipal,
           e.estado, e.o_que_funciona, e.observacoes, e.ativa
    FROM escolas e LEFT JOIN redes r ON r.id = e.rede_id
    WHERE e.ativa = 1 ORDER BY e.id
""").fetchall()
escola_map = {}
for e in escolas:
    rede_subq = f"(SELECT id FROM redes WHERE nome = {esc(e['rede_nome'])} LIMIT 1)" if e['rede_nome'] else "NULL"
    lines.append(f"INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)")
    lines.append(f"  VALUES ({esc(e['nome'])}, {rede_subq}, {esc(e['cnpj'])}, {esc(e['inscricao_municipal'])},")
    lines.append(f"          {esc(e['estado'] or 'RJ')}, {esc(e['o_que_funciona'])}, {esc(e['observacoes'])}, TRUE)")
    lines.append(f"ON CONFLICT DO NOTHING;")
lines.append("")

# 3. Tipos de documentos
lines.append("-- 3. TIPOS DE DOCUMENTOS")
tipos_doc = conn.execute("SELECT nome, alerta_dias FROM tipos_documentos ORDER BY id").fetchall()
if tipos_doc:
    lines.append("INSERT INTO tipos_documentos (nome, alerta_dias) VALUES")
    vals = [f"  ({esc(t['nome'])}, {t['alerta_dias'] or 60})" for t in tipos_doc]
    lines.append(",\n".join(vals))
    lines.append("ON CONFLICT (nome) DO NOTHING;")
lines.append("")

# 4. Documentos
lines.append("-- 4. DOCUMENTOS")
docs = conn.execute("""
    SELECT e.nome AS escola_nome, t.nome AS tipo_nome,
           d.status, d.data_vencimento, d.observacoes
    FROM documentos d
    JOIN escolas e ON e.id = d.escola_id
    JOIN tipos_documentos t ON t.id = d.tipo_id
    WHERE e.ativa = 1 ORDER BY d.id
""").fetchall()
for d in docs:
    escola_subq = f"(SELECT id FROM escolas WHERE nome = {esc(d['escola_nome'])} LIMIT 1)"
    lines.append(f"INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)")
    lines.append(f"  VALUES ({escola_subq}, {esc(d['tipo_nome'])},")
    lines.append(f"          {esc(d['status'] or 'desconhecido')}, {esc(d['data_vencimento'])}, {esc(d['observacoes'])})")
    lines.append(f"ON CONFLICT DO NOTHING;")
lines.append("")

# 5. Processos SEI
lines.append("-- 5. PROCESSOS SEI")
procs = conn.execute("""
    SELECT p.numero, p.forma_exigencia, p.data_recebimento, p.prazo, p.status, p.observacoes,
           e.nome AS escola_nome
    FROM processos_sei p LEFT JOIN escolas e ON e.id = p.escola_id
    ORDER BY p.id
""").fetchall()
for p in procs:
    escola_subq = f"(SELECT id FROM escolas WHERE nome = {esc(p['escola_nome'])} LIMIT 1)" if p['escola_nome'] else "NULL"
    lines.append(f"INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)")
    lines.append(f"  VALUES ({esc(p['numero'])}, {escola_subq}, {esc(p['forma_exigencia'])},")
    lines.append(f"          {esc(p['data_recebimento'])}, {esc(p['prazo'])}, {esc(p['status'] or 'aberto')}, {esc(p['observacoes'])})")
    lines.append(f"ON CONFLICT DO NOTHING;")
lines.append("")

# 6. Tipos de processo (defaults)
lines.append("-- 6. TIPOS DE PROCESSO")
tipos_proc = [
    ("Autorização de Funcionamento", 1), ("Renovação de Autorização", 2),
    ("Renovação de Alvará", 3), ("Renovação — Licença Sanitária", 4),
    ("AVCB — Corpo de Bombeiros", 5), ("Laudo Técnico CREA", 6),
    ("Habite-se", 7), ("Transferência de Mantenedora", 8),
    ("Recredenciamento MEC", 9), ("Censo Escolar INEP", 10),
    ("Regularização Fiscal", 11), ("Processo Administrativo", 12), ("Outro", 13),
]
lines.append("INSERT INTO tipos_processo (nome, ordem) VALUES")
vals = [f"  ({esc(n)}, {o})" for n, o in tipos_proc]
lines.append(",\n".join(vals))
lines.append("ON CONFLICT DO NOTHING;")
lines.append("")

# 7. Usuário padrão (app) - requer que o auth.user já exista
lines.append("-- 7. USUÁRIO PADRÃO DA PLATAFORMA")
lines.append("-- Execute após criar o usuário no Supabase Authentication:")
lines.append("INSERT INTO usuarios_app (nome, cargo, email, setor, ativo)")
lines.append("  VALUES ('Brunna Miranda', 'Gestora Regulatória', 'brunna@raiz.edu.br', 'Regulatório', TRUE)")
lines.append("ON CONFLICT DO NOTHING;")
lines.append("")

lines.append("-- =============================================")
lines.append("-- MIGRAÇÃO CONCLUÍDA")
lines.append(f"-- {len(redes)} redes | {len(escolas)} escolas | {len(docs)} documentos | {len(procs)} processos")
lines.append("-- =============================================")

conn.close()

sql = "\n".join(lines)
out = Path("migracao_dados.sql")
out.write_text(sql, encoding="utf-8")
print(f"Gerado: migracao_dados.sql ({len(sql)//1024} KB)")
print(f"  {len(redes)} redes")
print(f"  {len(escolas)} escolas")
print(f"  {len(docs)} documentos")
print(f"  {len(procs)} processos SEI")
print()
print("PRÓXIMO PASSO:")
print("  1. Abra o Supabase Dashboard → SQL Editor → New query")
print("  2. Cole o conteúdo de migracao_dados.sql")
print("  3. Clique Run")
