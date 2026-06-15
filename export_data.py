import sqlite3, json
from collections import Counter

conn = sqlite3.connect('regulatorio.db')
conn.row_factory = sqlite3.Row

schools = conn.execute("""
    SELECT e.id, e.nome, e.cnpj, e.inscricao_municipal, e.estado,
           e.o_que_funciona, r.nome AS rede,
           SUM(CASE WHEN d.status IN ('vencido','pendente') THEN 1 ELSE 0 END) AS criticos,
           SUM(CASE WHEN d.status = 'a_vencer' THEN 1 ELSE 0 END) AS a_vencer,
           SUM(CASE WHEN d.status = 'ok' THEN 1 ELSE 0 END) AS ok_docs,
           COUNT(CASE WHEN d.status != 'nao_aplicavel' THEN 1 END) AS total_docs
    FROM escolas e
    LEFT JOIN redes r ON r.id = e.rede_id
    LEFT JOIN documentos d ON d.escola_id = e.id
    WHERE e.ativa = 1
    GROUP BY e.id ORDER BY r.nome, e.nome
""").fetchall()

docs = conn.execute("""
    SELECT d.id, e.nome AS escola, e.id AS escola_id, r.nome AS rede, e.estado,
           t.nome AS tipo, d.status, d.data_vencimento, d.observacoes
    FROM documentos d
    JOIN escolas e ON e.id = d.escola_id
    JOIN redes r ON r.id = e.rede_id
    JOIN tipos_documentos t ON t.id = d.tipo_id
    WHERE e.ativa = 1
    ORDER BY d.data_vencimento ASC
""").fetchall()

procs = conn.execute("""
    SELECT p.id, p.numero, p.forma_exigencia, p.data_recebimento,
           p.prazo, p.status, p.observacoes,
           COALESCE(e.nome, '') AS escola,
           COALESCE(e.id, 0) AS escola_id,
           COALESCE(r.nome, '') AS rede
    FROM processos_sei p
    LEFT JOIN escolas e ON e.id = p.escola_id
    LEFT JOIN redes r ON r.id = e.rede_id
    ORDER BY p.status, p.prazo
""").fetchall()

redes = conn.execute("SELECT id, nome FROM redes ORDER BY nome").fetchall()

data = {
    'schools': [dict(s) for s in schools],
    'docs':    [dict(d) for d in docs],
    'procs':   [dict(p) for p in procs],
    'redes':   [dict(r) for r in redes],
}

with open('data_export.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, default=str, indent=2)

print('Escolas:', len(data['schools']))
print('Documentos:', len(data['docs']))
print('Processos:', len(data['procs']))
print('Status docs:', dict(Counter(d['status'] for d in data['docs'])))
print('Status procs:', dict(Counter(p['status'] for p in data['procs'])))
conn.close()
