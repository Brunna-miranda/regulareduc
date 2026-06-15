import sqlite3
import os
from pathlib import Path
from datetime import date, datetime

DB_PATH = Path(__file__).parent / "regulatorio.db"

TIPOS_DOCS = [
    ("Licença Sanitária", 60),
    ("Ato Autorizativo - Sec. Educação", 365),
    ("PAA", 365),
    ("ETAP", 365),
    ("Habite-se", 0),
    ("Corpo de Bombeiros", 365),
    ("Alvará de Funcionamento", 365),
    ("Vigilância Sanitária", 365),
    ("Regimento Interno", 365),
    ("PPP", 365),
]

STATUS_LABELS = {
    "ok": "✅ OK",
    "a_vencer": "⚠️ A vencer",
    "vencido": "🔴 Vencido",
    "pendente": "❌ Pendente",
    "nao_aplicavel": "—",
    "desconhecido": "❓ Desconhecido",
}

STATUS_COLORS = {
    "ok": "#22c55e",
    "a_vencer": "#f59e0b",
    "vencido": "#ef4444",
    "pendente": "#ef4444",
    "nao_aplicavel": "#94a3b8",
    "desconhecido": "#cbd5e1",
}


def get_conn():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE IF NOT EXISTS redes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            rede_id INTEGER REFERENCES redes(id),
            cnpj TEXT,
            inscricao_municipal TEXT,
            estado TEXT DEFAULT 'RJ',
            o_que_funciona TEXT,
            observacoes TEXT,
            ativa INTEGER DEFAULT 1,
            criada_em TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS tipos_documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            alerta_dias INTEGER DEFAULT 60
        );

        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            escola_id INTEGER NOT NULL REFERENCES escolas(id),
            tipo_id INTEGER NOT NULL REFERENCES tipos_documentos(id),
            status TEXT DEFAULT 'desconhecido',
            data_vencimento TEXT,
            observacoes TEXT,
            arquivo_nome TEXT,
            arquivo_path TEXT,
            atualizado_em TEXT DEFAULT (datetime('now')),
            UNIQUE(escola_id, tipo_id)
        );

        CREATE TABLE IF NOT EXISTS processos_sei (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            escola_id INTEGER REFERENCES escolas(id),
            numero TEXT NOT NULL,
            forma_exigencia TEXT,
            data_recebimento TEXT,
            prazo TEXT,
            status TEXT DEFAULT 'aberto',
            observacoes TEXT,
            criado_em TEXT DEFAULT (datetime('now')),
            atualizado_em TEXT DEFAULT (datetime('now'))
        );
    """)

    for nome, alerta_dias in TIPOS_DOCS:
        c.execute(
            "INSERT OR IGNORE INTO tipos_documentos (nome, alerta_dias) VALUES (?, ?)",
            (nome, alerta_dias),
        )

    conn.commit()
    conn.close()


def has_data():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM escolas")
    count = c.fetchone()[0]
    conn.close()
    return count > 0


def get_dashboard_stats():
    conn = get_conn()
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM escolas WHERE ativa = 1")
    total_escolas = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM documentos WHERE status IN ('vencido', 'pendente')")
    docs_criticos = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM processos_sei WHERE status = 'aberto'")
    processos_abertos = c.fetchone()[0]

    today = date.today().isoformat()
    in_30 = date.today().replace(day=date.today().day).__class__.fromisoformat(today)
    from datetime import timedelta
    limit_30 = (date.today() + timedelta(days=30)).isoformat()

    c.execute(
        """SELECT COUNT(*) FROM documentos
           WHERE status = 'a_vencer' AND data_vencimento <= ?""",
        (limit_30,),
    )
    alertas_30 = c.fetchone()[0]

    conn.close()
    return {
        "total_escolas": total_escolas,
        "docs_criticos": docs_criticos,
        "processos_abertos": processos_abertos,
        "alertas_30": alertas_30,
    }


def get_status_por_rede():
    conn = get_conn()
    import pandas as pd

    df = pd.read_sql_query(
        """
        SELECT r.nome AS rede,
               d.status,
               COUNT(*) AS total
        FROM documentos d
        JOIN escolas e ON e.id = d.escola_id
        JOIN redes r ON r.id = e.rede_id
        WHERE e.ativa = 1 AND d.status != 'nao_aplicavel'
        GROUP BY r.nome, d.status
        """,
        conn,
    )
    conn.close()
    return df


def get_processos_urgentes():
    conn = get_conn()
    import pandas as pd

    df = pd.read_sql_query(
        """
        SELECT p.numero, p.forma_exigencia, p.data_recebimento, p.prazo, p.status,
               e.nome AS escola
        FROM processos_sei p
        LEFT JOIN escolas e ON e.id = p.escola_id
        WHERE p.status = 'aberto'
        ORDER BY p.prazo ASC
        LIMIT 10
        """,
        conn,
    )
    conn.close()
    return df


def get_vencimentos_proximos(dias=30):
    conn = get_conn()
    import pandas as pd
    from datetime import timedelta

    limite = (date.today() + timedelta(days=dias)).isoformat()
    today = date.today().isoformat()

    df = pd.read_sql_query(
        """
        SELECT e.nome AS escola, r.nome AS rede, t.nome AS documento,
               d.status, d.data_vencimento
        FROM documentos d
        JOIN escolas e ON e.id = d.escola_id
        JOIN redes r ON r.id = e.rede_id
        JOIN tipos_documentos t ON t.id = d.tipo_id
        WHERE d.data_vencimento IS NOT NULL
          AND d.data_vencimento <= ?
          AND e.ativa = 1
        ORDER BY d.data_vencimento ASC
        """,
        conn,
        params=(limite,),
    )
    conn.close()
    return df


def get_escolas(rede_id=None, estado=None, apenas_ativas=True):
    conn = get_conn()
    import pandas as pd

    query = """
        SELECT e.id, e.nome, r.nome AS rede, e.cnpj, e.inscricao_municipal,
               e.estado, e.o_que_funciona, e.ativa,
               SUM(CASE WHEN d.status IN ('vencido','pendente') THEN 1 ELSE 0 END) AS docs_criticos,
               SUM(CASE WHEN d.status = 'a_vencer' THEN 1 ELSE 0 END) AS docs_a_vencer,
               SUM(CASE WHEN d.status = 'ok' THEN 1 ELSE 0 END) AS docs_ok,
               COUNT(CASE WHEN d.status != 'nao_aplicavel' THEN 1 END) AS docs_total
        FROM escolas e
        LEFT JOIN redes r ON r.id = e.rede_id
        LEFT JOIN documentos d ON d.escola_id = e.id
        WHERE 1=1
    """
    params = []
    if rede_id:
        query += " AND e.rede_id = ?"
        params.append(rede_id)
    if estado:
        query += " AND e.estado = ?"
        params.append(estado)
    if apenas_ativas:
        query += " AND e.ativa = 1"
    query += " GROUP BY e.id ORDER BY r.nome, e.nome"

    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


def get_documentos_escola(escola_id):
    conn = get_conn()
    import pandas as pd

    df = pd.read_sql_query(
        """
        SELECT d.id, t.nome AS tipo, d.status, d.data_vencimento,
               d.observacoes, d.arquivo_nome, d.atualizado_em
        FROM tipos_documentos t
        LEFT JOIN documentos d ON d.tipo_id = t.id AND d.escola_id = ?
        ORDER BY t.id
        """,
        conn,
        params=(escola_id,),
    )
    conn.close()
    return df


def get_redes():
    conn = get_conn()
    import pandas as pd

    df = pd.read_sql_query("SELECT id, nome FROM redes ORDER BY nome", conn)
    conn.close()
    return df


def get_processos(escola_id=None, status=None):
    conn = get_conn()
    import pandas as pd

    query = """
        SELECT p.id, p.numero, p.forma_exigencia, p.data_recebimento, p.prazo,
               p.status, p.observacoes, p.criado_em,
               e.nome AS escola
        FROM processos_sei p
        LEFT JOIN escolas e ON e.id = p.escola_id
        WHERE 1=1
    """
    params = []
    if escola_id:
        query += " AND p.escola_id = ?"
        params.append(escola_id)
    if status:
        query += " AND p.status = ?"
        params.append(status)
    query += " ORDER BY p.prazo ASC, p.criado_em DESC"

    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


def upsert_documento(escola_id, tipo_id, status, data_vencimento=None,
                     observacoes=None, arquivo_nome=None, arquivo_path=None):
    conn = get_conn()
    conn.execute(
        """
        INSERT INTO documentos (escola_id, tipo_id, status, data_vencimento,
                                observacoes, arquivo_nome, arquivo_path, atualizado_em)
        VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
        ON CONFLICT(escola_id, tipo_id) DO UPDATE SET
            status = excluded.status,
            data_vencimento = excluded.data_vencimento,
            observacoes = excluded.observacoes,
            arquivo_nome = COALESCE(excluded.arquivo_nome, arquivo_nome),
            arquivo_path = COALESCE(excluded.arquivo_path, arquivo_path),
            atualizado_em = datetime('now')
        """,
        (escola_id, tipo_id, status, data_vencimento, observacoes, arquivo_nome, arquivo_path),
    )
    conn.commit()
    conn.close()


def save_processo(escola_id, numero, forma_exigencia, data_recebimento,
                  prazo, status, observacoes, processo_id=None):
    conn = get_conn()
    now = datetime.now().isoformat()
    if processo_id:
        conn.execute(
            """UPDATE processos_sei SET escola_id=?, numero=?, forma_exigencia=?,
               data_recebimento=?, prazo=?, status=?, observacoes=?, atualizado_em=?
               WHERE id=?""",
            (escola_id, numero, forma_exigencia, data_recebimento,
             prazo, status, observacoes, now, processo_id),
        )
    else:
        conn.execute(
            """INSERT INTO processos_sei
               (escola_id, numero, forma_exigencia, data_recebimento, prazo, status, observacoes, criado_em, atualizado_em)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (escola_id, numero, forma_exigencia, data_recebimento,
             prazo, status, observacoes, now, now),
        )
    conn.commit()
    conn.close()


def save_escola(nome, rede_id, cnpj, inscricao_municipal, estado,
                o_que_funciona, observacoes, escola_id=None):
    conn = get_conn()
    if escola_id:
        conn.execute(
            """UPDATE escolas SET nome=?, rede_id=?, cnpj=?, inscricao_municipal=?,
               estado=?, o_que_funciona=?, observacoes=? WHERE id=?""",
            (nome, rede_id, cnpj, inscricao_municipal, estado,
             o_que_funciona, observacoes, escola_id),
        )
    else:
        conn.execute(
            """INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes),
        )
    conn.commit()
    conn.close()


def get_tipos_documentos():
    conn = get_conn()
    import pandas as pd
    df = pd.read_sql_query("SELECT id, nome, alerta_dias FROM tipos_documentos ORDER BY id", conn)
    conn.close()
    return df
