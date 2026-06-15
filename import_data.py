"""
Importa dados das planilhas Excel para o banco SQLite.
"""
import re
import sqlite3
import pandas as pd
from pathlib import Path
from datetime import date, datetime
from database import get_conn, DB_PATH

PLANILHA_RISCOS = r"C:\Users\brunna.miranda\Documents\Brunna\2025.03.20 - Planilha de Riscos Regulatório.xlsx"
PLANILHA_PENDENCIAS = r"C:\Users\brunna.miranda\Downloads\2025.01.07 - Regulatório - Status das Pendências.xlsx"
PLANILHA_ACOMPANHAMENTO = r"C:\Users\brunna.miranda\Downloads\2025.05.13 - Acompanhamento regulatório.xlsx"

TIPO_MAP = {
    "Licença Sanitária": 1,
    "Ato Autorizativo - Sec. Educação": 2,
    "PAA": 3,
    "ETAP": 4,
    "Habite-se": 5,
    "Corpo de Bombeiros": 6,
    "Alvará de Funcionamento": 7,
    "Vigilância Sanitária": 8,
    "Regimento Interno": 9,
    "PPP": 10,
}

# Mapeamento nomes abas → nomes de rede
REDES_TABS = {
    "QI": "QI",
    "QI Metropolitano": "QI Metropolitano",
    "Escolas integradas": "Escolas Integradas",
    "Ao Cubo": "Ao Cubo",
    "Matriz": "Matriz",
    "Global Tree": "Global Tree",
    "CLV": "CLV",
    "Americano": "Americano",
    "União": "União",
    "Raiz Educação": "Raiz Educação",
    "Apogeu": "Apogeu",
}

# Mapeamento estados por rede
ESTADOS_REDE = {
    "Apogeu": "MG",
    "CLV": "MG",
    "Americano": "RJ",
    "União": "RJ",
}


def parse_status_field(value, tipo_nome=""):
    """Parse campos de status como 'Sim. Vencimento: 30/04/2025'"""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "desconhecido", None

    text = str(value).strip()
    upper = text.upper()

    if "UNIDADE FECHADA" in upper:
        return "nao_aplicavel", None

    if upper.startswith("NÃO") or upper.startswith("NAO") or "NÃO POSSUI" in upper:
        return "pendente", None

    if upper.startswith("SIM") or upper.startswith("S/"):
        date_match = re.search(r"(\d{2}/\d{2}/\d{4})", text)
        if date_match:
            date_str = date_match.group(1)
            try:
                dt = datetime.strptime(date_str, "%d/%m/%Y").date()
                today = date.today()
                days_left = (dt - today).days
                if dt < today:
                    return "vencido", dt.isoformat()
                elif days_left <= 60:
                    return "a_vencer", dt.isoformat()
                else:
                    return "ok", dt.isoformat()
            except Exception:
                pass
        return "ok", None

    if upper.startswith("AGUARDANDO") or "AGUARD" in upper:
        return "a_vencer", None

    return "desconhecido", None


def get_or_create_rede(conn, nome):
    c = conn.cursor()
    c.execute("SELECT id FROM redes WHERE nome = ?", (nome,))
    row = c.fetchone()
    if row:
        return row[0]
    c.execute("INSERT INTO redes (nome) VALUES (?)", (nome,))
    conn.commit()
    return c.lastrowid


def get_or_create_escola(conn, nome, rede_id, cnpj=None, inscricao_municipal=None,
                          estado="RJ", o_que_funciona=None):
    c = conn.cursor()
    nome_clean = str(nome).strip() if nome else ""
    if not nome_clean or nome_clean.upper() == "NAN":
        return None
    c.execute("SELECT id FROM escolas WHERE nome = ? AND rede_id = ?", (nome_clean, rede_id))
    row = c.fetchone()
    if row:
        return row[0]
    c.execute(
        "INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona) VALUES (?,?,?,?,?,?)",
        (nome_clean, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona),
    )
    conn.commit()
    return c.lastrowid


def import_riscos(conn, progress_fn=None):
    """Importa da Planilha de Riscos Regulatório"""
    xls = pd.ExcelFile(PLANILHA_RISCOS)
    total_sheets = len(xls.sheet_names)

    for i, sheet_name in enumerate(xls.sheet_names):
        rede_nome = REDES_TABS.get(sheet_name, sheet_name)
        estado = ESTADOS_REDE.get(rede_nome, "RJ")
        rede_id = get_or_create_rede(conn, rede_nome)

        df = pd.read_excel(PLANILHA_RISCOS, sheet_name=sheet_name)
        df.columns = [str(c).strip() for c in df.columns]

        for _, row in df.iterrows():
            # Unidade
            nome_raw = row.get("Unidade ") or row.get("Unidade")
            if not nome_raw or str(nome_raw).strip().upper() in ("NAN", ""):
                continue

            cnpj = str(row.get("CNPJ", "")).strip() if pd.notna(row.get("CNPJ", "")) else None
            insc = str(row.get("Insc. Municipal", "")).strip() if pd.notna(row.get("Insc. Municipal", "")) else None
            funciona = str(row.get("O que funciona na escola ", "") or row.get("O que funciona na escola", "")).strip()
            funciona = funciona if funciona.upper() != "NAN" else None

            escola_id = get_or_create_escola(conn, nome_raw, rede_id, cnpj, insc, estado, funciona)
            if not escola_id:
                continue

            # Documentos
            col_licenca = next((c for c in df.columns if "Licença" in c or "Licen" in c), None)
            col_autorizativo = next((c for c in df.columns if "Autorizativo" in c or "Secretaria" in c), None)
            col_paa = next((c for c in df.columns if "PAA" in c), None)
            col_etap = next((c for c in df.columns if "ETAP" in c), None)

            doc_fields = [
                (col_licenca, 1),
                (col_autorizativo, 2),
                (col_paa, 3),
                (col_etap, 4),
            ]

            for col, tipo_id in doc_fields:
                if col and col in row.index:
                    status, data_venc = parse_status_field(row[col])
                    obs = str(row[col]).strip() if pd.notna(row.get(col)) else None
                    obs = obs if obs and obs.upper() != "NAN" else None
                    conn.execute(
                        """INSERT INTO documentos (escola_id, tipo_id, status, data_vencimento, observacoes)
                           VALUES (?, ?, ?, ?, ?)
                           ON CONFLICT(escola_id, tipo_id) DO UPDATE SET
                             status=excluded.status,
                             data_vencimento=excluded.data_vencimento,
                             observacoes=excluded.observacoes""",
                        (escola_id, tipo_id, status, data_venc, obs),
                    )

        conn.commit()
        if progress_fn:
            progress_fn((i + 1) / total_sheets, f"Importando rede: {rede_nome}")


def import_pendencias(conn, progress_fn=None):
    """Importa da planilha Status das Pendências"""
    df = pd.read_excel(PLANILHA_PENDENCIAS, sheet_name="Escolas", header=1)
    df = df.rename(columns={df.columns[0]: "estado", df.columns[1]: "escola"})
    df = df[df["escola"].notna() & (df["escola"].astype(str).str.strip() != "")]

    # Pares de colunas: (doc_nome, status_col_index)
    doc_cols = [
        ("Habite-se", 5, 6),
        ("Corpo de Bombeiros", 7, 8),
        ("Alvará de Funcionamento", 9, 10),
        ("Vigilância Sanitária", 11, 12),
        ("Parecer Secretaria de Educação", 13, 14),
        ("ETAP", 15, 16),
        ("Regimento Interno", 17, 18),
        ("PPP", 19, 20),
    ]

    tipo_id_map = {
        "Habite-se": 5,
        "Corpo de Bombeiros": 6,
        "Alvará de Funcionamento": 7,
        "Vigilância Sanitária": 8,
        "Parecer Secretaria de Educação": 2,
        "ETAP": 4,
        "Regimento Interno": 9,
        "PPP": 10,
    }

    total = len(df)
    for i, (_, row) in enumerate(df.iterrows()):
        escola_nome = str(row.iloc[1]).strip()
        estado = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else "RJ"

        # Encontrar escola no banco
        conn2 = get_conn()
        c = conn2.cursor()
        c.execute("SELECT id FROM escolas WHERE nome LIKE ?", (f"%{escola_nome}%",))
        result = c.fetchone()
        conn2.close()

        escola_id = result[0] if result else None

        if not escola_id:
            # Criar escola sem rede conhecida
            c2 = conn.cursor()
            c2.execute("SELECT id FROM redes WHERE nome = 'Outras'")
            r = c2.fetchone()
            if not r:
                c2.execute("INSERT INTO redes (nome) VALUES ('Outras')")
                conn.commit()
                rede_id = c2.lastrowid
            else:
                rede_id = r[0]
            escola_id = get_or_create_escola(conn, escola_nome, rede_id, estado=estado)

        if not escola_id:
            continue

        for doc_nome, val_idx, status_idx in doc_cols:
            tipo_id = tipo_id_map.get(doc_nome)
            if not tipo_id:
                continue

            status_val = row.iloc[status_idx] if status_idx < len(row) else None
            status, data_venc = parse_status_field(status_val)

            if status == "desconhecido":
                continue

            conn.execute(
                """INSERT INTO documentos (escola_id, tipo_id, status, data_vencimento)
                   VALUES (?, ?, ?, ?)
                   ON CONFLICT(escola_id, tipo_id) DO UPDATE SET
                     status=excluded.status,
                     data_vencimento=excluded.data_vencimento
                   WHERE documentos.status = 'desconhecido'""",
                (escola_id, tipo_id, status, data_venc),
            )

        if progress_fn:
            progress_fn((i + 1) / total, f"Importando escola: {escola_nome}")

    conn.commit()


def import_acompanhamento(conn, progress_fn=None):
    """Importa processos SEI do Acompanhamento Regulatório"""
    df = pd.read_excel(PLANILHA_ACOMPANHAMENTO)
    df = df.dropna(how="all")

    # Preenche escola para linhas sem escola (continuação da anterior)
    df["Unidades"] = df["Unidades"].ffill()

    total = len(df)
    for i, (_, row) in enumerate(df.iterrows()):
        numero = str(row.get("Processo", "")).strip()
        if not numero or numero.upper() == "NAN":
            continue

        escola_nome = str(row.get("Unidades", "")).strip()
        escola_id = None

        if escola_nome and escola_nome.upper() != "NAN":
            c = conn.cursor()
            c.execute("SELECT id FROM escolas WHERE nome LIKE ?", (f"%{escola_nome[:15]}%",))
            result = c.fetchone()
            if result:
                escola_id = result[0]

        forma = str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else None
        forma = forma if forma and forma.upper() != "NAN" else None

        data_rec = str(row.iloc[3]).strip() if pd.notna(row.iloc[3]) else None
        data_rec = data_rec if data_rec and data_rec.upper() != "NAN" else None

        prazo_raw = str(row.iloc[4]).strip() if pd.notna(row.iloc[4]) else None
        prazo = prazo_raw if prazo_raw and prazo_raw.upper() != "NAN" else None

        obs = str(row.iloc[5]).strip() if len(row) > 5 and pd.notna(row.iloc[5]) else None
        obs = obs if obs and obs.upper() != "NAN" else None

        # Determina status pelo prazo/observação
        status = "aberto"
        if prazo:
            upper_prazo = prazo.upper()
            if any(w in upper_prazo for w in ["RESPONDIDO", "CUMPRIDO", "ENVIADO", "EMAIL ENVIADO"]):
                status = "cumprido"
            elif "AGUARDAR" in upper_prazo:
                status = "aguardando"

        conn.execute(
            """INSERT OR IGNORE INTO processos_sei
               (escola_id, numero, forma_exigencia, data_recebimento, prazo, status, observacoes)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (escola_id, numero, forma, data_rec, prazo, status, obs),
        )

        if progress_fn:
            progress_fn((i + 1) / total, f"Importando processo: {numero}")

    conn.commit()


def run_import(progress_fn=None):
    """Executa importação completa"""
    from database import init_db
    init_db()
    conn = get_conn()

    try:
        if progress_fn:
            progress_fn(0, "Iniciando importação...")

        import_riscos(conn, lambda p, m: progress_fn(p * 0.5, m) if progress_fn else None)
        import_pendencias(conn, lambda p, m: progress_fn(0.5 + p * 0.3, m) if progress_fn else None)
        import_acompanhamento(conn, lambda p, m: progress_fn(0.8 + p * 0.2, m) if progress_fn else None)

        if progress_fn:
            progress_fn(1.0, "Importação concluída!")
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    def prog(p, m):
        print(f"[{p:.0%}] {m}")

    ok, err = run_import(prog)
    if ok:
        print("[OK] Importacao concluida com sucesso!")
    else:
        print(f"[ERRO] {err}")
