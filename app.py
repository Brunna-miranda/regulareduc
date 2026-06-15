import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, timedelta

import database as db

st.set_page_config(
    page_title="Regulatório | Raiz Educação",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main-header {
        font-size: 28px; font-weight: 700; color: #1e3a5f;
        border-bottom: 3px solid #3b82f6; padding-bottom: 8px; margin-bottom: 20px;
    }
    .metric-card {
        background: white; border-radius: 12px; padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-left: 5px solid #3b82f6;
    }
    .metric-value { font-size: 36px; font-weight: 800; color: #1e3a5f; }
    .metric-label { font-size: 13px; color: #64748b; margin-top: 4px; }
    .status-ok { color: #16a34a; font-weight: 600; }
    .status-vencido { color: #dc2626; font-weight: 600; }
    .status-a_vencer { color: #d97706; font-weight: 600; }
    .status-pendente { color: #dc2626; }
    .status-desconhecido { color: #94a3b8; }
    .alert-banner {
        background: #fef3c7; border: 1px solid #fbbf24; border-radius: 8px;
        padding: 12px 16px; margin-bottom: 12px;
    }
    [data-testid="stSidebar"] { background: #1e3a5f; }
    [data-testid="stSidebar"] .css-1d391kg { background: #1e3a5f; }
</style>
""", unsafe_allow_html=True)


def init():
    db.init_db()
    if not db.has_data():
        st.warning("⚠️ Banco de dados vazio. Vá em **⚙️ Configurações** para importar os dados das planilhas.")
        if st.button("🚀 Importar dados agora", type="primary"):
            st.switch_page("pages/4_Configuracoes.py")
        return False
    return True


def render_semaforo_rede(df_status):
    if df_status.empty:
        return

    pivot = df_status.pivot_table(
        index="rede", columns="status", values="total", aggfunc="sum", fill_value=0
    ).reset_index()

    cols_order = ["ok", "a_vencer", "vencido", "pendente", "desconhecido"]
    colors = {
        "ok": "#22c55e",
        "a_vencer": "#f59e0b",
        "vencido": "#ef4444",
        "pendente": "#ef4444",
        "desconhecido": "#cbd5e1",
    }
    labels = {
        "ok": "OK",
        "a_vencer": "A vencer",
        "vencido": "Vencido",
        "pendente": "Pendente",
        "desconhecido": "Desconhecido",
    }

    fig = go.Figure()
    for col in cols_order:
        if col in pivot.columns:
            fig.add_trace(go.Bar(
                name=labels[col],
                x=pivot["rede"],
                y=pivot[col],
                marker_color=colors[col],
                text=pivot[col],
                textposition="inside",
                textfont_size=11,
            ))

    fig.update_layout(
        barmode="stack",
        height=320,
        margin=dict(l=0, r=0, t=10, b=0),
        legend=dict(orientation="h", y=-0.2),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(title="Documentos"),
        xaxis=dict(tickangle=-20),
        font=dict(family="Inter, sans-serif"),
    )
    st.plotly_chart(fig, use_container_width=True)


def render_processos_urgentes(df):
    if df.empty:
        st.info("Nenhum processo SEI aberto no momento.")
        return

    status_badge = {
        "aberto": "🔴 Aberto",
        "aguardando": "🟡 Aguardando",
        "cumprido": "🟢 Cumprido",
        "arquivado": "⚫ Arquivado",
    }

    for _, row in df.iterrows():
        escola = row.get("escola") or "—"
        numero = row.get("numero") or "—"
        forma = row.get("forma_exigencia") or "—"
        prazo = row.get("prazo") or "—"
        status_label = status_badge.get(row.get("status", "aberto"), "🔴 Aberto")

        st.markdown(f"""
        <div style="background:white;border-radius:8px;padding:12px 16px;margin-bottom:8px;
                    border-left:4px solid #ef4444;box-shadow:0 1px 4px rgba(0,0,0,0.06)">
            <div style="display:flex;justify-content:space-between;align-items:center">
                <strong style="color:#1e3a5f">{escola}</strong>
                <span style="font-size:12px;color:#64748b">{status_label}</span>
            </div>
            <div style="font-size:13px;color:#374151;margin-top:4px">
                📄 {numero} &nbsp;|&nbsp; {forma}
            </div>
            <div style="font-size:12px;color:#6b7280;margin-top:2px">
                ⏰ Prazo: {prazo}
            </div>
        </div>
        """, unsafe_allow_html=True)


def main():
    st.markdown('<div class="main-header">📋 Painel Regulatório — Raiz Educação</div>', unsafe_allow_html=True)

    if not init():
        return

    stats = db.get_dashboard_stats()

    # KPI Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="metric-card" style="border-left-color:#3b82f6">
            <div class="metric-value">{stats['total_escolas']}</div>
            <div class="metric-label">🏫 Escolas Ativas</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        color = "#ef4444" if stats['docs_criticos'] > 0 else "#22c55e"
        st.markdown(f"""
        <div class="metric-card" style="border-left-color:{color}">
            <div class="metric-value" style="color:{color}">{stats['docs_criticos']}</div>
            <div class="metric-label">🔴 Documentos Críticos</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        color = "#f59e0b" if stats['processos_abertos'] > 0 else "#22c55e"
        st.markdown(f"""
        <div class="metric-card" style="border-left-color:{color}">
            <div class="metric-value" style="color:{color}">{stats['processos_abertos']}</div>
            <div class="metric-label">📋 Processos SEI Abertos</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        color = "#f59e0b" if stats['alertas_30'] > 0 else "#22c55e"
        st.markdown(f"""
        <div class="metric-card" style="border-left-color:{color}">
            <div class="metric-value" style="color:{color}">{stats['alertas_30']}</div>
            <div class="metric-label">⚠️ Vencendo em 30 dias</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Linha 2: Semáforo por rede + Processos urgentes
    col_graf, col_proc = st.columns([3, 2])

    with col_graf:
        st.subheader("Status Regulatório por Rede")
        df_status = db.get_status_por_rede()
        render_semaforo_rede(df_status)

    with col_proc:
        st.subheader("🚨 Processos SEI Urgentes")
        df_proc = db.get_processos_urgentes()
        render_processos_urgentes(df_proc)

    st.markdown("---")

    # Linha 3: Vencimentos próximos
    st.subheader("📅 Vencimentos nos Próximos 60 Dias")
    df_venc = db.get_vencimentos_proximos(60)

    if df_venc.empty:
        st.success("✅ Nenhum documento vencendo nos próximos 60 dias.")
    else:
        # Colorir por proximidade
        def color_vencimento(val):
            try:
                dt = date.fromisoformat(val)
                days = (dt - date.today()).days
                if days < 0:
                    return "background-color: #fee2e2; color: #dc2626"
                elif days <= 30:
                    return "background-color: #fef3c7; color: #d97706"
                else:
                    return "background-color: #fef9c3"
            except Exception:
                return ""

        df_venc_show = df_venc.copy()
        df_venc_show["dias_restantes"] = df_venc_show["data_vencimento"].apply(
            lambda v: (date.fromisoformat(v) - date.today()).days if v else None
        )
        df_venc_show = df_venc_show.rename(columns={
            "escola": "Escola",
            "rede": "Rede",
            "documento": "Documento",
            "status": "Status",
            "data_vencimento": "Vencimento",
            "dias_restantes": "Dias",
        })

        styled = df_venc_show[["Escola", "Rede", "Documento", "Vencimento", "Dias"]].style.map(
            color_vencimento, subset=["Vencimento"]
        )
        st.dataframe(styled, use_container_width=True, height=250)

    st.markdown("""
    <div style="text-align:center;color:#94a3b8;font-size:12px;margin-top:20px">
        Raiz Educação — Plataforma de Gestão Regulatória &nbsp;|&nbsp; Dados atualizados em tempo real
    </div>
    """, unsafe_allow_html=True)


main()
