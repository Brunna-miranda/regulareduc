import streamlit as st
import pandas as pd
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import database as db

st.set_page_config(page_title="Escolas | Regulatório", page_icon="🏫", layout="wide")

st.markdown("""
<style>
    .school-card {
        background: white; border-radius: 10px; padding: 16px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.07); margin-bottom: 12px;
    }
    .badge-ok { background:#dcfce7; color:#16a34a; padding:2px 8px; border-radius:12px; font-size:11px; font-weight:600; }
    .badge-vencido { background:#fee2e2; color:#dc2626; padding:2px 8px; border-radius:12px; font-size:11px; font-weight:600; }
    .badge-a_vencer { background:#fef3c7; color:#d97706; padding:2px 8px; border-radius:12px; font-size:11px; font-weight:600; }
    .badge-pendente { background:#fee2e2; color:#dc2626; padding:2px 8px; border-radius:12px; font-size:11px; font-weight:600; }
    .badge-desconhecido { background:#f1f5f9; color:#64748b; padding:2px 8px; border-radius:12px; font-size:11px; }
</style>
""", unsafe_allow_html=True)


def status_saude(row):
    if row.get("docs_criticos", 0) > 0:
        return "vencido", f"🔴 {row['docs_criticos']} crítico(s)"
    elif row.get("docs_a_vencer", 0) > 0:
        return "a_vencer", f"🟡 {row['docs_a_vencer']} a vencer"
    elif row.get("docs_ok", 0) > 0:
        return "ok", "🟢 OK"
    return "desconhecido", "❓ Sem dados"


def render_documento_form(escola_id, escola_nome):
    st.subheader(f"📁 Documentos — {escola_nome}")

    df_docs = db.get_documentos_escola(escola_id)
    tipos = db.get_tipos_documentos()
    tipo_map = {row["id"]: row["nome"] for _, row in tipos.iterrows()}

    status_opts = {
        "ok": "✅ OK",
        "a_vencer": "⚠️ A vencer",
        "vencido": "🔴 Vencido",
        "pendente": "❌ Pendente",
        "nao_aplicavel": "— Não aplicável",
        "desconhecido": "❓ Desconhecido",
    }

    for _, doc in df_docs.iterrows():
        tipo_nome = str(doc.get("tipo", ""))
        doc_id = doc.get("id")
        status_atual = str(doc.get("status") or "desconhecido")
        data_venc = str(doc.get("data_vencimento") or "")
        obs_atual = str(doc.get("observacoes") or "")
        arquivo_nome = doc.get("arquivo_nome")

        with st.expander(f"{'✅' if status_atual=='ok' else '⚠️' if status_atual=='a_vencer' else '🔴' if status_atual in ('vencido','pendente') else '❓'} {tipo_nome}", expanded=False):
            col1, col2, col3 = st.columns([2, 2, 3])

            with col1:
                novo_status = st.selectbox(
                    "Status", options=list(status_opts.keys()),
                    format_func=lambda x: status_opts[x],
                    index=list(status_opts.keys()).index(status_atual) if status_atual in status_opts else 5,
                    key=f"status_{escola_id}_{doc.get('tipo')}",
                )

            with col2:
                nova_data = st.text_input(
                    "Vencimento (AAAA-MM-DD)",
                    value=data_venc[:10] if data_venc else "",
                    placeholder="Ex: 2025-04-30",
                    key=f"data_{escola_id}_{doc.get('tipo')}",
                )

            with col3:
                nova_obs = st.text_input(
                    "Observações",
                    value=obs_atual if obs_atual != "None" else "",
                    key=f"obs_{escola_id}_{doc.get('tipo')}",
                )

            col_upload, col_save = st.columns([3, 1])

            with col_upload:
                upload = st.file_uploader(
                    "📎 Anexar documento (PDF)",
                    type=["pdf"],
                    key=f"upload_{escola_id}_{doc.get('tipo')}",
                )

            with col_save:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("💾 Salvar", key=f"save_{escola_id}_{doc.get('tipo')}"):
                    arquivo_path = None
                    arquivo_nome_new = None

                    if upload:
                        doc_dir = Path(__file__).parent.parent / "documentos" / str(escola_id)
                        doc_dir.mkdir(parents=True, exist_ok=True)
                        dest = doc_dir / upload.name
                        dest.write_bytes(upload.read())
                        arquivo_path = str(dest)
                        arquivo_nome_new = upload.name

                    # Encontrar tipo_id pelo nome
                    tipo_id = None
                    for _, t in tipos.iterrows():
                        if t["nome"] == tipo_nome:
                            tipo_id = t["id"]
                            break

                    if tipo_id:
                        db.upsert_documento(
                            escola_id=escola_id,
                            tipo_id=tipo_id,
                            status=novo_status,
                            data_vencimento=nova_data if nova_data else None,
                            observacoes=nova_obs if nova_obs else None,
                            arquivo_nome=arquivo_nome_new,
                            arquivo_path=arquivo_path,
                        )
                        st.success("Salvo!")
                        st.rerun()

            if arquivo_nome and str(arquivo_nome) != "None":
                st.caption(f"📎 Arquivo atual: {arquivo_nome}")


def main():
    st.markdown("# 🏫 Escolas")
    db.init_db()

    # Filtros
    redes_df = db.get_redes()
    col_f1, col_f2, col_f3 = st.columns([3, 2, 2])

    with col_f1:
        rede_opts = ["Todas as redes"] + redes_df["nome"].tolist()
        rede_sel = st.selectbox("Filtrar por rede", rede_opts)
        rede_id = None if rede_sel == "Todas as redes" else int(redes_df[redes_df["nome"] == rede_sel]["id"].values[0])

    with col_f2:
        estado_sel = st.selectbox("Estado", ["Todos", "RJ", "MG", "SP"])
        estado = None if estado_sel == "Todos" else estado_sel

    with col_f3:
        busca = st.text_input("🔍 Buscar escola", placeholder="Nome...")

    # Dados
    df = db.get_escolas(rede_id=rede_id, estado=estado)

    if busca:
        df = df[df["nome"].str.contains(busca, case=False, na=False)]

    st.markdown(f"**{len(df)} escola(s) encontrada(s)**")

    # Resumo por saúde
    if not df.empty:
        criticas = int((df["docs_criticos"] > 0).sum())
        a_vencer = int(((df["docs_criticos"] == 0) & (df["docs_a_vencer"] > 0)).sum())
        ok = int(((df["docs_criticos"] == 0) & (df["docs_a_vencer"] == 0) & (df["docs_ok"] > 0)).sum())
        sem_dados = len(df) - criticas - a_vencer - ok

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("🔴 Críticas", criticas)
        c2.metric("🟡 A verificar", a_vencer)
        c3.metric("🟢 Em dia", ok)
        c4.metric("❓ Sem dados", sem_dados)

    st.markdown("---")

    # Lista de escolas
    escola_sel = st.session_state.get("escola_sel_id")

    for _, row in df.iterrows():
        saude_key, saude_label = status_saude(row)

        col_info, col_status, col_btn = st.columns([5, 2, 1])
        with col_info:
            st.markdown(
                f"**{row['nome']}** &nbsp; <span style='color:#64748b;font-size:12px'>{row.get('rede','')}</span>",
                unsafe_allow_html=True,
            )
            sub = []
            if row.get("cnpj"):
                sub.append(f"CNPJ: {row['cnpj']}")
            if row.get("estado"):
                sub.append(row["estado"])
            if sub:
                st.caption(" · ".join(sub))

        with col_status:
            st.markdown(f"<br><span class='badge-{saude_key}'>{saude_label}</span>", unsafe_allow_html=True)

        with col_btn:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("📂 Abrir", key=f"open_{row['id']}"):
                if st.session_state.get("escola_sel_id") == row["id"]:
                    st.session_state["escola_sel_id"] = None
                else:
                    st.session_state["escola_sel_id"] = row["id"]
                st.rerun()

        # Expandir detalhes da escola selecionada
        if st.session_state.get("escola_sel_id") == row["id"]:
            with st.container():
                st.markdown("---")
                render_documento_form(row["id"], row["nome"])

                # Processos SEI da escola
                st.subheader("📋 Processos SEI")
                df_proc = db.get_processos(escola_id=row["id"])
                if df_proc.empty:
                    st.info("Nenhum processo SEI vinculado a esta escola.")
                else:
                    st.dataframe(
                        df_proc[["numero", "forma_exigencia", "data_recebimento", "prazo", "status"]].rename(
                            columns={
                                "numero": "Número", "forma_exigencia": "Exigência",
                                "data_recebimento": "Recebido", "prazo": "Prazo", "status": "Status"
                            }
                        ),
                        use_container_width=True,
                    )
                st.markdown("---")

    # Formulário nova escola
    with st.expander("➕ Adicionar nova escola"):
        redes_opts = {r["nome"]: r["id"] for _, r in redes_df.iterrows()}
        with st.form("form_nova_escola"):
            c1, c2 = st.columns(2)
            with c1:
                nome = st.text_input("Nome da escola *")
                cnpj = st.text_input("CNPJ")
                insc = st.text_input("Inscrição Municipal")
            with c2:
                rede_nova = st.selectbox("Rede *", list(redes_opts.keys()))
                estado_novo = st.selectbox("Estado", ["RJ", "MG", "SP", "MG", "RS", "SC"])
                funciona = st.text_input("O que funciona na escola")
            obs_nova = st.text_area("Observações", height=60)

            if st.form_submit_button("➕ Criar escola"):
                if nome:
                    db.save_escola(
                        nome=nome, rede_id=redes_opts[rede_nova], cnpj=cnpj,
                        inscricao_municipal=insc, estado=estado_novo,
                        o_que_funciona=funciona, observacoes=obs_nova,
                    )
                    st.success(f"Escola '{nome}' criada!")
                    st.rerun()
                else:
                    st.error("Nome é obrigatório.")


main()
