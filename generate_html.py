"""Gera regulareduc.html — dados reais + campos editáveis + contatos SEEDUC."""
import json

with open('data_export.json', encoding='utf-8') as f:
    data = json.load(f)

data_js = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --pri:#1B3A6B;--sec:#F0F4FA;--surf:#FFFFFF;--acc:#2D6BE4;
  --txt:#1A1D23;--muted:#6B7280;--border:#E5E7EB;
  --green:#22C55E;--yellow:#F59E0B;--red:#EF4444;
  --gbg:#DCFCE7;--ybg:#FEF3C7;--rbg:#FEE2E2;
  --sw:242px;--hh:60px
}
body{font-family:'Inter',system-ui,sans-serif;background:var(--sec);color:var(--txt);min-height:100vh}
.sb{position:fixed;top:0;left:0;bottom:0;width:var(--sw);background:var(--pri);
    display:flex;flex-direction:column;z-index:100;overflow-y:auto}
.sb-logo{padding:18px 20px 14px;border-bottom:1px solid rgba(255,255,255,.12)}
.sb-logo-main{color:#fff;font-size:19px;font-weight:800;letter-spacing:-.5px}
.sb-logo-sub{color:rgba(255,255,255,.5);font-size:11px;margin-top:2px}
.sb-nav{flex:1;padding:10px 0}
.nav-sep{padding:14px 20px 6px;color:rgba(255,255,255,.3);font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase}
.ni{display:flex;align-items:center;gap:10px;padding:9px 20px;color:rgba(255,255,255,.7);
    cursor:pointer;font-size:13px;font-weight:500;border-left:3px solid transparent;transition:.15s}
.ni:hover{background:rgba(255,255,255,.08);color:#fff}
.ni.active{background:rgba(255,255,255,.13);color:#fff;border-left-color:var(--acc)}
.ni i{width:16px;height:16px;flex-shrink:0}
.sb-foot{padding:14px 20px;border-top:1px solid rgba(255,255,255,.1);display:flex;align-items:center;gap:10px}
.av{width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.2);display:flex;
    align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700}
.un{color:#fff;font-size:12px;font-weight:500}.ur{color:rgba(255,255,255,.5);font-size:10px}
.hd{position:fixed;top:0;left:var(--sw);right:0;height:var(--hh);background:#fff;
    border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 22px;z-index:99;gap:14px}
.hd-title{font-size:17px;font-weight:700;color:var(--pri);flex:1}
.btn-ic{width:34px;height:34px;border-radius:8px;border:none;background:var(--sec);
        display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--muted);
        transition:.15s;position:relative}
.btn-ic:hover{background:var(--border);color:var(--txt)}
.nb{position:absolute;top:3px;right:3px;width:16px;height:16px;background:var(--red);
    border-radius:50%;font-size:9px;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700}
.main{margin-left:var(--sw);margin-top:var(--hh);padding:22px;min-height:calc(100vh - var(--hh))}
.card{background:#fff;border-radius:12px;padding:20px;border:1px solid var(--border);box-shadow:0 1px 3px rgba(0,0,0,.04)}
.kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px}
.kpi-lbl{font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.5px}
.kpi-val{font-size:30px;font-weight:800;color:var(--pri);margin:5px 0 3px;line-height:1}
.kpi-sub{font-size:11px;color:var(--muted)}
.kpi-val.danger{color:var(--red)}.kpi-val.warn{color:var(--yellow)}.kpi-val.ok{color:var(--green)}
.farol-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:22px}
.fc{padding:14px;cursor:pointer;transition:transform .15s}.fc:hover{transform:translateY(-2px)}
.fc-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.fc-name{font-size:12px;font-weight:600;color:var(--txt);line-height:1.3}
.badge{display:inline-flex;align-items:center;gap:3px;padding:2px 7px;border-radius:20px;font-size:10px;font-weight:700}
.badge.ok{background:var(--gbg);color:#15803D}.badge.warn{background:var(--ybg);color:#92400E}
.badge.danger{background:var(--rbg);color:#991B1B}.badge.gray{background:#F3F4F6;color:#4B5563}
.badge.blue{background:#EFF6FF;color:#1D4ED8}
.st{display:inline-flex;align-items:center;gap:3px;padding:3px 8px;border-radius:20px;font-size:11px;font-weight:600;white-space:nowrap}
.st.ok{background:var(--gbg);color:#15803D}.st.warn{background:var(--ybg);color:#92400E}
.st.danger{background:var(--rbg);color:#991B1B}.st.gray{background:#F3F4F6;color:#4B5563}
.dot{width:6px;height:6px;border-radius:50%;display:inline-block;flex-shrink:0}
.dot.ok{background:var(--green)}.dot.warn{background:var(--yellow)}.dot.danger{background:var(--red)}.dot.gray{background:#9CA3AF}
.btn{padding:8px 15px;border-radius:8px;border:none;font-size:13px;font-weight:600;
     cursor:pointer;display:inline-flex;align-items:center;gap:5px;transition:.15s;font-family:inherit}
.btn-pri{background:var(--acc);color:#fff}.btn-pri:hover{background:#1E4FCC}
.btn-sec{background:var(--sec);color:var(--txt);border:1px solid var(--border)}.btn-sec:hover{background:var(--border)}
.btn-danger{background:var(--rbg);color:var(--red)}.btn-danger:hover{background:#FECACA}
.btn-sm{padding:4px 10px;font-size:11px;border-radius:6px}
.filters{display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap;align-items:center}
.search{display:flex;align-items:center;gap:7px;background:#fff;border:1px solid var(--border);
        border-radius:8px;padding:7px 11px;flex:1;min-width:180px}
.search input{border:none;outline:none;font-size:13px;color:var(--txt);background:transparent;flex:1;font-family:inherit}
.search input::placeholder{color:var(--muted)}
select.fs{padding:7px 11px;border:1px solid var(--border);border-radius:8px;font-size:13px;
          color:var(--txt);background:#fff;outline:none;cursor:pointer;font-family:inherit}
.sh{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:18px}
.sh-title{font-size:15px;font-weight:700;color:var(--txt)}.sh-sub{font-size:12px;color:var(--muted);margin-top:2px}
.tbl-wrap{overflow-x:auto;border-radius:10px;border:1px solid var(--border)}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;padding:9px 12px;font-size:10px;font-weight:700;text-transform:uppercase;
   letter-spacing:.5px;color:var(--muted);border-bottom:2px solid var(--border);white-space:nowrap;background:#fff}
td{padding:10px 12px;border-bottom:1px solid var(--border);vertical-align:middle}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:#FAFBFC}
.td-name{font-weight:600;font-size:13px}.td-sub{font-size:11px;color:var(--muted);margin-top:1px}
.pag{display:flex;align-items:center;justify-content:space-between;padding:12px 0 0}
.pag-info{font-size:12px;color:var(--muted)}.pag-btns{display:flex;gap:3px}
.pb{padding:5px 10px;border:1px solid var(--border);border-radius:6px;font-size:12px;
    cursor:pointer;background:#fff;color:var(--muted);font-family:inherit}
.pb.active{background:var(--acc);color:#fff;border-color:var(--acc)}.pb:hover:not(.active){background:var(--sec)}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:200;
         display:flex;align-items:center;justify-content:center;padding:20px}
.modal{background:#fff;border-radius:14px;width:100%;max-width:560px;max-height:90vh;
       overflow-y:auto;box-shadow:0 20px 60px rgba(0,0,0,.2)}
.modal-lg{max-width:720px}
.mh{padding:18px 22px;border-bottom:1px solid var(--border);display:flex;align-items:center;
    justify-content:space-between;position:sticky;top:0;background:#fff;border-radius:14px 14px 0 0;z-index:1}
.mh-title{font-size:15px;font-weight:700}
.mc{width:30px;height:30px;border-radius:6px;border:none;background:var(--sec);cursor:pointer;
    display:flex;align-items:center;justify-content:center;color:var(--muted)}
.mb{padding:22px}
.mf{padding:14px 22px;border-top:1px solid var(--border);display:flex;justify-content:flex-end;gap:8px;
    position:sticky;bottom:0;background:#fff;border-radius:0 0 14px 14px}
label{display:block;font-size:12px;font-weight:600;color:var(--txt);margin-bottom:5px}
input[type=text],input[type=date],input[type=email],input[type=tel],textarea,select.fi{
  width:100%;padding:9px 11px;border:1px solid var(--border);border-radius:8px;
  font-size:13px;color:var(--txt);outline:none;transition:border-color .15s;
  background:#fff;font-family:inherit}
input:focus,textarea:focus,select.fi:focus{border-color:var(--acc)}
textarea{resize:vertical;min-height:72px}
.fg{margin-bottom:14px}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.toasts{position:fixed;bottom:18px;right:18px;z-index:300;display:flex;flex-direction:column;gap:7px}
.toast{background:#fff;border-radius:10px;padding:11px 15px;box-shadow:0 4px 20px rgba(0,0,0,.15);
       display:flex;align-items:center;gap:9px;font-size:13px;min-width:230px;
       border-left:4px solid;animation:sIn .3s ease}
.toast.success{border-color:var(--green)}.toast.error{border-color:var(--red)}.toast.info{border-color:var(--acc)}
@keyframes sIn{from{transform:translateX(110%);opacity:0}to{transform:translateX(0);opacity:1}}
.tl-item{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid var(--border)}
.tl-item:last-child{border-bottom:none}
.tl-dot{width:8px;height:8px;border-radius:50%;margin-top:5px;flex-shrink:0}
.tl-body{flex:1}
.tl-title{font-size:13px;font-weight:500}.tl-meta{font-size:11px;color:var(--muted);margin-top:2px}
.sc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}
.sc{padding:18px;cursor:pointer;transition:transform .15s}.sc:hover{transform:translateY(-2px)}
.sc-name{font-size:14px;font-weight:700;margin-bottom:3px}
.sc-meta{font-size:11px;color:var(--muted);margin-bottom:8px}
.pbar{height:5px;background:var(--sec);border-radius:3px;overflow:hidden;margin:3px 0 5px}
.pbar-fill{height:100%;border-radius:3px}
.two-col{display:grid;grid-template-columns:2fr 1fr;gap:18px}
.drw-ov{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:150}
.drw{position:fixed;top:0;right:0;bottom:0;width:480px;background:#fff;z-index:151;
     overflow-y:auto;box-shadow:-4px 0 30px rgba(0,0,0,.15);animation:dIn .3s ease}
@keyframes dIn{from{transform:translateX(100%)}to{transform:translateX(0)}}
.drw-hd{padding:18px 22px;border-bottom:1px solid var(--border);position:sticky;top:0;
         background:#fff;z-index:1;display:flex;align-items:center;justify-content:space-between}
.drw-body{padding:18px 22px}
/* Treinamentos */
.trn-mapa{overflow-x:auto;margin-top:14px}
.trn-mapa table{border-collapse:collapse;font-size:11px;min-width:600px}
.trn-mapa th{padding:6px 8px;background:var(--pri);color:#fff;white-space:nowrap;font-size:10px;text-align:center}
.trn-mapa td.escola-col{padding:6px 10px;font-weight:500;font-size:12px;white-space:nowrap;background:#fff;border-bottom:1px solid var(--border)}
.trn-mapa td.status-cell{text-align:center;padding:5px;border:1px solid var(--border)}
.trn-cell-ok{background:#DCFCE7;color:#15803D;font-weight:700;font-size:10px}
.trn-cell-warn{background:#FEF3C7;color:#92400E;font-weight:700;font-size:10px}
.trn-cell-venc{background:#FEE2E2;color:#991B1B;font-weight:700;font-size:10px}
.trn-cell-nao{background:#F1F5F9;color:#94a3b8;font-size:10px}
.trn-tipo-card{padding:14px;cursor:pointer;transition:transform .15s;border-left:4px solid}
.trn-tipo-card:hover{transform:translateY(-2px)}
/* Situação documento */
.sit{display:inline-flex;align-items:center;gap:3px;padding:2px 8px;border-radius:20px;font-size:10px;font-weight:700;white-space:nowrap}
.sit-em_elaboracao{background:#F3F4F6;color:#4B5563}
.sit-protocolado{background:#EFF6FF;color:#1D4ED8}
.sit-em_analise{background:#FEF3C7;color:#92400E}
.sit-aprovado{background:#DCFCE7;color:#15803D}
.sit-exigencia{background:#FEE2E2;color:#991B1B}
.sit-arquivado{background:#F3F4F6;color:#9CA3AF}
/* ETAP */
.etap-membro{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid var(--border)}
.etap-do-row{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border)}
.etap-status{padding:4px 12px;border-radius:20px;font-size:11px;font-weight:700}
/* Legislações */
.leg-orgao{display:inline-block;padding:2px 8px;border-radius:12px;font-size:10px;font-weight:700;white-space:nowrap}
.leg-cee-rj{background:#EFF6FF;color:#1D4ED8}
.leg-cme-rj{background:#F0FDF4;color:#15803D}
.leg-smed-poa{background:#FEF3C7;color:#92400E}
.leg-sme-jf{background:#FDF4FF;color:#7C3AED}
.leg-seeduc-rj{background:#FEF9EC;color:#B45309}
.leg-mec{background:#FFF1F2;color:#BE123C}
.leg-outro{background:#F3F4F6;color:#4B5563}
.modelo-card{padding:16px;transition:transform .15s;cursor:pointer}
.modelo-card:hover{transform:translateY(-2px)}
/* Auditoria */
.aud-item{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border)}
.aud-resultado{display:flex;gap:6px}
.aud-btn{padding:4px 10px;border-radius:6px;border:2px solid var(--border);font-size:11px;font-weight:600;cursor:pointer;background:white;transition:.15s}
.aud-btn.conforme{border-color:var(--green);background:var(--gbg);color:#15803D}
.aud-btn.nao_conforme{border-color:var(--red);background:var(--rbg);color:#991B1B}
.aud-btn.nao_aplicavel{border-color:#9CA3AF;background:#F3F4F6;color:#4B5563}
/* Calendário */
.cal-grid{display:grid;grid-template-columns:repeat(7,1fr)}
.cal-dname{text-align:center;font-size:11px;font-weight:700;color:var(--muted);padding:7px 0;text-transform:uppercase;letter-spacing:.4px}
.cal-cell{min-height:92px;padding:5px;background:#fff;cursor:pointer;transition:.1s;
          border-right:1px solid var(--border);border-bottom:1px solid var(--border)}
.cal-cell:nth-child(7n){border-right:none}
.cal-cell:hover{background:#F5F8FF}
.cal-cell.cal-today{background:#EFF6FF}
.cal-cell.cal-past{background:#FAFAFA;opacity:.85}
.cal-cell.cal-empty{background:var(--sec);cursor:default;border-right:1px solid var(--border)}
.cal-day-num{font-size:12px;font-weight:600;margin-bottom:3px;color:var(--txt);line-height:1}
.cal-today-num{color:var(--acc);font-weight:800}
.cal-ev{font-size:9px;padding:2px 4px;border-radius:3px;overflow:hidden;text-overflow:ellipsis;
        white-space:nowrap;color:#fff;font-weight:600;margin-bottom:2px;line-height:1.4}
.cal-more{font-size:9px;color:var(--muted);font-weight:600;padding:1px 0 0 2px}
.cal-week-header{display:grid;grid-template-columns:repeat(7,1fr);
                 border-bottom:1px solid var(--border);border-top:1px solid var(--border)}
/* Arquivos */
.drop-zone{border:2px dashed var(--border);border-radius:10px;padding:28px 16px;text-align:center;
           cursor:pointer;transition:.2s;background:#fff}
.drop-zone:hover,.drop-zone.drag-over{border-color:var(--acc);background:#EFF6FF}
.arq-item{display:flex;align-items:center;gap:10px;padding:9px 11px;background:var(--sec);
          border-radius:8px;margin-bottom:6px;transition:.15s}
.arq-item:hover{background:#E8EDF5}
.arq-icon{font-size:22px;flex-shrink:0;line-height:1}
.arq-nome{font-size:13px;font-weight:500;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.arq-meta{font-size:11px;color:var(--muted);margin-top:1px}
.arq-cat{font-size:10px;padding:1px 6px;border-radius:8px;background:#EFF6FF;color:#1D4ED8;font-weight:600}
.proc-status{display:inline-flex;align-items:center;gap:4px;padding:3px 9px;border-radius:20px;font-size:11px;font-weight:700}
.ps-aberto{background:var(--rbg);color:#991B1B}
.ps-cumprido{background:var(--gbg);color:#15803D}
.ps-aguardando{background:var(--ybg);color:#92400E}
.empty{padding:50px 20px;text-align:center;color:var(--muted)}
.empty-icon{font-size:42px;margin-bottom:10px}
.empty-title{font-size:15px;font-weight:600;color:var(--txt);margin-bottom:6px}
.divider{height:1px;background:var(--border);margin:16px 0}
.tag{display:inline-block;padding:2px 7px;border-radius:5px;font-size:10px;font-weight:600;background:var(--sec);color:var(--muted)}
.tag.rede{background:#EFF6FF;color:#1D4ED8}
/* Contatos */
.ct-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.ct-card{padding:18px;transition:transform .15s}.ct-card:hover{transform:translateY(-2px)}
.ct-av{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;
       font-size:16px;font-weight:800;color:#fff;flex-shrink:0}
.ct-name{font-size:14px;font-weight:700}.ct-role{font-size:12px;color:var(--muted)}
.ct-info{font-size:12px;color:var(--txt);margin-top:6px;display:flex;flex-direction:column;gap:3px}
/* Financeiro */
.fin-chart{display:flex;align-items:flex-end;gap:5px;height:140px;padding:0 4px}
.fin-bar-col{flex:1;display:flex;flex-direction:column;align-items:center;gap:2px;min-width:0}
.fin-bar-wrap{flex:1;width:100%;display:flex;align-items:flex-end}
.fin-bar{width:100%;border-radius:4px 4px 0 0;min-height:3px;transition:height .5s}
.fin-bar-label{font-size:9px;color:var(--muted);text-align:center;white-space:nowrap;overflow:hidden;width:100%;text-overflow:ellipsis}
.fin-bar-val{font-size:8px;font-weight:600;color:var(--muted);text-align:center;white-space:nowrap}
.fin-st-pago{background:var(--gbg);color:#15803D}
.fin-st-pendente{background:var(--ybg);color:#92400E}
.fin-st-vencido{background:var(--rbg);color:#991B1B}
.fin-st-cancelado{background:#F3F4F6;color:#4B5563}
.cat-pct-bar{height:5px;background:var(--sec);border-radius:3px;overflow:hidden;margin-top:3px}
.cat-pct-fill{height:100%;border-radius:3px;background:var(--acc)}
/* Andamentos */
.and-item{background:var(--sec);border-radius:8px;padding:10px 12px;margin-bottom:8px}
.and-date{font-size:10px;color:var(--muted);font-weight:600;margin-bottom:3px}
.and-text{font-size:13px;color:var(--txt)}
.and-autor{font-size:10px;color:var(--muted);margin-top:3px}
/* Action buttons — sempre visíveis */
.act-btns{display:flex;gap:4px}
@media(max-width:1280px){.farol-grid{grid-template-columns:repeat(4,1fr)}}
@media(max-width:1024px){.kpi-grid{grid-template-columns:repeat(2,1fr)};.farol-grid{grid-template-columns:repeat(3,1fr)}}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
"""

# ── HTML STRUCTURE ─────────────────────────────────────────────────────────────
HTML = """
<div class="sb">
  <div class="sb-logo">
    <div class="sb-logo-main">RegularEduc</div>
    <div class="sb-logo-sub">Controle Regulatório Escolar</div>
  </div>
  <nav class="sb-nav">
    <div class="nav-sep">Principal</div>
    <div class="ni active" data-s="dashboard" onclick="go('dashboard')"><i data-lucide="layout-dashboard"></i>Dashboard</div>
    <div class="ni" data-s="docs" onclick="go('docs')"><i data-lucide="file-text"></i>Documentos</div>
    <div class="ni" data-s="processos" onclick="go('processos')"><i data-lucide="git-branch"></i>Processos SEI</div>
    <div class="nav-sep">Gestão</div>
    <div class="ni" data-s="escolas" onclick="go('escolas')"><i data-lucide="building-2"></i>Escolas</div>
    <div class="ni" data-s="etap" onclick="go('etap')"><i data-lucide="file-cog"></i>ETAP</div>
    <div class="ni" data-s="legislacoes" onclick="go('legislacoes')"><i data-lucide="scale"></i>Legislações</div>
    <div class="ni" data-s="licencas" onclick="go('licencas')"><i data-lucide="badge-check"></i>Licenças &amp; Alvarás</div>
    <div class="ni" data-s="financeiro" onclick="go('financeiro')"><i data-lucide="dollar-sign"></i>Financeiro</div>
    <div class="ni" data-s="contatos" onclick="go('contatos')"><i data-lucide="phone"></i>Contatos SEEDUC</div>
    <div class="ni" data-s="tarefas" onclick="go('tarefas')"><i data-lucide="check-square"></i>Tarefas</div>
    <div class="ni" data-s="treinamentos" onclick="go('treinamentos')"><i data-lucide="graduation-cap"></i>Treinamentos</div>
    <div class="nav-sep">Conformidade</div>
    <div class="ni" data-s="calendario" onclick="go('calendario')"><i data-lucide="calendar"></i>Calendário</div>
    <div class="ni" data-s="auditoria" onclick="go('auditoria')"><i data-lucide="clipboard-check"></i>Auditoria</div>
    <div class="ni" data-s="relatorios" onclick="go('relatorios')"><i data-lucide="bar-chart-2"></i>Relatórios</div>
    <div class="ni" data-s="config" onclick="go('config')"><i data-lucide="settings"></i>Configurações</div>
  </nav>
  <div class="sb-foot">
    <div class="av">BR</div>
    <div><div class="un">Brunna Miranda</div><div class="ur">Regulatório</div></div>
  </div>
</div>

<div class="hd">
  <div class="hd-title" id="page-title">Dashboard</div>
  <div style="flex:1"></div>
  <div style="font-size:12px;color:var(--muted)" id="hd-stats"></div>
  <div style="position:relative">
    <button class="btn-ic" onclick="toggleNotif()" id="notif-btn">
      <i data-lucide="bell" style="width:16px;height:16px"></i>
      <span class="nb" id="notif-count">0</span>
    </button>
    <div id="notif-panel" style="display:none;position:absolute;top:calc(100% + 8px);right:0;
         width:320px;background:#fff;border:1px solid var(--border);border-radius:12px;
         box-shadow:0 8px 30px rgba(0,0,0,.12);z-index:200;overflow:hidden">
      <div style="padding:12px 16px;border-bottom:1px solid var(--border);font-size:13px;font-weight:700;
                  display:flex;justify-content:space-between;align-items:center">
        Alertas <span id="notif-badge" style="background:var(--rbg);color:var(--red);padding:1px 7px;border-radius:10px;font-size:11px;font-weight:700"></span>
      </div>
      <div id="notif-list"></div>
    </div>
  </div>
</div>

<div class="main" id="main-content"></div>
<div class="toasts" id="toasts"></div>
<div id="modal-root"></div>
<div id="drawer-root"></div>
"""

# ── JAVASCRIPT ────────────────────────────────────────────────────────────────
JS = r"""
// ── DATA & PERSISTENCE ────────────────────────────────────────────────────────
const SEED = (()=>{const d=__DATA__;return d})();

function initDB(){
  try{
    const s=localStorage.getItem('rg_v3');
    if(s){const p=JSON.parse(s);return p;}
  }catch(e){}
  // Ensure andamentos array on all procs
  SEED.procs.forEach(p=>{if(!p.andamentos)p.andamentos=[];});
  SEED.contacts=[];
  return SEED;
}

const DB=initDB();
if(!DB.contacts)DB.contacts=[];
if(!DB.financeiro)DB.financeiro=[];
if(!DB.tarefas)DB.tarefas=[];
if(!DB.arquivos)DB.arquivos=[];
if(!DB.etaps)DB.etaps=[];
if(!DB.auditorias)DB.auditorias=[];
if(!DB.treinamentos)DB.treinamentos=[];
if(!DB.tipos_treinamento)DB.tipos_treinamento=[
  {id:1,nome:'Lei Lucas — Primeiros Socorros',sigla:'Lei Lucas',meses:24,lei:'Lei 13.722/2018',obrigatorio:true},
  {id:2,nome:'Evacuação e Combate a Incêndio',sigla:'Evacuação',meses:12,lei:'ABNT NBR 14276',obrigatorio:true},
  {id:3,nome:'Brigada de Incêndio',sigla:'Brigada',meses:12,lei:'ABNT NBR 14276',obrigatorio:true},
  {id:4,nome:'SIPAT — Semana de Prevenção de Acidentes',sigla:'SIPAT',meses:12,lei:'NR-5',obrigatorio:true},
  {id:5,nome:'Primeiros Socorros Básico',sigla:'Prim. Socorros',meses:24,lei:'NR-7',obrigatorio:false},
  {id:6,nome:'Proteção e Defesa Civil',sigla:'Def. Civil',meses:24,lei:'Lei 12.608/2012',obrigatorio:false},
  {id:7,nome:'NR-10 — Segurança Elétrica',sigla:'NR-10',meses:24,lei:'NR-10',obrigatorio:false},
  {id:8,nome:'Outro',sigla:'Outro',meses:12,lei:'',obrigatorio:false},
];
if(!DB.legislacoes)DB.legislacoes=[];
if(!DB.modelos_anexos)DB.modelos_anexos=[];
if(!DB.tipos_processo)DB.tipos_processo=[
  'Autorização de Funcionamento','Renovação de Autorização','Renovação de Alvará',
  'Renovação — Licença Sanitária','AVCB — Corpo de Bombeiros','Laudo Técnico CREA',
  'Habite-se','Transferência de Mantenedora','Recredenciamento MEC',
  'Censo Escolar INEP','Regularização Fiscal','Processo Administrativo','Outro'
];
if(!DB.usuarios)DB.usuarios=[{id:1,nome:'Brunna Miranda',cargo:'Gestora Regulatória',email:'brunna@raiz.edu.br',setor:'Regulatório',ativo:true}];
DB.procs.forEach(p=>{if(!p.andamentos)p.andamentos=[];});

function save(){
  try{localStorage.setItem('rg_v3',JSON.stringify(DB));}catch(e){}
}

// ── HELPERS ───────────────────────────────────────────────────────────────────
const today=new Date();
function daysUntil(s){if(!s)return null;return Math.ceil((new Date(s)-today)/86400000);}
function fmtDate(s){if(!s)return '—';const[y,m,d]=s.split('-');return`${d}/${m}/${y}`;}
function todayISO(){return today.toISOString().split('T')[0];}

function statusFromDoc(d){
  if(d.status&&d.status!=='desconhecido')return d.status;
  if(!d.data_vencimento)return'desconhecido';
  const n=daysUntil(d.data_vencimento);
  if(n<0)return'vencido';if(n<=60)return'a_vencer';return'ok';
}
function statusLabel(s){
  return{ok:'✅ OK',a_vencer:'⚠️ A vencer',vencido:'🔴 Vencido',pendente:'❌ Pendente',
         desconhecido:'❓ S/ info',aberto:'🔴 Aberto',cumprido:'🟢 Cumprido',aguardando:'🟡 Aguardando'}[s]||s;
}
function stClass(s){
  if(s==='ok')return'ok';if(s==='a_vencer')return'warn';
  if(s==='vencido'||s==='pendente')return'danger';
  if(s==='cumprido')return'ok';if(s==='aberto')return'danger';if(s==='aguardando')return'warn';
  return'gray';
}
function conformity(s){
  const known=s.ok_docs+s.criticos+s.a_vencer;
  if(!known)return null;
  return Math.round(s.ok_docs/known*100);
}
function conformityColor(p){
  if(p===null)return'#9CA3AF';if(p>=80)return'#22C55E';if(p>=50)return'#F59E0B';return'#EF4444';
}
function esc(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function nextId(arr){return arr.length?Math.max(...arr.map(x=>x.id||0))+1:1;}
function avatarColor(name){
  const colors=['#2D6BE4','#7C3AED','#059669','#D97706','#DC2626','#0891B2','#9333EA'];
  return colors[(name||'?').charCodeAt(0)%colors.length];
}

// ── NAVIGATION ────────────────────────────────────────────────────────────────
let cur='dashboard';
const state={docsPage:1,docsF:{rede:'',status:'',tipo:'',q:''},
             escolasF:{rede:'',q:'',status_u:''},procsF:{status:'',q:''},ctF:{q:'',regional:''},
             finF:{q:'',categoria:'',status:'',escola:'',ano:''},finPage:1,
             tarefasF:{q:'',status:'',resp:'',prioridade:'',escola:''},tarefasPage:1,
             calYear:new Date().getFullYear(),calMonth:new Date().getMonth()};
const TITLES={dashboard:'Dashboard',docs:'Documentos',processos:'Processos SEI',
  tarefas:'Tarefas',treinamentos:'Treinamentos Obrigatórios',
  escolas:'Escolas',etap:'ETAP',legislacoes:'Legislações & Modelos',
  licencas:'Licenças & Alvarás',financeiro:'Financeiro',
  contatos:'Contatos SEEDUC',calendario:'Calendário',auditoria:'Auditoria & Conformidade',
  relatorios:'Relatórios',config:'Configurações'};

function go(s){
  cur=s;
  document.querySelectorAll('.ni').forEach(el=>el.classList.toggle('active',el.dataset.s===s));
  document.getElementById('page-title').textContent=TITLES[s]||s;
  render();
}
function render(){
  const el=document.getElementById('main-content');
  const map={dashboard:renderDashboard,docs:renderDocs,processos:renderProcessos,
             tarefas:renderTarefas,treinamentos:renderTreinamentos,
             escolas:renderEscolas,etap:renderEtap,
             legislacoes:renderLegislacoes,licencas:renderLicencas,
             contatos:renderContatos,financeiro:renderFinanceiro,
             calendario:renderCalendario,auditoria:renderAuditoria,
             relatorios:renderRelatorios,config:renderConfig};
  el.innerHTML=(map[cur]||renderWIP)();
  lucide.createIcons();
  updateHeader();
  updateNotifs();
}

function updateHeader(){
  const v=DB.docs.filter(d=>statusFromDoc(d)==='vencido').length;
  document.getElementById('hd-stats').textContent=`${DB.schools.length} escolas · ${v} vencimentos críticos`;
}

// ── NOTIFICATIONS ─────────────────────────────────────────────────────────────
let notifOpen=false;
function updateNotifs(){
  const v=DB.docs.filter(d=>statusFromDoc(d)==='vencido');
  const w=DB.docs.filter(d=>statusFromDoc(d)==='a_vencer');
  const ab=DB.procs.filter(p=>p.status==='aberto');
  const tot=v.length+w.length+ab.length;
  document.getElementById('notif-count').textContent=tot>99?'99+':tot;
  document.getElementById('notif-badge').textContent=tot+' alertas';
  const items=[
    ...v.slice(0,5).map(d=>({t:`🔴 Doc. vencido — ${d.escola}`,d:`${d.tipo} · ${fmtDate(d.data_vencimento)}`})),
    ...w.slice(0,3).map(d=>({t:`🟡 Vence em breve — ${d.escola}`,d:`${d.tipo} · ${fmtDate(d.data_vencimento)}`})),
    ...ab.slice(0,3).map(p=>({t:`📋 Processo aberto — ${p.escola||'—'}`,d:p.numero})),
  ].slice(0,10);
  document.getElementById('notif-list').innerHTML=items.map(n=>`
    <div style="padding:10px 16px;border-bottom:1px solid var(--border);cursor:pointer"
         onmouseover="this.style.background='#f9fafb'" onmouseout="this.style.background=''">
      <div style="font-size:13px;font-weight:500">${esc(n.t)}</div>
      <div style="font-size:11px;color:var(--muted);margin-top:2px">${esc(n.d)}</div>
    </div>`).join('')||'<div style="padding:20px;text-align:center;color:var(--muted);font-size:13px">Sem alertas</div>';
}
function toggleNotif(){notifOpen=!notifOpen;document.getElementById('notif-panel').style.display=notifOpen?'block':'none';}
document.addEventListener('click',e=>{
  const btn=document.getElementById('notif-btn'),pan=document.getElementById('notif-panel');
  if(!btn.contains(e.target)&&!pan.contains(e.target)){notifOpen=false;pan.style.display='none';}
});

// ── DASHBOARD ─────────────────────────────────────────────────────────────────
function renderDashboard(){
  const docs=DB.docs.map(d=>({...d,_s:statusFromDoc(d)}));
  const venc=docs.filter(d=>d._s==='vencido').length;
  const pend=docs.filter(d=>d._s==='pendente').length;
  const avencer=docs.filter(d=>d._s==='a_vencer').length;
  const ab=DB.procs.filter(p=>p.status==='aberto').length;
  const known=docs.filter(d=>['ok','vencido','a_vencer','pendente'].includes(d._s));
  const conf=known.length?Math.round(docs.filter(d=>d._s==='ok').length/known.length*100):0;
  const tipos=[...new Set(DB.docs.map(d=>d.tipo))].sort();
  const farolCards=tipos.map(tipo=>{
    const items=docs.filter(d=>d.tipo===tipo);
    const ok=items.filter(d=>d._s==='ok').length;
    const w=items.filter(d=>d._s==='a_vencer').length;
    const bad=items.filter(d=>['vencido','pendente'].includes(d._s)).length;
    let st='ok';if(bad>0)st='danger';else if(w>0)st='warn';
    const nd=items.filter(d=>d.data_vencimento).sort((a,b)=>a.data_vencimento.localeCompare(b.data_vencimento));
    const next=nd.length?fmtDate(nd[0].data_vencimento):'—';
    return`<div class="card fc" onclick="go('docs')">
      <div class="fc-head"><div class="fc-name">${esc(tipo)}</div>
        <span class="badge ${st}">${{ok:'Regular',warn:'Atenção',danger:'Crítico'}[st]}</span></div>
      <div style="display:flex;gap:10px;font-size:11px;color:var(--muted);margin-top:6px">
        <span>🟢 ${ok}</span><span>🟡 ${w}</span><span>🔴 ${bad}</span></div>
      <div style="font-size:10px;color:var(--muted);margin-top:4px">Próx. venc.: ${next}</div>
    </div>`;
  }).join('');
  const proximos=docs.filter(d=>d.data_vencimento&&d._s!=='desconhecido')
    .sort((a,b)=>a.data_vencimento.localeCompare(b.data_vencimento)).slice(0,12);
  const timeline=proximos.map(d=>{
    const days=daysUntil(d.data_vencimento);
    const dt=days===null?'':days<0?`(${Math.abs(days)}d atrás)`:days===0?'(hoje)':`(em ${days}d)`;
    const c={ok:'var(--green)',a_vencer:'var(--yellow)',vencido:'var(--red)',pendente:'var(--red)'}[d._s]||'#9CA3AF';
    return`<div class="tl-item">
      <div class="tl-dot" style="background:${c}"></div>
      <div class="tl-body">
        <div class="tl-title">${esc(d.escola)} <span class="tag rede">${esc(d.rede)}</span></div>
        <div class="tl-meta">${esc(d.tipo)} · ${fmtDate(d.data_vencimento)} ${dt}</div>
      </div>
      <span class="st ${stClass(d._s)}" style="font-size:10px">${statusLabel(d._s)}</span>
    </div>`;
  }).join('')||'<div class="empty"><div class="empty-sub">Sem vencimentos registrados</div></div>';
  const procRows=DB.procs.filter(p=>p.status==='aberto').map(p=>`
    <div class="tl-item">
      <div class="tl-dot" style="background:var(--red)"></div>
      <div class="tl-body">
        <div class="tl-title" style="font-size:12px">${esc(p.numero)}</div>
        <div class="tl-meta">${esc(p.escola||'—')} · ${esc(p.forma_exigencia||'—')}</div>
        <div class="tl-meta" style="color:#374151;margin-top:2px">${esc(p.prazo||'—')}</div>
      </div>
    </div>`).join('')||'<div class="empty"><div class="empty-sub">Sem processos abertos</div></div>';
  const porRede={};
  DB.schools.forEach(s=>{
    if(!porRede[s.rede])porRede[s.rede]={escolas:0,criticos:0};
    porRede[s.rede].escolas++;porRede[s.rede].criticos+=(s.criticos||0);
  });
  const redeRows=Object.entries(porRede).sort((a,b)=>b[1].criticos-a[1].criticos).map(([r,v])=>`
    <tr><td><span class="tag rede">${esc(r)}</span></td><td>${v.escolas}</td>
    <td>${v.criticos>0?`<span style="color:var(--red);font-weight:700">${v.criticos}</span>`:'<span style="color:var(--green)">0</span>'}</td></tr>`).join('');
  return`
  <div class="kpi-grid">
    <div class="card"><div class="kpi-lbl">Total de Escolas</div><div class="kpi-val">${DB.schools.length}</div><div class="kpi-sub">em ${DB.redes.length} redes</div></div>
    <div class="card"><div class="kpi-lbl">Docs Vencidos / Pendentes</div><div class="kpi-val danger">${venc+pend}</div><div class="kpi-sub">${venc} vencidos · ${pend} pendentes</div></div>
    <div class="card"><div class="kpi-lbl">Processos SEI Abertos</div><div class="kpi-val warn">${ab}</div><div class="kpi-sub">${DB.procs.filter(p=>p.status==='cumprido').length} cumpridos</div></div>
    <div class="card"><div class="kpi-lbl">Conformidade Geral</div><div class="kpi-val ok">${conf}%</div><div class="kpi-sub">docs com status: ${known.length} de ${DB.docs.length}</div></div>
  </div>
  <div class="sh"><div><div class="sh-title">Faróis por Tipo de Documento</div>
    <div class="sh-sub">Status consolidado de ${DB.docs.length} documentos em ${DB.schools.length} escolas</div></div>
  </div>
  <div class="farol-grid">${farolCards}</div>
  <div class="two-col">
    <div class="card"><div class="sh"><div class="sh-title">⏰ Vencimentos / Pendências</div>
      <button class="btn btn-sec btn-sm" onclick="go('docs')">Ver todos</button></div>${timeline}</div>
    <div style="display:flex;flex-direction:column;gap:16px">
      <div class="card"><div class="sh"><div class="sh-title">📋 Processos SEI Abertos</div>
        <button class="btn btn-sec btn-sm" onclick="go('processos')">Ver todos</button></div>${procRows}</div>
      <div class="card"><div class="sh"><div class="sh-title">📊 Pendências por Rede</div></div>
        <table><thead><tr><th>Rede</th><th>Escolas</th><th>Críticos</th></tr></thead>
        <tbody>${redeRows}</tbody></table></div>
    </div>
  </div>`;
}

// ── DOCUMENTOS ────────────────────────────────────────────────────────────────
function renderDocs(){
  const f=state.docsF;
  const tipos=[...new Set(DB.docs.map(d=>d.tipo))].sort();
  const redes=[...new Set(DB.docs.map(d=>d.rede))].sort();
  let fl=DB.docs.map(d=>({...d,_s:statusFromDoc(d)}));
  if(f.rede)fl=fl.filter(d=>d.rede===f.rede);
  if(f.status)fl=fl.filter(d=>d._s===f.status);
  if(f.tipo)fl=fl.filter(d=>d.tipo===f.tipo);
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(d=>d.escola.toLowerCase().includes(q)||d.tipo.toLowerCase().includes(q));}
  fl.sort((a,b)=>{const o={vencido:0,pendente:1,a_vencer:2,ok:3,desconhecido:4};return(o[a._s]||5)-(o[b._s]||5);});
  const PG=30,tot=fl.length,pages=Math.max(1,Math.ceil(tot/PG)),p=Math.min(state.docsPage,pages);
  const slice=fl.slice((p-1)*PG,p*PG);
  const rows=slice.map(d=>{
    const days=d.data_vencimento?daysUntil(d.data_vencimento):null;
    const dt=days!==null?`<span style="font-size:10px;padding:1px 6px;border-radius:8px;font-weight:700;
      background:${days<0?'var(--rbg)':days<=30?'var(--ybg)':'var(--gbg)'};
      color:${days<0?'#991B1B':days<=30?'#92400E':'#15803D'}">${days<0?Math.abs(days)+'d atr.':days===0?'hoje':days+'d'}</span>`:'';
    return`<tr>
      <td onclick="openDocDetail(${d.id})" style="cursor:pointer"><div class="td-name">${esc(d.escola)}</div><div class="td-sub">${esc(d.rede)} · ${d.estado}</div></td>
      <td onclick="openDocDetail(${d.id})" style="cursor:pointer">${esc(d.tipo)}</td>
      <td><span class="st ${stClass(d._s)}">${statusLabel(d._s)}</span></td>
      <td>${d.situacao?`<span class="sit sit-${d.situacao}">${{'em_elaboracao':'📝 Elaborando','protocolado':'📬 Protocolado','em_analise':'🔍 Em análise','exigencia':'⚠️ Exigência','aprovado':'✅ Aprovado','arquivado':'📁 Arquivado'}[d.situacao]||d.situacao}</span>`:'<span style="color:var(--muted);font-size:11px">—</span>'}</td>
      <td style="font-size:11px;color:var(--muted)">${d.numero_protocolo?`<span style="font-size:10px">${esc(d.numero_protocolo)}</span>`:'—'}</td>
      <td>${fmtDate(d.data_vencimento)} ${dt}</td>
      <td><div class="act-btns">
        <button class="btn btn-sec btn-sm" onclick="openEditDoc(${d.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteDoc(${d.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div></td>
    </tr>`;
  }).join('');
  const pgBtns=Array.from({length:Math.min(pages,8)},(_,i)=>`<button class="pb${p===i+1?' active':''}" onclick="setDocsPage(${i+1})">${i+1}</button>`).join('');
  const cv=fl.filter(d=>d._s==='vencido'||d._s==='pendente').length;
  const cw=fl.filter(d=>d._s==='a_vencer').length;
  const co=fl.filter(d=>d._s==='ok').length;
  return`
  <div class="sh">
    <div><div class="sh-title">Documentos Regulatórios</div>
      <div class="sh-sub"><span style="color:var(--red);font-weight:600">${cv} críticos</span> · <span style="color:var(--yellow);font-weight:600">${cw} atenção</span> · <span style="color:var(--green);font-weight:600">${co} ok</span> · ${tot} total</div>
    </div>
    <button class="btn btn-pri" onclick="openNewDoc()"><i data-lucide="plus" style="width:14px;height:14px"></i>Novo Documento</button>
  </div>
  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar escola ou tipo..." value="${esc(f.q)}" oninput="state.docsF.q=this.value;state.docsPage=1;render()"></div>
    <select class="fs" onchange="state.docsF.rede=this.value;state.docsPage=1;render()">
      <option value="">Todas as redes</option>${redes.map(r=>`<option value="${esc(r)}"${f.rede===r?' selected':''}>${esc(r)}</option>`).join('')}</select>
    <select class="fs" onchange="state.docsF.tipo=this.value;state.docsPage=1;render()">
      <option value="">Todos os tipos</option>${tipos.map(t=>`<option value="${esc(t)}"${f.tipo===t?' selected':''}>${esc(t)}</option>`).join('')}</select>
    <select class="fs" onchange="state.docsF.status=this.value;state.docsPage=1;render()">
      <option value="">Todos os status</option>
      <option value="vencido"${f.status==='vencido'?' selected':''}>🔴 Vencido</option>
      <option value="a_vencer"${f.status==='a_vencer'?' selected':''}>🟡 A vencer</option>
      <option value="pendente"${f.status==='pendente'?' selected':''}>❌ Pendente</option>
      <option value="ok"${f.status==='ok'?' selected':''}>✅ OK</option>
      <option value="desconhecido"${f.status==='desconhecido'?' selected':''}>❓ S/ info</option>
    </select>
  </div>
  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr><th>Escola / Rede</th><th>Tipo</th><th>Validade</th><th>Situação SEEDUC/SME</th><th>Protocolo</th><th>Vencimento</th><th></th></tr></thead>
    <tbody>${rows||'<tr><td colspan="7"><div class="empty"><div class="empty-icon">📂</div><div class="empty-title">Nenhum documento encontrado</div></div></td></tr>'}</tbody></table>
  </div>
  <div class="pag"><div class="pag-info">Exibindo ${Math.min((p-1)*PG+1,tot)}–${Math.min(p*PG,tot)} de ${tot}</div>
    <div class="pag-btns">${pgBtns}</div></div>`;
}
function setDocsPage(p){state.docsPage=p;render();}

function openDocDetail(id){
  const d=DB.docs.find(x=>x.id===id);if(!d)return;
  const st=statusFromDoc(d);
  const days=d.data_vencimento?daysUntil(d.data_vencimento):null;
  const daysText=days===null?'—':days<0?`Vencido há ${Math.abs(days)} dias`:days===0?'Vence hoje':`Vence em ${days} dias`;
  showModal('Detalhe do Documento',`
    <div style="display:grid;gap:12px">
      <div><label>Escola</label><div style="font-weight:600">${esc(d.escola)}</div></div>
      <div class="fr"><div><label>Rede</label><div>${esc(d.rede)}</div></div><div><label>Estado</label><div>${d.estado}</div></div></div>
      <div><label>Tipo</label><div style="font-weight:600">${esc(d.tipo)}</div></div>
      <div class="fr">
        <div><label>Status</label><div><span class="st ${stClass(st)}">${statusLabel(st)}</span></div></div>
        <div><label>Vencimento</label><div>${fmtDate(d.data_vencimento)}</div></div>
      </div>
      <div><label>Prazo</label><div style="font-weight:600;color:${days!==null&&days<0?'var(--red)':days!==null&&days<=30?'var(--yellow)':'inherit'}">${daysText}</div></div>
      ${d.observacoes?`<div><label>Observações</label><div style="font-size:12px;background:var(--sec);padding:8px;border-radius:6px">${esc(d.observacoes)}</div></div>`:''}
    </div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Fechar</button>
     <button class="btn btn-pri" onclick="closeModal();openEditDoc(${id})"><i data-lucide="pencil" style="width:13px;height:13px"></i>Editar</button>`
  );
}

function openEditDoc(id){
  const d=DB.docs.find(x=>x.id===id)||{};
  const tipos=[...new Set(DB.docs.map(x=>x.tipo))].sort();
  showModal(id?'Editar Documento':'Novo Documento',`
    <div id="ef-escola" class="fg"><label>Escola</label><div style="font-weight:600;font-size:14px">${esc(d.escola||'')}</div></div>
    <div class="fg"><label>Tipo de Documento</label>
      <select class="fi" id="ef-tipo"><option value="">Selecione...</option>
        ${tipos.map(t=>`<option value="${esc(t)}"${d.tipo===t?' selected':''}>${esc(t)}</option>`).join('')}
      </select></div>
    <div class="fr">
      <div class="fg"><label>Validade</label>
        <select class="fi" id="ef-status">
          <option value="ok"${d.status==='ok'?' selected':''}>✅ OK</option>
          <option value="a_vencer"${d.status==='a_vencer'?' selected':''}>⚠️ A vencer</option>
          <option value="vencido"${d.status==='vencido'?' selected':''}>🔴 Vencido</option>
          <option value="pendente"${d.status==='pendente'?' selected':''}>❌ Pendente</option>
          <option value="desconhecido"${(d.status==='desconhecido'||!d.status)?' selected':''}>❓ Desconhecido</option>
        </select></div>
      <div class="fg"><label>Vencimento</label>
        <input type="date" class="fi" id="ef-data" value="${d.data_vencimento||''}"></div>
    </div>
    <div class="fg"><label>Situação no Processo SEEDUC/SME</label>
      <select class="fi" id="ef-situacao">
        <option value=""${!d.situacao?' selected':''}>— Não aplicável / sem processo —</option>
        <option value="em_elaboracao"${d.situacao==='em_elaboracao'?' selected':''}>📝 Em elaboração</option>
        <option value="protocolado"${d.situacao==='protocolado'?' selected':''}>📬 Protocolado</option>
        <option value="em_analise"${d.situacao==='em_analise'?' selected':''}>🔍 Em análise pela SEC</option>
        <option value="exigencia"${d.situacao==='exigencia'?' selected':''}>⚠️ Exigência pendente</option>
        <option value="aprovado"${d.situacao==='aprovado'?' selected':''}>✅ Aprovado</option>
        <option value="arquivado"${d.situacao==='arquivado'?' selected':''}>📁 Arquivado</option>
      </select></div>
    <div class="fr">
      <div class="fg"><label>Número de Protocolo</label>
        <input type="text" class="fi" id="ef-protocolo" value="${esc(d.numero_protocolo||'')}" placeholder="Ex: SEI-030001/001234/2025"></div>
      <div class="fg"><label>Data de Protocolo</label>
        <input type="date" class="fi" id="ef-dt-protocolo" value="${d.data_protocolo||''}"></div>
    </div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="ef-obs" rows="3">${esc(d.observacoes||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveDoc(${id})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

const RENEWAL_MONTHS={'Licença Sanitária':12,'Alvará de Funcionamento':12,'Vigilância Sanitária':12,
  'AVCB / Bombeiros':24,'Corpo de Bombeiros':24,'Certidão Negativa':6,
  'PAA':0,'ETAP':0,'Habite-se':0,'PPP':12,'Regimento Interno':24,
  'Ato Autorizativo - Sec. Educação':0};

function saveDoc(id){
  const tipo=document.getElementById('ef-tipo').value;
  const status=document.getElementById('ef-status').value;
  const data=document.getElementById('ef-data').value;
  const obs=document.getElementById('ef-obs').value.trim();
  const situacao=document.getElementById('ef-situacao').value;
  const protocolo=document.getElementById('ef-protocolo').value.trim();
  const dtProto=document.getElementById('ef-dt-protocolo').value;
  if(!tipo){showToast('Selecione o tipo de documento','error');return;}
  const idx=DB.docs.findIndex(x=>x.id===id);
  if(idx>=0){
    const prev=DB.docs[idx];
    Object.assign(DB.docs[idx],{tipo,status,data_vencimento:data||null,observacoes:obs||null,
      situacao:situacao||null,numero_protocolo:protocolo||null,data_protocolo:dtProto||null});
    // Renovação automática: se documento marcado ok/aprovado com vencimento
    const meses=RENEWAL_MONTHS[tipo];
    if(meses&&meses>0&&data&&(status==='ok')&&prev.status!=='ok'){
      const venc=new Date(data);venc.setMonth(venc.getMonth()-2); // alerta 2 meses antes
      const prazoISO=venc.toISOString().split('T')[0];
      const escola=DB.docs[idx].escola;
      const jaExiste=DB.tarefas.some(t=>t.titulo&&t.titulo.includes('Renovar')&&t.titulo.includes(tipo)&&t.escola===escola&&t.status==='pendente');
      if(!jaExiste){
        DB.tarefas.push({id:nextId(DB.tarefas),titulo:`Renovar ${tipo}`,
          descricao:`Iniciar processo de renovação — vencimento em ${fmtDate(data)}`,
          responsavel:DB.usuarios[0]?.nome||null,escola,
          categoria:'Alvará/Licença',prioridade:'media',prazo:prazoISO,
          status:'pendente',criada_em:todayISO()});
        showToast(`✅ Tarefa de renovação criada automaticamente para ${fmtDate(data)}!`);
      }
    }
  }
  save();closeModal();render();showToast('Documento salvo!');
}

function openNewDoc(){
  const tipos=[...new Set(DB.docs.map(x=>x.tipo))].sort();
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));
  const redes=[...new Set(DB.schools.map(s=>s.rede))].sort();
  showModal('Novo Documento',`
    <div class="fg"><label>Escola *</label>
      <select class="fi" id="nd-escola" onchange="updateNdRede(this)">
        <option value="">Selecione a escola...</option>
        ${escolas.map(s=>`<option value="${s.id}" data-rede="${esc(s.rede)}" data-nome="${esc(s.nome)}">${esc(s.nome)} (${esc(s.rede)})</option>`).join('')}
      </select></div>
    <div class="fg"><label>Tipo de Documento *</label>
      <select class="fi" id="nd-tipo"><option value="">Selecione...</option>
        ${tipos.map(t=>`<option value="${esc(t)}">${esc(t)}</option>`).join('')}
        <option value="_custom">Outro (digitar abaixo)</option>
      </select></div>
    <div class="fg" id="nd-custom-wrap" style="display:none"><label>Tipo personalizado</label>
      <input type="text" class="fi" id="nd-custom" placeholder="Ex: Laudo CREA..."></div>
    <div class="fr">
      <div class="fg"><label>Status</label>
        <select class="fi" id="nd-status">
          <option value="desconhecido">❓ Desconhecido</option>
          <option value="ok">✅ OK</option>
          <option value="a_vencer">⚠️ A vencer</option>
          <option value="vencido">🔴 Vencido</option>
          <option value="pendente">❌ Pendente</option>
        </select></div>
      <div class="fg"><label>Vencimento</label>
        <input type="date" class="fi" id="nd-data"></div>
    </div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="nd-obs" rows="2"></textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="addDoc()"><i data-lucide="plus" style="width:13px;height:13px"></i>Adicionar</button>`
  );
  document.getElementById('nd-tipo').onchange=function(){
    document.getElementById('nd-custom-wrap').style.display=this.value==='_custom'?'block':'none';
  };
}

function updateNdRede(){}

function addDoc(){
  const selEscola=document.getElementById('nd-escola');
  const escolaId=parseInt(selEscola.value);
  const selOpt=selEscola.options[selEscola.selectedIndex];
  const escolaNome=selOpt?selOpt.dataset.nome:'';
  const rede=selOpt?selOpt.dataset.rede:'';
  const tipoSel=document.getElementById('nd-tipo').value;
  const tipo=tipoSel==='_custom'?document.getElementById('nd-custom').value.trim():tipoSel;
  const status=document.getElementById('nd-status').value;
  const data=document.getElementById('nd-data').value;
  const obs=document.getElementById('nd-obs').value.trim();
  const escola=DB.schools.find(s=>s.id===escolaId);
  if(!escolaId||!tipo){showToast('Preencha escola e tipo','error');return;}
  const newDoc={id:nextId(DB.docs),escola:escolaNome,escola_id:escolaId,rede,estado:escola?escola.estado:'',
                tipo,status,data_vencimento:data||null,observacoes:obs||null};
  DB.docs.push(newDoc);
  save();closeModal();render();showToast('Documento adicionado!');
}

function deleteDoc(id){
  if(!confirm('Excluir este documento?'))return;
  DB.docs=DB.docs.filter(d=>d.id!==id);
  save();render();showToast('Documento excluído','error');
}

// ── PROCESSOS ─────────────────────────────────────────────────────────────────
function renderProcessos(){
  const f=state.procsF;
  let fl=[...DB.procs];
  if(f.status)fl=fl.filter(p=>p.status===f.status);
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(p=>p.numero.toLowerCase().includes(q)||(p.escola||'').toLowerCase().includes(q)||(p.forma_exigencia||'').toLowerCase().includes(q));}
  const ab=DB.procs.filter(p=>p.status==='aberto').length;
  const cu=DB.procs.filter(p=>p.status==='cumprido').length;
  const rows=fl.map(p=>`
    <tr>
      <td onclick="openProcDetail(${p.id})" style="cursor:pointer">
        <div class="td-name" style="font-size:12px">${esc(p.numero)}</div></td>
      <td style="font-size:11px">${p.tipo_processo?`<span class="tag rede" style="font-size:10px">${esc(p.tipo_processo)}</span>`:'<span style="color:var(--muted)">—</span>'}</td>
      <td onclick="openProcDetail(${p.id})" style="cursor:pointer">
        <div class="td-name">${esc(p.escola||'—')}</div><div class="td-sub">${esc(p.rede||'—')}</div></td>
      <td style="font-size:12px;max-width:140px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(p.forma_exigencia||'—')}</td>
      <td style="font-size:12px;color:var(--acc);font-weight:500">${p.responsavel?`<span>👤 ${esc(p.responsavel)}</span>`:'<span style="color:var(--muted)">—</span>'}</td>
      <td style="font-size:12px;max-width:160px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(p.prazo||'—')}</td>
      <td><span class="proc-status ps-${p.status}">${statusLabel(p.status)}</span></td>
      <td style="text-align:center">
        ${(()=>{const it=p.checklist_items||[];const d=it.filter(i=>i.done).length,t=it.length;
          if(!t)return`<button class="btn btn-sec btn-sm" style="font-size:10px" onclick="openProcDetail(${p.id})">
            <i data-lucide="plus" style="width:10px;height:10px"></i>Adicionar</button>`;
          const pct=Math.round(d/t*100);
          return`<div onclick="openProcDetail(${p.id})" style="cursor:pointer">
            <div style="font-size:10px;font-weight:700;color:${pct===100?'var(--green)':pct>=60?'var(--yellow)':'var(--red)'};margin-bottom:3px">${d}/${t} — ${pct}%</div>
            <div style="width:60px;height:5px;background:#e5e7eb;border-radius:3px;overflow:hidden;margin:0 auto">
              <div style="height:100%;width:${pct}%;background:${pct===100?'var(--green)':pct>=60?'var(--yellow)':'var(--red)'};border-radius:3px"></div>
            </div></div>`;})()}
      </td>
      <td><div class="act-btns">
        <button class="btn btn-pri btn-sm" onclick="openProcDetail(${p.id})" title="Andamentos e Checklist">
          <i data-lucide="list-checks" style="width:11px;height:11px"></i>Checklist</button>
        <button class="btn btn-sec btn-sm" onclick="openEditProc(${p.id})" title="Editar processo">
          <i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteProc(${p.id})" title="Excluir">
          <i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div></td>
    </tr>`).join('');
  return`
  <div class="sh">
    <div><div class="sh-title">Processos SEI Regulatórios</div>
      <div class="sh-sub"><span style="color:var(--red);font-weight:600">${ab} abertos</span> · <span style="color:var(--green);font-weight:600">${cu} cumpridos</span></div>
    </div>
    <button class="btn btn-pri" onclick="openNewProc()"><i data-lucide="plus" style="width:14px;height:14px"></i>Novo Processo</button>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:18px">
    <div class="card" style="padding:14px;cursor:pointer" onclick="state.procsF.status='';render()">
      <div class="kpi-lbl">Total</div><div class="kpi-val">${DB.procs.length}</div></div>
    <div class="card" style="padding:14px;cursor:pointer" onclick="state.procsF.status='aberto';render()">
      <div class="kpi-lbl">Em Aberto</div><div class="kpi-val danger">${ab}</div></div>
    <div class="card" style="padding:14px;cursor:pointer" onclick="state.procsF.status='cumprido';render()">
      <div class="kpi-lbl">Cumpridos</div><div class="kpi-val ok">${cu}</div></div>
  </div>
  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Número, escola, exigência..." value="${esc(f.q)}" oninput="state.procsF.q=this.value;render()"></div>
    <select class="fs" onchange="state.procsF.status=this.value;render()">
      <option value="">Todos os status</option>
      <option value="aberto"${f.status==='aberto'?' selected':''}>🔴 Aberto</option>
      <option value="cumprido"${f.status==='cumprido'?' selected':''}>🟢 Cumprido</option>
      <option value="aguardando"${f.status==='aguardando'?' selected':''}>🟡 Aguardando</option>
    </select>
  </div>
  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr><th>Número</th><th>Tipo</th><th>Escola</th><th>Exigência</th><th>Responsável</th><th>Prazo</th><th>Status</th><th>📋 Checklist</th><th></th></tr></thead>
    <tbody>${rows||'<tr><td colspan="7"><div class="empty"><div class="empty-icon">📋</div><div class="empty-title">Nenhum processo encontrado</div></div></td></tr>'}</tbody></table>
  </div>`;
}

function openProcDetail(id){
  const p=DB.procs.find(x=>x.id===id);if(!p)return;
  if(!p.andamentos)p.andamentos=[];
  const andHtml=p.andamentos.length?p.andamentos.map(a=>`
    <div class="and-item">
      <div class="and-date">${fmtDate(a.data)} · ${esc(a.autor||'')}</div>
      <div class="and-text">${esc(a.texto)}</div>
    </div>`).join(''):'<div style="color:var(--muted);font-size:12px;margin-bottom:8px">Nenhum andamento registrado.</div>';
  showModal('Processo SEI — Detalhes',`
    <div style="display:grid;gap:10px">
      <div><label>Número</label><div style="font-weight:700;font-size:13px;word-break:break-all">${esc(p.numero)}</div></div>
      <div class="fr">
        <div><label>Escola</label><div style="font-weight:600">${esc(p.escola||'—')}</div></div>
        <div><label>Rede</label><div>${esc(p.rede||'—')}</div></div>
      </div>
      <div><label>Forma da Exigência</label><div>${esc(p.forma_exigencia||'—')}</div></div>
      <div class="fr">
        <div><label>Data Recebimento</label><div style="font-size:12px">${esc(p.data_recebimento||'—')}</div></div>
        <div><label>Status</label><div><span class="proc-status ps-${p.status}">${statusLabel(p.status)}</span></div></div>
      </div>
      <div><label>Prazo / Cumprimento</label><div style="font-size:12px">${esc(p.prazo||'—')}</div></div>
      ${p.observacoes?`<div><label>Observações</label><div style="font-size:12px;background:var(--sec);padding:8px;border-radius:6px">${esc(p.observacoes)}</div></div>`:''}
    </div>
    <div class="divider"></div>
    <div style="font-weight:700;font-size:13px;margin-bottom:10px">📋 Andamentos</div>
    <div id="andamentos-list">${andHtml}</div>
    <div style="background:var(--sec);border-radius:8px;padding:12px;margin-top:8px">
      <label>Novo Andamento</label>
      <textarea class="fi" id="novo-and" rows="2" placeholder="Descreva o andamento..." style="margin-bottom:8px"></textarea>
      <div class="fr">
        <input type="date" class="fi" id="novo-and-data" value="${todayISO()}">
        <button class="btn btn-pri btn-sm" onclick="addAndamento(${id})">
          <i data-lucide="plus" style="width:12px;height:12px"></i>Adicionar</button>
      </div>
    </div>
    ${renderChecklistSection(p)}`,
    `<button class="btn btn-sec" onclick="closeModal()">Fechar</button>
     <button class="btn btn-sec" onclick="scrollToChecklist()" title="Ir para checklist">
       <i data-lucide="list-checks" style="width:13px;height:13px"></i>Ver Checklist</button>
     <button class="btn btn-pri" onclick="closeModal();openEditProc(${id})"><i data-lucide="pencil" style="width:13px;height:13px"></i>Editar</button>`
  ,'modal-lg');
  // Scroll automático para o checklist se já tiver itens
  setTimeout(()=>{
    const chkEl=document.getElementById('chk-list-'+id);
    if(chkEl)chkEl.scrollIntoView({behavior:'smooth',block:'start'});
  },120);
}

function scrollToChecklist(){
  const modal=document.querySelector('.modal');
  if(!modal)return;
  // Encontra a div do checklist dentro do modal
  const chkDivs=modal.querySelectorAll('[id^="chk-list-"]');
  if(chkDivs.length>0){chkDivs[0].scrollIntoView({behavior:'smooth',block:'start'});}
}

function addAndamento(procId){
  const txt=document.getElementById('novo-and').value.trim();
  const dt=document.getElementById('novo-and-data').value;
  if(!txt){showToast('Digite o andamento','error');return;}
  const p=DB.procs.find(x=>x.id===procId);if(!p)return;
  if(!p.andamentos)p.andamentos=[];
  p.andamentos.push({id:Date.now(),data:dt||todayISO(),texto:txt,autor:'Brunna Miranda'});
  save();
  const andHtml=p.andamentos.map(a=>`
    <div class="and-item">
      <div class="and-date">${fmtDate(a.data)} · ${esc(a.autor)}</div>
      <div class="and-text">${esc(a.texto)}</div>
    </div>`).join('');
  document.getElementById('andamentos-list').innerHTML=andHtml;
  document.getElementById('novo-and').value='';
  showToast('Andamento registrado!');
}

function openEditProc(id){
  const p=DB.procs.find(x=>x.id===id)||{};
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));
  showModal(id?'Editar Processo SEI':'Novo Processo SEI',`
    <div class="fr">
      <div class="fg"><label>Número SEI *</label>
        <input type="text" class="fi" id="ep-num" value="${esc(p.numero||'')}" placeholder="Ex: SEI-030001/063541/2024"></div>
      <div class="fg"><label>Tipo de Processo</label>
        <select class="fi" id="ep-tipo">
          <option value="">Selecione o tipo...</option>
          ${DB.tipos_processo.map(t=>`<option value="${esc(t)}"${p.tipo_processo===t?' selected':''}>${esc(t)}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
    <div class="fg"><label>Escola</label>
      <select class="fi" id="ep-escola">
        <option value="">— sem escola —</option>
        ${escolas.map(s=>`<option value="${s.id}" data-rede="${esc(s.rede)}" data-nome="${esc(s.nome)}"${p.escola_id===s.id?' selected':''}>${esc(s.nome)} (${esc(s.rede)})</option>`).join('')}
      </select></div>
    <div class="fg"><label>Responsável</label>
      <select class="fi" id="ep-resp">
        <option value="">— sem responsável —</option>
        ${DB.usuarios.filter(u=>u.ativo).map(u=>`<option value="${esc(u.nome)}"${p.responsavel===u.nome?' selected':''}>${esc(u.nome)} — ${esc(u.cargo||'')}</option>`).join('')}
      </select></div>
    </div>
    <div class="fg"><label>Forma da Exigência</label>
      <input type="text" class="fi" id="ep-forma" value="${esc(p.forma_exigencia||'')}" placeholder="Ex: E-mail com exigência"></div>
    <div class="fr">
      <div class="fg"><label>Data de Recebimento</label>
        <input type="text" class="fi" id="ep-rec" value="${esc(p.data_recebimento||'')}" placeholder="Ex: 27/03/2025"></div>
      <div class="fg"><label>Status</label>
        <select class="fi" id="ep-status">
          <option value="aberto"${p.status==='aberto'?' selected':''}>🔴 Aberto</option>
          <option value="aguardando"${p.status==='aguardando'?' selected':''}>🟡 Aguardando</option>
          <option value="cumprido"${p.status==='cumprido'?' selected':''}>🟢 Cumprido</option>
          <option value="arquivado"${p.status==='arquivado'?' selected':''}>⚫ Arquivado</option>
        </select></div>
    </div>
    <div class="fg"><label>Prazo / Data de Cumprimento</label>
      <input type="text" class="fi" id="ep-prazo" value="${esc(p.prazo||'')}" placeholder="Ex: Cumprir até 30/05/2025"></div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="ep-obs" rows="3">${esc(p.observacoes||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveProc(${id})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

function openNewProc(){openEditProc(0);}

function saveProc(id){
  const num=document.getElementById('ep-num').value.trim();
  if(!num){showToast('Preencha o número do processo','error');return;}
  const selEscola=document.getElementById('ep-escola');
  const escolaId=parseInt(selEscola.value)||null;
  const selOpt=selEscola.options[selEscola.selectedIndex];
  const escolaNome=escolaId&&selOpt?selOpt.dataset.nome:'';
  const rede=escolaId&&selOpt?selOpt.dataset.rede:'';
  const updates={numero:num,escola:escolaNome,escola_id:escolaId,rede,
    tipo_processo:document.getElementById('ep-tipo').value||null,
    responsavel:document.getElementById('ep-resp').value||null,
    forma_exigencia:document.getElementById('ep-forma').value.trim()||null,
    data_recebimento:document.getElementById('ep-rec').value.trim()||null,
    status:document.getElementById('ep-status').value,
    prazo:document.getElementById('ep-prazo').value.trim()||null,
    observacoes:document.getElementById('ep-obs').value.trim()||null};
  if(id>0){
    const idx=DB.procs.findIndex(x=>x.id===id);
    if(idx>=0)Object.assign(DB.procs[idx],updates);
  }else{
    DB.procs.push({id:nextId(DB.procs),andamentos:[],...updates});
  }
  save();closeModal();render();showToast('Processo salvo!');
}

function deleteProc(id){
  if(!confirm('Excluir este processo?'))return;
  DB.procs=DB.procs.filter(p=>p.id!==id);
  save();render();showToast('Processo excluído','error');
}

// ── ESCOLAS ───────────────────────────────────────────────────────────────────
const STATUS_UNIDADE={
  'em_funcionamento':{label:'Em funcionamento',color:'#22C55E',bg:'#DCFCE7',cls:'ok'},
  'encerrada_seeduc':{label:'Encerrada na SEEDUC',color:'#F59E0B',bg:'#FEF3C7',cls:'warn'},
  'fechada':{label:'Fechada',color:'#EF4444',bg:'#FEE2E2',cls:'danger'},
};
function stUnidade(s){return STATUS_UNIDADE[s.status_unidade]||STATUS_UNIDADE['em_funcionamento'];}

function renderEscolas(){
  const f=state.escolasF;
  const redes=[...new Set(DB.schools.map(s=>s.rede))].sort();
  let fl=[...DB.schools];
  if(f.rede)fl=fl.filter(s=>s.rede===f.rede);
  if(f.status_u)fl=fl.filter(s=>(s.status_unidade||'em_funcionamento')===f.status_u);
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(s=>s.nome.toLowerCase().includes(q));}
  const cards=fl.map(s=>{
    const conf=conformity(s);const cc=conformityColor(conf);
    const docSt=s.criticos>0?'danger':s.a_vencer>0?'warn':'ok';
    const docLbl=s.criticos>0?`${s.criticos} crítico(s)`:s.a_vencer>0?`${s.a_vencer} a vencer`:'Em dia';
    const unSt=stUnidade(s);
    return`<div class="card sc" onclick="openEscolaDrawer(${s.id})"
      style="${s.status_unidade==='fechada'?'opacity:.75;':''}${s.status_unidade==='encerrada_seeduc'?'border-left:4px solid #F59E0B;':''}">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:4px">
        <div class="sc-name" style="${s.status_unidade==='fechada'?'text-decoration:line-through;color:var(--muted)':''}">${esc(s.nome)}</div>
        <span class="badge ${docSt}">${docLbl}</span>
      </div>
      <div style="margin-bottom:5px">
        <span style="display:inline-flex;align-items:center;gap:4px;padding:2px 8px;border-radius:20px;
                      font-size:10px;font-weight:700;background:${unSt.bg};color:${unSt.color}">
          ${ {em_funcionamento:'🟢',encerrada_seeduc:'🟡',fechada:'🔴'}[s.status_unidade||'em_funcionamento'] } ${unSt.label}
        </span>
      </div>
      <div class="sc-meta">${esc(s.rede)} · ${s.estado}</div>
      ${s.cnpj?`<div style="font-size:10px;color:var(--muted);margin-bottom:2px">CNPJ: ${s.cnpj}</div>`:''}
      ${s.codigo_censo?`<div style="font-size:10px;color:var(--muted);margin-bottom:6px">INEP/Censo: <strong>${s.codigo_censo}</strong></div>`:`<div style="font-size:10px;color:#f59e0b;margin-bottom:6px;cursor:pointer" onclick="event.stopPropagation();openEditEscola(${s.id})">⚠️ INEP não informado</div>`}
      <div style="font-size:11px;color:var(--muted);margin-bottom:3px">Conformidade: <strong style="color:${cc}">${conf!==null?conf+'%':'s/ dados'}</strong> · ${s.total_docs} docs</div>
      <div class="pbar"><div class="pbar-fill" style="width:${conf||0}%;background:${cc}"></div></div>
      <div style="display:flex;gap:8px;font-size:10px;color:var(--muted);margin-top:5px;align-items:center">
        <span>🟢 ${s.ok_docs}</span><span>🟡 ${s.a_vencer}</span><span>🔴 ${s.criticos}</span>
        <span style="margin-left:auto">📁 ${(DB.arquivos||[]).filter(a=>a.escola_id===s.id).length}</span>
      </div>
      <div style="display:flex;gap:6px;margin-top:10px">
        <button class="btn btn-pri btn-sm" style="flex:1;justify-content:center" onclick="event.stopPropagation();openEditEscola(${s.id})">
          <i data-lucide="pencil" style="width:11px;height:11px"></i>Editar</button>
        <button class="btn btn-danger btn-sm" onclick="event.stopPropagation();deleteEscola(${s.id})">
          <i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div>
    </div>`;
  }).join('');
  return`
  <div class="sh">
    <div><div class="sh-title">Escolas Cadastradas</div>
      <div class="sh-sub">
        ${fl.length} de ${DB.schools.length} escolas ·
        <span style="color:var(--green);font-weight:600">${DB.schools.filter(s=>!s.status_unidade||s.status_unidade==='em_funcionamento').length} em funcionamento</span> ·
        <span style="color:var(--yellow);font-weight:600">${DB.schools.filter(s=>s.status_unidade==='encerrada_seeduc').length} encerradas SEEDUC</span> ·
        <span style="color:var(--red);font-weight:600">${DB.schools.filter(s=>s.status_unidade==='fechada').length} fechadas</span>
      </div></div>
    <button class="btn btn-pri" onclick="openEditEscola(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Nova Escola</button>
  </div>
  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar escola..." value="${esc(f.q)}" oninput="state.escolasF.q=this.value;render()"></div>
    <select class="fs" onchange="state.escolasF.rede=this.value;render()">
      <option value="">Todas as redes</option>
      ${redes.map(r=>`<option value="${esc(r)}"${f.rede===r?' selected':''}>${esc(r)}</option>`).join('')}
    </select>
    <select class="fs" onchange="state.escolasF.status_u=this.value;render()">
      <option value="">Todos os status</option>
      <option value="em_funcionamento"${f.status_u==='em_funcionamento'?' selected':''}>🟢 Em funcionamento</option>
      <option value="encerrada_seeduc"${f.status_u==='encerrada_seeduc'?' selected':''}>🟡 Encerrada na SEEDUC</option>
      <option value="fechada"${f.status_u==='fechada'?' selected':''}>🔴 Fechada</option>
    </select>
  </div>
  <div class="sc-grid">${cards||'<div class="empty"><div class="empty-icon">🏫</div><div class="empty-title">Nenhuma escola encontrada</div></div>'}</div>`;
}

function openEscolaDrawer(id){
  const s=DB.schools.find(x=>x.id===id);if(!s)return;
  const conf=conformity(s);const cc=conformityColor(conf);
  const sDocs=DB.docs.map(d=>({...d,_s:statusFromDoc(d)})).filter(d=>d.escola_id===id);
  const sProcs=DB.procs.filter(p=>p.escola_id===id);
  const docRows=sDocs.map(d=>`
    <div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border)">
      <span class="dot ${stClass(d._s)}"></span>
      <div style="flex:1"><div style="font-size:13px;font-weight:500">${esc(d.tipo)}</div>
        <div style="font-size:11px;color:var(--muted)">${fmtDate(d.data_vencimento)}</div></div>
      <span class="st ${stClass(d._s)}" style="font-size:10px">${statusLabel(d._s)}</span>
      <button class="btn btn-sec btn-sm" onclick="closeDrawer();openEditDoc(${d.id})">
        <i data-lucide="pencil" style="width:11px;height:11px"></i></button>
    </div>`).join('')||'<div style="color:var(--muted);font-size:12px;padding:8px 0">Sem documentos cadastrados</div>';
  const procRows=sProcs.map(p=>`
    <div style="padding:8px 0;border-bottom:1px solid var(--border)">
      <div style="font-size:12px;font-weight:500">${esc(p.numero)}</div>
      <div style="font-size:11px;color:var(--muted)">${esc(p.forma_exigencia||'—')} · ${esc(p.prazo||'—')}</div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:4px">
        <span class="proc-status ps-${p.status}" style="font-size:10px">${statusLabel(p.status)}</span>
        <button class="btn btn-sec btn-sm" onclick="closeDrawer();openProcDetail(${p.id})">
          <i data-lucide="list" style="width:11px;height:11px"></i></button>
      </div>
    </div>`).join('')||'<div style="color:var(--muted);font-size:12px;padding:8px 0">Sem processos vinculados</div>';
  document.getElementById('drawer-root').innerHTML=`
    <div class="drw-ov" onclick="closeDrawer()"></div>
    <div class="drw">
      <div class="drw-hd">
        <div><div style="font-size:16px;font-weight:700">${esc(s.nome)}</div>
          <div style="font-size:12px;color:var(--muted)">${esc(s.rede)} · ${s.estado}</div></div>
        <div style="display:flex;gap:6px;align-items:center">
          <button class="btn btn-sec btn-sm" onclick="openEditEscola(${s.id})">
            <i data-lucide="pencil" style="width:11px;height:11px"></i>Editar</button>
          <button class="btn btn-danger btn-sm" onclick="deleteEscola(${s.id})">
            <i data-lucide="trash-2" style="width:11px;height:11px"></i>Excluir</button>
          <button class="mc" onclick="closeDrawer()"><i data-lucide="x" style="width:14px;height:14px"></i></button>
        </div>
      </div>
      <div class="drw-body">
        <div style="margin-bottom:12px">
          ${(()=>{const u=stUnidade(s);return`<span style="display:inline-flex;align-items:center;gap:6px;
            padding:5px 14px;border-radius:20px;font-size:12px;font-weight:700;
            background:${u.bg};color:${u.color}">
            ${{em_funcionamento:'🟢',encerrada_seeduc:'🟡',fechada:'🔴'}[s.status_unidade||'em_funcionamento']} ${u.label}
          </span>`;})()}
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px">
          <div class="card" style="padding:12px"><div class="kpi-lbl">Conformidade</div>
            <div style="font-size:22px;font-weight:800;color:${cc}">${conf!==null?conf+'%':'—'}</div></div>
          <div class="card" style="padding:12px"><div class="kpi-lbl">Docs Críticos</div>
            <div style="font-size:22px;font-weight:800;color:var(--red)">${s.criticos}</div></div>
        </div>
        <div style="background:var(--sec);border-radius:8px;padding:10px 12px;margin-bottom:12px;font-size:12px;display:grid;grid-template-columns:1fr 1fr;gap:6px">
          ${s.cnpj?`<div><span style="color:var(--muted);font-size:10px;font-weight:600;text-transform:uppercase">CNPJ</span><div style="font-weight:600;margin-top:1px">${s.cnpj}</div></div>`:''}
          ${s.inscricao_municipal?`<div><span style="color:var(--muted);font-size:10px;font-weight:600;text-transform:uppercase">Insc. Municipal</span><div style="font-weight:600;margin-top:1px">${s.inscricao_municipal}</div></div>`:''}
          <div style="grid-column:1/-1">
            <span style="color:var(--muted);font-size:10px;font-weight:600;text-transform:uppercase">Código INEP / Censo Escolar</span>
            <div style="display:flex;align-items:center;gap:8px;margin-top:3px">
              ${s.codigo_censo
                ?`<span style="font-size:15px;font-weight:800;color:var(--pri);letter-spacing:1px">${esc(s.codigo_censo)}</span>`
                :`<span style="color:#f59e0b;font-size:12px;font-weight:600">⚠️ Não informado</span>`}
              <button class="btn btn-sec btn-sm" style="padding:2px 8px;font-size:10px" onclick="openEditEscola(${id})">
                <i data-lucide="pencil" style="width:10px;height:10px"></i>${s.codigo_censo?'Alterar':'Informar'}</button>
            </div>
          </div>
          ${s.estado?`<div><span style="color:var(--muted);font-size:10px;font-weight:600;text-transform:uppercase">Estado</span><div style="font-weight:600;margin-top:1px">${s.estado}</div></div>`:''}
        </div>
        ${s.o_que_funciona?`<div style="font-size:12px;padding:8px;background:var(--sec);border-radius:6px;margin-bottom:10px">🏫 ${esc(s.o_que_funciona)}</div>`:''}
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <div style="font-weight:700;font-size:13px">📄 Documentos (${sDocs.length})</div>
          <button class="btn btn-pri btn-sm" onclick="closeDrawer();openNewDocForSchool(${id})">
            <i data-lucide="plus" style="width:11px;height:11px"></i>Add Doc</button>
        </div>
        ${docRows}
        <div class="divider"></div>
        <div style="font-weight:700;font-size:13px;margin-bottom:8px">📋 Processos SEI (${sProcs.length})</div>
        ${procRows}
        <div class="divider"></div>
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">
          <div style="font-weight:700;font-size:13px">
            📁 Arquivos Importados (${(DB.arquivos||[]).filter(a=>a.escola_id===id).length})
          </div>
          <button class="btn btn-pri btn-sm" onclick="showImportArquivoModal(${id},'${esc(s.nome)}')">
            <i data-lucide="upload" style="width:11px;height:11px"></i>Importar Arquivo</button>
        </div>
        <div id="escola-files-${id}">${renderArquivosEscola(id)}</div>
      </div>
    </div>`;
  lucide.createIcons();
}

function openNewDocForSchool(escolaId){
  const s=DB.schools.find(x=>x.id===escolaId);
  openNewDoc();
  setTimeout(()=>{
    const sel=document.getElementById('nd-escola');
    if(sel)sel.value=escolaId;
  },50);
}

function closeDrawer(){document.getElementById('drawer-root').innerHTML='';}

function openEditEscola(id){
  const s=id?DB.schools.find(x=>x.id===id):null;
  const redes=[...new Set(DB.schools.map(x=>x.rede))].sort();
  const defStatus=s?s.status_unidade||'em_funcionamento':'em_funcionamento';
  showModal(id?'Editar Escola':'Nova Escola',`
    <div class="fr">
      <div class="fg"><label>Nome da Escola *</label>
        <input type="text" class="fi" id="es-nome" value="${esc(s?s.nome:'')}" placeholder="Nome completo da escola"></div>
      <div class="fg"><label>Rede</label>
        <div style="display:flex;gap:6px">
          <select class="fi" id="es-rede" style="flex:1">
            ${redes.map(r=>`<option value="${esc(r)}"${s&&s.rede===r?' selected':''}>${esc(r)}</option>`).join('')}
            <option value="__nova__">+ Nova rede...</option>
          </select>
        </div>
        <input type="text" class="fi" id="es-rede-nova" placeholder="Nome da nova rede"
               style="margin-top:6px;display:none" oninput="">
      </div>
    </div>
    <div class="fr">
      <div class="fg"><label>CNPJ</label>
        <input type="text" class="fi" id="es-cnpj" value="${esc(s?s.cnpj||'':'')}" placeholder="00.000.000/0000-00"></div>
      <div class="fg"><label>Inscrição Municipal</label>
        <input type="text" class="fi" id="es-insc" value="${esc(s?s.inscricao_municipal||'':'')}"></div>
    </div>
    <div class="fg">
      <label style="font-size:13px;font-weight:700">🏫 Status da Unidade</label>
      <div style="display:flex;gap:8px;margin-top:4px">
        ${Object.entries(STATUS_UNIDADE).map(([k,v])=>`
          <label style="flex:1;cursor:pointer">
            <input type="radio" name="es-status-u" value="${k}" style="display:none" ${defStatus===k?'checked':''}>
            <div class="es-st-opt" data-val="${k}" style="padding:8px;border-radius:8px;text-align:center;
                 border:2px solid ${defStatus===k?v.color:'var(--border)'};
                 background:${defStatus===k?v.bg:'white'};
                 font-size:11px;font-weight:700;color:${v.color};transition:.15s;cursor:pointer"
                 onclick="selectEsStatusU('${k}')">
              ${{em_funcionamento:'🟢',encerrada_seeduc:'🟡',fechada:'🔴'}[k]} ${v.label}
            </div>
          </label>`).join('')}
      </div>
    </div>
    <div class="fg">
      <label style="font-size:13px;font-weight:700;color:var(--pri)">🏛️ Código INEP / Número do Censo Escolar</label>
      <input type="text" class="fi" id="es-censo" value="${esc(s?s.codigo_censo||'':'')}"
             placeholder="Ex: 33012345" maxlength="8"
             style="font-size:18px;font-weight:700;letter-spacing:2px;text-align:center;border-color:var(--acc)">
      <div style="font-size:11px;color:var(--muted);margin-top:4px">Código de 8 dígitos atribuído pelo INEP.</div>
    </div>
    <div class="fr">
      <div class="fg"><label>Estado (UF)</label>
        <select class="fi" id="es-estado">
          ${['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO'].map(uf=>`<option value="${uf}"${s&&s.estado===uf?' selected':''}>${uf}</option>`).join('')}
        </select></div>
      <div class="fg"><label>O que funciona na escola</label>
        <input type="text" class="fi" id="es-funciona" value="${esc(s?s.o_que_funciona||'':'')}" placeholder="Ex: Fundamental, Médio..."></div>
    </div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="es-obs" rows="2">${esc(s?s.observacoes||'':'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     ${id?`<button class="btn btn-danger" onclick="deleteEscola(${id});closeModal()"><i data-lucide="trash-2" style="width:13px;height:13px"></i>Excluir</button>`:''}
     <button class="btn btn-pri" onclick="saveEscola(${id||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
  // Mostrar campo rede nova quando seleciona "+ Nova rede"
  setTimeout(()=>{const sel=document.getElementById('es-rede');
    if(sel)sel.onchange=()=>{const inp=document.getElementById('es-rede-nova');if(inp)inp.style.display=sel.value==='__nova__'?'block':'none';};},50);
}

function selectEsStatusU(val){
  document.querySelectorAll('.es-st-opt').forEach(el=>{
    const v=el.dataset.val;
    const u=STATUS_UNIDADE[v];
    if(v===val){el.style.borderColor=u.color;el.style.background=u.bg;}
    else{el.style.borderColor='var(--border)';el.style.background='white';}
  });
  document.querySelector(`input[name="es-status-u"][value="${val}"]`).checked=true;
}

function saveEscola(id){
  const nome=document.getElementById('es-nome').value.trim();
  if(!nome){showToast('Nome é obrigatório','error');return;}
  const censo=document.getElementById('es-censo').value.trim().replace(/\D/g,'');
  if(censo&&(censo.length<6||censo.length>8)){showToast('Código INEP deve ter 6 a 8 dígitos','error');return;}
  const statusU=document.querySelector('input[name="es-status-u"]:checked');
  const redeEl=document.getElementById('es-rede');
  let rede=redeEl?redeEl.value:'';
  if(rede==='__nova__'){
    const nova=document.getElementById('es-rede-nova');
    rede=(nova?nova.value:'').trim();
    if(!rede){showToast('Digite o nome da nova rede','error');return;}
    if(!DB.redes.find(r=>r.nome===rede))DB.redes.push({id:nextId(DB.redes),nome:rede});
  }
  const rec={nome,rede,
    cnpj:document.getElementById('es-cnpj').value.trim()||null,
    inscricao_municipal:document.getElementById('es-insc').value.trim()||null,
    codigo_censo:censo||null,
    status_unidade:statusU?statusU.value:'em_funcionamento',
    estado:document.getElementById('es-estado').value,
    o_que_funciona:document.getElementById('es-funciona').value.trim()||null,
    observacoes:document.getElementById('es-obs').value.trim()||null,
    ativa:1,ok_docs:0,a_vencer:0,criticos:0,total_docs:0};
  if(id>0){
    const idx=DB.schools.findIndex(x=>x.id===id);
    if(idx>=0)Object.assign(DB.schools[idx],rec);
    save();closeModal();showToast(`"${nome}" atualizada!`);
    openEscolaDrawer(id);
  }else{
    const novaEscola={id:nextId(DB.schools),...rec};
    DB.schools.push(novaEscola);
    save();closeModal();render();showToast(`"${nome}" cadastrada!`);
  }
}

function deleteEscola(id){
  const s=DB.schools.find(x=>x.id===id);if(!s)return;
  const docs=DB.docs.filter(d=>d.escola_id===id).length;
  const arqs=(DB.arquivos||[]).filter(a=>a.escola_id===id).length;
  const msg=`Excluir "${s.nome}"?\n\n${docs} documentos, ${arqs} arquivos e todos os dados vinculados serão removidos permanentemente.`;
  if(!confirm(msg))return;
  DB.schools=DB.schools.filter(x=>x.id!==id);
  DB.docs=DB.docs.filter(d=>d.escola_id!==id);
  DB.procs=DB.procs.filter(p=>p.escola_id!==id);
  DB.tarefas=DB.tarefas.filter(t=>t.escola!==s.nome);
  DB.financeiro=DB.financeiro.filter(f=>f.escola!==s.nome);
  DB.arquivos=(DB.arquivos||[]).filter(a=>a.escola_id!==id);
  save();closeDrawer();render();showToast(`"${s.nome}" excluída`,'error');
}

// ── LICENÇAS ──────────────────────────────────────────────────────────────────
function renderLicencas(){
  const keywords=['Licença','Alvará','Sanitária','Bombeiros','Vigilância'];
  const fl=DB.docs.map(d=>({...d,_s:statusFromDoc(d)}))
    .filter(d=>keywords.some(k=>d.tipo.includes(k)))
    .sort((a,b)=>{const o={vencido:0,pendente:1,a_vencer:2,ok:3,desconhecido:4};return(o[a._s]||5)-(o[b._s]||5);});
  if(!fl.length)return renderWIP();
  const rows=fl.map(d=>`
    <tr>
      <td><div class="td-name">${esc(d.escola)}</div><div class="td-sub">${esc(d.rede)} · ${d.estado}</div></td>
      <td>${esc(d.tipo)}</td>
      <td><span class="st ${stClass(d._s)}">${statusLabel(d._s)}</span></td>
      <td>${fmtDate(d.data_vencimento)}</td>
      <td style="font-size:11px;color:var(--muted);max-width:180px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(d.observacoes||'—')}</td>
      <td><div class="act-btns">
        <button class="btn btn-sec btn-sm" onclick="openEditDoc(${d.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
      </div></td>
    </tr>`).join('');
  const cv=fl.filter(d=>d._s==='vencido'||d._s==='pendente').length;
  const cw=fl.filter(d=>d._s==='a_vencer').length;
  return`
  <div class="sh"><div>
    <div class="sh-title">Licenças &amp; Alvarás</div>
    <div class="sh-sub"><span style="color:var(--red);font-weight:600">${cv} críticos</span> · <span style="color:var(--yellow);font-weight:600">${cw} atenção</span> · ${fl.length} total</div>
  </div></div>
  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr><th>Escola</th><th>Tipo</th><th>Status</th><th>Vencimento</th><th>Observações</th><th></th></tr></thead>
    <tbody>${rows}</tbody></table>
  </div>`;
}

// ── CONTATOS SEEDUC ───────────────────────────────────────────────────────────
function renderContatos(){
  const f=state.ctF;
  let fl=[...DB.contacts];
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(c=>(c.nome||'').toLowerCase().includes(q)||(c.email||'').toLowerCase().includes(q)||(c.regional||'').toLowerCase().includes(q));}
  if(f.regional)fl=fl.filter(c=>c.regional===f.regional);
  const regionais=[...new Set(DB.contacts.map(c=>c.regional).filter(Boolean))].sort();
  const cards=fl.map(c=>{
    const initials=(c.nome||'?').split(' ').map(w=>w[0]).slice(0,2).join('').toUpperCase();
    const bgColor=avatarColor(c.nome);
    return`<div class="card ct-card">
      <div style="display:flex;gap:12px;align-items:flex-start">
        <div class="ct-av" style="background:${bgColor}">${initials}</div>
        <div style="flex:1;min-width:0">
          <div class="ct-name">${esc(c.nome||'')}</div>
          <div class="ct-role">${esc(c.cargo||'')}${c.regional?` · ${esc(c.regional)}`:''}</div>
          <div class="ct-info">
            ${c.telefone?`<span>📞 ${esc(c.telefone)}</span>`:''}
            ${c.email?`<span>✉️ <a href="mailto:${esc(c.email)}" style="color:var(--acc)">${esc(c.email)}</a></span>`:''}
            ${c.escola_vinculada?`<span>🏫 ${esc(c.escola_vinculada)}</span>`:''}
          </div>
          ${c.observacoes?`<div style="font-size:11px;color:var(--muted);margin-top:6px;font-style:italic">${esc(c.observacoes)}</div>`:''}
        </div>
      </div>
      <div style="display:flex;gap:6px;margin-top:12px;justify-content:flex-end">
        <button class="btn btn-sec btn-sm" onclick="openEditContato(${c.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i>Editar</button>
        <button class="btn btn-danger btn-sm" onclick="deleteContato(${c.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div>
    </div>`;
  }).join('');
  const empty=`
    <div style="grid-column:1/-1">
      <div class="card" style="padding:60px 30px;text-align:center">
        <div style="font-size:48px;margin-bottom:16px">📞</div>
        <div style="font-size:17px;font-weight:700;margin-bottom:8px">Nenhum contato cadastrado</div>
        <div style="color:var(--muted);font-size:14px;margin-bottom:20px;max-width:400px;margin-left:auto;margin-right:auto">
          Cadastre aqui os inspetores, coordenadores e contatos da SEEDUC vinculados às suas escolas.
        </div>
        <button class="btn btn-pri" onclick="openEditContato(null)">
          <i data-lucide="plus" style="width:14px;height:14px"></i>Cadastrar primeiro contato
        </button>
      </div>
    </div>`;
  return`
  <div class="sh">
    <div><div class="sh-title">Contatos SEEDUC</div>
      <div class="sh-sub">Inspetores, coordenadores e fiscais vinculados às escolas · ${DB.contacts.length} cadastrado(s)</div></div>
    <button class="btn btn-pri" onclick="openEditContato(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Novo Contato</button>
  </div>
  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar nome, e-mail, regional..." value="${esc(f.q)}" oninput="state.ctF.q=this.value;render()"></div>
    ${regionais.length?`<select class="fs" onchange="state.ctF.regional=this.value;render()">
      <option value="">Todas as regionais</option>
      ${regionais.map(r=>`<option value="${esc(r)}"${f.regional===r?' selected':''}>${esc(r)}</option>`).join('')}
    </select>`:''}
  </div>
  <div class="ct-grid">${fl.length?cards:empty}</div>`;
}

function openEditContato(id){
  const c=id?DB.contacts.find(x=>x.id===id)||{}:{};
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));
  const cargos=['Inspetor Escolar','Coordenador Regional','Fiscal de Ensino','Supervisor Escolar',
                'Coordenador de Área','Chefe de Departamento','Outro'];
  const regionaisSEEDUC=['1ª CRE','2ª CRE','3ª CRE','4ª CRE','5ª CRE','6ª CRE','7ª CRE','8ª CRE','9ª CRE','10ª CRE',
                         'SEEDUC Central','SEEDUC Niterói','Outra'];
  showModal(id?'Editar Contato SEEDUC':'Novo Contato SEEDUC',`
    <div class="fr">
      <div class="fg"><label>Nome completo *</label>
        <input type="text" class="fi" id="ct-nome" value="${esc(c.nome||'')}" placeholder="Ex: Maria Silva Santos"></div>
      <div class="fg"><label>Cargo / Função *</label>
        <select class="fi" id="ct-cargo">
          <option value="">Selecione...</option>
          ${cargos.map(g=>`<option value="${g}"${c.cargo===g?' selected':''}>${g}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Regional SEEDUC</label>
        <select class="fi" id="ct-regional">
          <option value="">Selecione...</option>
          ${regionaisSEEDUC.map(r=>`<option value="${r}"${c.regional===r?' selected':''}>${r}</option>`).join('')}
        </select></div>
      <div class="fg"><label>Escola vinculada</label>
        <select class="fi" id="ct-escola">
          <option value="">— geral / todas —</option>
          ${escolas.map(s=>`<option value="${esc(s.nome)}"${c.escola_vinculada===s.nome?' selected':''}>${esc(s.nome)}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Telefone</label>
        <input type="tel" class="fi" id="ct-tel" value="${esc(c.telefone||'')}" placeholder="(21) 99999-0000"></div>
      <div class="fg"><label>E-mail</label>
        <input type="email" class="fi" id="ct-email" value="${esc(c.email||'')}" placeholder="nome@seeduc.rj.gov.br"></div>
    </div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="ct-obs" rows="3" placeholder="Área de atuação, horários, notas importantes...">${esc(c.observacoes||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveContato(${id||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

function saveContato(id){
  const nome=document.getElementById('ct-nome').value.trim();
  const cargo=document.getElementById('ct-cargo').value;
  if(!nome){showToast('Nome é obrigatório','error');return;}
  const data={nome,cargo,regional:document.getElementById('ct-regional').value,
    escola_vinculada:document.getElementById('ct-escola').value,
    telefone:document.getElementById('ct-tel').value.trim(),
    email:document.getElementById('ct-email').value.trim(),
    observacoes:document.getElementById('ct-obs').value.trim()};
  if(id>0){
    const idx=DB.contacts.findIndex(x=>x.id===id);
    if(idx>=0)Object.assign(DB.contacts[idx],data);
  }else{
    DB.contacts.push({id:nextId(DB.contacts),...data});
  }
  save();closeModal();render();showToast('Contato salvo!');
}

function deleteContato(id){
  if(!confirm('Excluir este contato?'))return;
  DB.contacts=DB.contacts.filter(c=>c.id!==id);
  save();render();showToast('Contato excluído','error');
}

// ── CHECKLIST TEMPLATES ───────────────────────────────────────────────────────
const CHK_TEMPLATES={
  seeduc_autorizacao:{label:'SEEDUC — Autorização de Funcionamento',orgao:'SEEDUC',items:[
    'Requerimento endereçado ao Diretor da SEEDUC',
    'Cópia autenticada do CNPJ',
    'Ato constitutivo da mantenedora',
    'Regimento Escolar aprovado pela SEEDUC',
    'ETAP — Estudo Técnico de Adequação de Projeto',
    'PAA — Plano de Adequação à Acessibilidade',
    'Habite-se do imóvel',
    'Alvará de Funcionamento da Prefeitura',
    'AVCB — Laudo do Corpo de Bombeiros válido',
    'Licença Sanitária da Vigilância Sanitária',
    'ART/RRT do responsável técnico',
    'Planta baixa aprovada (CREA ou CAU)',
    'Certidão negativa de débitos municipais',
    'Certidão negativa de débitos estaduais',
    'Certidão negativa de débitos federais (Receita Federal)',
  ]},
  seeduc_renovacao:{label:'SEEDUC — Renovação de Autorização',orgao:'SEEDUC',items:[
    'Requerimento de renovação endereçado à SEEDUC',
    'Relatório de atividades do ano letivo anterior',
    'ETAP atualizada',
    'PAA atualizado (se houver alterações)',
    'Certidões negativas válidas',
    'Ata do Conselho Escolar (atualizada)',
    'PPP — Projeto Político Pedagógico atualizado',
    'Regimento Interno atualizado',
    'Comprovante de pagamento de encargos escolares',
    'Dados atualizados no Educacenso (INEP)',
  ]},
  seeduc_transferencia:{label:'SEEDUC — Transferência de Mantenedora',orgao:'SEEDUC',items:[
    'Requerimento de transferência',
    'Contrato social da nova mantenedora',
    'CNPJ da nova mantenedora',
    'Ata de assembléia aprovando a transferência',
    'Certidões negativas da nova mantenedora',
    'Termo de responsabilidade assinado',
    'Documentação do imóvel (contrato de locação ou escritura)',
  ]},
  sme_alvara:{label:'SME — Alvará de Funcionamento',orgao:'SME',items:[
    'Requerimento endereçado à SME',
    'Cópia do CNPJ',
    'Habite-se do imóvel',
    'AVCB — Auto de Vistoria do Corpo de Bombeiros',
    'Licença Sanitária da Vigilância Sanitária Municipal',
    'Planta baixa aprovada pela Prefeitura',
    'ART ou RRT de responsável técnico',
    'Comprovante de endereço do imóvel',
    'Certidão negativa de débitos municipais',
  ]},
  sme_renovacao:{label:'SME — Renovação de Alvará',orgao:'SME',items:[
    'Requerimento de renovação',
    'AVCB dentro da validade',
    'Licença Sanitária válida',
    'Certidão negativa de débitos municipais',
    'Comprovante de pagamento da taxa de renovação',
    'Cadastro atualizado na Prefeitura',
  ]},
  sanitaria:{label:'Vigilância Sanitária — Renovação de Licença',orgao:'Vigilância Sanitária',items:[
    'Requerimento de renovação',
    'Comprovante de pagamento da taxa sanitária',
    'Planta baixa com destinação dos ambientes',
    'Manual de Boas Práticas (cantina/refeitório)',
    'Responsável técnico habilitado (nutricionista ou similar)',
    'Certificado de desinsetização/desratização',
    'Laudos de análise de água (se aplicável)',
    'Relatório de vistoria anterior (se solicitado)',
  ]},
  bombeiros:{label:'Corpo de Bombeiros — AVCB',orgao:'Corpo de Bombeiros',items:[
    'Requerimento de vistoria ao Corpo de Bombeiros',
    'Planta de incêndio aprovada',
    'ART/RRT do projeto de prevenção e combate a incêndios',
    'Extintores vistoriados e dentro do prazo de validade',
    'Sinalizações de emergência instaladas (saídas, rotas)',
    'Iluminação de emergência funcionando',
    'Alarme de incêndio operacional',
    'Hidrantes e mangueiras em condições de uso',
    'Porta corta-fogo instalada (se exigida)',
    'Brigada de incêndio treinada (lista de membros)',
    'Laudo anterior (CLCB ou AVCB) — para renovação',
  ]},
  crea_laudo:{label:'CREA — Laudo Técnico',orgao:'CREA',items:[
    'Contratação de engenheiro habilitado no CREA',
    'ART (Anotação de Responsabilidade Técnica) registrada',
    'Laudo de vistoria das instalações elétricas',
    'Laudo de vistoria das instalações hidráulicas (se aplicável)',
    'Laudo de acessibilidade (NBR 9050)',
    'Laudo estrutural do imóvel',
    'Planta baixa atualizada assinada pelo responsável técnico',
    'Comprovante de quitação de anuidade CREA do engenheiro',
  ]},
  inep_censo:{label:'INEP — Censo Escolar',orgao:'INEP/MEC',items:[
    'Código INEP da escola cadastrado',
    'Acesso ao sistema Educacenso confirmado',
    'Dados de matrícula atualizados por etapa/modalidade',
    'Dados de turmas atualizados',
    'Dados de docentes e funcionários atualizados',
    'Dados de infraestrutura atualizados (salas, laboratórios, etc.)',
    'Dados de equipamentos atualizados',
    'Validação pelo dirigente municipal ou estadual',
    'Declaração de encerramento de coleta assinada',
  ]},
  mec_recredenciamento:{label:'MEC — Recredenciamento de IES',orgao:'MEC',items:[
    'Formulário eletrônico no e-MEC preenchido',
    'PDI — Plano de Desenvolvimento Institucional atualizado',
    'Relatório de autoavaliação da CPA',
    'Relatório de avaliação institucional INEP/MEC anterior',
    'Demonstrações financeiras auditadas',
    'Titulação do corpo docente (Lattes atualizado)',
    'Infraestrutura física — memorial descritivo',
    'Acervo da biblioteca comprovado',
    'Certidões negativas da mantenedora',
  ]},
  custom:{label:'Checklist personalizado',orgao:'',items:[]},
};

function renderChecklistSection(p){
  if(!p.checklist_items)p.checklist_items=[];
  const items=p.checklist_items;
  const done=items.filter(i=>i.done).length;
  const total=items.length;
  const pct=total?Math.round(done/total*100):0;
  const tmplOpts=Object.entries(CHK_TEMPLATES).map(([k,v])=>`<option value="${k}">${v.label}</option>`).join('');
  const itemsHtml=items.map(item=>`
    <div style="display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid var(--border)">
      <input type="checkbox" ${item.done?'checked':''} style="margin-top:2px;accent-color:var(--green);width:16px;height:16px;flex-shrink:0;cursor:pointer"
             onchange="toggleChkItem(${p.id},${item.id},this.checked)">
      <div style="flex:1;min-width:0">
        <div style="font-size:13px;${item.done?'text-decoration:line-through;color:var(--muted)':''}">${esc(item.texto)}</div>
        ${item.obs?`<div style="font-size:11px;color:var(--muted);margin-top:2px">💬 ${esc(item.obs)}</div>`:''}
      </div>
      <button onclick="addChkObs(${p.id},${item.id})" title="Adicionar observação"
              style="background:none;border:none;cursor:pointer;color:var(--muted);font-size:13px;padding:0;line-height:1">✏️</button>
      <button onclick="deleteChkItem(${p.id},${item.id})"
              style="background:none;border:none;cursor:pointer;color:var(--muted);font-size:16px;padding:0;line-height:1">×</button>
    </div>`).join('');
  return`
  <div class="divider"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">
    <div style="font-weight:700;font-size:13px">📋 Checklist de Documentos</div>
    <div style="display:flex;gap:6px">
      <select class="fi" id="chk-tmpl-${p.id}" style="font-size:11px;padding:4px 8px;width:auto;max-width:220px">
        <option value="">Aplicar template...</option>${tmplOpts}
      </select>
      <button class="btn btn-sec btn-sm" onclick="applyChkTemplate(${p.id})">Aplicar</button>
    </div>
  </div>
  ${total>0?`
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
    <div style="flex:1;height:8px;background:var(--sec);border-radius:4px;overflow:hidden">
      <div style="height:100%;border-radius:4px;transition:width .3s;
                  background:${pct===100?'var(--green)':pct>=60?'var(--yellow)':'var(--red)'};
                  width:${pct}%"></div>
    </div>
    <span style="font-size:12px;font-weight:700;color:${pct===100?'var(--green)':pct>=60?'var(--yellow)':'var(--red)'};flex-shrink:0">
      ${done}/${total} — ${pct}% ${pct===100?'✅ Completo':'concluído'}
    </span>
  </div>`:''}
  <div id="chk-list-${p.id}">${itemsHtml||'<div style="color:var(--muted);font-size:12px;padding:10px 0;text-align:center">Nenhum item. Aplique um template ou adicione manualmente.</div>'}</div>
  <div style="display:flex;gap:8px;margin-top:10px;background:var(--sec);border-radius:8px;padding:10px">
    <input type="text" class="fi" id="chk-new-${p.id}" placeholder="Adicionar documento ou item personalizado..."
           style="margin:0" onkeydown="if(event.key==='Enter')addChkItem(${p.id})">
    <button class="btn btn-pri btn-sm" onclick="addChkItem(${p.id})" style="flex-shrink:0;white-space:nowrap">
      <i data-lucide="plus" style="width:12px;height:12px"></i>Adicionar
    </button>
  </div>`;
}

function toggleChkItem(procId,itemId,done){
  const p=DB.procs.find(x=>x.id===procId);
  if(!p||!p.checklist_items)return;
  const item=p.checklist_items.find(i=>i.id===itemId);
  if(item)item.done=done;
  save();
  // Atualiza barra de progresso sem fechar modal
  const items=p.checklist_items;
  const d=items.filter(i=>i.done).length,t=items.length;
  const pct=t?Math.round(d/t*100):0;
  // Re-render só a barra
  openProcDetail(procId);
}

function addChkItem(procId){
  const input=document.getElementById('chk-new-'+procId);
  const texto=(input?input.value:'').trim();
  if(!texto){showToast('Digite o item','error');return;}
  const p=DB.procs.find(x=>x.id===procId);if(!p)return;
  if(!p.checklist_items)p.checklist_items=[];
  p.checklist_items.push({id:Date.now(),texto,done:false,obs:''});
  save();openProcDetail(procId);showToast('Item adicionado!');
}

function deleteChkItem(procId,itemId){
  const p=DB.procs.find(x=>x.id===procId);if(!p||!p.checklist_items)return;
  p.checklist_items=p.checklist_items.filter(i=>i.id!==itemId);
  save();openProcDetail(procId);
}

function applyChkTemplate(procId){
  const sel=document.getElementById('chk-tmpl-'+procId);
  const key=sel?sel.value:'';
  if(!key){showToast('Selecione um template','error');return;}
  const tmpl=CHK_TEMPLATES[key];if(!tmpl)return;
  const p=DB.procs.find(x=>x.id===procId);if(!p)return;
  if(p.checklist_items&&p.checklist_items.length>0&&!confirm('Substituir checklist atual pelo template "'+tmpl.label+'"?'))return;
  p.checklist_items=tmpl.items.map((texto,i)=>({id:Date.now()+i,texto,done:false,obs:''}));
  save();openProcDetail(procId);showToast(`Template "${tmpl.label}" aplicado!`);
}

function addChkObs(procId,itemId){
  const p=DB.procs.find(x=>x.id===procId);if(!p)return;
  const item=p.checklist_items&&p.checklist_items.find(i=>i.id===itemId);if(!item)return;
  const obs=prompt('Observação para: "'+item.texto+'"',item.obs||'');
  if(obs===null)return;
  item.obs=obs.trim();
  save();openProcDetail(procId);
}

// ── TAREFAS ───────────────────────────────────────────────────────────────────
const TAREFA_CATS=['Alvará/Licença','Processo SEI','Financeiro','Documento','Auditoria','Vigilância Sanitária','Outro'];
const PRIORIDADES={alta:{label:'🔴 Alta',cls:'danger'},media:{label:'🟡 Média',cls:'warn'},baixa:{label:'🟢 Baixa',cls:'ok'}};
const TAREFA_STATUS={pendente:'⏳ Pendente',em_andamento:'🔵 Em Andamento',concluida:'✅ Concluída',cancelada:'✖ Cancelada'};

function renderTarefas(){
  const f=state.tarefasF;
  let fl=[...DB.tarefas];
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(t=>(t.titulo||'').toLowerCase().includes(q)||(t.escola||'').toLowerCase().includes(q));}
  if(f.status)fl=fl.filter(t=>t.status===f.status);
  if(f.resp)fl=fl.filter(t=>t.responsavel===f.resp);
  if(f.prioridade)fl=fl.filter(t=>t.prioridade===f.prioridade);
  if(f.escola)fl=fl.filter(t=>t.escola===f.escola);
  fl.sort((a,b)=>{const op={alta:0,media:1,baixa:2};const os=op[a.prioridade||'baixa']-op[b.prioridade||'baixa'];return os||((a.prazo||'').localeCompare(b.prazo||''));});

  const PG=30,tot=fl.length,pages=Math.max(1,Math.ceil(tot/PG)),p=Math.min(state.tarefasPage,pages);
  const slice=fl.slice((p-1)*PG,p*PG);
  const respOpts=[...new Set(DB.tarefas.map(t=>t.responsavel).filter(Boolean))].sort();
  const escolaOpts=[...new Set(DB.tarefas.map(t=>t.escola).filter(Boolean))].sort();

  // KPI cols
  const kpis=['pendente','em_andamento','concluida','cancelada'].map(s=>{
    const cnt=DB.tarefas.filter(t=>t.status===s).length;
    const cls={pendente:'warn',em_andamento:'info',concluida:'ok',cancelada:'gray'}[s]||'gray';
    return`<div class="card" style="padding:14px;cursor:pointer" onclick="state.tarefasF.status=state.tarefasF.status==='${s}'?'':'${s}';render()">
      <div class="kpi-lbl">${TAREFA_STATUS[s].replace(/[⏳🔵✅✖]/g,'').trim()}</div>
      <div class="kpi-val ${cls}">${cnt}</div></div>`;
  }).join('');

  const rows=slice.map(t=>{
    const pr=PRIORIDADES[t.prioridade||'media'];
    const days=t.prazo&&t.status!=='concluida'?daysUntil(t.prazo):null;
    const daysTag=days!==null?`<span style="font-size:10px;padding:1px 5px;border-radius:6px;font-weight:700;
      background:${days<0?'var(--rbg)':days<=7?'var(--rbg)':days<=30?'var(--ybg)':'var(--gbg)'};
      color:${days<0?'#991B1B':days<=7?'#991B1B':days<=30?'#92400E':'#15803D'}">${days<0?Math.abs(days)+'d atr.':days+'d'}</span>`:'';
    return`<tr>
      <td onclick="openEditTarefa(${t.id})" style="cursor:pointer">
        <div class="td-name">${esc(t.titulo||'—')}</div>
        ${t.descricao?`<div class="td-sub" style="max-width:240px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(t.descricao)}</div>`:''}
      </td>
      <td><span class="badge ${pr.cls}" style="font-size:10px">${pr.label}</span></td>
      <td style="font-size:12px">${t.responsavel?`<span style="color:var(--acc);font-weight:500">👤 ${esc(t.responsavel)}</span>`:'<span style="color:var(--muted)">—</span>'}</td>
      <td style="font-size:12px">${esc(t.escola||'—')}</td>
      <td style="font-size:12px;color:var(--muted)">${esc(t.categoria||'—')}</td>
      <td>${fmtDate(t.prazo)} ${daysTag}</td>
      <td><span class="badge ${{pendente:'warn',em_andamento:'blue',concluida:'ok',cancelada:'gray'}[t.status]||'gray'}">${TAREFA_STATUS[t.status]||t.status}</span></td>
      <td><div class="act-btns">
        <button class="btn btn-sec btn-sm" onclick="openEditTarefa(${t.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteTarefa(${t.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div></td>
    </tr>`;
  }).join('');

  const pgBtns=Array.from({length:Math.min(pages,8)},(_,i)=>`<button class="pb${p===i+1?' active':''}" onclick="state.tarefasPage=${i+1};render()">${i+1}</button>`).join('');

  return`
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px">${kpis}</div>
  <div class="sh">
    <div><div class="sh-title">Tarefas e Ações</div>
      <div class="sh-sub">${tot} tarefa(s) · ${DB.tarefas.filter(t=>t.status==='pendente'&&t.prazo&&daysUntil(t.prazo)<=7&&daysUntil(t.prazo)>=0).length} urgentes (7 dias)</div></div>
    <button class="btn btn-pri" onclick="openEditTarefa(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Nova Tarefa</button>
  </div>
  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar tarefa ou escola..." value="${esc(f.q)}" oninput="state.tarefasF.q=this.value;state.tarefasPage=1;render()"></div>
    <select class="fs" onchange="state.tarefasF.status=this.value;state.tarefasPage=1;render()">
      <option value="">Todos os status</option>
      ${Object.entries(TAREFA_STATUS).map(([k,v])=>`<option value="${k}"${f.status===k?' selected':''}>${v}</option>`).join('')}
    </select>
    <select class="fs" onchange="state.tarefasF.prioridade=this.value;state.tarefasPage=1;render()">
      <option value="">Todas as prioridades</option>
      ${Object.entries(PRIORIDADES).map(([k,v])=>`<option value="${k}"${f.prioridade===k?' selected':''}>${v.label}</option>`).join('')}
    </select>
    <select class="fs" onchange="state.tarefasF.resp=this.value;state.tarefasPage=1;render()">
      <option value="">Todos os responsáveis</option>
      ${DB.usuarios.filter(u=>u.ativo).map(u=>`<option value="${esc(u.nome)}"${f.resp===u.nome?' selected':''}>${esc(u.nome)}</option>`).join('')}
    </select>
    ${escolaOpts.length?`<select class="fs" onchange="state.tarefasF.escola=this.value;state.tarefasPage=1;render()">
      <option value="">Todas as escolas</option>
      ${escolaOpts.map(e=>`<option value="${esc(e)}"${f.escola===e?' selected':''}>${esc(e)}</option>`).join('')}
    </select>`:''}
  </div>
  ${DB.tarefas.length===0?`
  <div class="card" style="padding:60px 30px;text-align:center">
    <div style="font-size:48px;margin-bottom:14px">✅</div>
    <div style="font-size:17px;font-weight:700;margin-bottom:8px">Nenhuma tarefa cadastrada</div>
    <div style="color:var(--muted);font-size:14px;max-width:420px;margin:0 auto 20px">
      Crie tarefas para rastrear renovações, pagamentos e ações regulatórias.
      Atribua um responsável e defina o prazo.
    </div>
    <button class="btn btn-pri" onclick="openEditTarefa(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Criar primeira tarefa</button>
  </div>`:`
  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr>
      <th>Tarefa</th><th>Prioridade</th><th>Responsável</th><th>Escola</th>
      <th>Categoria</th><th>Prazo</th><th>Status</th><th></th>
    </tr></thead>
    <tbody>${rows||'<tr><td colspan="8"><div class="empty"><div class="empty-icon">🔍</div><div class="empty-title">Nenhuma tarefa encontrada</div></div></td></tr>'}</tbody></table>
  </div>
  ${tot>PG?`<div class="pag"><div class="pag-info">Exibindo ${Math.min((p-1)*PG+1,tot)}–${Math.min(p*PG,tot)} de ${tot}</div>
    <div class="pag-btns">${pgBtns}</div></div>`:''}`}`;
}

function openEditTarefa(id){
  const t=id?DB.tarefas.find(x=>x.id===id)||{}:{};
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));
  showModal(id?'Editar Tarefa':'Nova Tarefa',`
    <div class="fg"><label>Título da Tarefa *</label>
      <input type="text" class="fi" id="ta-titulo" value="${esc(t.titulo||'')}" placeholder="Ex: Renovar alvará QI Botafogo"></div>
    <div class="fg"><label>Descrição</label>
      <textarea class="fi" id="ta-desc" rows="2" placeholder="Detalhes, links de referência, documentos necessários...">${esc(t.descricao||'')}</textarea></div>
    <div class="fr">
      <div class="fg"><label>Responsável *</label>
        <select class="fi" id="ta-resp">
          <option value="">Selecione...</option>
          ${DB.usuarios.filter(u=>u.ativo).map(u=>`<option value="${esc(u.nome)}"${t.responsavel===u.nome?' selected':''}>${esc(u.nome)} — ${esc(u.cargo||'')}</option>`).join('')}
        </select></div>
      <div class="fg"><label>Prioridade</label>
        <select class="fi" id="ta-prio">
          ${Object.entries(PRIORIDADES).map(([k,v])=>`<option value="${k}"${(t.prioridade||'media')===k?' selected':''}>${v.label}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Escola vinculada</label>
        <select class="fi" id="ta-escola">
          <option value="">— geral —</option>
          ${escolas.map(s=>`<option value="${esc(s.nome)}"${t.escola===s.nome?' selected':''}>${esc(s.nome)}</option>`).join('')}
        </select></div>
      <div class="fg"><label>Categoria</label>
        <select class="fi" id="ta-cat">
          <option value="">—</option>
          ${TAREFA_CATS.map(c=>`<option value="${esc(c)}"${t.categoria===c?' selected':''}>${esc(c)}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Prazo</label>
        <input type="date" class="fi" id="ta-prazo" value="${t.prazo||''}"></div>
      <div class="fg"><label>Status</label>
        <select class="fi" id="ta-status">
          ${Object.entries(TAREFA_STATUS).map(([k,v])=>`<option value="${k}"${(t.status||'pendente')===k?' selected':''}>${v}</option>`).join('')}
        </select></div>
    </div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="ta-obs" rows="2">${esc(t.observacoes||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     ${id?`<button class="btn btn-danger btn-sm" onclick="deleteTarefa(${id});closeModal()">Excluir</button>`:''}
     <button class="btn btn-pri" onclick="saveTarefa(${id||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

function saveTarefa(id){
  const titulo=document.getElementById('ta-titulo').value.trim();
  if(!titulo){showToast('Título é obrigatório','error');return;}
  const escola=document.getElementById('ta-escola').value;
  const rec={titulo,descricao:document.getElementById('ta-desc').value.trim()||null,
    responsavel:document.getElementById('ta-resp').value||null,
    prioridade:document.getElementById('ta-prio').value||'media',
    escola,categoria:document.getElementById('ta-cat').value||null,
    prazo:document.getElementById('ta-prazo').value||null,
    status:document.getElementById('ta-status').value||'pendente',
    observacoes:document.getElementById('ta-obs').value.trim()||null};
  if(id>0){const idx=DB.tarefas.findIndex(x=>x.id===id);if(idx>=0)Object.assign(DB.tarefas[idx],rec);}
  else DB.tarefas.push({id:nextId(DB.tarefas),criada_em:todayISO(),...rec});
  save();closeModal();render();showToast('Tarefa salva!');
}

function deleteTarefa(id){
  if(!confirm('Excluir esta tarefa?'))return;
  DB.tarefas=DB.tarefas.filter(x=>x.id!==id);
  save();render();showToast('Tarefa excluída','error');
}

// ── CONFIGURAÇÕES ─────────────────────────────────────────────────────────────
function renderConfig(){
  const storageKB=Math.round(JSON.stringify(DB).length/1024);
  const usersRows=DB.usuarios.map(u=>`
    <tr>
      <td>
        <div style="display:flex;align-items:center;gap:10px">
          <div class="ct-av" style="width:32px;height:32px;font-size:12px;background:${avatarColor(u.nome)}">${(u.nome||'?').split(' ').map(w=>w[0]).slice(0,2).join('').toUpperCase()}</div>
          <div><div style="font-weight:600;font-size:13px">${esc(u.nome)}</div>
               <div style="font-size:11px;color:var(--muted)">${esc(u.email||'')}</div></div>
        </div>
      </td>
      <td style="font-size:12px">${esc(u.cargo||'—')}</td>
      <td style="font-size:12px">${esc(u.setor||'—')}</td>
      <td><span class="badge ${u.ativo?'ok':'gray'}">${u.ativo?'Ativo':'Inativo'}</span></td>
      <td><div class="act-btns" style="opacity:1">
        <button class="btn btn-sec btn-sm" onclick="openEditUsuario(${u.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        ${DB.usuarios.length>1?`<button class="btn btn-danger btn-sm" onclick="deleteUsuario(${u.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>`:''}
      </div></td>
    </tr>`).join('');
  return`
  <div style="max-width:720px">
    <div class="card" style="margin-bottom:16px">
      <div class="sh">
        <div><div class="sh-title">👥 Usuários da Plataforma</div>
          <div class="sh-sub">Gerencie quem pode ser atribuído como responsável em tarefas, processos e pagamentos</div></div>
        <button class="btn btn-pri" onclick="openEditUsuario(null)">
          <i data-lucide="user-plus" style="width:14px;height:14px"></i>Novo Usuário</button>
      </div>
      <div class="tbl-wrap" style="margin-top:10px">
        <table><thead><tr><th>Nome / E-mail</th><th>Cargo</th><th>Setor</th><th>Status</th><th></th></tr></thead>
        <tbody>${usersRows}</tbody></table>
      </div>
    </div>
    <div class="card" style="margin-bottom:16px">
      <div class="sh-title" style="margin-bottom:14px">📊 Resumo dos Dados</div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px">
        ${[['Escolas',DB.schools.length],['Documentos',DB.docs.length],
           ['Processos SEI',DB.procs.length],['Tarefas',DB.tarefas.length],
           ['Contatos SEEDUC',DB.contacts.length],['Lançamentos Fin.',DB.financeiro.length],
           ['Total Pago',fmtCurrency(DB.financeiro.filter(x=>x.status==='pago').reduce((s,x)=>s+(x.valor||0),0))],
           ['Total Pendente',fmtCurrency(DB.financeiro.filter(x=>x.status==='pendente').reduce((s,x)=>s+(x.valor||0),0))],
           ['Usuários',DB.usuarios.length],
           ['Arquivos',DB.arquivos.length]].map(([l,v])=>`
          <div style="background:var(--sec);border-radius:8px;padding:12px">
            <div style="font-size:10px;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.4px">${l}</div>
            <div style="font-size:20px;font-weight:800;color:var(--pri);margin-top:3px">${v}</div>
          </div>`).join('')}
      </div>
      <div style="margin-top:12px;font-size:12px;color:var(--muted)">Armazenamento local: ~${storageKB} KB</div>
    </div>
    <!-- Gerenciar Redes -->
    <div class="card" style="margin-bottom:16px">
      <div class="sh">
        <div class="sh-title">🌐 Redes Escolares</div>
        <button class="btn btn-pri btn-sm" onclick="addRede()"><i data-lucide="plus" style="width:13px;height:13px"></i>Nova Rede</button>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:8px">
        ${[...new Set(DB.schools.map(s=>s.rede))].sort().map(r=>`
          <div style="display:flex;align-items:center;gap:6px;background:var(--sec);
                       border-radius:20px;padding:4px 10px 4px 12px">
            <span style="font-size:12px;font-weight:600">${esc(r)}</span>
            <span style="font-size:10px;color:var(--muted)">${DB.schools.filter(s=>s.rede===r).length} esc.</span>
            <button onclick="renameRede('${esc(r)}')" style="background:none;border:none;cursor:pointer;color:var(--muted);font-size:12px;padding:0">✏️</button>
          </div>`).join('')}
      </div>
    </div>
    <!-- Tipos de Processo -->
    <div class="card" style="margin-bottom:16px">
      <div class="sh">
        <div class="sh-title">📋 Tipos de Processo SEI</div>
        <button class="btn btn-pri btn-sm" onclick="addTipoProcesso()"><i data-lucide="plus" style="width:13px;height:13px"></i>Novo Tipo</button>
      </div>
      <div style="margin-top:8px;display:flex;flex-direction:column;gap:4px">
        ${DB.tipos_processo.map((t,i)=>`
          <div style="display:flex;align-items:center;gap:8px;padding:7px 10px;background:var(--sec);border-radius:8px">
            <span style="flex:1;font-size:13px">${esc(t)}</span>
            <button onclick="editTipoProcesso(${i})" style="background:none;border:none;cursor:pointer;color:var(--muted);font-size:13px;padding:0">✏️</button>
            <button onclick="deleteTipoProcesso(${i})" style="background:none;border:none;cursor:pointer;color:var(--red);font-size:14px;padding:0;line-height:1">×</button>
          </div>`).join('')}
      </div>
    </div>
    <div class="card" style="margin-bottom:16px">
      <div class="sh-title" style="margin-bottom:12px">💾 Exportar Dados</div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <button class="btn btn-pri" onclick="exportData()"><i data-lucide="download" style="width:14px;height:14px"></i>Exportar JSON completo</button>
        <button class="btn btn-sec" onclick="exportFinCSV()"><i data-lucide="file-spreadsheet" style="width:14px;height:14px"></i>Exportar Financeiro CSV</button>
      </div>
    </div>
    <div class="card" style="border:1px solid var(--rbg)">
      <div class="sh-title" style="margin-bottom:8px;color:var(--red)">⚠️ Zona de Perigo</div>
      <p style="font-size:13px;color:var(--muted);margin-bottom:12px">
        Limpa todos os dados editados e retorna ao estado original das planilhas. <strong>Não pode ser desfeito.</strong>
      </p>
      <button class="btn btn-danger" onclick="resetData()">
        <i data-lucide="rotate-ccw" style="width:14px;height:14px"></i>Resetar para dados originais</button>
    </div>
  </div>`;
}

function openEditUsuario(id){
  const u=id?DB.usuarios.find(x=>x.id===id)||{}:{};
  showModal(id?'Editar Usuário':'Novo Usuário',`
    <div class="fr">
      <div class="fg"><label>Nome completo *</label>
        <input type="text" class="fi" id="us-nome" value="${esc(u.nome||'')}" placeholder="Ex: Maria Silva"></div>
      <div class="fg"><label>Cargo / Função</label>
        <input type="text" class="fi" id="us-cargo" value="${esc(u.cargo||'')}" placeholder="Ex: Gestora Regulatória"></div>
    </div>
    <div class="fr">
      <div class="fg"><label>E-mail</label>
        <input type="email" class="fi" id="us-email" value="${esc(u.email||'')}" placeholder="nome@empresa.com.br"></div>
      <div class="fg"><label>Setor</label>
        <input type="text" class="fi" id="us-setor" value="${esc(u.setor||'')}" placeholder="Ex: Regulatório, Financeiro..."></div>
    </div>
    <div class="fg"><label>Status</label>
      <select class="fi" id="us-ativo">
        <option value="1"${u.ativo!==false?' selected':''}>✅ Ativo</option>
        <option value="0"${u.ativo===false?' selected':''}>❌ Inativo</option>
      </select></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveUsuario(${id||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

function saveUsuario(id){
  const nome=document.getElementById('us-nome').value.trim();
  if(!nome){showToast('Nome é obrigatório','error');return;}
  const rec={nome,cargo:document.getElementById('us-cargo').value.trim(),
    email:document.getElementById('us-email').value.trim(),
    setor:document.getElementById('us-setor').value.trim(),
    ativo:document.getElementById('us-ativo').value==='1'};
  if(id>0){const idx=DB.usuarios.findIndex(x=>x.id===id);if(idx>=0)Object.assign(DB.usuarios[idx],rec);}
  else DB.usuarios.push({id:nextId(DB.usuarios),...rec});
  save();closeModal();render();showToast('Usuário salvo!');
}

function deleteUsuario(id){
  if(DB.usuarios.length<=1){showToast('É necessário ao menos 1 usuário','error');return;}
  if(!confirm('Excluir este usuário? Tarefas e processos vinculados não serão afetados.'))return;
  DB.usuarios=DB.usuarios.filter(x=>x.id!==id);
  save();render();showToast('Usuário removido','error');
}

// Gestão de Redes
function addRede(){
  const nome=prompt('Nome da nova rede:','');
  if(!nome||!nome.trim())return;
  const n=nome.trim();
  if(DB.redes.find(r=>r.nome===n)){showToast('Rede já existe','error');return;}
  if(!DB.redes)DB.redes=[];
  DB.redes.push({id:nextId(DB.redes),nome:n});
  save();render();showToast(`Rede "${n}" adicionada!`);
}
function renameRede(nome){
  const novo=prompt(`Renomear rede "${nome}" para:`,nome);
  if(!novo||!novo.trim()||novo.trim()===nome)return;
  const n=novo.trim();
  DB.schools.forEach(s=>{if(s.rede===nome)s.rede=n;});
  DB.docs.forEach(d=>{if(d.rede===nome)d.rede=n;});
  DB.procs.forEach(p=>{if(p.rede===nome)p.rede=n;});
  DB.financeiro.forEach(f=>{if(f.rede===nome)f.rede=n;});
  const ri=DB.redes?DB.redes.findIndex(r=>r.nome===nome):-1;
  if(ri>=0)DB.redes[ri].nome=n;
  save();render();showToast(`Rede renomeada para "${n}"!`);
}
// Gestão de Tipos de Processo
function addTipoProcesso(){
  const t=prompt('Nome do tipo de processo:','');
  if(!t||!t.trim())return;
  DB.tipos_processo.push(t.trim());
  save();render();showToast('Tipo de processo adicionado!');
}
function editTipoProcesso(i){
  const novo=prompt('Editar tipo:',DB.tipos_processo[i]);
  if(!novo||!novo.trim())return;
  DB.tipos_processo[i]=novo.trim();
  save();render();showToast('Tipo atualizado!');
}
function deleteTipoProcesso(i){
  if(!confirm(`Excluir tipo "${DB.tipos_processo[i]}"?`))return;
  DB.tipos_processo.splice(i,1);
  save();render();showToast('Tipo removido','error');
}

function exportData(){
  const blob=new Blob([JSON.stringify(DB,null,2)],{type:'application/json'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download=`regulareduc_${todayISO()}.json`;a.click();
  showToast('Exportação iniciada!');
}

function resetData(){
  if(!confirm('Tem certeza? Todos os dados editados serão perdidos.'))return;
  localStorage.removeItem('rg_v3');
  location.reload();
}

// ── FINANCEIRO ────────────────────────────────────────────────────────────────
const FIN_CATS=['Alvará de Funcionamento','Licença Sanitária','AVCB / Bombeiros','Taxa INEP / MEC',
  'Vigilância Sanitária','Taxa Cartório','Honorários Despachante','Taxa CREA / Laudo',
  'Imposto / Tributo','Multa / Penalidade','Outro'];
const FIN_FORMAS=['Boleto','PIX','TED/DOC','Cartão','Dinheiro','Outro'];

function fmtCurrency(v){
  return new Intl.NumberFormat('pt-BR',{style:'currency',currency:'BRL'}).format(v||0);
}
function fmtMes(ym){
  if(!ym)return'—';
  const[y,m]=ym.split('-');
  const nomes=['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'];
  return`${nomes[parseInt(m)-1]}/${y.slice(2)}`;
}
function finStatusClass(s){
  return{pago:'fin-st-pago',pendente:'fin-st-pendente',vencido:'fin-st-vencido',cancelado:'fin-st-cancelado'}[s]||'fin-st-pendente';
}
function finStatusLabel(s){
  return{pago:'✅ Pago',pendente:'⏳ Pendente',vencido:'🔴 Vencido',cancelado:'✖ Cancelado'}[s]||s;
}

function renderFinanceiro(){
  const f=state.finF;
  let fl=[...DB.financeiro];
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(x=>(x.descricao||'').toLowerCase().includes(q)||(x.escola||'').toLowerCase().includes(q)||(x.orgao||'').toLowerCase().includes(q));}
  if(f.categoria)fl=fl.filter(x=>x.categoria===f.categoria);
  if(f.status)fl=fl.filter(x=>x.status===f.status);
  if(f.escola)fl=fl.filter(x=>x.escola===f.escola);
  if(f.ano)fl=fl.filter(x=>(x.data_pagamento||x.data_vencimento||'').startsWith(f.ano));

  const pago=fl.filter(x=>x.status==='pago').reduce((s,x)=>s+(x.valor||0),0);
  const pendente=fl.filter(x=>x.status==='pendente').reduce((s,x)=>s+(x.valor||0),0);
  const vencido=fl.filter(x=>x.status==='vencido').reduce((s,x)=>s+(x.valor||0),0);
  const prox30=fl.filter(x=>x.status==='pendente'&&x.data_vencimento&&daysUntil(x.data_vencimento)>=0&&daysUntil(x.data_vencimento)<=30).reduce((s,x)=>s+(x.valor||0),0);
  const total=pago+pendente+vencido;

  // ── Gráfico mensal ────────────────────────────────────────────────────────
  const anoAtual=new Date().getFullYear();
  const monthMap={};
  for(let m=1;m<=12;m++)monthMap[`${anoAtual}-${String(m).padStart(2,'0')}`]=0;
  fl.forEach(x=>{
    const date=x.data_pagamento||x.data_vencimento;
    if(!date)return;
    const ym=date.slice(0,7);
    if(monthMap[ym]!==undefined)monthMap[ym]+=(x.valor||0);
  });
  const maxMes=Math.max(...Object.values(monthMap),1);
  const chartBars=Object.entries(monthMap).map(([ym,val])=>{
    const pct=Math.max((val/maxMes*100),val>0?4:0);
    const cor=val>0?'var(--acc)':'var(--border)';
    return`<div class="fin-bar-col">
      ${val>0?`<div class="fin-bar-val">${fmtCurrency(val).replace('R$','').trim()}</div>`:'<div class="fin-bar-val">&nbsp;</div>'}
      <div class="fin-bar-wrap"><div class="fin-bar" style="height:${pct}%;background:${cor}"></div></div>
      <div class="fin-bar-label">${fmtMes(ym)}</div>
    </div>`;
  }).join('');

  // ── Por categoria ─────────────────────────────────────────────────────────
  const byCat={};
  fl.forEach(x=>{if(!byCat[x.categoria||'Outro'])byCat[x.categoria||'Outro']=0;byCat[x.categoria||'Outro']+=(x.valor||0);});
  const maxCat=Math.max(...Object.values(byCat),1);
  const catRows=Object.entries(byCat).sort((a,b)=>b[1]-a[1]).map(([cat,val])=>`
    <div style="margin-bottom:10px">
      <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:2px">
        <span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:150px">${esc(cat)}</span>
        <span style="font-weight:700;flex-shrink:0;margin-left:8px">${fmtCurrency(val)}</span>
      </div>
      <div class="cat-pct-bar"><div class="cat-pct-fill" style="width:${(val/maxCat*100).toFixed(1)}%"></div></div>
    </div>`).join('');

  // ── Por escola ────────────────────────────────────────────────────────────
  const byEscola={};
  fl.forEach(x=>{if(x.escola){if(!byEscola[x.escola])byEscola[x.escola]=0;byEscola[x.escola]+=(x.valor||0);}});
  const topEscolas=Object.entries(byEscola).sort((a,b)=>b[1]-a[1]).slice(0,6);
  const maxEsc=topEscolas.length?topEscolas[0][1]:1;
  const escolaRows=topEscolas.map(([e,v])=>`
    <div style="margin-bottom:8px">
      <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:2px">
        <span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:160px">${esc(e)}</span>
        <span style="font-weight:600;flex-shrink:0;margin-left:6px">${fmtCurrency(v)}</span>
      </div>
      <div class="cat-pct-bar"><div class="cat-pct-fill" style="width:${(v/maxEsc*100).toFixed(1)}%;background:var(--green)"></div></div>
    </div>`).join('');

  // ── Tabela ────────────────────────────────────────────────────────────────
  const PG=25,tot=fl.length;
  const sortedFl=[...fl].sort((a,b)=>(b.data_vencimento||'').localeCompare(a.data_vencimento||''));
  const pages=Math.max(1,Math.ceil(tot/PG));
  const p=Math.min(state.finPage,pages);
  const slice=sortedFl.slice((p-1)*PG,p*PG);
  const anos=[...new Set(DB.financeiro.map(x=>(x.data_pagamento||x.data_vencimento||'').slice(0,4)).filter(Boolean))].sort().reverse();
  const escolas=[...new Set(DB.financeiro.map(x=>x.escola).filter(Boolean))].sort();

  const rows=slice.map(x=>{
    const days=x.data_vencimento&&x.status!=='pago'?daysUntil(x.data_vencimento):null;
    const daysTag=days!==null&&days<=30?`<span style="font-size:10px;padding:1px 5px;border-radius:6px;font-weight:700;
      background:${days<0?'var(--rbg)':'var(--ybg)'};color:${days<0?'#991B1B':'#92400E'}">${days<0?Math.abs(days)+'d atr.':days+'d'}</span>`:'';
    return`<tr>
      <td><div class="td-name">${esc(x.descricao||'—')}</div>
          <div class="td-sub">${esc(x.categoria||'—')}</div></td>
      <td><div class="td-name" style="font-size:12px">${esc(x.escola||'—')}</div>
          <div class="td-sub">${esc(x.rede||'')}</div></td>
      <td style="font-size:12px">${esc(x.orgao||'—')}</td>
      <td style="font-weight:700;font-size:14px">${fmtCurrency(x.valor)}</td>
      <td>${fmtDate(x.data_vencimento)} ${daysTag}</td>
      <td>${fmtDate(x.data_pagamento)}</td>
      <td><span class="badge ${finStatusClass(x.status)}">${finStatusLabel(x.status)}</span></td>
      <td><div class="act-btns">
        <button class="btn btn-sec btn-sm" onclick="openEditFin(${x.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteFin(${x.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div></td>
    </tr>`;
  }).join('');

  const pgBtns=Array.from({length:Math.min(pages,8)},(_,i)=>`<button class="pb${p===i+1?' active':''}" onclick="state.finPage=${i+1};render()">${i+1}</button>`).join('');

  return`
  <div class="kpi-grid">
    <div class="card"><div class="kpi-lbl">Total Pago</div>
      <div class="kpi-val ok" style="font-size:22px">${fmtCurrency(pago)}</div>
      <div class="kpi-sub">${fl.filter(x=>x.status==='pago').length} lançamentos</div></div>
    <div class="card"><div class="kpi-lbl">Pendente</div>
      <div class="kpi-val warn" style="font-size:22px">${fmtCurrency(pendente)}</div>
      <div class="kpi-sub">${fl.filter(x=>x.status==='pendente').length} a pagar</div></div>
    <div class="card"><div class="kpi-lbl">Vencido (em atraso)</div>
      <div class="kpi-val danger" style="font-size:22px">${fmtCurrency(vencido)}</div>
      <div class="kpi-sub">${fl.filter(x=>x.status==='vencido').length} em atraso</div></div>
    <div class="card"><div class="kpi-lbl">Vence em 30 dias</div>
      <div class="kpi-val warn" style="font-size:22px">${fmtCurrency(prox30)}</div>
      <div class="kpi-sub">previsão de desembolso</div></div>
  </div>

  ${DB.financeiro.length===0?`
  <div class="card" style="padding:60px 30px;text-align:center">
    <div style="font-size:48px;margin-bottom:16px">💰</div>
    <div style="font-size:17px;font-weight:700;margin-bottom:8px">Nenhum lançamento financeiro</div>
    <div style="color:var(--muted);font-size:14px;max-width:400px;margin:0 auto 20px">
      Cadastre aqui taxas, emolumentos, alvarás, multas e demais despesas regulatórias de cada escola.
    </div>
    <button class="btn btn-pri" onclick="openEditFin(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Cadastrar primeiro lançamento</button>
  </div>`:
  `<div style="display:grid;grid-template-columns:2fr 1fr 1fr;gap:16px;margin-bottom:22px">
    <div class="card">
      <div style="font-weight:700;font-size:13px;margin-bottom:12px">📊 Desembolso Mensal — ${anoAtual}</div>
      <div class="fin-chart">${chartBars}</div>
    </div>
    <div class="card">
      <div style="font-weight:700;font-size:13px;margin-bottom:12px">📂 Por Categoria</div>
      ${catRows||'<div style="color:var(--muted);font-size:12px">Sem dados</div>'}
    </div>
    <div class="card">
      <div style="font-weight:700;font-size:13px;margin-bottom:12px">🏫 Por Escola (Top)</div>
      ${escolaRows||'<div style="color:var(--muted);font-size:12px">Sem dados</div>'}
    </div>
  </div>`}

  <div class="sh">
    <div><div class="sh-title">Lançamentos Financeiros</div>
      <div class="sh-sub">${tot} registro(s) · Total geral: <strong>${fmtCurrency(total)}</strong></div></div>
    <div style="display:flex;gap:8px">
      <button class="btn btn-sec" onclick="exportFinCSV()" title="Exportar planilha CSV">
        <i data-lucide="download" style="width:14px;height:14px"></i>Exportar CSV</button>
      <button class="btn btn-pri" onclick="openEditFin(null)">
        <i data-lucide="plus" style="width:14px;height:14px"></i>Novo Lançamento</button>
    </div>
  </div>

  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar descrição, escola, órgão..." value="${esc(f.q)}" oninput="state.finF.q=this.value;state.finPage=1;render()"></div>
    <select class="fs" onchange="state.finF.categoria=this.value;state.finPage=1;render()">
      <option value="">Todas as categorias</option>
      ${FIN_CATS.map(c=>`<option value="${esc(c)}"${f.categoria===c?' selected':''}>${esc(c)}</option>`).join('')}
    </select>
    <select class="fs" onchange="state.finF.status=this.value;state.finPage=1;render()">
      <option value="">Todos os status</option>
      <option value="pago"${f.status==='pago'?' selected':''}>✅ Pago</option>
      <option value="pendente"${f.status==='pendente'?' selected':''}>⏳ Pendente</option>
      <option value="vencido"${f.status==='vencido'?' selected':''}>🔴 Vencido</option>
      <option value="cancelado"${f.status==='cancelado'?' selected':''}>✖ Cancelado</option>
    </select>
    <select class="fs" onchange="state.finF.escola=this.value;state.finPage=1;render()">
      <option value="">Todas as escolas</option>
      ${escolas.map(e=>`<option value="${esc(e)}"${f.escola===e?' selected':''}>${esc(e)}</option>`).join('')}
    </select>
    <select class="fs" onchange="state.finF.ano=this.value;state.finPage=1;render()">
      <option value="">Todos os anos</option>
      ${anos.map(a=>`<option value="${a}"${f.ano===a?' selected':''}>${a}</option>`).join('')}
    </select>
  </div>

  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr>
      <th>Descrição / Categoria</th><th>Escola</th><th>Órgão / Fornecedor</th>
      <th>Valor</th><th>Vencimento</th><th>Pagamento</th><th>Status</th><th></th>
    </tr></thead>
    <tbody>${rows||'<tr><td colspan="8"><div class="empty"><div class="empty-icon">💸</div><div class="empty-title">Nenhum lançamento encontrado</div></div></td></tr>'}</tbody></table>
  </div>
  ${tot>PG?`<div class="pag"><div class="pag-info">Exibindo ${Math.min((p-1)*PG+1,tot)}–${Math.min(p*PG,tot)} de ${tot}</div>
    <div class="pag-btns">${pgBtns}</div></div>`:''}`;
}

function openEditFin(id){
  const x=id?DB.financeiro.find(f=>f.id===id)||{}:{};
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));
  showModal(id?'Editar Lançamento':'Novo Lançamento Financeiro',`
    <div class="fg"><label>Descrição *</label>
      <input type="text" class="fi" id="fi-desc" value="${esc(x.descricao||'')}" placeholder="Ex: Renovação Alvará de Funcionamento"></div>
    <div class="fr">
      <div class="fg"><label>Categoria *</label>
        <select class="fi" id="fi-cat">
          <option value="">Selecione...</option>
          ${FIN_CATS.map(c=>`<option value="${esc(c)}"${x.categoria===c?' selected':''}>${esc(c)}</option>`).join('')}
        </select></div>
      <div class="fg"><label>Escola</label>
        <select class="fi" id="fi-escola" onchange="updateFinRede(this)">
          <option value="">— sem escola —</option>
          ${escolas.map(s=>`<option value="${esc(s.nome)}" data-rede="${esc(s.rede)}"${x.escola===s.nome?' selected':''}>${esc(s.nome)}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Órgão / Fornecedor</label>
        <input type="text" class="fi" id="fi-orgao" value="${esc(x.orgao||'')}" placeholder="Ex: Prefeitura RJ, SESAU..."></div>
      <div class="fg"><label>Responsável</label>
        <select class="fi" id="fi-resp">
          <option value="">— sem responsável —</option>
          ${DB.usuarios.filter(u=>u.ativo).map(u=>`<option value="${esc(u.nome)}"${x.responsavel===u.nome?' selected':''}>${esc(u.nome)} — ${esc(u.cargo||'')}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Valor (R$) *</label>
        <input type="text" class="fi" id="fi-valor" value="${x.valor?String(x.valor).replace('.',','):''}" placeholder="Ex: 1.850,00"></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Data de Vencimento</label>
        <input type="date" class="fi" id="fi-dvenc" value="${x.data_vencimento||''}"></div>
      <div class="fg"><label>Data de Pagamento</label>
        <input type="date" class="fi" id="fi-dpag" value="${x.data_pagamento||''}"></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Status</label>
        <select class="fi" id="fi-status">
          <option value="pendente"${x.status==='pendente'||!x.status?' selected':''}>⏳ Pendente</option>
          <option value="pago"${x.status==='pago'?' selected':''}>✅ Pago</option>
          <option value="vencido"${x.status==='vencido'?' selected':''}>🔴 Vencido</option>
          <option value="cancelado"${x.status==='cancelado'?' selected':''}>✖ Cancelado</option>
        </select></div>
      <div class="fg"><label>Forma de Pagamento</label>
        <select class="fi" id="fi-forma">
          <option value="">—</option>
          ${FIN_FORMAS.map(f2=>`<option value="${f2}"${x.forma_pagamento===f2?' selected':''}>${f2}</option>`).join('')}
        </select></div>
    </div>
    <div class="fg"><label>Observações / Comprovante</label>
      <textarea class="fi" id="fi-obs" rows="2" placeholder="Nº do boleto, protocolo, referência...">${esc(x.observacoes||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveFin(${id||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

function updateFinRede(){}

function saveFin(id){
  const desc=document.getElementById('fi-desc').value.trim();
  const cat=document.getElementById('fi-cat').value;
  if(!desc||!cat){showToast('Preencha descrição e categoria','error');return;}
  const selEsc=document.getElementById('fi-escola');
  const selOpt=selEsc.options[selEsc.selectedIndex];
  const escola=selEsc.value||'';
  const rede=escola&&selOpt?selOpt.dataset.rede:'';
  const valorStr=document.getElementById('fi-valor').value.replace(/\./g,'').replace(',','.');
  const valor=parseFloat(valorStr)||0;
  if(valor<=0){showToast('Informe um valor válido','error');return;}
  const rec={descricao:desc,categoria:cat,escola,rede,
    orgao:document.getElementById('fi-orgao').value.trim(),
    responsavel:document.getElementById('fi-resp').value||null,
    valor,data_vencimento:document.getElementById('fi-dvenc').value||null,
    data_pagamento:document.getElementById('fi-dpag').value||null,
    status:document.getElementById('fi-status').value,
    forma_pagamento:document.getElementById('fi-forma').value,
    observacoes:document.getElementById('fi-obs').value.trim()||null};
  if(id>0){
    const idx=DB.financeiro.findIndex(x=>x.id===id);
    if(idx>=0)Object.assign(DB.financeiro[idx],rec);
  }else{
    DB.financeiro.push({id:nextId(DB.financeiro),...rec});
  }
  save();closeModal();render();showToast('Lançamento salvo!');
}

function deleteFin(id){
  if(!confirm('Excluir este lançamento?'))return;
  DB.financeiro=DB.financeiro.filter(x=>x.id!==id);
  save();render();showToast('Lançamento excluído','error');
}

function exportFinCSV(){
  const f=state.finF;
  let fl=[...DB.financeiro];
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(x=>(x.descricao||'').toLowerCase().includes(q)||(x.escola||'').toLowerCase().includes(q));}
  if(f.categoria)fl=fl.filter(x=>x.categoria===f.categoria);
  if(f.status)fl=fl.filter(x=>x.status===f.status);
  if(f.escola)fl=fl.filter(x=>x.escola===f.escola);
  if(f.ano)fl=fl.filter(x=>(x.data_pagamento||x.data_vencimento||'').startsWith(f.ano));
  fl.sort((a,b)=>(b.data_vencimento||'').localeCompare(a.data_vencimento||''));
  const hdrs=['Descrição','Categoria','Escola','Rede','Órgão/Fornecedor','Valor (R$)',
              'Vencimento','Data Pagamento','Status','Forma Pagamento','Observações'];
  const rows=fl.map(x=>[x.descricao,x.categoria,x.escola,x.rede,x.orgao,
    (x.valor||0).toFixed(2).replace('.',','),
    fmtDate(x.data_vencimento),fmtDate(x.data_pagamento),
    finStatusLabel(x.status).replace(/[✅⏳🔴✖]/g,'').trim(),
    x.forma_pagamento||'',x.observacoes||'']);
  const csv='﻿'+[hdrs,...rows].map(r=>r.map(c=>`"${String(c||'').replace(/"/g,'""')}"`).join(';')).join('\r\n');
  const blob=new Blob([csv],{type:'text/csv;charset=utf-8;'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download=`financeiro_regulatorio_${todayISO()}.csv`;a.click();
  showToast(`${fl.length} lançamentos exportados!`);
}

// ── WIP ───────────────────────────────────────────────────────────────────────
function renderWIP(){
  return`<div class="card" style="margin-top:40px;text-align:center;padding:60px 30px">
    <div style="font-size:48px;margin-bottom:16px">🚧</div>
    <div style="font-size:18px;font-weight:700;margin-bottom:8px">${TITLES[cur]||cur}</div>
    <div style="color:var(--muted);font-size:14px;max-width:400px;margin:0 auto">Seção em desenvolvimento. Use as abas já disponíveis.</div>
    <button class="btn btn-pri" style="margin-top:20px" onclick="go('dashboard')">
      <i data-lucide="layout-dashboard" style="width:14px;height:14px"></i>Dashboard</button>
  </div>`;
}

// ── MODAL ─────────────────────────────────────────────────────────────────────
function showModal(title,body,footer,extraClass=''){
  document.getElementById('modal-root').innerHTML=`
    <div class="overlay" onclick="if(event.target===this)closeModal()">
      <div class="modal ${extraClass}">
        <div class="mh"><div class="mh-title">${title}</div>
          <button class="mc" onclick="closeModal()"><i data-lucide="x" style="width:14px;height:14px"></i></button></div>
        <div class="mb">${body}</div>
        <div class="mf">${footer||'<button class="btn btn-sec" onclick="closeModal()">Fechar</button>'}</div>
      </div>
    </div>`;
  lucide.createIcons();
}
function closeModal(){document.getElementById('modal-root').innerHTML='';}

// ── TOAST ─────────────────────────────────────────────────────────────────────
function showToast(msg,type='success'){
  const id='t'+Date.now();
  const icons={success:'check-circle',error:'x-circle',info:'info'};
  const colors={success:'var(--green)',error:'var(--red)',info:'var(--acc)'};
  const el=document.createElement('div');
  el.className=`toast ${type}`;el.id=id;
  el.innerHTML=`<i data-lucide="${icons[type]||'info'}" style="width:16px;height:16px;color:${colors[type]};flex-shrink:0"></i>${esc(msg)}`;
  document.getElementById('toasts').prepend(el);
  lucide.createIcons();
  setTimeout(()=>{const t=document.getElementById(id);if(t)t.remove();},3500);
}

// ── LEGISLAÇÕES ───────────────────────────────────────────────────────────────
const LEG_ORGAOS=[
  {value:'CEE RJ',     label:'CEE RJ — Conselho Estadual de Educação',      cls:'leg-cee-rj'},
  {value:'CME RJ',     label:'CME RJ — Conselho Municipal de Educação',      cls:'leg-cme-rj'},
  {value:'SMED POA',   label:'SMED Porto Alegre — Sec. Municipal de Educação',cls:'leg-smed-poa'},
  {value:'SME JF',     label:'SME Juiz de Fora — Sec. Municipal de Educação',cls:'leg-sme-jf'},
  {value:'SEEDUC RJ',  label:'SEEDUC RJ — Sec. Estadual de Educação',        cls:'leg-seeduc-rj'},
  {value:'MEC',        label:'MEC — Ministério da Educação',                 cls:'leg-mec'},
  {value:'Outro',      label:'Outro',                                        cls:'leg-outro'},
];
const LEG_TIPOS=['Deliberação','Resolução','Lei','Decreto','Portaria','Instrução Normativa','Parecer','Nota Técnica','Outro'];
const MODELO_CATS=['SEEDUC RJ','CME RJ','CEE RJ','SMED Porto Alegre','SME Juiz de Fora','Geral','Outro'];

function legOrgaoCls(v){return(LEG_ORGAOS.find(o=>o.value===v)||{cls:'leg-outro'}).cls;}

if(!state.legTab)state.legTab='leis';

function renderLegislacoes(){
  const tab=state.legTab||'leis';
  const tabBtns=`
    <div class="view-toggle" style="margin-bottom:18px">
      <button class="${tab==='leis'?'active':''}" onclick="state.legTab='leis';render()">📚 Legislações e Deliberações</button>
      <button class="${tab==='modelos'?'active':''}" onclick="state.legTab='modelos';render()">📎 Modelos de Anexos</button>
    </div>`;
  return tabBtns+(tab==='leis'?renderLegLeis():renderLegModelos());
}

function renderLegLeis(){
  const f=state.legF||{q:'',orgao:'',tipo:''};
  if(!state.legF)state.legF={q:'',orgao:'',tipo:''};
  let fl=[...DB.legislacoes];
  if(f.orgao)fl=fl.filter(l=>l.orgao===f.orgao);
  if(f.tipo)fl=fl.filter(l=>l.tipo===f.tipo);
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(l=>(l.titulo||'').toLowerCase().includes(q)||(l.ementa||'').toLowerCase().includes(q)||(l.numero||'').toLowerCase().includes(q));}
  fl.sort((a,b)=>(b.data||'').localeCompare(a.data||''));

  // Contadores por órgão
  const countBadges=LEG_ORGAOS.map(o=>{
    const n=DB.legislacoes.filter(l=>l.orgao===o.value).length;
    if(!n)return'';
    return`<span class="leg-orgao ${o.cls}" style="cursor:pointer;margin-right:4px" onclick="state.legF={...state.legF,orgao:'${esc(o.value)}'};render()">${esc(o.value)} <strong>${n}</strong></span>`;
  }).join('');

  const rows=fl.map(l=>`
    <tr>
      <td style="max-width:280px">
        <div class="td-name">${esc(l.titulo||'—')}</div>
        ${l.ementa?`<div class="td-sub" style="max-width:260px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(l.ementa)}</div>`:''}
      </td>
      <td><span class="leg-orgao ${legOrgaoCls(l.orgao)}">${esc(l.orgao||'—')}</span></td>
      <td style="font-size:12px">${esc(l.tipo||'—')}</td>
      <td style="font-size:12px;font-weight:600">${esc(l.numero||'—')}</td>
      <td style="font-size:12px">${fmtDate(l.data)}</td>
      <td>
        ${l.arquivo_id?`<button class="btn btn-pri btn-sm" onclick="viewLegArquivo('${l.arquivo_id}','${esc(l.arquivo_nome||'')}')">
          <i data-lucide="download" style="width:11px;height:11px"></i>PDF</button>`:
          `<span style="font-size:11px;color:var(--muted)">Sem arquivo</span>`}
        ${l.link_oficial?`<a href="${esc(l.link_oficial)}" target="_blank" class="btn btn-sec btn-sm" style="margin-left:4px;text-decoration:none">🔗</a>`:''}
      </td>
      <td><div class="act-btns">
        <button class="btn btn-sec btn-sm" onclick="openEditLeg(${l.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteLeg(${l.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div></td>
    </tr>`).join('');

  return`
  <div class="sh">
    <div>
      <div class="sh-title">Legislações e Deliberações</div>
      <div class="sh-sub">${DB.legislacoes.length} documento(s) cadastrado(s)</div>
    </div>
    <button class="btn btn-pri" onclick="openEditLeg(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Nova Legislação</button>
  </div>

  <div style="margin-bottom:14px;padding:12px;background:var(--sec);border-radius:10px">
    <div style="font-size:11px;font-weight:600;color:var(--muted);margin-bottom:8px;text-transform:uppercase;letter-spacing:.5px">Filtrar por órgão</div>
    <div style="display:flex;flex-wrap:wrap;gap:6px;align-items:center">
      <span class="leg-orgao" style="background:var(--border);color:var(--txt);cursor:pointer" onclick="state.legF={...state.legF,orgao:''};render()">Todos</span>
      ${countBadges||'<span style="font-size:12px;color:var(--muted)">Nenhuma legislação cadastrada</span>'}
    </div>
  </div>

  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar título, número, ementa..." value="${esc(f.q||'')}"
             oninput="state.legF={...state.legF,q:this.value};render()"></div>
    <select class="fs" onchange="state.legF={...state.legF,orgao:this.value};render()">
      <option value="">Todos os órgãos</option>
      ${LEG_ORGAOS.map(o=>`<option value="${esc(o.value)}"${f.orgao===o.value?' selected':''}>${esc(o.value)}</option>`).join('')}
    </select>
    <select class="fs" onchange="state.legF={...state.legF,tipo:this.value};render()">
      <option value="">Todos os tipos</option>
      ${LEG_TIPOS.map(t=>`<option value="${esc(t)}"${f.tipo===t?' selected':''}>${esc(t)}</option>`).join('')}
    </select>
  </div>

  ${fl.length===0?`
  <div class="card" style="padding:50px 30px;text-align:center">
    <div style="font-size:42px;margin-bottom:12px">⚖️</div>
    <div style="font-size:16px;font-weight:700;margin-bottom:8px">Nenhuma legislação cadastrada</div>
    <div style="color:var(--muted);font-size:13px;max-width:400px;margin:0 auto 20px">
      Cadastre as deliberações do CEE RJ, CME RJ, legislações da SMED Porto Alegre e SME Juiz de Fora.
    </div>
    <button class="btn btn-pri" onclick="openEditLeg(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Cadastrar primeira legislação</button>
  </div>`:`
  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr>
      <th>Título</th><th>Órgão</th><th>Tipo</th><th>Número</th><th>Data</th><th>Arquivo</th><th></th>
    </tr></thead>
    <tbody>${rows}</tbody></table>
  </div>`}`;
}

function openEditLeg(id){
  const l=id?DB.legislacoes.find(x=>x.id===id)||{}:{};
  showModal(id?'Editar Legislação':'Nova Legislação',`
    <div class="fg"><label>Título *</label>
      <input type="text" class="fi" id="lg-titulo" value="${esc(l.titulo||'')}"
             placeholder="Ex: Deliberação CEE-RJ nº 330/2020 — Credenciamento de escolas"></div>
    <div class="fr">
      <div class="fg"><label>Órgão *</label>
        <select class="fi" id="lg-orgao">
          <option value="">Selecione...</option>
          ${LEG_ORGAOS.map(o=>`<option value="${esc(o.value)}"${l.orgao===o.value?' selected':''}>${esc(o.label)}</option>`).join('')}
        </select></div>
      <div class="fg"><label>Tipo *</label>
        <select class="fi" id="lg-tipo">
          <option value="">Selecione...</option>
          ${LEG_TIPOS.map(t=>`<option value="${esc(t)}"${l.tipo===t?' selected':''}>${esc(t)}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Número / Identificação</label>
        <input type="text" class="fi" id="lg-num" value="${esc(l.numero||'')}" placeholder="Ex: 330/2020"></div>
      <div class="fg"><label>Data de Publicação</label>
        <input type="date" class="fi" id="lg-data" value="${l.data||''}"></div>
    </div>
    <div class="fg"><label>Ementa (resumo)</label>
      <textarea class="fi" id="lg-ementa" rows="3" placeholder="Resumo do conteúdo da legislação...">${esc(l.ementa||'')}</textarea></div>
    <div class="fg"><label>Link oficial (opcional)</label>
      <input type="text" class="fi" id="lg-link" value="${esc(l.link_oficial||'')}"
             placeholder="https://www.rj.gov.br/..."></div>
    <div class="fg"><label>Arquivo PDF</label>
      <div style="display:flex;gap:8px;align-items:center">
        <input type="file" id="lg-file" accept=".pdf,.doc,.docx" style="font-size:12px;flex:1">
        ${l.arquivo_nome?`<span style="font-size:11px;color:var(--muted)">Atual: ${esc(l.arquivo_nome)}</span>`:''}
      </div>
    </div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveLeg(${id||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

async function saveLeg(id){
  const titulo=document.getElementById('lg-titulo').value.trim();
  const orgao=document.getElementById('lg-orgao').value;
  const tipo=document.getElementById('lg-tipo').value;
  if(!titulo||!orgao||!tipo){showToast('Título, órgão e tipo são obrigatórios','error');return;}
  const fileInput=document.getElementById('lg-file');
  const file=fileInput&&fileInput.files[0];
  let arquivo_id=id?((DB.legislacoes.find(x=>x.id===id)||{}).arquivo_id||null):null;
  let arquivo_nome=id?((DB.legislacoes.find(x=>x.id===id)||{}).arquivo_nome||null):null;
  if(file){
    if(file.size>20*1024*1024){showToast('Arquivo maior que 20MB','error');return;}
    showToast('Salvando arquivo...','info');
    const reader=new FileReader();
    const dataURL=await new Promise((res,rej)=>{reader.onload=e=>res(e.target.result);reader.onerror=rej;reader.readAsDataURL(file);});
    const newId='leg_'+Date.now();
    await storeFileContent(newId,dataURL);
    if(arquivo_id&&arquivo_id!==newId){try{await removeFileContent(arquivo_id);}catch(e){}}
    arquivo_id=newId;arquivo_nome=file.name;
  }
  const rec={titulo,orgao,tipo,
    numero:document.getElementById('lg-num').value.trim()||null,
    data:document.getElementById('lg-data').value||null,
    ementa:document.getElementById('lg-ementa').value.trim()||null,
    link_oficial:document.getElementById('lg-link').value.trim()||null,
    arquivo_id,arquivo_nome,
    criado_em:todayISO()};
  if(id>0){const idx=DB.legislacoes.findIndex(x=>x.id===id);if(idx>=0)Object.assign(DB.legislacoes[idx],rec);}
  else DB.legislacoes.push({id:nextId(DB.legislacoes),...rec});
  save();closeModal();render();showToast('Legislação salva!');
}

async function viewLegArquivo(arquivoId,nome){
  try{
    const dataURL=await loadFileContent(arquivoId);
    if(!dataURL){showToast('Arquivo não encontrado','error');return;}
    const a=document.createElement('a');a.href=dataURL;a.download=nome||'documento.pdf';a.click();
  }catch(e){showToast('Erro ao abrir arquivo','error');}
}

async function deleteLeg(id){
  const l=DB.legislacoes.find(x=>x.id===id);if(!l)return;
  if(!confirm(`Excluir "${l.titulo}"?`))return;
  if(l.arquivo_id)try{await removeFileContent(l.arquivo_id);}catch(e){}
  DB.legislacoes=DB.legislacoes.filter(x=>x.id!==id);
  save();render();showToast('Legislação excluída','error');
}

// ── MODELOS DE ANEXOS ─────────────────────────────────────────────────────────
function renderLegModelos(){
  const f=state.modeloF||{q:'',cat:''};
  if(!state.modeloF)state.modeloF={q:'',cat:''};
  let fl=[...DB.modelos_anexos];
  if(f.cat)fl=fl.filter(m=>m.categoria===f.cat);
  if(f.q){const q=f.q.toLowerCase();fl=fl.filter(m=>(m.titulo||'').toLowerCase().includes(q)||(m.descricao||'').toLowerCase().includes(q));}
  fl.sort((a,b)=>(a.categoria||'').localeCompare(b.categoria||'')||a.titulo.localeCompare(b.titulo));

  const catColors={'SEEDUC RJ':'#FEF9EC','CME RJ':'#F0FDF4','CEE RJ':'#EFF6FF',
    'SMED Porto Alegre':'#FEF3C7','SME Juiz de Fora':'#FDF4FF','Geral':'#F3F4F6','Outro':'#F3F4F6'};
  const catTextColors={'SEEDUC RJ':'#B45309','CME RJ':'#15803D','CEE RJ':'#1D4ED8',
    'SMED Porto Alegre':'#92400E','SME Juiz de Fora':'#7C3AED','Geral':'#4B5563','Outro':'#4B5563'};

  const cards=fl.map(m=>{
    const bg=catColors[m.categoria]||'#F3F4F6';
    const tc=catTextColors[m.categoria]||'#4B5563';
    return`<div class="card modelo-card" onclick="openModeloDetail(${m.id})">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px">
        <span style="padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;background:${bg};color:${tc}">${esc(m.categoria||'Geral')}</span>
        ${m.versao?`<span style="font-size:10px;color:var(--muted)">v${esc(m.versao)}</span>`:''}
      </div>
      <div style="font-size:14px;font-weight:700;margin-bottom:6px">${esc(m.titulo)}</div>
      ${m.descricao?`<div style="font-size:12px;color:var(--muted);margin-bottom:10px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical">${esc(m.descricao)}</div>`:''}
      <div style="display:flex;gap:6px">
        ${m.arquivo_id?`<button class="btn btn-pri btn-sm" onclick="event.stopPropagation();viewLegArquivo('${m.arquivo_id}','${esc(m.arquivo_nome||'modelo')}')">
          <i data-lucide="download" style="width:11px;height:11px"></i>Baixar</button>`:''}
        <button class="btn btn-sec btn-sm" onclick="event.stopPropagation();openEditModelo(${m.id})">
          <i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="event.stopPropagation();deleteModelo(${m.id})">
          <i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div>
    </div>`;
  }).join('');

  return`
  <div class="sh">
    <div>
      <div class="sh-title">Modelos de Anexos</div>
      <div class="sh-sub">${DB.modelos_anexos.length} modelo(s) · Use para padronizar documentos enviados à SEEDUC, SME e órgãos</div>
    </div>
    <button class="btn btn-pri" onclick="openEditModelo(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Novo Modelo</button>
  </div>
  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar título ou descrição..." value="${esc(f.q||'')}"
             oninput="state.modeloF={...state.modeloF,q:this.value};render()"></div>
    <select class="fs" onchange="state.modeloF={...state.modeloF,cat:this.value};render()">
      <option value="">Todas as categorias</option>
      ${MODELO_CATS.map(c=>`<option value="${esc(c)}"${f.cat===c?' selected':''}>${esc(c)}</option>`).join('')}
    </select>
  </div>
  ${fl.length===0?`
  <div class="card" style="padding:50px 30px;text-align:center">
    <div style="font-size:42px;margin-bottom:12px">📎</div>
    <div style="font-size:16px;font-weight:700;margin-bottom:8px">Nenhum modelo cadastrado</div>
    <div style="color:var(--muted);font-size:13px;max-width:400px;margin:0 auto 20px">
      Cadastre requerimentos, formulários e modelos de anexos usados nos processos junto às secretarias de educação.
    </div>
    <button class="btn btn-pri" onclick="openEditModelo(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Cadastrar primeiro modelo</button>
  </div>`:`
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px">${cards}</div>`}`;
}

function openModeloDetail(id){
  const m=DB.modelos_anexos.find(x=>x.id===id);if(!m)return;
  showModal(m.titulo,`
    <div style="margin-bottom:14px">
      <span style="padding:3px 10px;border-radius:20px;font-size:11px;font-weight:700;
                   background:var(--sec);color:var(--muted)">${esc(m.categoria||'Geral')}</span>
      ${m.versao?`<span style="margin-left:8px;font-size:11px;color:var(--muted)">Versão: ${esc(m.versao)}</span>`:''}
    </div>
    ${m.descricao?`<div style="font-size:13px;margin-bottom:16px;line-height:1.6">${esc(m.descricao)}</div>`:''}
    ${m.instrucoes?`<div style="background:var(--sec);border-radius:8px;padding:12px;font-size:12px;margin-bottom:14px"><strong>Instruções de uso:</strong><br>${esc(m.instrucoes)}</div>`:''}`,
    `<button class="btn btn-sec" onclick="closeModal()">Fechar</button>
     <button class="btn btn-sec" onclick="closeModal();openEditModelo(${id})"><i data-lucide="pencil" style="width:13px;height:13px"></i>Editar</button>
     ${m.arquivo_id?`<button class="btn btn-pri" onclick="viewLegArquivo('${m.arquivo_id}','${esc(m.arquivo_nome||'modelo')}')"><i data-lucide="download" style="width:13px;height:13px"></i>Baixar Arquivo</button>`:''}`
  );
}

function openEditModelo(id){
  const m=id?DB.modelos_anexos.find(x=>x.id===id)||{}:{};
  showModal(id?'Editar Modelo de Anexo':'Novo Modelo de Anexo',`
    <div class="fg"><label>Título *</label>
      <input type="text" class="fi" id="mo-titulo" value="${esc(m.titulo||'')}"
             placeholder="Ex: Requerimento de Autorização de Funcionamento"></div>
    <div class="fr">
      <div class="fg"><label>Categoria / Órgão *</label>
        <select class="fi" id="mo-cat">
          <option value="">Selecione...</option>
          ${MODELO_CATS.map(c=>`<option value="${esc(c)}"${m.categoria===c?' selected':''}>${esc(c)}</option>`).join('')}
        </select></div>
      <div class="fg"><label>Versão / Ano</label>
        <input type="text" class="fi" id="mo-versao" value="${esc(m.versao||'')}"
               placeholder="Ex: 2024, Jan/2025..."></div>
    </div>
    <div class="fg"><label>Descrição</label>
      <textarea class="fi" id="mo-desc" rows="3"
                placeholder="Para que serve este modelo, quando usar...">${esc(m.descricao||'')}</textarea></div>
    <div class="fg"><label>Instruções de preenchimento</label>
      <textarea class="fi" id="mo-inst" rows="3"
                placeholder="Como preencher, campos obrigatórios, observações...">${esc(m.instrucoes||'')}</textarea></div>
    <div class="fg"><label>Arquivo (PDF, Word, etc.)</label>
      <div style="display:flex;gap:8px;align-items:center">
        <input type="file" id="mo-file" accept=".pdf,.doc,.docx,.xlsx,.odt" style="font-size:12px;flex:1">
        ${m.arquivo_nome?`<span style="font-size:11px;color:var(--muted)">Atual: ${esc(m.arquivo_nome)}</span>`:''}
      </div>
    </div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveModelo(${id||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

async function saveModelo(id){
  const titulo=document.getElementById('mo-titulo').value.trim();
  const cat=document.getElementById('mo-cat').value;
  if(!titulo||!cat){showToast('Título e categoria são obrigatórios','error');return;}
  const fileInput=document.getElementById('mo-file');
  const file=fileInput&&fileInput.files[0];
  let arquivo_id=id?((DB.modelos_anexos.find(x=>x.id===id)||{}).arquivo_id||null):null;
  let arquivo_nome=id?((DB.modelos_anexos.find(x=>x.id===id)||{}).arquivo_nome||null):null;
  if(file){
    if(file.size>20*1024*1024){showToast('Arquivo maior que 20MB','error');return;}
    showToast('Salvando arquivo...','info');
    const reader=new FileReader();
    const dataURL=await new Promise((res,rej)=>{reader.onload=e=>res(e.target.result);reader.onerror=rej;reader.readAsDataURL(file);});
    const newId='mod_'+Date.now();
    await storeFileContent(newId,dataURL);
    if(arquivo_id&&arquivo_id!==newId){try{await removeFileContent(arquivo_id);}catch(e){}}
    arquivo_id=newId;arquivo_nome=file.name;
  }
  const rec={titulo,categoria:cat,versao:document.getElementById('mo-versao').value.trim()||null,
    descricao:document.getElementById('mo-desc').value.trim()||null,
    instrucoes:document.getElementById('mo-inst').value.trim()||null,
    arquivo_id,arquivo_nome,criado_em:todayISO()};
  if(id>0){const idx=DB.modelos_anexos.findIndex(x=>x.id===id);if(idx>=0)Object.assign(DB.modelos_anexos[idx],rec);}
  else DB.modelos_anexos.push({id:nextId(DB.modelos_anexos),...rec});
  save();closeModal();render();showToast('Modelo salvo!');
}

async function deleteModelo(id){
  const m=DB.modelos_anexos.find(x=>x.id===id);if(!m)return;
  if(!confirm(`Excluir modelo "${m.titulo}"?`))return;
  if(m.arquivo_id)try{await removeFileContent(m.arquivo_id);}catch(e){}
  DB.modelos_anexos=DB.modelos_anexos.filter(x=>x.id!==id);
  save();render();showToast('Modelo excluído','error');
}

// ── TREINAMENTOS ──────────────────────────────────────────────────────────────
function trnStatus(t){
  if(!t.data_vencimento)return'nao_realizado';
  const d=daysUntil(t.data_vencimento);
  if(d<0)return'vencido';
  if(d<=60)return'a_renovar';
  return'em_dia';
}
const TRN_STATUS={
  em_dia:{label:'✅ Em dia',cls:'trn-cell-ok',badge:'ok'},
  a_renovar:{label:'⚠️ A renovar',cls:'trn-cell-warn',badge:'warn'},
  vencido:{label:'🔴 Vencido',cls:'trn-cell-venc',badge:'danger'},
  nao_realizado:{label:'— Não realizado',cls:'trn-cell-nao',badge:'gray'},
};

function renderTreinamentos(){
  const fT=state.trnF||{q:'',rede:'',tipo:'',status:''};
  if(!state.trnF)state.trnF={q:'',rede:'',tipo:'',status:''};
  const tab=state.trnTab||'lista';

  const redes=[...new Set(DB.schools.map(s=>s.rede))].sort();
  const obrigatorios=DB.tipos_treinamento.filter(t=>t.obrigatorio);

  // Enriquecer registros com status calculado
  const allTrn=DB.treinamentos.map(t=>({...t,_status:trnStatus(t)}));

  // Filtros
  let fl=[...allTrn];
  if(fT.rede)fl=fl.filter(t=>t.rede===fT.rede);
  if(fT.tipo)fl=fl.filter(t=>t.tipo_nome===fT.tipo);
  if(fT.status)fl=fl.filter(t=>t._status===fT.status);
  if(fT.q){const q=fT.q.toLowerCase();fl=fl.filter(t=>(t.escola||'').toLowerCase().includes(q)||(t.tipo_nome||'').toLowerCase().includes(q)||(t.instrutor||'').toLowerCase().includes(q));}

  // KPIs
  const emDia=allTrn.filter(t=>t._status==='em_dia').length;
  const aRen=allTrn.filter(t=>t._status==='a_renovar').length;
  const venc=allTrn.filter(t=>t._status==='vencido').length;
  const naoR=allTrn.filter(t=>t._status==='nao_realizado').length;

  const tabBtns=`
    <div class="view-toggle" style="margin-bottom:16px">
      <button class="${tab==='lista'?'active':''}" onclick="state.trnTab='lista';render()">
        <i data-lucide="list" style="width:12px;height:12px"></i>Lista de Registros</button>
      <button class="${tab==='mapa'?'active':''}" onclick="state.trnTab='mapa';render()">
        <i data-lucide="grid" style="width:12px;height:12px"></i>Mapa de Conformidade</button>
      <button class="${tab==='tipos'?'active':''}" onclick="state.trnTab='tipos';render()">
        <i data-lucide="settings" style="width:12px;height:12px"></i>Tipos de Treinamento</button>
    </div>`;

  const kpis=`
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px">
    <div class="card" style="padding:14px">
      <div class="kpi-lbl">Total de Registros</div>
      <div class="kpi-val">${allTrn.length}</div>
      <div class="kpi-sub">${DB.schools.length} escolas</div>
    </div>
    <div class="card" style="padding:14px;border-left:4px solid var(--green)">
      <div class="kpi-lbl">Em Dia</div>
      <div class="kpi-val ok">${emDia}</div>
    </div>
    <div class="card" style="padding:14px;border-left:4px solid var(--yellow)">
      <div class="kpi-lbl">A Renovar (≤60d)</div>
      <div class="kpi-val warn">${aRen}</div>
    </div>
    <div class="card" style="padding:14px;border-left:4px solid var(--red)">
      <div class="kpi-lbl">Vencidos / Não Realizados</div>
      <div class="kpi-val danger">${venc+naoR}</div>
    </div>
  </div>`;

  let content='';
  if(tab==='lista') content=renderTrnLista(fl,redes,fT);
  else if(tab==='mapa') content=renderTrnMapa(allTrn);
  else content=renderTrnTipos();

  return`
  <div class="sh">
    <div><div class="sh-title">Treinamentos Obrigatórios</div>
      <div class="sh-sub">Gestão de treinamentos regulatórios por escola — Lei Lucas, Evacuação, Brigada e outros</div>
    </div>
    <button class="btn btn-pri" onclick="openEditTreinamento(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Novo Registro</button>
  </div>
  ${kpis}
  ${tabBtns}
  ${content}`;
}

function renderTrnLista(fl,redes,fT){
  const tipos=[...new Set(DB.tipos_treinamento.map(t=>t.nome))];
  const rows=fl.sort((a,b)=>{
    const o={vencido:0,nao_realizado:1,a_renovar:2,em_dia:3};
    return(o[a._status]||4)-(o[b._status]||4);
  }).map(t=>{
    const st=TRN_STATUS[t._status]||TRN_STATUS.nao_realizado;
    const days=t.data_vencimento?daysUntil(t.data_vencimento):null;
    const daysTag=days!==null?`<span style="font-size:10px;padding:1px 6px;border-radius:8px;font-weight:700;
      background:${days<0?'var(--rbg)':days<=30?'var(--ybg)':'var(--gbg)'};
      color:${days<0?'#991B1B':days<=30?'#92400E':'#15803D'}">${days<0?Math.abs(days)+'d atr.':days+'d'}</span>`:'';
    const tipoInfo=DB.tipos_treinamento.find(x=>x.nome===t.tipo_nome)||{};
    return`<tr>
      <td><div class="td-name">${esc(t.escola||'—')}</div><div class="td-sub">${esc(t.rede||'')}</div></td>
      <td>
        <div style="font-weight:600;font-size:13px">${esc(t.tipo_nome||'—')}</div>
        ${tipoInfo.lei?`<div style="font-size:10px;color:var(--muted)">${esc(tipoInfo.lei)}</div>`:''}
      </td>
      <td><span class="badge ${st.badge}">${st.label}</span></td>
      <td style="font-size:12px">${fmtDate(t.data_realizacao)}</td>
      <td>${fmtDate(t.data_vencimento)} ${daysTag}</td>
      <td style="font-size:12px;color:var(--muted)">${esc(t.instrutor||'—')}</td>
      <td style="text-align:center;font-size:12px">${t.num_participantes||'—'}</td>
      <td>
        ${t.carga_horaria?`<span style="font-size:11px;background:var(--sec);padding:2px 7px;border-radius:10px">${t.carga_horaria}h</span>`:'—'}
      </td>
      <td><div class="act-btns">
        <button class="btn btn-sec btn-sm" onclick="openEditTreinamento(${t.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteTreinamento(${t.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div></td>
    </tr>`;
  }).join('');

  return`
  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar escola, tipo ou instrutor..." value="${esc(fT.q||'')}"
             oninput="state.trnF.q=this.value;render()"></div>
    <select class="fs" onchange="state.trnF.rede=this.value;render()">
      <option value="">Todas as redes</option>
      ${redes.map(r=>`<option value="${esc(r)}"${fT.rede===r?' selected':''}>${esc(r)}</option>`).join('')}
    </select>
    <select class="fs" onchange="state.trnF.tipo=this.value;render()">
      <option value="">Todos os tipos</option>
      ${DB.tipos_treinamento.map(t=>`<option value="${esc(t.nome)}"${fT.tipo===t.nome?' selected':''}>${esc(t.nome)}</option>`).join('')}
    </select>
    <select class="fs" onchange="state.trnF.status=this.value;render()">
      <option value="">Todos os status</option>
      <option value="em_dia"${fT.status==='em_dia'?' selected':''}>✅ Em dia</option>
      <option value="a_renovar"${fT.status==='a_renovar'?' selected':''}>⚠️ A renovar</option>
      <option value="vencido"${fT.status==='vencido'?' selected':''}>🔴 Vencido</option>
      <option value="nao_realizado"${fT.status==='nao_realizado'?' selected':''}>— Não realizado</option>
    </select>
  </div>
  ${fl.length===0?`
  <div class="card" style="padding:50px 30px;text-align:center">
    <div style="font-size:42px;margin-bottom:12px">🎓</div>
    <div style="font-size:16px;font-weight:700;margin-bottom:8px">Nenhum treinamento cadastrado</div>
    <div style="color:var(--muted);font-size:13px;max-width:420px;margin:0 auto 20px">
      Registre os treinamentos obrigatórios de cada escola: Lei Lucas, Evacuação de Incêndio, Brigada e outros.
    </div>
    <button class="btn btn-pri" onclick="openEditTreinamento(null)">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Registrar primeiro treinamento</button>
  </div>`:`
  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr>
      <th>Escola</th><th>Tipo de Treinamento</th><th>Status</th>
      <th>Realização</th><th>Vencimento</th><th>Instrutor</th>
      <th>Participantes</th><th>Carga</th><th></th>
    </tr></thead>
    <tbody>${rows}</tbody></table>
  </div>`}`;
}

function renderTrnMapa(allTrn){
  const obrigatorios=DB.tipos_treinamento.filter(t=>t.obrigatorio);
  const escolas=[...DB.schools].sort((a,b)=>{
    // Ordenar por mais não-conformes primeiro
    const trnA=allTrn.filter(t=>t.escola_id===a.id);
    const trnB=allTrn.filter(t=>t.escola_id===b.id);
    const badA=trnA.filter(t=>['vencido','nao_realizado','a_renovar'].includes(t._status)).length;
    const badB=trnB.filter(t=>['vencido','nao_realizado','a_renovar'].includes(t._status)).length;
    return badB-badA;
  });

  const headerCols=obrigatorios.map(t=>`<th title="${esc(t.nome)}" style="max-width:80px;white-space:normal;text-align:center;padding:6px 4px">${esc(t.sigla)}</th>`).join('');

  const rows=escolas.map(s=>{
    const cells=obrigatorios.map(tipo=>{
      const reg=allTrn.filter(t=>t.escola_id===s.id&&t.tipo_nome===tipo.nome);
      if(!reg.length){
        return`<td class="status-cell trn-cell-nao">—</td>`;
      }
      // Pegar o registro mais recente
      const latest=reg.sort((a,b)=>(b.data_realizacao||'').localeCompare(a.data_realizacao||''))[0];
      const st=latest._status;
      const days=latest.data_vencimento?daysUntil(latest.data_vencimento):null;
      const label=days!==null?(days<0?Math.abs(days)+'d':days+'d'):'OK';
      const cls={em_dia:'trn-cell-ok',a_renovar:'trn-cell-warn',vencido:'trn-cell-venc',nao_realizado:'trn-cell-nao'}[st];
      return`<td class="status-cell ${cls}" title="${fmtDate(latest.data_vencimento)}"
              onclick="openEditTreinamento(${latest.id})" style="cursor:pointer">${label}</td>`;
    }).join('');
    const naoConformes=obrigatorios.filter(tipo=>{
      const reg=allTrn.filter(t=>t.escola_id===s.id&&t.tipo_nome===tipo.nome);
      if(!reg.length)return true;
      return['vencido','a_renovar'].includes(reg[0]._status);
    }).length;
    const cor=naoConformes===0?'var(--green)':naoConformes<=2?'var(--yellow)':'var(--red)';
    return`<tr>
      <td class="escola-col" style="border-right:2px solid var(--border)">
        <div style="display:flex;align-items:center;gap:8px">
          <div style="width:8px;height:8px;border-radius:50%;background:${cor};flex-shrink:0"></div>
          <div>
            <div>${esc(s.nome)}</div>
            <div style="font-size:10px;color:var(--muted)">${esc(s.rede)}</div>
          </div>
        </div>
      </td>
      ${cells}
    </tr>`;
  }).join('');

  return`
  <div class="card" style="padding:16px">
    <div style="font-size:13px;font-weight:700;margin-bottom:4px">Mapa de Conformidade — Treinamentos Obrigatórios</div>
    <div style="font-size:12px;color:var(--muted);margin-bottom:12px">Clique em uma célula para ver/editar o registro. Mostra apenas treinamentos obrigatórios.</div>
    <div style="display:flex;gap:12px;font-size:11px;margin-bottom:10px;flex-wrap:wrap">
      <span><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:var(--gbg);margin-right:4px"></span>✅ Em dia</span>
      <span><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:var(--ybg);margin-right:4px"></span>⚠️ A renovar</span>
      <span><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:var(--rbg);margin-right:4px"></span>🔴 Vencido</span>
      <span><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#F1F5F9;margin-right:4px"></span>— Não realizado</span>
    </div>
    <div class="trn-mapa">
      <table>
        <thead><tr>
          <th style="text-align:left;min-width:180px">Escola</th>
          ${headerCols}
        </tr></thead>
        <tbody>${rows}</tbody>
      </table>
    </div>
  </div>`;
}

function renderTrnTipos(){
  const rows=DB.tipos_treinamento.map((t,i)=>`
    <tr>
      <td><div class="td-name">${esc(t.nome)}</div></td>
      <td><span class="tag rede" style="font-size:10px">${esc(t.sigla)}</span></td>
      <td style="font-size:12px">${esc(t.lei||'—')}</td>
      <td style="font-size:12px;text-align:center">${t.meses} meses</td>
      <td><span class="badge ${t.obrigatorio?'danger':'gray'}">${t.obrigatorio?'Obrigatório':'Opcional'}</span></td>
      <td>
        <div style="font-size:11px;color:var(--muted)">
          ${DB.treinamentos.filter(r=>r.tipo_nome===t.nome).length} registros
        </div>
      </td>
      <td><div class="act-btns">
        <button class="btn btn-sec btn-sm" onclick="editTipoTreinamento(${i})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        ${DB.tipos_treinamento.length>1?`<button class="btn btn-danger btn-sm" onclick="deleteTipoTreinamento(${i})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>`:''}
      </div></td>
    </tr>`).join('');

  return`
  <div class="sh">
    <div class="sh-title" style="margin-bottom:0">Tipos de Treinamento</div>
    <button class="btn btn-pri btn-sm" onclick="addTipoTreinamento()">
      <i data-lucide="plus" style="width:13px;height:13px"></i>Novo Tipo</button>
  </div>
  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr>
      <th>Nome</th><th>Sigla</th><th>Base Legal</th><th>Periodicidade</th><th>Caráter</th><th>Registros</th><th></th>
    </tr></thead>
    <tbody>${rows}</tbody></table>
  </div>`;
}

function openEditTreinamento(id){
  const t=id?DB.treinamentos.find(x=>x.id===id)||{}:{};
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));
  showModal(id?'Editar Registro de Treinamento':'Novo Registro de Treinamento',`
    <div class="fr">
      <div class="fg"><label>Escola *</label>
        <select class="fi" id="tt-escola">
          <option value="">Selecione...</option>
          ${escolas.map(s=>`<option value="${s.id}" data-nome="${esc(s.nome)}" data-rede="${esc(s.rede)}"${t.escola_id===s.id?' selected':''}>${esc(s.nome)} (${esc(s.rede)})</option>`).join('')}
        </select></div>
      <div class="fg"><label>Tipo de Treinamento *</label>
        <select class="fi" id="tt-tipo" onchange="autoPreenchePeriodo(this)">
          <option value="">Selecione...</option>
          ${DB.tipos_treinamento.map(x=>`<option value="${esc(x.nome)}" data-meses="${x.meses}"${t.tipo_nome===x.nome?' selected':''}>${esc(x.nome)}</option>`).join('')}
        </select></div>
    </div>
    <div style="font-size:11px;color:var(--muted);margin-top:-8px;margin-bottom:10px" id="tt-lei-info"></div>
    <div class="fr">
      <div class="fg"><label>Data de Realização</label>
        <input type="date" class="fi" id="tt-realizacao" value="${t.data_realizacao||''}"
               oninput="autoCalcVencimento()"></div>
      <div class="fg"><label>Data de Vencimento</label>
        <input type="date" class="fi" id="tt-vencimento" value="${t.data_vencimento||''}"></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Instrutor / Empresa</label>
        <input type="text" class="fi" id="tt-instrutor" value="${esc(t.instrutor||'')}" placeholder="Ex: Bombeiros Voluntários, SESC..."></div>
      <div class="fg"><label>Nº de Participantes</label>
        <input type="number" class="fi" id="tt-participantes" value="${t.num_participantes||''}" min="1" placeholder="Ex: 25"></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Carga Horária (horas)</label>
        <input type="number" class="fi" id="tt-carga" value="${t.carga_horaria||''}" min="1" placeholder="Ex: 8"></div>
      <div class="fg"><label>Certificado emitido?</label>
        <select class="fi" id="tt-cert">
          <option value="sim"${t.certificado_emitido!==false?' selected':''}>✅ Sim</option>
          <option value="nao"${t.certificado_emitido===false?' selected':''}>❌ Não</option>
        </select></div>
    </div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="tt-obs" rows="2" placeholder="Conteúdo abordado, local, observações...">${esc(t.observacoes||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveTreinamento(${id||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
  // Preencher info da lei selecionada
  setTimeout(()=>{
    const sel=document.getElementById('tt-tipo');
    if(sel)autoPreenchePeriodo(sel);
    document.getElementById('tt-tipo')?.addEventListener('change',function(){autoPreenchePeriodo(this);});
  },50);
}

function autoPreenchePeriodo(sel){
  const opt=sel.options[sel.selectedIndex];
  const meses=parseInt(opt?.dataset?.meses)||0;
  const nome=sel.value;
  const tipo=DB.tipos_treinamento.find(t=>t.nome===nome);
  const infoEl=document.getElementById('tt-lei-info');
  if(infoEl&&tipo)infoEl.textContent=`${tipo.lei?'Base legal: '+tipo.lei+' · ':''}Renovação a cada ${tipo.meses} meses`;
  autoCalcVencimento();
}

function autoCalcVencimento(){
  const dt=document.getElementById('tt-realizacao')?.value;
  const sel=document.getElementById('tt-tipo');
  const opt=sel?.options[sel?.selectedIndex];
  const meses=parseInt(opt?.dataset?.meses)||0;
  const vencEl=document.getElementById('tt-vencimento');
  if(dt&&meses&&vencEl&&!vencEl.value){
    const d=new Date(dt);d.setMonth(d.getMonth()+meses);
    vencEl.value=d.toISOString().split('T')[0];
  }
}

function saveTreinamento(id){
  const selE=document.getElementById('tt-escola');
  const escolaId=parseInt(selE?.value)||null;
  const selOpt=selE?.options[selE?.selectedIndex];
  const tipoNome=document.getElementById('tt-tipo')?.value;
  if(!escolaId||!tipoNome){showToast('Escola e tipo são obrigatórios','error');return;}
  const rec={
    escola_id:escolaId,
    escola:selOpt?selOpt.dataset.nome:'',
    rede:selOpt?selOpt.dataset.rede:'',
    tipo_nome:tipoNome,
    data_realizacao:document.getElementById('tt-realizacao')?.value||null,
    data_vencimento:document.getElementById('tt-vencimento')?.value||null,
    instrutor:document.getElementById('tt-instrutor')?.value?.trim()||null,
    num_participantes:parseInt(document.getElementById('tt-participantes')?.value)||null,
    carga_horaria:parseInt(document.getElementById('tt-carga')?.value)||null,
    certificado_emitido:document.getElementById('tt-cert')?.value!=='nao',
    observacoes:document.getElementById('tt-obs')?.value?.trim()||null,
  };
  if(id>0){const idx=DB.treinamentos.findIndex(x=>x.id===id);if(idx>=0)Object.assign(DB.treinamentos[idx],rec);}
  else DB.treinamentos.push({id:nextId(DB.treinamentos),...rec});
  save();closeModal();render();showToast('Treinamento salvo!');
}

function deleteTreinamento(id){
  if(!confirm('Excluir este registro de treinamento?'))return;
  DB.treinamentos=DB.treinamentos.filter(x=>x.id!==id);
  save();render();showToast('Treinamento excluído','error');
}

function addTipoTreinamento(){
  const nome=prompt('Nome do tipo de treinamento:','');
  if(!nome?.trim())return;
  const sigla=prompt('Sigla (abreviação):',nome.trim().split(' ')[0]);
  const meses=parseInt(prompt('Periodicidade (meses de validade):','12')||'12');
  const lei=prompt('Base legal (opcional):','');
  DB.tipos_treinamento.push({
    id:nextId(DB.tipos_treinamento.map((_,i)=>({id:i+1}))),
    nome:nome.trim(),sigla:sigla?.trim()||nome.trim(),
    meses,lei:lei?.trim()||'',obrigatorio:false
  });
  save();render();showToast('Tipo de treinamento adicionado!');
}

function editTipoTreinamento(i){
  const t=DB.tipos_treinamento[i];if(!t)return;
  showModal('Editar Tipo de Treinamento',`
    <div class="fg"><label>Nome completo</label>
      <input type="text" class="fi" id="ttp-nome" value="${esc(t.nome)}"></div>
    <div class="fr">
      <div class="fg"><label>Sigla</label>
        <input type="text" class="fi" id="ttp-sigla" value="${esc(t.sigla)}"></div>
      <div class="fg"><label>Periodicidade (meses)</label>
        <input type="number" class="fi" id="ttp-meses" value="${t.meses}" min="1"></div>
    </div>
    <div class="fg"><label>Base Legal</label>
      <input type="text" class="fi" id="ttp-lei" value="${esc(t.lei||'')}" placeholder="Ex: Lei 13.722/2018"></div>
    <div class="fg"><label>Caráter</label>
      <select class="fi" id="ttp-obrig">
        <option value="1"${t.obrigatorio?' selected':''}>Obrigatório</option>
        <option value="0"${!t.obrigatorio?' selected':''}>Opcional</option>
      </select></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveTipoTreinamento(${i})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

function saveTipoTreinamento(i){
  const t=DB.tipos_treinamento[i];if(!t)return;
  t.nome=document.getElementById('ttp-nome')?.value?.trim()||t.nome;
  t.sigla=document.getElementById('ttp-sigla')?.value?.trim()||t.sigla;
  t.meses=parseInt(document.getElementById('ttp-meses')?.value)||t.meses;
  t.lei=document.getElementById('ttp-lei')?.value?.trim()||'';
  t.obrigatorio=document.getElementById('ttp-obrig')?.value==='1';
  save();closeModal();render();showToast('Tipo atualizado!');
}

function deleteTipoTreinamento(i){
  if(!confirm(`Excluir tipo "${DB.tipos_treinamento[i]?.nome}"?`))return;
  DB.tipos_treinamento.splice(i,1);
  save();render();showToast('Tipo removido','error');
}

// ── AUDITORIA ─────────────────────────────────────────────────────────────────
const AUDIT_TEMPLATE=[
  {cat:'Licenciamento Municipal',items:['Alvará de Funcionamento vigente','Habite-se apresentado','AVCB Corpo de Bombeiros vigente']},
  {cat:'Vigilância Sanitária',items:['Licença Sanitária vigente','Manual de Boas Práticas','Certificado de desinsetização atualizado']},
  {cat:'Secretaria de Educação (SEEDUC/SME)',items:['Ato Autorizativo publicado no DO','PAA aprovado pela SEC','ETAP aprovada pela SEC','Regimento Interno aprovado','PPP atualizado','Código INEP cadastrado']},
  {cat:'CREA / Laudos Técnicos',items:['Laudo de instalações elétricas (ART)','Laudo de acessibilidade NBR 9050','ART do responsável técnico registrada']},
  {cat:'Documentação Corporativa',items:['CNPJ ativo e atualizado','Certidão Negativa Federal','Certidão Negativa Estadual','Certidão Negativa Municipal']},
];

function renderAuditoria(){
  const auditorias=[...DB.auditorias].sort((a,b)=>(b.data||'').localeCompare(a.data||''));
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));

  const rows=auditorias.map(a=>{
    const conf=a.items?a.items.filter(i=>i.resultado==='conforme').length:0;
    const nc=a.items?a.items.filter(i=>i.resultado==='nao_conforme').length:0;
    const total=a.items?a.items.filter(i=>i.resultado&&i.resultado!=='nao_aplicavel').length:0;
    const pct=total?Math.round(conf/total*100):0;
    return`<tr>
      <td><div class="td-name">${esc(a.escola)}</div><div class="td-sub">${esc(a.rede||'')}</div></td>
      <td style="font-size:12px">${fmtDate(a.data)}</td>
      <td style="font-size:12px">${esc(a.auditor||'—')}</td>
      <td>
        <div style="display:flex;align-items:center;gap:8px">
          <div style="width:60px;height:6px;background:var(--sec);border-radius:3px;overflow:hidden">
            <div style="height:100%;width:${pct}%;background:${pct>=80?'var(--green)':pct>=50?'var(--yellow)':'var(--red)'};border-radius:3px"></div>
          </div>
          <span style="font-size:11px;font-weight:700;color:${pct>=80?'var(--green)':pct>=50?'var(--yellow)':'var(--red)'}">${pct}%</span>
          ${nc>0?`<span class="badge danger">${nc} NC</span>`:''}
        </div>
      </td>
      <td><span class="badge ${a.status==='concluida'?'ok':'warn'}">${a.status==='concluida'?'Concluída':'Em andamento'}</span></td>
      <td><div class="act-btns">
        <button class="btn btn-pri btn-sm" onclick="openAuditDetail(${a.id})">Ver</button>
        <button class="btn btn-danger btn-sm" onclick="deleteAuditoria(${a.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div></td>
    </tr>`;
  }).join('');

  return`
  <div class="sh">
    <div><div class="sh-title">Auditoria & Conformidade</div>
      <div class="sh-sub">Vistorias internas de documentação por escola</div></div>
    <button class="btn btn-pri" onclick="openNovaAuditoria()">
      <i data-lucide="clipboard-check" style="width:14px;height:14px"></i>Nova Auditoria</button>
  </div>
  ${auditorias.length===0?`
  <div class="card" style="padding:60px 30px;text-align:center">
    <div style="font-size:48px;margin-bottom:14px">📋</div>
    <div style="font-size:17px;font-weight:700;margin-bottom:8px">Nenhuma auditoria realizada</div>
    <div style="color:var(--muted);font-size:14px;max-width:400px;margin:0 auto 20px">
      Realize vistorias internas para verificar a situação documental de cada escola antes de protocolar na SEEDUC/SME.
    </div>
    <button class="btn btn-pri" onclick="openNovaAuditoria()">
      <i data-lucide="plus" style="width:14px;height:14px"></i>Iniciar primeira auditoria</button>
  </div>`:`
  <div class="card tbl-wrap" style="padding:0">
    <table><thead><tr><th>Escola</th><th>Data</th><th>Auditor</th><th>Conformidade</th><th>Status</th><th></th></tr></thead>
    <tbody>${rows}</tbody></table>
  </div>`}`;
}

function openNovaAuditoria(){
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));
  showModal('Nova Auditoria',`
    <div class="fr">
      <div class="fg"><label>Escola *</label>
        <select class="fi" id="aud-escola">
          <option value="">Selecione...</option>
          ${escolas.map(s=>`<option value="${s.id}" data-nome="${esc(s.nome)}" data-rede="${esc(s.rede)}">${esc(s.nome)} (${esc(s.rede)})</option>`).join('')}
        </select></div>
      <div class="fg"><label>Data *</label>
        <input type="date" class="fi" id="aud-data" value="${todayISO()}"></div>
    </div>
    <div class="fg"><label>Auditor</label>
      <select class="fi" id="aud-auditor">
        ${DB.usuarios.filter(u=>u.ativo).map(u=>`<option value="${esc(u.nome)}">${esc(u.nome)}</option>`).join('')}
      </select></div>
    <div class="fg"><label>Observação Geral</label>
      <textarea class="fi" id="aud-obs" rows="2"></textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="criarAuditoria()"><i data-lucide="play" style="width:13px;height:13px"></i>Iniciar</button>`
  );
}

function criarAuditoria(){
  const selEsc=document.getElementById('aud-escola');
  const escolaId=parseInt(selEsc.value)||null;
  const selOpt=selEsc.options[selEsc.selectedIndex];
  if(!escolaId){showToast('Selecione uma escola','error');return;}
  const escola=selOpt.dataset.nome;
  const rede=selOpt.dataset.rede;
  const data=document.getElementById('aud-data').value;
  const auditor=document.getElementById('aud-auditor').value;
  const obs=document.getElementById('aud-obs').value.trim();
  const items=[];
  AUDIT_TEMPLATE.forEach(cat=>{
    cat.items.forEach(item=>{
      items.push({id:Date.now()+Math.random(),cat:cat.cat,item,resultado:null,obs:''});
    });
  });
  const id=nextId(DB.auditorias);
  DB.auditorias.push({id,escola_id:escolaId,escola,rede,data,auditor,status:'em_andamento',items,obs_geral:obs||null});
  save();closeModal();openAuditDetail(id);
}

function openAuditDetail(id){
  const a=DB.auditorias.find(x=>x.id===id);if(!a)return;
  const conf=a.items.filter(i=>i.resultado==='conforme').length;
  const nc=a.items.filter(i=>i.resultado==='nao_conforme').length;
  const na=a.items.filter(i=>i.resultado==='nao_aplicavel').length;
  const total=a.items.filter(i=>i.resultado&&i.resultado!=='nao_aplicavel').length;
  const pct=total?Math.round(conf/total*100):0;

  const cats=[...new Set(a.items.map(i=>i.cat))];
  const itemsHtml=cats.map(cat=>`
    <div style="margin-bottom:16px">
      <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--muted);margin-bottom:8px;padding-bottom:4px;border-bottom:2px solid var(--border)">${esc(cat)}</div>
      ${a.items.filter(i=>i.cat===cat).map(item=>`
        <div class="aud-item">
          <div style="flex:1;font-size:13px">${esc(item.item)}</div>
          <div class="aud-resultado">
            <button class="aud-btn${item.resultado==='conforme'?' conforme':''}" onclick="setAudItem(${id},'${item.id}','conforme')">✅ Conforme</button>
            <button class="aud-btn${item.resultado==='nao_conforme'?' nao_conforme':''}" onclick="setAudItem(${id},'${item.id}','nao_conforme')">❌ Não conforme</button>
            <button class="aud-btn${item.resultado==='nao_aplicavel'?' nao_aplicavel':''}" onclick="setAudItem(${id},'${item.id}','nao_aplicavel')">— N/A</button>
          </div>
        </div>
        ${item.resultado==='nao_conforme'?`<div style="margin-left:0;margin-bottom:8px">
          <input type="text" class="fi" placeholder="Observação sobre a não conformidade..."
                 value="${esc(item.obs||'')}" style="font-size:11px"
                 onchange="setAudItemObs(${id},'${item.id}',this.value)"></div>`:''}`
      ).join('')}
    </div>`).join('');

  showModal(`Auditoria — ${a.escola}`,`
    <div style="display:flex;gap:12px;margin-bottom:16px">
      <div class="card" style="padding:12px;flex:1;text-align:center">
        <div style="font-size:24px;font-weight:800;color:${pct>=80?'var(--green)':pct>=50?'var(--yellow)':'var(--red)'}">${pct}%</div>
        <div style="font-size:11px;color:var(--muted)">Conformidade</div>
      </div>
      <div class="card" style="padding:12px;flex:1;text-align:center">
        <div style="font-size:24px;font-weight:800;color:var(--green)">${conf}</div>
        <div style="font-size:11px;color:var(--muted)">Conformes</div>
      </div>
      <div class="card" style="padding:12px;flex:1;text-align:center">
        <div style="font-size:24px;font-weight:800;color:var(--red)">${nc}</div>
        <div style="font-size:11px;color:var(--muted)">Não conformes</div>
      </div>
    </div>
    <div style="font-size:12px;color:var(--muted);margin-bottom:14px">
      ${esc(a.escola)} · ${fmtDate(a.data)} · Auditor: ${esc(a.auditor||'—')}
    </div>
    ${itemsHtml}`,
    `<button class="btn btn-sec" onclick="closeModal()">Fechar</button>
     ${a.status==='em_andamento'?`<button class="btn btn-pri" onclick="concluirAuditoria(${id})"><i data-lucide="check" style="width:13px;height:13px"></i>Concluir</button>`:''}
     <button class="btn btn-sec" onclick="exportAuditoria(${id})"><i data-lucide="download" style="width:13px;height:13px"></i>Exportar</button>`
  ,'modal-lg');
}

function setAudItem(audId,itemId,resultado){
  const a=DB.auditorias.find(x=>x.id===audId);if(!a)return;
  const item=a.items.find(i=>String(i.id)===String(itemId));if(!item)return;
  item.resultado=resultado;save();openAuditDetail(audId);
}
function setAudItemObs(audId,itemId,obs){
  const a=DB.auditorias.find(x=>x.id===audId);if(!a)return;
  const item=a.items.find(i=>String(i.id)===String(itemId));if(item)item.obs=obs;save();
}
function concluirAuditoria(id){
  const a=DB.auditorias.find(x=>x.id===id);if(!a)return;
  const semResultado=a.items.filter(i=>!i.resultado).length;
  if(semResultado>0&&!confirm(`${semResultado} item(ns) sem resultado. Concluir assim mesmo?`))return;
  a.status='concluida';
  const nc=a.items.filter(i=>i.resultado==='nao_conforme');
  if(nc.length>0){
    nc.forEach(item=>{
      DB.tarefas.push({id:nextId(DB.tarefas),titulo:`[Auditoria] ${item.item}`,
        descricao:item.obs||`Não conformidade identificada em auditoria de ${fmtDate(a.data)}`,
        responsavel:DB.usuarios[0]?.nome||null,escola:a.escola,
        categoria:'Auditoria',prioridade:'alta',prazo:null,status:'pendente',criada_em:todayISO()});
    });
    showToast(`${nc.length} tarefa(s) criada(s) para as não conformidades!`);
  }
  save();closeModal();render();showToast('Auditoria concluída!');
}
function deleteAuditoria(id){
  if(!confirm('Excluir esta auditoria?'))return;
  DB.auditorias=DB.auditorias.filter(x=>x.id!==id);
  save();render();showToast('Auditoria excluída','error');
}
function exportAuditoria(id){
  const a=DB.auditorias.find(x=>x.id===id);if(!a)return;
  const conf=a.items.filter(i=>i.resultado==='conforme').length;
  const nc=a.items.filter(i=>i.resultado==='nao_conforme').length;
  const total=a.items.filter(i=>i.resultado&&i.resultado!=='nao_aplicavel').length;
  const pct=total?Math.round(conf/total*100):0;
  const rows=[
    [`RELATÓRIO DE AUDITORIA — ${a.escola}`],[`Data: ${fmtDate(a.data)}`],[`Auditor: ${a.auditor||'—'}`],
    [`Conformidade: ${pct}% (${conf} conformes / ${nc} não conformes)`],[],
    ['Categoria','Item','Resultado','Observação'],
    ...a.items.map(i=>[i.cat,i.item,{conforme:'Conforme',nao_conforme:'Não Conforme',nao_aplicavel:'N/A'}[i.resultado]||'—',i.obs||''])
  ];
  const csv='﻿'+rows.map(r=>r.map(c=>`"${String(c||'').replace(/"/g,'""')}"`).join(';')).join('\r\n');
  const blob=new Blob([csv],{type:'text/csv;charset=utf-8;'});
  const link=document.createElement('a');link.href=URL.createObjectURL(blob);
  link.download=`auditoria_${a.escola.replace(/[^a-z0-9]/gi,'_')}_${a.data}.csv`;link.click();
  showToast('Auditoria exportada!');
}

// ── ETAP ───────────────────────────────────────────────────────────────────────
const ETAP_STATUS_MAP={
  pendente:{label:'⏳ Pendente',color:'#94a3b8',bg:'#F1F5F9'},
  em_elaboracao:{label:'📝 Em elaboração',color:'#4B5563',bg:'#F3F4F6'},
  protocolado:{label:'📬 Protocolado',color:'#1D4ED8',bg:'#EFF6FF'},
  em_analise:{label:'🔍 Em análise',color:'#92400E',bg:'#FEF3C7'},
  exigencia:{label:'⚠️ Exigência',color:'#991B1B',bg:'#FEE2E2'},
  aprovado:{label:'✅ Aprovado',color:'#15803D',bg:'#DCFCE7'},
};

function renderEtap(){
  const f=state.escolasF||{rede:'',q:''};
  const redes=[...new Set(DB.schools.map(s=>s.rede))].sort();
  let escolas=[...DB.schools];
  if(f.rede)escolas=escolas.filter(s=>s.rede===f.rede);
  if(f.q){const q=f.q.toLowerCase();escolas=escolas.filter(s=>s.nome.toLowerCase().includes(q));}

  const cards=escolas.map(s=>{
    const etap=DB.etaps.find(e=>e.escola_id===s.id);
    const st=etap?ETAP_STATUS_MAP[etap.status]||ETAP_STATUS_MAP.pendente:ETAP_STATUS_MAP.pendente;
    const membros=etap?etap.membros.length:0;
    const dos_=etap?etap.publicacoes_do.length:0;
    return`<div class="card" style="padding:16px;cursor:pointer;transition:transform .15s" onclick="openEtapDetail(${s.id})"
               onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform=''">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px">
        <div style="font-size:14px;font-weight:700">${esc(s.nome)}</div>
        <span style="padding:3px 10px;border-radius:20px;font-size:10px;font-weight:700;
                     background:${st.bg};color:${st.color}">${st.label}</span>
      </div>
      <div style="font-size:11px;color:var(--muted);margin-bottom:8px">${esc(s.rede)} · ${s.estado}</div>
      ${etap&&etap.numero_protocolo?`<div style="font-size:10px;color:var(--muted);margin-bottom:6px">📬 ${esc(etap.numero_protocolo)}</div>`:''}
      <div style="display:flex;gap:12px;font-size:11px;color:var(--muted)">
        <span>👥 ${membros} membro(s)</span>
        <span>📰 ${dos_} pub. DO</span>
        ${etap&&etap.data_aprovacao?`<span style="color:var(--green);font-weight:600">✅ Aprovada em ${fmtDate(etap.data_aprovacao)}</span>`:''}
      </div>
    </div>`;
  }).join('');

  return`
  <div class="sh">
    <div><div class="sh-title">ETAP — Estudo Técnico de Adequação de Projeto</div>
      <div class="sh-sub">Acompanhamento das ETAPs por unidade escolar · ${DB.etaps.filter(e=>e.status==='aprovado').length} aprovadas · ${DB.etaps.filter(e=>e.status==='em_analise').length} em análise</div></div>
  </div>
  <div class="filters">
    <div class="search"><i data-lucide="search" style="width:14px;height:14px;color:var(--muted)"></i>
      <input placeholder="Buscar escola..." oninput="state.escolasF={...state.escolasF,q:this.value};render()"></div>
    <select class="fs" onchange="state.escolasF={...state.escolasF,rede:this.value};render()">
      <option value="">Todas as redes</option>
      ${redes.map(r=>`<option value="${esc(r)}"${f.rede===r?' selected':''}>${esc(r)}</option>`).join('')}
    </select>
  </div>
  <div class="sc-grid">${cards||'<div class="empty"><div class="empty-icon">📐</div><div class="empty-title">Nenhuma escola encontrada</div></div>'}</div>`;
}

function openEtapDetail(escolaId){
  const s=DB.schools.find(x=>x.id===escolaId);if(!s)return;
  let etap=DB.etaps.find(e=>e.escola_id===escolaId);
  if(!etap){
    etap={id:nextId(DB.etaps),escola_id:escolaId,escola:s.nome,rede:s.rede,
      versao:'1',data_elaboracao:null,data_protocolo:null,numero_protocolo:null,
      status:'pendente',data_aprovacao:null,obs:null,membros:[],publicacoes_do:[],processos_vinculados:[]};
    DB.etaps.push(etap);save();
  }
  const st=ETAP_STATUS_MAP[etap.status]||ETAP_STATUS_MAP.pendente;
  const membrosHtml=etap.membros.length?etap.membros.map(m=>`
    <div class="etap-membro">
      <div class="ct-av" style="width:36px;height:36px;font-size:12px;background:${avatarColor(m.nome)};flex-shrink:0">
        ${(m.nome||'?').split(' ').map(w=>w[0]).slice(0,2).join('').toUpperCase()}</div>
      <div style="flex:1;min-width:0">
        <div style="font-size:13px;font-weight:600">${esc(m.nome)}</div>
        <div style="font-size:11px;color:var(--muted)">${esc(m.cargo||'')}${m.registro?` · ${esc(m.registro)}`:''}</div>
        <div style="font-size:11px;color:var(--muted)">${m.telefone?`📞 ${esc(m.telefone)}&nbsp;&nbsp;`:''}${m.email?`✉️ ${esc(m.email)}`:''}</div>
        ${m.art?`<div style="font-size:10px;background:var(--sec);padding:2px 6px;border-radius:4px;margin-top:4px;display:inline-block">ART/RRT: ${esc(m.art)}</div>`:''}
      </div>
      <div style="display:flex;gap:4px">
        <button class="btn btn-sec btn-sm" onclick="openEditMembroEtap(${escolaId},${m.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteMembroEtap(${escolaId},${m.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div>
    </div>`).join('')
    :`<div style="color:var(--muted);font-size:12px;padding:10px 0">Nenhum membro cadastrado.</div>`;

  const dosHtml=etap.publicacoes_do.length?etap.publicacoes_do.map(d=>`
    <div class="etap-do-row">
      <div style="flex:1">
        <div style="font-size:13px;font-weight:600">${esc(d.tipo||'Publicação')}</div>
        <div style="font-size:11px;color:var(--muted)">DO nº ${esc(d.numero_do||'—')} · ${fmtDate(d.data_publicacao)}${d.pagina?` · Pág. ${esc(d.pagina)}`:''}</div>
        ${d.link?`<a href="${esc(d.link)}" target="_blank" style="font-size:10px;color:var(--acc)">🔗 Ver publicação</a>`:''}
        ${d.obs?`<div style="font-size:10px;color:var(--muted);margin-top:2px">${esc(d.obs)}</div>`:''}
      </div>
      <div style="display:flex;gap:4px">
        <button class="btn btn-sec btn-sm" onclick="openEditDoEtap(${escolaId},${d.id})"><i data-lucide="pencil" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteDoEtap(${escolaId},${d.id})"><i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div>
    </div>`).join('')
    :`<div style="color:var(--muted);font-size:12px;padding:10px 0">Nenhuma publicação cadastrada.</div>`;

  const procsVinc=DB.procs.filter(p=>etap.processos_vinculados&&etap.processos_vinculados.includes(p.id));
  const procsHtml=procsVinc.length?procsVinc.map(p=>`
    <div style="padding:8px 0;border-bottom:1px solid var(--border)">
      <div style="font-size:12px;font-weight:500">${esc(p.numero)}</div>
      <div style="display:flex;align-items:center;gap:8px;margin-top:3px">
        <span class="proc-status ps-${p.status}" style="font-size:10px">${statusLabel(p.status)}</span>
        <span style="font-size:11px;color:var(--muted)">${esc(p.prazo||'—')}</span>
      </div>
    </div>`).join('')
    :`<div style="color:var(--muted);font-size:12px;padding:6px 0">Nenhum processo vinculado.</div>`;

  showModal(`ETAP — ${s.nome}`,`
    <!-- Status e dados principais -->
    <div style="background:${st.bg};border-radius:10px;padding:14px;margin-bottom:16px">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">
        <span style="font-size:13px;font-weight:700;color:${st.color}">${st.label}</span>
        <button class="btn btn-sec btn-sm" onclick="openEditEtap(${escolaId})"><i data-lucide="pencil" style="width:11px;height:11px"></i>Editar ETAP</button>
      </div>
      <div class="fr" style="gap:10px">
        <div><label style="font-size:10px">Versão</label><div style="font-weight:700">${esc(etap.versao||'—')}</div></div>
        <div><label style="font-size:10px">Elaboração</label><div>${fmtDate(etap.data_elaboracao)}</div></div>
        <div><label style="font-size:10px">Protocolo</label><div>${fmtDate(etap.data_protocolo)}</div></div>
        <div><label style="font-size:10px">Aprovação</label><div style="color:${etap.data_aprovacao?'var(--green)':'var(--muted)'}">${fmtDate(etap.data_aprovacao)}</div></div>
      </div>
      ${etap.numero_protocolo?`<div style="margin-top:8px;font-size:11px">📬 Protocolo: <strong>${esc(etap.numero_protocolo)}</strong></div>`:''}
      ${etap.obs?`<div style="margin-top:6px;font-size:11px;color:var(--muted)">${esc(etap.obs)}</div>`:''}
    </div>

    <!-- Membros -->
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
      <div style="font-weight:700;font-size:13px">👥 Equipe / Membros</div>
      <button class="btn btn-pri btn-sm" onclick="openEditMembroEtap(${escolaId},null)">
        <i data-lucide="plus" style="width:11px;height:11px"></i>Novo Membro</button>
    </div>
    ${membrosHtml}

    <div class="divider"></div>

    <!-- Publicações DO -->
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
      <div style="font-weight:700;font-size:13px">📰 Publicações no Diário Oficial</div>
      <button class="btn btn-pri btn-sm" onclick="openEditDoEtap(${escolaId},null)">
        <i data-lucide="plus" style="width:11px;height:11px"></i>Nova Publicação</button>
    </div>
    ${dosHtml}

    <div class="divider"></div>

    <!-- Processos vinculados -->
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
      <div style="font-weight:700;font-size:13px">📋 Processos SEI Vinculados</div>
      <button class="btn btn-sec btn-sm" onclick="openVincularProcesso(${escolaId})">
        <i data-lucide="link" style="width:11px;height:11px"></i>Vincular</button>
    </div>
    ${procsHtml}`,
    `<button class="btn btn-sec" onclick="closeModal()">Fechar</button>`,
  'modal-lg');
}

function openEditEtap(escolaId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId)||{};
  showModal('Editar ETAP',`
    <div class="fr">
      <div class="fg"><label>Versão</label>
        <input type="text" class="fi" id="etap-ver" value="${esc(etap.versao||'1')}" placeholder="Ex: 1, 2, 3..."></div>
      <div class="fg"><label>Status</label>
        <select class="fi" id="etap-st">
          ${Object.entries(ETAP_STATUS_MAP).map(([k,v])=>`<option value="${k}"${etap.status===k?' selected':''}>${v.label}</option>`).join('')}
        </select></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Data de Elaboração</label>
        <input type="date" class="fi" id="etap-elab" value="${etap.data_elaboracao||''}"></div>
      <div class="fg"><label>Data de Protocolo</label>
        <input type="date" class="fi" id="etap-proto" value="${etap.data_protocolo||''}"></div>
    </div>
    <div class="fg"><label>Número do Protocolo SEI</label>
      <input type="text" class="fi" id="etap-num-proto" value="${esc(etap.numero_protocolo||'')}" placeholder="Ex: SEI-030001/001234/2025"></div>
    <div class="fg"><label>Data de Aprovação</label>
      <input type="date" class="fi" id="etap-aprov" value="${etap.data_aprovacao||''}"></div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="etap-obs" rows="2">${esc(etap.obs||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveEtap(${escolaId})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}

function saveEtap(escolaId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  Object.assign(etap,{
    versao:document.getElementById('etap-ver').value.trim()||'1',
    status:document.getElementById('etap-st').value,
    data_elaboracao:document.getElementById('etap-elab').value||null,
    data_protocolo:document.getElementById('etap-proto').value||null,
    numero_protocolo:document.getElementById('etap-num-proto').value.trim()||null,
    data_aprovacao:document.getElementById('etap-aprov').value||null,
    obs:document.getElementById('etap-obs').value.trim()||null,
  });
  save();closeModal();openEtapDetail(escolaId);showToast('ETAP salva!');
}

function openEditMembroEtap(escolaId,membroId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  const m=membroId?etap.membros.find(x=>x.id===membroId)||{}:{};
  showModal(membroId?'Editar Membro':'Novo Membro da Equipe ETAP',`
    <div class="fr">
      <div class="fg"><label>Nome completo *</label>
        <input type="text" class="fi" id="mb-nome" value="${esc(m.nome||'')}" placeholder="Ex: Eduardo Martins"></div>
      <div class="fg"><label>Cargo / Função *</label>
        <input type="text" class="fi" id="mb-cargo" value="${esc(m.cargo||'')}" placeholder="Ex: Engenheiro Responsável, Arquiteto..."></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Registro profissional (CREA/CAU)</label>
        <input type="text" class="fi" id="mb-reg" value="${esc(m.registro||'')}" placeholder="Ex: CREA 12345-SP"></div>
      <div class="fg"><label>Número ART/RRT</label>
        <input type="text" class="fi" id="mb-art" value="${esc(m.art||'')}" placeholder="Nº da ART ou RRT"></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Telefone</label>
        <input type="tel" class="fi" id="mb-tel" value="${esc(m.telefone||'')}" placeholder="(21) 99999-0000"></div>
      <div class="fg"><label>E-mail</label>
        <input type="email" class="fi" id="mb-email" value="${esc(m.email||'')}" placeholder="nome@empresa.com.br"></div>
    </div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="mb-obs" rows="2">${esc(m.obs||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveMembroEtap(${escolaId},${membroId||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}
function saveMembroEtap(escolaId,membroId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  const nome=document.getElementById('mb-nome').value.trim();
  if(!nome){showToast('Nome é obrigatório','error');return;}
  const rec={nome,cargo:document.getElementById('mb-cargo').value.trim(),
    registro:document.getElementById('mb-reg').value.trim(),art:document.getElementById('mb-art').value.trim(),
    telefone:document.getElementById('mb-tel').value.trim(),email:document.getElementById('mb-email').value.trim(),
    obs:document.getElementById('mb-obs').value.trim()};
  if(membroId>0){const idx=etap.membros.findIndex(x=>x.id===membroId);if(idx>=0)Object.assign(etap.membros[idx],rec);}
  else etap.membros.push({id:nextId(etap.membros),...rec});
  save();closeModal();openEtapDetail(escolaId);showToast('Membro salvo!');
}
function deleteMembroEtap(escolaId,membroId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  if(!confirm('Excluir membro?'))return;
  etap.membros=etap.membros.filter(x=>x.id!==membroId);
  save();openEtapDetail(escolaId);showToast('Membro removido','error');
}

function openEditDoEtap(escolaId,doId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  const d=doId?etap.publicacoes_do.find(x=>x.id===doId)||{}:{};
  const tipos=['Autorização de Funcionamento','Renovação de Autorização','Transferência de Mantenedora',
    'Recredenciamento','Suspensão','Cassação','Ato de Credenciamento','Outro'];
  showModal(doId?'Editar Publicação DO':'Nova Publicação no Diário Oficial',`
    <div class="fr">
      <div class="fg"><label>Tipo de Publicação *</label>
        <select class="fi" id="do-tipo">
          <option value="">Selecione...</option>
          ${tipos.map(t=>`<option value="${t}"${d.tipo===t?' selected':''}>${t}</option>`).join('')}
        </select></div>
      <div class="fg"><label>Data de Publicação *</label>
        <input type="date" class="fi" id="do-data" value="${d.data_publicacao||''}"></div>
    </div>
    <div class="fr">
      <div class="fg"><label>Número / Edição do DO</label>
        <input type="text" class="fi" id="do-num" value="${esc(d.numero_do||'')}" placeholder="Ex: DO 47.234"></div>
      <div class="fg"><label>Página</label>
        <input type="text" class="fi" id="do-pag" value="${esc(d.pagina||'')}" placeholder="Ex: 15"></div>
    </div>
    <div class="fg"><label>Link para o DO (opcional)</label>
      <input type="text" class="fi" id="do-link" value="${esc(d.link||'')}" placeholder="https://..."></div>
    <div class="fg"><label>Observações</label>
      <textarea class="fi" id="do-obs" rows="2">${esc(d.obs||'')}</textarea></div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="saveDoEtap(${escolaId},${doId||0})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}
function saveDoEtap(escolaId,doId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  const tipo=document.getElementById('do-tipo').value;
  const data=document.getElementById('do-data').value;
  if(!tipo||!data){showToast('Tipo e data são obrigatórios','error');return;}
  const rec={tipo,data_publicacao:data,numero_do:document.getElementById('do-num').value.trim()||null,
    pagina:document.getElementById('do-pag').value.trim()||null,
    link:document.getElementById('do-link').value.trim()||null,
    obs:document.getElementById('do-obs').value.trim()||null};
  if(doId>0){const idx=etap.publicacoes_do.findIndex(x=>x.id===doId);if(idx>=0)Object.assign(etap.publicacoes_do[idx],rec);}
  else etap.publicacoes_do.push({id:nextId(etap.publicacoes_do),...rec});
  save();closeModal();openEtapDetail(escolaId);showToast('Publicação DO salva!');
}
function deleteDoEtap(escolaId,doId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  if(!confirm('Excluir publicação?'))return;
  etap.publicacoes_do=etap.publicacoes_do.filter(x=>x.id!==doId);
  save();openEtapDetail(escolaId);showToast('Publicação removida','error');
}
function openVincularProcesso(escolaId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  const escola=DB.schools.find(s=>s.id===escolaId);
  const disponiveis=DB.procs.filter(p=>p.escola_id===escolaId||!p.escola_id);
  const html=disponiveis.map(p=>{
    const vinc=etap.processos_vinculados&&etap.processos_vinculados.includes(p.id);
    return`<div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border)">
      <input type="checkbox" ${vinc?'checked':''} id="pv-${p.id}" style="accent-color:var(--acc);width:16px;height:16px">
      <div style="flex:1">
        <div style="font-size:12px;font-weight:500">${esc(p.numero)}</div>
        <div style="font-size:11px;color:var(--muted)">${esc(p.escola||'—')} · ${esc(p.prazo||'—')}</div>
      </div>
      <span class="proc-status ps-${p.status}" style="font-size:10px">${statusLabel(p.status)}</span>
    </div>`;
  }).join('')||'<div style="color:var(--muted);font-size:12px;padding:10px 0">Sem processos disponíveis.</div>';
  showModal('Vincular Processos SEI à ETAP',
    `<div>${html}</div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="salvarVinculosEtap(${escolaId})"><i data-lucide="save" style="width:13px;height:13px"></i>Salvar</button>`
  );
}
function salvarVinculosEtap(escolaId){
  const etap=DB.etaps.find(e=>e.escola_id===escolaId);if(!etap)return;
  const checkboxes=document.querySelectorAll('[id^="pv-"]');
  etap.processos_vinculados=[];
  checkboxes.forEach(cb=>{if(cb.checked)etap.processos_vinculados.push(parseInt(cb.id.replace('pv-','')));});
  save();closeModal();openEtapDetail(escolaId);showToast('Vínculos salvos!');
}

// ── RELATÓRIOS ────────────────────────────────────────────────────────────────
const RELAT_SECOES=[
  {id:'kpis',     label:'Resumo Executivo / KPIs',        icon:'📊'},
  {id:'documentos',label:'Documentos Regulatórios',       icon:'📄'},
  {id:'processos', label:'Processos SEI',                 icon:'📋'},
  {id:'tarefas',   label:'Tarefas e Pendências',          icon:'✅'},
  {id:'financeiro',label:'Situação Financeira',           icon:'💰'},
  {id:'conformidade',label:'Conformidade por Rede',       icon:'📈'},
  {id:'escolas',   label:'Lista de Escolas',              icon:'🏫'},
  {id:'contatos',  label:'Contatos SEEDUC',               icon:'📞'},
];

const relState={escopo:'geral',escola_id:null,formato:'excel',
  secoes:{kpis:true,documentos:true,processos:true,tarefas:false,
          financeiro:true,conformidade:true,escolas:true,contatos:false}};

function renderRelatorios(){
  const escolas=[...DB.schools].sort((a,b)=>a.nome.localeCompare(b.nome));
  const secoesAtivas=RELAT_SECOES.filter(s=>relState.secoes[s.id]);
  const escola=relState.escola_id?DB.schools.find(s=>s.id===relState.escola_id):null;
  const titulo=relState.escopo==='geral'?'Relatório Regulatório — Panorama Geral'
              :escola?`Relatório — ${escola.nome}`:'Selecione uma escola';
  return`
  <div style="display:grid;grid-template-columns:1fr 340px;gap:20px;align-items:start">
    <div>
      <!-- STEP 1 -->
      <div class="card" style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px">1. ESCOPO</div>
        <div style="display:flex;gap:10px;margin-bottom:10px">
          ${[['geral','🏫','Panorama Geral',`Todas as ${DB.schools.length} escolas`],
             ['unidade','🔍','Unidade Específica','Selecionar escola']].map(([v,i,t,d])=>`
            <label style="flex:1;cursor:pointer;display:block">
              <input type="radio" name="rl-escopo" value="${v}" ${relState.escopo===v?'checked':''}
                     onchange="relState.escopo='${v}';reRenderRelat()" style="display:none">
              <div style="padding:14px;border:2px solid ${relState.escopo===v?'var(--acc)':'var(--border)'};
                           border-radius:10px;text-align:center;transition:.15s;cursor:pointer;
                           background:${relState.escopo===v?'#EFF6FF':'white'}">
                <div style="font-size:22px;margin-bottom:4px">${i}</div>
                <div style="font-size:13px;font-weight:700">${t}</div>
                <div style="font-size:11px;color:var(--muted)">${d}</div>
              </div>
            </label>`).join('')}
        </div>
        ${relState.escopo==='unidade'?`
        <div class="fg" style="margin-top:4px">
          <label>Escola</label>
          <select class="fi" id="rl-escola" onchange="relState.escola_id=parseInt(this.value)||null;reRenderRelat()">
            <option value="">Selecione a escola...</option>
            ${escolas.map(s=>`<option value="${s.id}"${relState.escola_id===s.id?' selected':''}>${esc(s.nome)} — ${esc(s.rede)}</option>`).join('')}
          </select>
        </div>`:''}
      </div>
      <!-- STEP 2 -->
      <div class="card" style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px">2. SEÇÕES A INCLUIR</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
          ${RELAT_SECOES.map(s=>`
            <label style="display:flex;align-items:center;gap:10px;padding:10px 12px;cursor:pointer;
                           border:1.5px solid ${relState.secoes[s.id]?'var(--acc)':'var(--border)'};
                           border-radius:8px;transition:.15s;background:${relState.secoes[s.id]?'#EFF6FF':'white'}">
              <input type="checkbox" ${relState.secoes[s.id]?'checked':''}
                     onchange="relState.secoes['${s.id}']=this.checked;reRenderRelat()"
                     style="accent-color:var(--acc);width:15px;height:15px;flex-shrink:0">
              <span style="font-size:13px">${s.icon} ${s.label}</span>
            </label>`).join('')}
        </div>
        <div style="margin-top:10px;display:flex;gap:8px">
          <button class="btn btn-sec btn-sm" onclick="RELAT_SECOES.forEach(s=>relState.secoes[s.id]=true);reRenderRelat()">Marcar todas</button>
          <button class="btn btn-sec btn-sm" onclick="RELAT_SECOES.forEach(s=>relState.secoes[s.id]=false);reRenderRelat()">Desmarcar todas</button>
        </div>
      </div>
      <!-- STEP 3 -->
      <div class="card" style="margin-bottom:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px">3. FORMATO DE SAÍDA</div>
        <div style="display:flex;gap:10px">
          ${[['excel','📊','Excel (.xlsx)','Planilhas com abas por categoria','#217346'],
             ['word','📄','Word (.docx)','Relatório com tabelas e títulos','#2B579A'],
             ['pptx','📊','PowerPoint (.pptx)','Apresentação com slides prontos','#D04423']].map(([f,i,t,d,c])=>`
            <label style="flex:1;cursor:pointer;display:block">
              <input type="radio" name="rl-fmt" value="${f}" ${relState.formato===f?'checked':''}
                     onchange="relState.formato='${f}';reRenderRelat()" style="display:none">
              <div style="padding:14px;border:2px solid ${relState.formato===f?c:'var(--border)'};
                           border-radius:10px;text-align:center;cursor:pointer;transition:.15s;
                           background:${relState.formato===f?c+'11':'white'}">
                <div style="font-size:26px;margin-bottom:6px">${i}</div>
                <div style="font-size:12px;font-weight:700;color:${relState.formato===f?c:'var(--txt)'}">${t}</div>
                <div style="font-size:10px;color:var(--muted);margin-top:2px">${d}</div>
              </div>
            </label>`).join('')}
        </div>
      </div>
      <!-- GERAR -->
      <button class="btn btn-pri" style="width:100%;padding:14px;font-size:15px;border-radius:12px"
              onclick="gerarRelatorio()">
        <i data-lucide="download" style="width:18px;height:18px"></i>
        Gerar ${relState.formato==='excel'?'Planilha Excel':relState.formato==='word'?'Documento Word':'Apresentação PowerPoint'}
      </button>
    </div>

    <!-- Preview -->
    <div>
      <div class="card" style="position:sticky;top:80px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px">PRÉVIA DO CONTEÚDO</div>
        <div style="border:1px solid var(--border);border-radius:8px;overflow:hidden;margin-bottom:14px">
          <div style="background:var(--pri);color:#fff;padding:10px 14px">
            <div style="font-size:13px;font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${titulo}</div>
            <div style="font-size:10px;opacity:.7;margin-top:2px">${fmtDate(todayISO())} · ${secoesAtivas.length} seção(ões)</div>
          </div>
          <div style="padding:8px 14px">
            ${secoesAtivas.length?secoesAtivas.map((s,i)=>`
              <div style="display:flex;align-items:center;gap:8px;padding:5px 0;
                           border-bottom:${i<secoesAtivas.length-1?'1px solid var(--border)':'none'}">
                <span style="font-size:13px">${s.icon}</span>
                <span style="font-size:12px;font-weight:500;flex:1">${s.label}</span>
                <span style="font-size:10px;color:var(--muted)">${getRelatCount(s.id)}</span>
              </div>`).join('')
            :'<div style="color:var(--muted);font-size:12px;padding:8px 0">Nenhuma seção marcada</div>'}
          </div>
        </div>
        <div style="font-size:11px;color:var(--muted);background:var(--sec);border-radius:8px;padding:10px">
          <strong>Formato:</strong>
          ${relState.formato==='excel'?'📊 Excel — cada seção em uma aba separada':
            relState.formato==='word'?'📄 Word — relatório contínuo com tabelas':'📊 PowerPoint — um slide por seção'}
        </div>
      </div>
    </div>
  </div>`;
}

function reRenderRelat(){
  if(cur!=='relatorios')return;
  document.getElementById('main-content').innerHTML=renderRelatorios();
  lucide.createIcons();
}

function getRelatCount(id){
  const isGeral=relState.escopo==='geral';
  const eId=relState.escola_id;
  const eNome=eId?(DB.schools.find(s=>s.id===eId)||{}).nome:null;
  const byE=arr=>isGeral?arr:arr.filter(x=>x.escola_id===eId||x.escola===eNome);
  const map={
    kpis:isGeral?`${DB.schools.length} escolas`:'1 escola',
    documentos:`${byE(DB.docs).length} docs`,
    processos:`${byE(DB.procs).length} proc.`,
    tarefas:`${(isGeral?DB.tarefas:DB.tarefas.filter(t=>t.escola===eNome)).length} tarefas`,
    financeiro:`${(isGeral?DB.financeiro:DB.financeiro.filter(f=>f.escola===eNome)).length} lançamentos`,
    conformidade:`${DB.redes.length} redes`,
    escolas:isGeral?`${DB.schools.length} escolas`:'1 escola',
    contatos:`${DB.contacts.length} contatos`,
  };
  return map[id]||'';
}

// ── Funções de geração ──────────────────────────────────────────────────────
function loadLib(url){
  return new Promise((res,rej)=>{
    const ex=document.querySelector(`script[src="${url}"]`);
    if(ex){if(ex.dataset.loaded)res();else{ex.addEventListener('load',res);ex.addEventListener('error',()=>rej(new Error('Falha: '+url)));}return;}
    const s=document.createElement('script');s.src=url;
    s.onload=()=>{s.dataset.loaded='1';res();};
    s.onerror=()=>rej(new Error('Falha ao carregar: '+url));
    document.head.appendChild(s);
  });
}
function downloadBlob(blob,name){const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),10000);}

function buildRelatData(){
  const isGeral=relState.escopo==='geral';
  const eId=relState.escola_id;
  const escola=eId?DB.schools.find(s=>s.id===eId):null;
  const eNome=escola?escola.nome:null;
  const byE=arr=>isGeral?arr:arr.filter(x=>x.escola_id===eId||x.escola===eNome);
  const docs=byE(DB.docs).map(d=>({...d,_s:statusFromDoc(d)}));
  const procs=byE(DB.procs);
  const tarefas=isGeral?DB.tarefas:DB.tarefas.filter(t=>t.escola===eNome);
  const fin=isGeral?DB.financeiro:DB.financeiro.filter(f=>f.escola===eNome);
  const kpis={
    total_escolas:isGeral?DB.schools.length:1,
    docs_vencidos:docs.filter(d=>d._s==='vencido').length,
    docs_pendentes:docs.filter(d=>d._s==='pendente').length,
    docs_a_vencer:docs.filter(d=>d._s==='a_vencer').length,
    docs_ok:docs.filter(d=>d._s==='ok').length,
    procs_abertos:procs.filter(p=>p.status==='aberto').length,
    procs_cumpridos:procs.filter(p=>p.status==='cumprido').length,
    tarefas_pendentes:tarefas.filter(t=>t.status==='pendente').length,
    total_pago:fin.filter(f=>f.status==='pago').reduce((s,f)=>s+(f.valor||0),0),
    total_pendente:fin.filter(f=>f.status==='pendente').reduce((s,f)=>s+(f.valor||0),0),
    total_vencido:fin.filter(f=>f.status==='vencido').reduce((s,f)=>s+(f.valor||0),0),
  };
  return{docs,procs,tarefas,fin,escola,kpis,isGeral,secoes:relState.secoes,
         titulo:isGeral?'Relatório Regulatório — Panorama Geral':`Relatório Regulatório — ${eNome||''}`};
}

async function gerarRelatorio(){
  if(relState.escopo==='unidade'&&!relState.escola_id){showToast('Selecione uma escola','error');return;}
  if(!RELAT_SECOES.some(s=>relState.secoes[s.id])){showToast('Selecione ao menos uma seção','error');return;}
  const data=buildRelatData();
  showToast(`Gerando ${relState.formato.toUpperCase()}...`,'info');
  try{
    if(relState.formato==='excel')await gerarExcel(data);
    else if(relState.formato==='word')await gerarWord(data);
    else await gerarPPTX(data);
    showToast('Arquivo gerado e baixado!');
  }catch(e){console.error(e);showToast('Erro: '+(e.message||String(e)),'error');}
}

// ── EXCEL ─────────────────────────────────────────────────────────────────────
async function gerarExcel(data){
  await loadLib('https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js');
  const wb=XLSX.utils.book_new();
  const aoa=(...rows)=>XLSX.utils.aoa_to_sheet(rows);

  // KPIs
  if(data.secoes.kpis){
    const ws=XLSX.utils.aoa_to_sheet([
      [data.titulo],['Gerado em:', fmtDate(todayISO())],[],
      ['INDICADOR','VALOR'],
      ['Total de Escolas',data.kpis.total_escolas],
      ['Documentos Vencidos',data.kpis.docs_vencidos],
      ['Documentos Pendentes',data.kpis.docs_pendentes],
      ['Documentos a Vencer (60d)',data.kpis.docs_a_vencer],
      ['Documentos OK',data.kpis.docs_ok],
      ['Processos SEI Abertos',data.kpis.procs_abertos],
      ['Processos SEI Cumpridos',data.kpis.procs_cumpridos],
      ['Total Pago (R$)',data.kpis.total_pago],
      ['Total Pendente (R$)',data.kpis.total_pendente],
      ['Total Vencido (R$)',data.kpis.total_vencido],
    ]);
    XLSX.utils.book_append_sheet(wb,ws,'KPIs');
  }

  // Documentos
  if(data.secoes.documentos&&data.docs.length){
    const ws=XLSX.utils.aoa_to_sheet([
      ['Escola','Rede','Estado','Tipo de Documento','Status','Vencimento','Observações'],
      ...data.docs.map(d=>[d.escola,d.rede,d.estado,d.tipo,
        statusLabel(d._s).replace(/[✅⚠️🔴❌❓]/g,'').trim(),
        fmtDate(d.data_vencimento),d.observacoes||''])
    ]);
    XLSX.utils.book_append_sheet(wb,ws,'Documentos');
  }

  // Processos
  if(data.secoes.processos&&data.procs.length){
    const ws=XLSX.utils.aoa_to_sheet([
      ['Número','Escola','Rede','Exigência','Recebimento','Prazo','Status','Responsável','Observações'],
      ...data.procs.map(p=>[p.numero,p.escola,p.rede,p.forma_exigencia,
        p.data_recebimento,p.prazo,
        statusLabel(p.status).replace(/[✅🔴🟡⚫]/g,'').trim(),
        p.responsavel||'',p.observacoes||''])
    ]);
    XLSX.utils.book_append_sheet(wb,ws,'Processos SEI');
  }

  // Tarefas
  if(data.secoes.tarefas&&data.tarefas.length){
    const ws=XLSX.utils.aoa_to_sheet([
      ['Título','Responsável','Escola','Categoria','Prioridade','Prazo','Status','Descrição'],
      ...data.tarefas.map(t=>[t.titulo,t.responsavel,t.escola,t.categoria,t.prioridade,
        fmtDate(t.prazo),(TAREFA_STATUS[t.status]||t.status).replace(/[⏳🔵✅✖]/g,'').trim(),t.descricao||''])
    ]);
    XLSX.utils.book_append_sheet(wb,ws,'Tarefas');
  }

  // Financeiro
  if(data.secoes.financeiro&&data.fin.length){
    const ws=XLSX.utils.aoa_to_sheet([
      ['Descrição','Categoria','Escola','Rede','Órgão/Fornecedor','Valor (R$)','Vencimento','Pagamento','Status','Responsável','Observações'],
      ...data.fin.map(f=>[f.descricao,f.categoria,f.escola,f.rede,f.orgao,
        f.valor,(f.valor||0).toFixed(2),fmtDate(f.data_vencimento),fmtDate(f.data_pagamento),
        finStatusLabel(f.status).replace(/[✅⏳🔴✖]/g,'').trim(),f.responsavel||'',f.observacoes||''])
    ]);
    XLSX.utils.book_append_sheet(wb,ws,'Financeiro');
  }

  // Conformidade por Rede
  if(data.secoes.conformidade){
    const byR={};
    DB.schools.forEach(s=>{
      if(!byR[s.rede])byR[s.rede]={escolas:0,criticos:0,a_vencer:0,ok:0};
      byR[s.rede].escolas++;byR[s.rede].criticos+=(s.criticos||0);
      byR[s.rede].a_vencer+=(s.a_vencer||0);byR[s.rede].ok+=(s.ok_docs||0);
    });
    const ws=XLSX.utils.aoa_to_sheet([
      ['Rede','Escolas','Docs Críticos','A Vencer','OK'],
      ...Object.entries(byR).sort((a,b)=>b[1].criticos-a[1].criticos)
        .map(([r,v])=>[r,v.escolas,v.criticos,v.a_vencer,v.ok])
    ]);
    XLSX.utils.book_append_sheet(wb,ws,'Conformidade por Rede');
  }

  // Escolas
  if(data.secoes.escolas){
    const schools=data.isGeral?DB.schools:[data.escola].filter(Boolean);
    const ws=XLSX.utils.aoa_to_sheet([
      ['Nome','Rede','Estado','CNPJ','Insc. Municipal','INEP/Censo','Status Unidade','Docs OK','A Vencer','Críticos','Total Docs'],
      ...schools.map(s=>[s.nome,s.rede,s.estado,s.cnpj||'',s.inscricao_municipal||'',s.codigo_censo||'',
        (STATUS_UNIDADE[s.status_unidade||'em_funcionamento']||{}).label||'',
        s.ok_docs,s.a_vencer,s.criticos,s.total_docs])
    ]);
    XLSX.utils.book_append_sheet(wb,ws,'Escolas');
  }

  // Contatos SEEDUC
  if(data.secoes.contatos&&DB.contacts.length){
    const ws=XLSX.utils.aoa_to_sheet([
      ['Nome','Cargo','Regional','Escola Vinculada','Telefone','E-mail','Observações'],
      ...DB.contacts.map(c=>[c.nome,c.cargo,c.regional,c.escola_vinculada,c.telefone,c.email,c.observacoes||''])
    ]);
    XLSX.utils.book_append_sheet(wb,ws,'Contatos SEEDUC');
  }

  const slug=data.isGeral?'panorama_geral':(data.escola?data.escola.nome.replace(/[^a-zA-Z0-9]/g,'_').slice(0,30):'escola');
  XLSX.writeFile(wb,`relatorio_${slug}_${todayISO()}.xlsx`);
}

// ── WORD ──────────────────────────────────────────────────────────────────────
async function gerarWord(data){
  await loadLib('https://cdn.jsdelivr.net/npm/docx@8.5.0/build/index.umd.min.js');
  const {Document,Paragraph,TextRun,Table,TableRow,TableCell,
         HeadingLevel,AlignmentType,WidthType,ShadingType,Packer}=docx;
  const PRI='1B3A6B',ACC='2D6BE4';

  const h1=(t)=>new Paragraph({
    children:[new TextRun({text:t,bold:true,size:36,color:PRI})],
    heading:HeadingLevel.HEADING_1,spacing:{before:400,after:160}});
  const h2=(t)=>new Paragraph({
    children:[new TextRun({text:t,bold:true,size:26,color:ACC})],
    heading:HeadingLevel.HEADING_2,spacing:{before:280,after:120}});
  const p=(t,opts={})=>new Paragraph({
    children:[new TextRun({text:t||'—',size:20,...opts})]});
  const mkTable=(headers,rows)=>new Table({
    width:{size:100,type:WidthType.PERCENTAGE},
    rows:[
      new TableRow({children:headers.map(h=>new TableCell({
        shading:{fill:PRI,type:ShadingType.SOLID,color:'auto'},
        children:[new Paragraph({children:[new TextRun({text:h,bold:true,color:'FFFFFF',size:18})],alignment:AlignmentType.CENTER})]}))}),
      ...rows.map((row,ri)=>new TableRow({children:row.map(cell=>new TableCell({
        shading:ri%2===0?undefined:{fill:'F0F4FA',type:ShadingType.SOLID,color:'auto'},
        children:[new Paragraph({children:[new TextRun({text:String(cell==null?'—':cell),size:18})]})]}))}))]});

  const ch=[];
  // Capa
  ch.push(new Paragraph({children:[new TextRun({text:data.titulo,bold:true,size:52,color:PRI})],alignment:AlignmentType.CENTER,spacing:{before:1800,after:400}}));
  ch.push(new Paragraph({children:[new TextRun({text:'Gerado em '+fmtDate(todayISO()),size:22,color:'666666'})],alignment:AlignmentType.CENTER,spacing:{after:200}}));
  ch.push(new Paragraph({children:[new TextRun({text:'RegularEduc — Plataforma de Gestão Regulatória',size:20,color:'999999'})],alignment:AlignmentType.CENTER,spacing:{after:1000}}));

  // KPIs
  if(data.secoes.kpis){
    ch.push(h1('Resumo Executivo'));
    ch.push(mkTable(['Indicador','Valor'],[
      ['Total de Escolas',String(data.kpis.total_escolas)],
      ['Documentos Vencidos',String(data.kpis.docs_vencidos)],
      ['Documentos Pendentes',String(data.kpis.docs_pendentes)],
      ['Docs a Vencer (60d)',String(data.kpis.docs_a_vencer)],
      ['Documentos OK',String(data.kpis.docs_ok)],
      ['Processos SEI Abertos',String(data.kpis.procs_abertos)],
      ['Total Pago',fmtCurrency(data.kpis.total_pago)],
      ['Total Pendente',fmtCurrency(data.kpis.total_pendente)],
      ['Total Vencido',fmtCurrency(data.kpis.total_vencido)],
    ]));
  }

  // Documentos
  if(data.secoes.documentos&&data.docs.length){
    ch.push(h1('Documentos Regulatórios'));
    ch.push(mkTable(['Escola','Rede','Tipo','Status','Vencimento'],
      data.docs.map(d=>[d.escola,d.rede,d.tipo,
        statusLabel(d._s).replace(/[✅⚠️🔴❌❓]/g,'').trim(),fmtDate(d.data_vencimento)])));
  }

  // Processos
  if(data.secoes.processos&&data.procs.length){
    ch.push(h1('Processos SEI'));
    ch.push(mkTable(['Número','Escola','Exigência','Prazo','Status','Responsável'],
      data.procs.map(p=>[p.numero,p.escola,p.forma_exigencia,p.prazo,
        statusLabel(p.status).replace(/[✅🔴🟡⚫]/g,'').trim(),p.responsavel||'—'])));
  }

  // Financeiro
  if(data.secoes.financeiro&&data.fin.length){
    ch.push(h1('Situação Financeira'));
    ch.push(mkTable(['Descrição','Escola','Órgão','Valor','Vencimento','Status'],
      data.fin.map(f=>[f.descricao,f.escola,f.orgao,fmtCurrency(f.valor),
        fmtDate(f.data_vencimento),finStatusLabel(f.status).replace(/[✅⏳🔴✖]/g,'').trim()])));
  }

  // Tarefas
  if(data.secoes.tarefas&&data.tarefas.length){
    ch.push(h1('Tarefas e Pendências'));
    ch.push(mkTable(['Tarefa','Responsável','Escola','Prioridade','Prazo','Status'],
      data.tarefas.map(t=>[t.titulo,t.responsavel||'—',t.escola,t.prioridade,fmtDate(t.prazo),
        (TAREFA_STATUS[t.status]||t.status).replace(/[⏳🔵✅✖]/g,'').trim()])));
  }

  // Conformidade por Rede
  if(data.secoes.conformidade&&data.isGeral){
    ch.push(h1('Conformidade por Rede'));
    const byR={};
    DB.schools.forEach(s=>{if(!byR[s.rede])byR[s.rede]={escolas:0,criticos:0,a_vencer:0,ok:0};
      byR[s.rede].escolas++;byR[s.rede].criticos+=(s.criticos||0);byR[s.rede].a_vencer+=(s.a_vencer||0);byR[s.rede].ok+=(s.ok_docs||0);});
    ch.push(mkTable(['Rede','Escolas','Críticos','A Vencer','OK'],
      Object.entries(byR).sort((a,b)=>b[1].criticos-a[1].criticos)
        .map(([r,v])=>[r,String(v.escolas),String(v.criticos),String(v.a_vencer),String(v.ok)])));
  }

  // Escolas
  if(data.secoes.escolas){
    ch.push(h1('Escolas'));
    const schools=data.isGeral?DB.schools:[data.escola].filter(Boolean);
    ch.push(mkTable(['Nome','Rede','Estado','INEP/Censo','Status Unidade','Docs Críticos'],
      schools.map(s=>[s.nome,s.rede,s.estado,s.codigo_censo||'—',
        (STATUS_UNIDADE[s.status_unidade||'em_funcionamento']||{}).label||'',String(s.criticos||0)])));
  }

  // Contatos
  if(data.secoes.contatos&&DB.contacts.length){
    ch.push(h1('Contatos SEEDUC'));
    ch.push(mkTable(['Nome','Cargo','Regional','Escola','Telefone','E-mail'],
      DB.contacts.map(c=>[c.nome,c.cargo,c.regional,c.escola_vinculada,c.telefone||'—',c.email||'—'])));
  }

  const doc=new Document({sections:[{properties:{},children:ch}]});
  const blob=await Packer.toBlob(doc);
  const slug=data.isGeral?'panorama_geral':(data.escola?data.escola.nome.replace(/[^a-zA-Z0-9]/g,'_').slice(0,30):'escola');
  downloadBlob(blob,`relatorio_${slug}_${todayISO()}.docx`);
}

// ── POWERPOINT ────────────────────────────────────────────────────────────────
async function gerarPPTX(data){
  await loadLib('https://cdn.jsdelivr.net/npm/pptxgenjs@3.12.0/dist/pptxgen.bundle.js');
  const pptx=new PptxGenJS();
  pptx.layout='LAYOUT_WIDE';
  const PRI='1B3A6B',ACC='2D6BE4',W='FFFFFF',RED='EF4444',YLW='F59E0B',GRN='22C55E',LGRAY='F0F4FA';
  const addTitle=(sl,t)=>{sl.addText(t,{x:.4,y:.25,w:'92%',h:.7,fontSize:22,bold:true,color:PRI});
    sl.addShape(pptx.ShapeType.line,{x:.4,y:.85,w:'92%',h:0,line:{color:ACC,width:2}});};
  const addTable=(sl,hdrs,rows,y=1.0)=>{
    if(!rows.length)return;
    const tableData=[
      hdrs.map(h=>({text:h,options:{bold:true,color:W,fill:PRI,fontSize:9}})),
      ...rows.map((row,ri)=>row.map(cell=>({
        text:String(cell==null?'—':cell).slice(0,35),
        options:{fill:ri%2===0?W:LGRAY,fontSize:8,valign:'middle'}})))
    ];
    sl.addTable(tableData,{x:.4,y,w:'92%',rowH:.3,border:{type:'solid',pt:.5,color:'DDDDDD'}});
  };
  const kpiBox=(sl,val,label,color,x)=>{
    sl.addShape(pptx.ShapeType.roundRect,{x,y:1.1,w:2.9,h:1.7,fill:{color:'F8FAFF'},line:{color,width:2}});
    sl.addText(String(val),{x,y:1.2,w:2.9,h:.9,fontSize:26,bold:true,color,align:'center'});
    sl.addText(label,{x,y:2.05,w:2.9,h:.55,fontSize:11,color:'666666',align:'center'});
  };

  // Slide 1: Capa
  let sl=pptx.addSlide();
  sl.background={color:PRI};
  sl.addText(data.titulo,{x:.5,y:1.6,w:'90%',h:1.4,fontSize:32,bold:true,color:W,align:'center'});
  sl.addText('Gerado em '+fmtDate(todayISO()),{x:.5,y:3.2,w:'90%',h:.5,fontSize:14,color:'AABBDD',align:'center'});
  sl.addText('RegularEduc · Plataforma de Gestão Regulatória',{x:.5,y:3.9,w:'90%',h:.4,fontSize:11,color:'8899BB',align:'center'});

  // Slide 2: KPIs
  if(data.secoes.kpis){
    sl=pptx.addSlide();addTitle(sl,'Resumo Executivo');
    kpiBox(sl,data.kpis.total_escolas,'Escolas',ACC,.4);
    kpiBox(sl,data.kpis.docs_vencidos+data.kpis.docs_pendentes,'Docs Críticos',RED,3.5);
    kpiBox(sl,data.kpis.procs_abertos,'Processos Abertos',YLW,6.6);
    kpiBox(sl,fmtCurrency(data.kpis.total_pendente),'Valor Pendente',YLW,9.7);
    if(data.kpis.docs_ok||data.kpis.docs_vencidos){
      const total=data.kpis.docs_ok+data.kpis.docs_vencidos+data.kpis.docs_pendentes+data.kpis.docs_a_vencer||1;
      [[data.kpis.docs_vencidos+data.kpis.docs_pendentes,'Críticos',RED],
       [data.kpis.docs_a_vencer,'A vencer',YLW],[data.kpis.docs_ok,'OK',GRN]].forEach(([n,l,c],i)=>{
        const y=3.1+i*.55;const w=n/total*9;
        sl.addText(l,{x:.4,y,w:1.6,h:.45,fontSize:12,color:'333333'});
        if(w>0)sl.addShape(pptx.ShapeType.rect,{x:2.2,y:y+.08,w,h:.3,fill:{color:c}});
        sl.addText(String(n),{x:2.2+w+.1,y,w:1,h:.45,fontSize:12,bold:true,color:c});
      });
    }
  }

  // Slide 3: Documentos
  if(data.secoes.documentos&&data.docs.length){
    sl=pptx.addSlide();addTitle(sl,'Documentos Regulatórios');
    addTable(sl,['Escola','Rede','Tipo','Status','Vencimento'],
      data.docs.slice(0,12).map(d=>[d.escola?.slice(0,22),d.rede,d.tipo?.slice(0,28),
        statusLabel(d._s).replace(/[✅⚠️🔴❌❓]/g,'').trim(),fmtDate(d.data_vencimento)]));
  }

  // Slide 4: Processos
  if(data.secoes.processos&&data.procs.length){
    sl=pptx.addSlide();addTitle(sl,'Processos SEI');
    addTable(sl,['Número','Escola','Exigência','Prazo','Status','Responsável'],
      data.procs.slice(0,10).map(p=>[p.numero?.slice(0,22),(p.escola||'—').slice(0,18),
        (p.forma_exigencia||'—').slice(0,22),(p.prazo||'—').slice(0,20),
        statusLabel(p.status).replace(/[✅🔴🟡⚫]/g,'').trim(),p.responsavel||'—']));
  }

  // Slide 5: Financeiro
  if(data.secoes.financeiro&&data.fin.length){
    sl=pptx.addSlide();addTitle(sl,'Situação Financeira');
    kpiBox(sl,fmtCurrency(data.kpis.total_pago),'Total Pago',GRN,.4);
    kpiBox(sl,fmtCurrency(data.kpis.total_pendente),'Pendente',YLW,4.8);
    kpiBox(sl,fmtCurrency(data.kpis.total_vencido),'Vencido',RED,9.2);
    addTable(sl,['Descrição','Escola','Valor','Vencimento','Status'],
      data.fin.slice(0,8).map(f=>[(f.descricao||'—').slice(0,25),(f.escola||'—').slice(0,20),
        fmtCurrency(f.valor||0),fmtDate(f.data_vencimento),
        finStatusLabel(f.status).replace(/[✅⏳🔴✖]/g,'').trim()]),3.0);
  }

  // Slide 6: Conformidade
  if(data.secoes.conformidade&&data.isGeral){
    sl=pptx.addSlide();addTitle(sl,'Conformidade por Rede');
    const byR={};
    DB.schools.forEach(s=>{if(!byR[s.rede])byR[s.rede]={escolas:0,criticos:0,a_vencer:0,ok:0};
      byR[s.rede].escolas++;byR[s.rede].criticos+=(s.criticos||0);byR[s.rede].a_vencer+=(s.a_vencer||0);byR[s.rede].ok+=(s.ok_docs||0);});
    addTable(sl,['Rede','Escolas','Críticos','A Vencer','OK'],
      Object.entries(byR).sort((a,b)=>b[1].criticos-a[1].criticos)
        .map(([r,v])=>[r,String(v.escolas),String(v.criticos),String(v.a_vencer),String(v.ok)]));
  }

  // Slide 7: Tarefas
  if(data.secoes.tarefas&&data.tarefas.length){
    sl=pptx.addSlide();addTitle(sl,'Tarefas e Pendências');
    addTable(sl,['Tarefa','Responsável','Escola','Prioridade','Prazo','Status'],
      data.tarefas.slice(0,10).map(t=>[(t.titulo||'—').slice(0,25),t.responsavel||'—',
        (t.escola||'—').slice(0,18),t.prioridade,fmtDate(t.prazo),
        (TAREFA_STATUS[t.status]||t.status).replace(/[⏳🔵✅✖]/g,'').trim()]));
  }

  // Slide 8: Escolas
  if(data.secoes.escolas){
    sl=pptx.addSlide();addTitle(sl,'Escolas Cadastradas');
    const schools=data.isGeral?DB.schools:[data.escola].filter(Boolean);
    addTable(sl,['Nome','Rede','Estado','INEP/Censo','Status','Críticos'],
      schools.slice(0,12).map(s=>[s.nome?.slice(0,22),s.rede,s.estado,s.codigo_censo||'—',
        (STATUS_UNIDADE[s.status_unidade||'em_funcionamento']||{}).label?.slice(0,18)||'',String(s.criticos||0)]));
  }

  const slug=data.isGeral?'panorama_geral':(data.escola?data.escola.nome.replace(/[^a-zA-Z0-9]/g,'_').slice(0,30):'escola');
  await pptx.writeFile({fileName:`relatorio_${slug}_${todayISO()}.pptx`});
}

// ── CALENDÁRIO ────────────────────────────────────────────────────────────────
const CAL_MONTHS=['Janeiro','Fevereiro','Março','Abril','Maio','Junho',
                  'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'];
const CAL_DAYS=['Dom','Seg','Ter','Qua','Qui','Sex','Sáb'];

function extractDateFromText(text){
  if(!text)return null;
  const m1=text.match(/(\d{2})\/(\d{2})\/(\d{4})/);
  if(m1)return`${m1[3]}-${m1[2]}-${m1[1]}`;
  const m3=text.match(/(\d{4})-(\d{2})-(\d{2})/);
  if(m3)return`${m3[1]}-${m3[2]}-${m3[3]}`;
  const m2=text.match(/(\d{2})\/(\d{2})\b/);
  if(m2){const y=new Date().getFullYear();return`${y}-${m2[2]}-${m2[1]}`;}
  return null;
}

function buildCalendarEvents(){
  const ev=[];
  // Documentos
  DB.docs.forEach(d=>{
    if(!d.data_vencimento)return;
    const st=statusFromDoc(d);
    const color={ok:'#22C55E',a_vencer:'#F59E0B',vencido:'#EF4444',pendente:'#EF4444',desconhecido:'#94a3b8'}[st]||'#94a3b8';
    ev.push({date:d.data_vencimento,title:d.tipo,escola:d.escola,rede:d.rede||'',
             type:'doc',status:st,color,id:d.id,icon:'📄',
             detail:`${d.tipo} — ${d.escola}`,nav:'docs'});
  });
  // Processos SEI
  DB.procs.forEach(p=>{
    const date=extractDateFromText(p.prazo);
    if(!date)return;
    const color={aberto:'#EF4444',aguardando:'#F59E0B',cumprido:'#22C55E',arquivado:'#94a3b8'}[p.status]||'#3B82F6';
    ev.push({date,title:p.numero,escola:p.escola||'—',rede:p.rede||'',
             type:'proc',status:p.status,color,id:p.id,icon:'📋',
             detail:`${p.numero} — ${p.escola||'—'}`,nav:'processos'});
  });
  // Tarefas
  DB.tarefas.forEach(t=>{
    if(!t.prazo||t.status==='concluida'||t.status==='cancelada')return;
    const color={alta:'#EF4444',media:'#F59E0B',baixa:'#22C55E'}[t.prioridade||'media'];
    ev.push({date:t.prazo,title:t.titulo,escola:t.escola||'—',rede:'',
             type:'tarefa',status:t.status,color,id:t.id,icon:'✅',
             detail:`${t.titulo} — Resp: ${t.responsavel||'—'}`,nav:'tarefas'});
  });
  // Financeiro
  DB.financeiro.forEach(f=>{
    if(f.status==='pago'||f.status==='cancelado')return;
    if(f.data_vencimento){
      const color=f.status==='vencido'?'#EF4444':'#F59E0B';
      ev.push({date:f.data_vencimento,title:f.descricao,escola:f.escola||'—',rede:f.rede||'',
               type:'fin',status:f.status,color,id:f.id,icon:'💰',
               detail:`${f.descricao} — ${fmtCurrency(f.valor)}`,nav:'financeiro'});
    }
  });
  return ev.sort((a,b)=>a.date.localeCompare(b.date));
}

function renderCalendario(){
  const year=state.calYear,month=state.calMonth;
  const curYear=new Date().getFullYear(),maxYear=curYear+5;
  const allEvents=buildCalendarEvents();
  const todayStr=todayISO();
  const monthPrefix=`${year}-${String(month+1).padStart(2,'0')}`;

  // Group by day for this month
  const byDay={};
  allEvents.filter(e=>e.date.startsWith(monthPrefix)).forEach(e=>{
    const d=parseInt(e.date.slice(8,10));
    if(!byDay[d])byDay[d]=[];byDay[d].push(e);
  });

  const firstDow=new Date(year,month,1).getDay();
  const daysInMonth=new Date(year,month+1,0).getDate();

  // Day name row
  const dayNames=CAL_DAYS.map(d=>`<div class="cal-dname">${d}</div>`).join('');

  // Empty cells + day cells
  let cells='';
  for(let i=0;i<firstDow;i++)cells+='<div class="cal-cell cal-empty"></div>';
  for(let d=1;d<=daysInMonth;d++){
    const dateStr=`${monthPrefix}-${String(d).padStart(2,'0')}`;
    const isToday=dateStr===todayStr;
    const isPast=dateStr<todayStr&&!isToday;
    const dayEvts=byDay[d]||[];
    const shown=dayEvts.slice(0,3);
    const more=dayEvts.length-3;
    const evHtml=shown.map(e=>`<div class="cal-ev" style="background:${e.color}" title="${esc(e.detail)}">${e.icon} ${esc(e.title.length>20?e.title.slice(0,19)+'…':e.title)}</div>`).join('');
    cells+=`<div class="cal-cell${isToday?' cal-today':''}${isPast?' cal-past':''}" onclick="showDayEvents('${dateStr}')">
      <div class="cal-day-num${isToday?' cal-today-num':''}">${d}</div>
      ${evHtml}${more>0?`<div class="cal-more">+${more} mais</div>`:''}
    </div>`;
  }

  // Upcoming events (global, sorted, from today)
  const upcoming=allEvents.filter(e=>e.date>=todayStr).slice(0,30);
  const upcomingHtml=upcoming.length?upcoming.map(e=>{
    const days=daysUntil(e.date);
    const dt=days===0?'Hoje':days===1?'Amanhã':`em ${days}d`;
    return`<div style="display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid var(--border);cursor:pointer"
                onclick="closeModal();go('${e.nav}')">
      <div style="width:34px;height:34px;border-radius:8px;background:${e.color}22;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0">${e.icon}</div>
      <div style="flex:1;min-width:0">
        <div style="font-size:12px;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(e.title)}</div>
        <div style="font-size:11px;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(e.escola)}</div>
        <div style="font-size:10px;font-weight:700;color:${e.color};margin-top:2px">${fmtDate(e.date)} · ${dt}</div>
      </div>
    </div>`;
  }).join(''):`<div style="padding:24px 0;text-align:center;color:var(--muted);font-size:12px">
    Nenhum vencimento futuro cadastrado.<br>Adicione documentos ou processos com datas.</div>`;

  // Stats for this month
  const mc={doc:0,proc:0,tarefa:0,fin:0};
  allEvents.filter(e=>e.date.startsWith(monthPrefix)).forEach(e=>mc[e.type]=(mc[e.type]||0)+1);

  // Year tabs
  const yearTabs=Array.from({length:6},(_,i)=>curYear+i).map(y=>`
    <button class="btn btn-sm ${y===year?'btn-pri':'btn-sec'}" style="min-width:52px"
            onclick="state.calYear=${y};if(${y}===${curYear})state.calMonth=Math.max(state.calMonth,${new Date().getMonth()});render()">${y}</button>`
  ).join('');

  const canPrev=!(year===curYear&&month===new Date().getMonth());
  const canNext=!(year===maxYear&&month===11);

  return`
  <!-- Year nav -->
  <div style="display:flex;gap:6px;align-items:center;margin-bottom:16px;flex-wrap:wrap">
    ${yearTabs}
    <div style="margin-left:auto;display:flex;gap:12px;font-size:12px;color:var(--muted);align-items:center;flex-wrap:wrap">
      <span>📄 ${mc.doc} docs</span><span>📋 ${mc.proc} proc.</span>
      <span>✅ ${mc.tarefa} tarefas</span><span>💰 ${mc.fin} fin.</span>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 300px;gap:16px;align-items:start">
    <!-- Calendar -->
    <div class="card" style="padding:0;overflow:hidden">
      <div style="display:flex;align-items:center;justify-content:space-between;padding:14px 18px;
                  border-bottom:1px solid var(--border);background:var(--pri)">
        <button class="btn btn-sm" style="background:rgba(255,255,255,.2);color:#fff;border:none"
                onclick="calPrev()" ${!canPrev?'disabled style="opacity:.35;cursor:not-allowed"':''}>
          <i data-lucide="chevron-left" style="width:14px;height:14px"></i></button>
        <div style="font-size:17px;font-weight:800;color:#fff">${CAL_MONTHS[month]} ${year}</div>
        <button class="btn btn-sm" style="background:rgba(255,255,255,.2);color:#fff;border:none"
                onclick="calNext()" ${!canNext?'disabled style="opacity:.35;cursor:not-allowed"':''}>
          <i data-lucide="chevron-right" style="width:14px;height:14px"></i></button>
      </div>
      <div class="cal-week-header">${dayNames}</div>
      <div class="cal-grid">${cells}</div>
    </div>

    <!-- Side panel -->
    <div style="display:flex;flex-direction:column;gap:14px">
      <div class="card" style="padding:0;overflow:hidden">
        <div style="padding:12px 16px;border-bottom:1px solid var(--border);
                    display:flex;align-items:center;justify-content:space-between">
          <span style="font-size:13px;font-weight:700">📅 Próximos Vencimentos</span>
          <span style="font-size:11px;color:var(--muted)">${upcoming.length} eventos</span>
        </div>
        <div style="padding:0 16px;max-height:440px;overflow-y:auto">${upcomingHtml}</div>
      </div>
      <div class="card" style="padding:14px">
        <div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px">Legenda</div>
        ${[['📄','Documentos','data_vencimento'],['📋','Processos SEI','prazo declarado'],
           ['✅','Tarefas','data limite'],['💰','Financeiro','vencimento']].map(([i,t,s])=>`
          <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
            <span style="font-size:15px">${i}</span>
            <div><div style="font-size:12px;font-weight:600">${t}</div>
                 <div style="font-size:10px;color:var(--muted)">${s}</div></div>
          </div>`).join('')}
        <div class="divider"></div>
        ${[['#22C55E','OK / Em dia'],['#F59E0B','Atenção / Próximo'],['#EF4444','Vencido / Urgente'],['#3B82F6','Em andamento'],['#94a3b8','Desconhecido']].map(([c,l])=>`
          <div style="display:flex;align-items:center;gap:5px;margin-bottom:5px">
            <div style="width:10px;height:10px;border-radius:2px;background:${c};flex-shrink:0"></div>
            <span style="font-size:11px">${l}</span></div>`).join('')}
      </div>
    </div>
  </div>`;
}

function calPrev(){
  const curYear=new Date().getFullYear(),curMonth=new Date().getMonth();
  if(state.calMonth===0){
    if(state.calYear<=curYear)return;
    state.calYear--;state.calMonth=11;
  }else{
    if(state.calYear===curYear&&state.calMonth-1<curMonth)return;
    state.calMonth--;
  }
  render();
}
function calNext(){
  const maxYear=new Date().getFullYear()+5;
  if(state.calMonth===11){if(state.calYear>=maxYear)return;state.calYear++;state.calMonth=0;}
  else state.calMonth++;
  render();
}

function showDayEvents(dateStr){
  const events=buildCalendarEvents().filter(e=>e.date===dateStr);
  const [y,m,d]=dateStr.split('-');
  const label=`${d}/${m}/${y}`;
  if(!events.length){showToast(`Sem eventos em ${label}`,'info');return;}
  const typeLabels={doc:'Documento',proc:'Processo SEI',tarefa:'Tarefa',fin:'Financeiro'};
  const html=events.map(e=>`
    <div style="display:flex;align-items:flex-start;gap:12px;padding:13px 0;border-bottom:1px solid var(--border);cursor:pointer"
         onclick="closeModal();go('${e.nav}')">
      <div style="width:42px;height:42px;border-radius:10px;background:${e.color}22;display:flex;
                  align-items:center;justify-content:center;font-size:22px;flex-shrink:0">${e.icon}</div>
      <div style="flex:1">
        <div style="font-size:10px;font-weight:700;text-transform:uppercase;color:var(--muted);margin-bottom:3px">
          ${typeLabels[e.type]||e.type}
          <span style="width:8px;height:8px;border-radius:50%;background:${e.color};display:inline-block;margin-left:4px;vertical-align:middle"></span>
        </div>
        <div style="font-size:14px;font-weight:700">${esc(e.title)}</div>
        <div style="font-size:12px;color:var(--muted);margin-top:3px">${esc(e.escola)}</div>
        ${e.rede?`<span class="tag rede" style="margin-top:5px;display:inline-block">${esc(e.rede)}</span>`:''}
        <div style="font-size:11px;color:var(--acc);margin-top:4px;font-style:italic">Clique para abrir →</div>
      </div>
    </div>`).join('');
  showModal(`📅 ${label} — ${events.length} evento(s)`,html,
    `<button class="btn btn-sec" onclick="closeModal()">Fechar</button>`,'modal-lg');
}

// ── INDEXEDDB — ARQUIVOS ─────────────────────────────────────────────────────
const ARQ_CATS=['Autorização Sec. Educação','Alvará de Funcionamento','Licença Sanitária',
  'AVCB / Bombeiros','ETAP','PAA','Regimento Interno','PPP','Certidão Negativa',
  'Contrato','Laudo Técnico','Comprovante de Pagamento','Processo SEI','Outro'];

const FILE_ICONS={'application/pdf':'📄','image/jpeg':'🖼️','image/png':'🖼️','image/gif':'🖼️',
  'image/webp':'🖼️','application/msword':'📝','application/vnd.openxmlformats-officedocument.wordprocessingml.document':'📝',
  'application/vnd.ms-excel':'📊','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':'📊',
  'text/plain':'📃','application/zip':'🗜️'};

let _fileDB=null;
let _selectedFile=null;

function openFileDB(){
  return new Promise((res,rej)=>{
    if(_fileDB){res(_fileDB);return;}
    const r=indexedDB.open('regulareduc_files',1);
    r.onupgradeneeded=e=>{const db=e.target.result;if(!db.objectStoreNames.contains('files'))db.createObjectStore('files',{keyPath:'id'});};
    r.onsuccess=e=>{_fileDB=e.target.result;res(_fileDB);};
    r.onerror=e=>rej(e.target.error);
  });
}
async function storeFileContent(id,dataURL){
  const db=await openFileDB();
  return new Promise((res,rej)=>{const tx=db.transaction('files','readwrite');tx.objectStore('files').put({id,dataURL});tx.oncomplete=res;tx.onerror=e=>rej(e.target.error);});
}
async function loadFileContent(id){
  const db=await openFileDB();
  return new Promise((res,rej)=>{const tx=db.transaction('files','readonly');const r=tx.objectStore('files').get(id);r.onsuccess=e=>res(e.target.result?e.target.result.dataURL:null);r.onerror=e=>rej(e.target.error);});
}
async function removeFileContent(id){
  const db=await openFileDB();
  return new Promise((res,rej)=>{const tx=db.transaction('files','readwrite');tx.objectStore('files').delete(id);tx.oncomplete=res;tx.onerror=e=>rej(e.target.error);});
}

function fmtSize(bytes){
  if(!bytes)return'—';
  if(bytes<1024)return bytes+'B';
  if(bytes<1048576)return(bytes/1024).toFixed(0)+'KB';
  return(bytes/1048576).toFixed(1)+'MB';
}

function renderArquivosEscola(escolaId){
  const arqs=(DB.arquivos||[]).filter(a=>a.escola_id===escolaId)
    .sort((a,b)=>(b.data_upload||'').localeCompare(a.data_upload||''));
  if(!arqs.length)return`<div style="text-align:center;padding:20px;color:var(--muted);font-size:12px">
    <div style="font-size:28px;margin-bottom:6px">📂</div>
    Nenhum arquivo importado ainda. Clique em "+ Importar Arquivo" para adicionar.
  </div>`;
  return arqs.map(a=>{
    const icon=FILE_ICONS[a.tipo_mime]||'📎';
    return`<div class="arq-item">
      <div class="arq-icon">${icon}</div>
      <div style="flex:1;min-width:0">
        <div class="arq-nome" title="${esc(a.nome)}">${esc(a.nome)}</div>
        <div class="arq-meta">
          <span class="arq-cat">${esc(a.categoria||'Outro')}</span>
          &nbsp;${fmtSize(a.tamanho)} · ${fmtDate(a.data_upload)}
          ${a.descricao?` · <em>${esc(a.descricao)}</em>`:''}
        </div>
      </div>
      <div style="display:flex;gap:4px;flex-shrink:0">
        <button class="btn btn-pri btn-sm" onclick="viewArquivo('${a.id}')" title="Abrir/Baixar">
          <i data-lucide="download" style="width:11px;height:11px"></i></button>
        <button class="btn btn-danger btn-sm" onclick="deleteArquivo('${a.id}',${escolaId})" title="Excluir">
          <i data-lucide="trash-2" style="width:11px;height:11px"></i></button>
      </div>
    </div>`;
  }).join('');
}

function showImportArquivoModal(escolaId,escolaNome){
  _selectedFile=null;
  showModal('Importar Arquivo — '+escolaNome,`
    <div class="fg">
      <label>Arquivo *</label>
      <div class="drop-zone" id="drop-zone"
           onclick="document.getElementById('arq-picker').click()"
           ondragover="event.preventDefault();this.classList.add('drag-over')"
           ondragleave="this.classList.remove('drag-over')"
           ondrop="handleArqDrop(event)">
        <div style="font-size:34px;margin-bottom:8px">📁</div>
        <div style="font-size:13px;color:var(--muted)">Clique aqui ou arraste o arquivo</div>
        <div style="font-size:11px;color:var(--muted);margin-top:4px">PDF · JPG · PNG · DOC · XLS · TXT (máx. 15MB)</div>
        <input type="file" id="arq-picker" style="display:none"
               accept=".pdf,.jpg,.jpeg,.png,.gif,.doc,.docx,.xls,.xlsx,.txt,.zip"
               onchange="onArqPick(this)">
        <div id="arq-preview" style="margin-top:10px;font-size:12px;font-weight:600;color:var(--acc)"></div>
      </div>
    </div>
    <div class="fr">
      <div class="fg"><label>Categoria</label>
        <select class="fi" id="arq-cat">
          ${ARQ_CATS.map(c=>`<option value="${c}">${c}</option>`).join('')}
        </select></div>
      <div class="fg"><label>Descrição (opcional)</label>
        <input type="text" class="fi" id="arq-desc" placeholder="Ex: Renovado em 2025"></div>
    </div>
    <div id="arq-progress" style="display:none;margin-top:8px">
      <div style="font-size:12px;color:var(--muted);margin-bottom:4px">Salvando arquivo...</div>
      <div style="height:4px;background:var(--sec);border-radius:2px;overflow:hidden">
        <div style="height:100%;background:var(--acc);width:0%;transition:width .3s;border-radius:2px" id="arq-pbar"></div>
      </div>
    </div>`,
    `<button class="btn btn-sec" onclick="closeModal()">Cancelar</button>
     <button class="btn btn-pri" onclick="confirmarImportArquivo(${escolaId},'${esc(escolaNome)}')">
       <i data-lucide="upload" style="width:13px;height:13px"></i>Salvar Arquivo</button>`
  );
}

function onArqPick(input){
  if(input.files&&input.files[0])setArqFile(input.files[0]);
}
function handleArqDrop(event){
  event.preventDefault();
  document.getElementById('drop-zone').classList.remove('drag-over');
  if(event.dataTransfer.files&&event.dataTransfer.files[0])setArqFile(event.dataTransfer.files[0]);
}
function setArqFile(file){
  _selectedFile=file;
  const el=document.getElementById('arq-preview');
  if(el)el.innerHTML=`✓ ${esc(file.name)} <span style="font-weight:400;color:var(--muted)">(${fmtSize(file.size)})</span>`;
}

async function confirmarImportArquivo(escolaId,escolaNome){
  if(!_selectedFile){showToast('Selecione um arquivo','error');return;}
  const MAX=15*1024*1024;
  if(_selectedFile.size>MAX){showToast('Arquivo maior que 15MB não suportado','error');return;}
  const cat=document.getElementById('arq-cat').value;
  const desc=document.getElementById('arq-desc').value.trim();
  const prog=document.getElementById('arq-progress');
  const pbar=document.getElementById('arq-pbar');
  const nome=_selectedFile.name;
  if(prog)prog.style.display='block';
  if(pbar)pbar.style.width='30%';
  try{
    const reader=new FileReader();
    reader.onprogress=e=>{if(pbar&&e.lengthComputable)pbar.style.width=Math.min(80,Math.round(e.loaded/e.total*80))+'%';};
    const dataURL=await new Promise((res,rej)=>{reader.onload=e=>res(e.target.result);reader.onerror=rej;reader.readAsDataURL(_selectedFile);});
    if(pbar)pbar.style.width='90%';
    const id='arq_'+Date.now()+'_'+Math.random().toString(36).slice(2,7);
    await storeFileContent(id,dataURL);
    if(!DB.arquivos)DB.arquivos=[];
    DB.arquivos.push({id,escola_id:escolaId,escola_nome:escolaNome,nome,tipo_mime:_selectedFile.type,
      categoria:cat,tamanho:_selectedFile.size,data_upload:todayISO(),descricao:desc||null});
    save();
    if(pbar)pbar.style.width='100%';
    _selectedFile=null;
    closeModal();
    showToast(`"${nome}" importado com sucesso!`);
    openEscolaDrawer(escolaId);
  }catch(e){
    showToast('Erro ao salvar: '+(e.message||e),'error');
    if(prog)prog.style.display='none';
  }
}

async function viewArquivo(id){
  const meta=(DB.arquivos||[]).find(a=>a.id===id);
  showToast('Carregando arquivo...','info');
  try{
    const dataURL=await loadFileContent(id);
    if(!dataURL){showToast('Arquivo não encontrado no armazenamento local','error');return;}
    const mime=meta?meta.tipo_mime:'application/octet-stream';
    const isPDF=mime==='application/pdf';
    const isImg=mime.startsWith('image/');
    if(isPDF||isImg){
      // Open in new tab
      const w=window.open();
      if(w){w.document.write(`<html><body style="margin:0;background:#333"><${isImg?'img':'iframe'} src="${dataURL}" style="width:100%;height:100vh;border:none;display:block"></${isImg?'img':'iframe'}></body></html>`);w.document.close();}
    }else{
      // Trigger download
      const a=document.createElement('a');a.href=dataURL;a.download=meta?meta.nome:'arquivo';a.click();
    }
  }catch(e){showToast('Erro ao abrir: '+(e.message||e),'error');}
}

async function deleteArquivo(id,escolaId){
  if(!confirm('Excluir este arquivo? Esta ação não pode ser desfeita.'))return;
  try{await removeFileContent(id);}catch(e){}
  DB.arquivos=(DB.arquivos||[]).filter(a=>a.id!==id);
  save();
  openEscolaDrawer(escolaId);
  showToast('Arquivo excluído','error');
}

// ── INIT ──────────────────────────────────────────────────────────────────────
go('dashboard');
"""

JS = JS.replace('__DATA__', data_js)

full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RegularEduc — Controle Regulatório</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@0.263.1/dist/umd/lucide.min.js"></script>
<style>{CSS}</style>
</head>
<body>
{HTML}
<script>
{JS}
</script>
</body>
</html>"""

with open('regulareduc.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f'Gerado: regulareduc.html ({len(full_html)//1024} KB)')
