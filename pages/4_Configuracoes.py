import streamlit as st
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import database as db

st.set_page_config(page_title="Configurações | Regulatório", page_icon="⚙️", layout="wide")


def main():
    st.markdown("# ⚙️ Configurações")
    db.init_db()

    tab1, tab2, tab3 = st.tabs(["📥 Importar dados", "📤 Exportar", "🗄️ Banco de dados"])

    # ------------------------------------------------------------------ TAB 1
    with tab1:
        st.subheader("📥 Importar dados das planilhas Excel")
        st.info(
            "Esta ação importa automaticamente os dados das planilhas de regulatório "
            "já existentes para o banco de dados da plataforma."
        )

        from import_data import (
            PLANILHA_RISCOS, PLANILHA_PENDENCIAS, PLANILHA_ACOMPANHAMENTO
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Planilhas detectadas:**")
            for label, path in [
                ("Riscos Regulatório", PLANILHA_RISCOS),
                ("Status das Pendências", PLANILHA_PENDENCIAS),
                ("Acompanhamento", PLANILHA_ACOMPANHAMENTO),
            ]:
                exists = Path(path).exists()
                icon = "✅" if exists else "❌"
                st.markdown(f"{icon} `{Path(path).name}`")

        with col2:
            st.markdown("**O que será importado:**")
            st.markdown("""
            - 🏫 Escolas por rede (QI, Ao Cubo, Global Tree...)
            - 📄 Status de Licença Sanitária, ETAP, PAA, Ato Autorizativo
            - 📋 Processos SEI ativos com prazos
            - 📊 Status de Habite-se, Bombeiros, Alvará, Regimento, PPP
            """)

        st.markdown("---")

        reimport = st.checkbox("⚠️ Reimportar (apaga dados existentes e reimporta tudo)", value=False)

        if st.button("🚀 Iniciar importação", type="primary"):
            if reimport:
                import sqlite3
                conn = db.get_conn()
                conn.executescript("""
                    DELETE FROM processos_sei;
                    DELETE FROM documentos;
                    DELETE FROM escolas;
                    DELETE FROM redes;
                """)
                conn.commit()
                conn.close()
                st.warning("Dados anteriores removidos. Reimportando...")

            from import_data import run_import

            progress_bar = st.progress(0.0)
            status_text = st.empty()

            def update_progress(p, msg):
                progress_bar.progress(min(float(p), 1.0))
                status_text.text(msg)

            ok, err = run_import(update_progress)

            if ok:
                progress_bar.progress(1.0)
                status_text.text("✅ Importação concluída com sucesso!")
                st.success("Dados importados! Navegue pelo painel para ver o resultado.")
                st.balloons()
            else:
                st.error(f"❌ Erro durante a importação: {err}")
                st.code(err)

        st.markdown("---")

        # Upload manual de novas planilhas
        st.subheader("📤 Importar outra planilha")
        st.caption("Para importar uma planilha diferente, faça o upload abaixo.")
        uploaded = st.file_uploader("Selecionar arquivo Excel (.xlsx)", type=["xlsx"])
        if uploaded:
            dest = Path(__file__).parent.parent / "uploads" / uploaded.name
            dest.parent.mkdir(exist_ok=True)
            dest.write_bytes(uploaded.getvalue())
            st.success(f"Arquivo '{uploaded.name}' salvo em: `{dest}`")
            st.info("Para importar este arquivo, ajuste os caminhos em `import_data.py` e reimporte.")

    # ------------------------------------------------------------------ TAB 2
    with tab2:
        st.subheader("📤 Exportar dados completos")
        import pandas as pd

        conn = db.get_conn()

        col1, col2 = st.columns(2)

        with col1:
            df_escolas = pd.read_sql_query(
                """SELECT e.nome, r.nome as rede, e.cnpj, e.inscricao_municipal,
                          e.estado, e.o_que_funciona
                   FROM escolas e LEFT JOIN redes r ON r.id = e.rede_id
                   WHERE e.ativa = 1 ORDER BY r.nome, e.nome""",
                conn,
            )
            csv_escolas = df_escolas.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                "⬇️ Escolas (.csv)",
                data=csv_escolas,
                file_name="escolas.csv",
                mime="text/csv",
            )

        with col2:
            df_docs = pd.read_sql_query(
                """SELECT e.nome as escola, r.nome as rede, t.nome as documento,
                          d.status, d.data_vencimento, d.observacoes
                   FROM documentos d
                   JOIN escolas e ON e.id = d.escola_id
                   JOIN redes r ON r.id = e.rede_id
                   JOIN tipos_documentos t ON t.id = d.tipo_id
                   WHERE e.ativa = 1 ORDER BY r.nome, e.nome, t.id""",
                conn,
            )
            csv_docs = df_docs.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                "⬇️ Documentos (.csv)",
                data=csv_docs,
                file_name="documentos_regulatorio.csv",
                mime="text/csv",
            )

        df_proc = pd.read_sql_query(
            """SELECT e.nome as escola, p.numero, p.forma_exigencia,
                      p.data_recebimento, p.prazo, p.status, p.observacoes
               FROM processos_sei p LEFT JOIN escolas e ON e.id = p.escola_id
               ORDER BY p.status, p.prazo""",
            conn,
        )
        csv_proc = df_proc.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "⬇️ Processos SEI (.csv)",
            data=csv_proc,
            file_name="processos_sei.csv",
            mime="text/csv",
        )

        conn.close()

    # ------------------------------------------------------------------ TAB 3
    with tab3:
        st.subheader("🗄️ Status do banco de dados")
        conn = db.get_conn()
        c = conn.cursor()

        tabelas = ["redes", "escolas", "tipos_documentos", "documentos", "processos_sei"]
        cols = st.columns(len(tabelas))
        for i, tabela in enumerate(tabelas):
            c.execute(f"SELECT COUNT(*) FROM {tabela}")
            count = c.fetchone()[0]
            cols[i].metric(tabela, count)

        conn.close()

        st.markdown("---")
        st.caption(f"📂 Banco de dados: `{db.DB_PATH}`")

        if st.button("🔄 Recriar tabelas (mantém dados)"):
            db.init_db()
            st.success("Tabelas verificadas/atualizadas.")


main()
