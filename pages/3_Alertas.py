import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date, timedelta
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
import database as db

st.set_page_config(page_title="Alertas | Regulatório", page_icon="⚠️", layout="wide")


def render_alerta_card(row, urgencia):
    colors = {
        "vencido": ("#fee2e2", "#dc2626", "🔴 VENCIDO"),
        "urgente": ("#fef3c7", "#d97706", "🟡 Urgente"),
        "atencao": ("#fef9c3", "#ca8a04", "⚠️ Atenção"),
    }
    bg, text_color, label = colors.get(urgencia, ("#f8fafc", "#374151", "ℹ️"))

    venc = row.get("data_vencimento", "—")
    try:
        days = (date.fromisoformat(venc) - date.today()).days
        days_text = f"{abs(days)} dias atrás" if days < 0 else f"em {days} dias"
    except Exception:
        days_text = ""

    st.markdown(
        f"""<div style='background:{bg};border-left:4px solid {text_color};border-radius:8px;
                padding:12px 16px;margin-bottom:8px'>
            <div style='display:flex;justify-content:space-between;align-items:center'>
                <strong style='color:#1e3a5f;font-size:14px'>{row.get('escola','—')}</strong>
                <span style='font-size:12px;background:{text_color};color:white;
                             padding:2px 8px;border-radius:10px'>{label}</span>
            </div>
            <div style='font-size:13px;color:#374151;margin-top:4px'>
                📄 {row.get('documento','—')} &nbsp;·&nbsp;
                <span style='color:#64748b'>{row.get('rede','—')}</span>
            </div>
            <div style='font-size:12px;color:{text_color};font-weight:600;margin-top:4px'>
                📅 Vencimento: {venc} {f'({days_text})' if days_text else ''}
            </div>
        </div>""",
        unsafe_allow_html=True,
    )


def main():
    st.markdown("# ⚠️ Alertas de Vencimento")
    db.init_db()

    hoje = date.today()

    # Buscar todos com vencimento definido
    df_all = db.get_vencimentos_proximos(365)  # até 1 ano

    if df_all.empty:
        st.success("✅ Nenhum alerta de vencimento registrado.")
        return

    def classify(venc_str):
        try:
            d = date.fromisoformat(venc_str)
            days = (d - hoje).days
            if days < 0:
                return "vencido"
            elif days <= 30:
                return "urgente"
            elif days <= 60:
                return "atencao"
            else:
                return "ok"
        except Exception:
            return "ok"

    df_all["urgencia"] = df_all["data_vencimento"].apply(classify)
    df_all["dias"] = df_all["data_vencimento"].apply(
        lambda v: (date.fromisoformat(v) - hoje).days if v else None
    )

    vencidos = df_all[df_all["urgencia"] == "vencido"]
    urgentes = df_all[df_all["urgencia"] == "urgente"]
    atencao = df_all[df_all["urgencia"] == "atencao"]

    # KPIs
    c1, c2, c3 = st.columns(3)
    c1.metric("🔴 Vencidos", len(vencidos), help="Documentos com data de vencimento no passado")
    c2.metric("🟡 Urgente (≤30 dias)", len(urgentes))
    c3.metric("⚠️ Atenção (31-60 dias)", len(atencao))

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(
        [f"🔴 Vencidos ({len(vencidos)})", f"🟡 Urgentes ({len(urgentes)})", f"⚠️ Atenção ({len(atencao)})"]
    )

    with tab1:
        if vencidos.empty:
            st.success("✅ Nenhum documento vencido!")
        else:
            st.warning(f"⚠️ {len(vencidos)} documento(s) com prazo vencido. Regularize com urgência.")

            # Agrupar por documento
            for doc_tipo in vencidos["documento"].unique():
                sub = vencidos[vencidos["documento"] == doc_tipo].sort_values("dias")
                st.markdown(f"**📄 {doc_tipo}** — {len(sub)} escola(s)")
                for _, row in sub.iterrows():
                    render_alerta_card(row, "vencido")
                st.markdown("")

    with tab2:
        if urgentes.empty:
            st.success("✅ Nenhum documento vencendo nos próximos 30 dias.")
        else:
            st.info(f"📌 {len(urgentes)} documento(s) vencem nos próximos 30 dias.")
            for _, row in urgentes.sort_values("dias").iterrows():
                render_alerta_card(row, "urgente")

    with tab3:
        if atencao.empty:
            st.success("✅ Nenhum documento vencendo em 31-60 dias.")
        else:
            for _, row in atencao.sort_values("dias").iterrows():
                render_alerta_card(row, "atencao")

    st.markdown("---")

    # Exportar relatório
    st.subheader("📊 Exportar Relatório de Alertas")
    col_exp1, col_exp2 = st.columns(2)

    with col_exp1:
        df_export = df_all[df_all["urgencia"] != "ok"].sort_values("dias")[
            ["escola", "rede", "documento", "data_vencimento", "dias", "urgencia"]
        ].rename(columns={
            "escola": "Escola", "rede": "Rede", "documento": "Documento",
            "data_vencimento": "Vencimento", "dias": "Dias restantes", "urgencia": "Urgência"
        })

        csv = df_export.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "⬇️ Baixar CSV de alertas",
            data=csv,
            file_name=f"alertas_regulatorio_{hoje.isoformat()}.csv",
            mime="text/csv",
        )

    with col_exp2:
        # Resumo por rede
        resumo = df_all[df_all["urgencia"] != "ok"].groupby(["rede", "urgencia"]).size().reset_index(name="qtd")
        if not resumo.empty:
            resumo_csv = resumo.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                "⬇️ Baixar resumo por rede",
                data=resumo_csv,
                file_name=f"resumo_alertas_{hoje.isoformat()}.csv",
                mime="text/csv",
            )


main()
