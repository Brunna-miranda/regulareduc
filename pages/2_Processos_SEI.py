import streamlit as st
import pandas as pd
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import database as db

st.set_page_config(page_title="Processos SEI | Regulatório", page_icon="📋", layout="wide")

STATUS_MAP = {
    "aberto": "🔴 Aberto",
    "aguardando": "🟡 Aguardando",
    "cumprido": "🟢 Cumprido",
    "arquivado": "⚫ Arquivado",
}

STATUS_BG = {
    "aberto": "#fee2e2",
    "aguardando": "#fef3c7",
    "cumprido": "#dcfce7",
    "arquivado": "#f1f5f9",
}


def main():
    st.markdown("# 📋 Processos SEI")
    db.init_db()

    # Filtros
    col_f1, col_f2, col_f3 = st.columns([2, 2, 3])
    with col_f1:
        status_filter = st.selectbox(
            "Status",
            ["Todos"] + list(STATUS_MAP.keys()),
            format_func=lambda x: "Todos" if x == "Todos" else STATUS_MAP[x],
        )
    with col_f2:
        redes_df = db.get_redes()
        escola_df = db.get_escolas()
        escola_opts = {"Todas as escolas": None}
        for _, e in escola_df.iterrows():
            escola_opts[e["nome"]] = e["id"]
        escola_sel = st.selectbox("Escola", list(escola_opts.keys()))
    with col_f3:
        busca = st.text_input("🔍 Buscar por número ou escola", placeholder="SEI-030001/...")

    status_param = None if status_filter == "Todos" else status_filter
    escola_id_param = escola_opts.get(escola_sel)

    df = db.get_processos(escola_id=escola_id_param, status=status_param)

    if busca:
        mask = (
            df["numero"].str.contains(busca, case=False, na=False) |
            df["escola"].str.contains(busca, case=False, na=False)
        )
        df = df[mask]

    # Contadores
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔴 Abertos", int((df["status"] == "aberto").sum()))
    c2.metric("🟡 Aguardando", int((df["status"] == "aguardando").sum()))
    c3.metric("🟢 Cumpridos", int((df["status"] == "cumprido").sum()))
    c4.metric("Total", len(df))

    st.markdown("---")

    # Tabela de processos
    if df.empty:
        st.info("Nenhum processo encontrado com os filtros selecionados.")
    else:
        for _, row in df.iterrows():
            bg = STATUS_BG.get(row.get("status", "aberto"), "#f8fafc")
            status_label = STATUS_MAP.get(row.get("status", "aberto"), "—")

            with st.container():
                col_main, col_status = st.columns([5, 1])

                with col_main:
                    st.markdown(
                        f"""<div style='background:{bg};border-radius:8px;padding:14px 18px;margin-bottom:8px'>
                        <div style='display:flex;justify-content:space-between;align-items:flex-start'>
                            <div>
                                <strong style='font-size:15px;color:#1e3a5f'>{row.get('numero','—')}</strong>
                                &nbsp;<span style='color:#64748b;font-size:13px'>{row.get('escola') or '—'}</span>
                            </div>
                            <span style='font-size:13px;font-weight:600'>{status_label}</span>
                        </div>
                        <div style='font-size:13px;color:#374151;margin-top:6px'>
                            📌 {row.get('forma_exigencia') or '—'}
                        </div>
                        <div style='font-size:12px;color:#6b7280;margin-top:4px;display:flex;gap:20px'>
                            <span>📅 Recebido: {row.get('data_recebimento') or '—'}</span>
                            <span>⏰ Prazo: {row.get('prazo') or '—'}</span>
                        </div>
                        {f"<div style='font-size:12px;color:#4b5563;margin-top:4px'>💬 {row['observacoes']}</div>" if row.get('observacoes') else ''}
                        </div>""",
                        unsafe_allow_html=True,
                    )

            # Editar processo (expandível)
            with st.expander(f"✏️ Editar processo {row.get('numero','')}", expanded=False):
                escolas_all = db.get_escolas()
                escola_map = {"(sem escola)": None}
                for _, e in escolas_all.iterrows():
                    escola_map[e["nome"]] = e["id"]

                with st.form(f"form_proc_{row['id']}"):
                    c1, c2 = st.columns(2)
                    with c1:
                        new_numero = st.text_input("Número SEI", value=row.get("numero", ""))
                        new_forma = st.text_input("Forma da exigência", value=row.get("forma_exigencia") or "")
                        new_data = st.text_input("Data recebimento", value=row.get("data_recebimento") or "")
                    with c2:
                        new_prazo = st.text_input("Prazo", value=row.get("prazo") or "")
                        new_status = st.selectbox(
                            "Status",
                            options=list(STATUS_MAP.keys()),
                            format_func=lambda x: STATUS_MAP[x],
                            index=list(STATUS_MAP.keys()).index(row.get("status", "aberto"))
                            if row.get("status") in STATUS_MAP else 0,
                        )
                        new_escola_nome = st.selectbox(
                            "Escola",
                            list(escola_map.keys()),
                            index=list(escola_map.keys()).index(row.get("escola"))
                            if row.get("escola") in escola_map else 0,
                        )
                    new_obs = st.text_area("Observações", value=row.get("observacoes") or "", height=80)

                    if st.form_submit_button("💾 Salvar alterações"):
                        db.save_processo(
                            escola_id=escola_map[new_escola_nome],
                            numero=new_numero,
                            forma_exigencia=new_forma,
                            data_recebimento=new_data,
                            prazo=new_prazo,
                            status=new_status,
                            observacoes=new_obs,
                            processo_id=row["id"],
                        )
                        st.success("Processo atualizado!")
                        st.rerun()

    st.markdown("---")

    # Novo processo
    with st.expander("➕ Registrar novo processo SEI"):
        escolas_all = db.get_escolas()
        escola_map2 = {"(sem escola)": None}
        for _, e in escolas_all.iterrows():
            escola_map2[e["nome"]] = e["id"]

        with st.form("form_novo_processo"):
            c1, c2 = st.columns(2)
            with c1:
                novo_num = st.text_input("Número SEI *", placeholder="Ex: SEI-030001/063541/2024")
                nova_forma = st.text_input("Forma da exigência", placeholder="E-mail com exigência")
                nova_data = st.text_input("Data de recebimento", placeholder="Ex: 27/03/2025")
            with c2:
                novo_prazo = st.text_input("Prazo / Data de cumprimento")
                novo_status = st.selectbox("Status", list(STATUS_MAP.keys()), format_func=lambda x: STATUS_MAP[x])
                nova_escola = st.selectbox("Escola vinculada", list(escola_map2.keys()))
            nova_obs = st.text_area("Observações", height=70)

            if st.form_submit_button("➕ Criar processo"):
                if novo_num.strip():
                    db.save_processo(
                        escola_id=escola_map2[nova_escola],
                        numero=novo_num.strip(),
                        forma_exigencia=nova_forma or None,
                        data_recebimento=nova_data or None,
                        prazo=novo_prazo or None,
                        status=novo_status,
                        observacoes=nova_obs or None,
                    )
                    st.success(f"Processo {novo_num} registrado!")
                    st.rerun()
                else:
                    st.error("Número SEI é obrigatório.")


main()
