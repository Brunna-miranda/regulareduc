"""
Gera regulareduc_supabase.html — versão com autenticação e dados centralizados no Supabase.
Execute: python -X utf8 build_supabase.py
"""

SUPABASE_URL = "https://ruirdarbiftvnducmfxt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1aXJkYXJiaWZ0dm5kdWNtZnh0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODEyODk0MzcsImV4cCI6MjA5Njg2NTQzN30.XznYUuv30VAW6jtH3leuaFFlOZC_ViMOCU1wGZnUJd8"

# ── CSS login + loading ────────────────────────────────────────────────────────
CSS_LOGIN = """
#login-root{position:fixed;inset:0;background:#F0F4FA;display:flex;align-items:center;justify-content:center;z-index:9999}
.login-card{background:#fff;border-radius:16px;padding:36px;width:100%;max-width:420px;box-shadow:0 8px 40px rgba(0,0,0,.12)}
.login-logo{font-size:26px;font-weight:800;color:#1B3A6B;letter-spacing:-.5px;text-align:center;margin-bottom:4px}
.login-sub{font-size:12px;color:#6B7280;text-align:center;margin-bottom:24px}
.login-tabs{display:flex;background:#F0F4FA;border-radius:10px;padding:3px;margin-bottom:20px}
.login-tab{flex:1;padding:8px;border:none;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;background:transparent;color:#6B7280;transition:.15s;font-family:inherit}
.login-tab.active{background:#fff;color:#1B3A6B;box-shadow:0 1px 4px rgba(0,0,0,.1)}
.login-input{width:100%;padding:11px 14px;border:1.5px solid #E5E7EB;border-radius:10px;font-size:14px;outline:none;margin-bottom:12px;font-family:inherit;transition:border-color .15s;box-sizing:border-box}
.login-input:focus{border-color:#2D6BE4}
.login-btn{width:100%;padding:12px;background:#1B3A6B;color:#fff;border:none;border-radius:10px;font-size:14px;font-weight:700;cursor:pointer;transition:.15s;font-family:inherit;margin-top:4px}
.login-btn:hover{background:#2D6BE4}
.login-btn:disabled{opacity:.6;cursor:not-allowed}
.login-msg{font-size:12px;padding:10px 14px;border-radius:8px;margin-bottom:14px;display:none;line-height:1.5}
.login-msg.show{display:block}
.login-msg.error{background:#FEE2E2;color:#991B1B;border:1px solid #FECACA}
.login-msg.info{background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE}
.login-msg.success{background:#DCFCE7;color:#15803D;border:1px solid #BBF7D0}
#loading-overlay{position:fixed;inset:0;background:rgba(27,58,107,.92);display:none;align-items:center;justify-content:center;z-index:9998;flex-direction:column;gap:16px}
.loading-spinner{width:40px;height:40px;border:3px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .8s linear infinite}
.loading-text{color:#fff;font-size:14px;font-weight:500}
@keyframes spin{to{transform:rotate(360deg)}}
"""

# ── HTML login screen + loading overlay ───────────────────────────────────────
HTML_LOGIN = """
<div id="login-root">
  <div class="login-card">
    <div class="login-logo">RegularEduc</div>
    <div class="login-sub">Plataforma de Gestão Regulatória Escolar</div>
    <!-- Tabs -->
    <div class="login-tabs">
      <button class="login-tab active" id="tab-login" onclick="switchTab('login')">Entrar</button>
      <button class="login-tab" id="tab-register" onclick="switchTab('register')">Criar Conta</button>
    </div>
    <!-- Mensagem -->
    <div class="login-msg" id="login-msg"></div>
    <!-- Formulário Entrar -->
    <div id="form-login">
      <input class="login-input" type="email" id="li-email" placeholder="E-mail"
             onkeydown="if(event.key==='Enter')document.getElementById('li-pw').focus()">
      <input class="login-input" type="password" id="li-pw" placeholder="Senha"
             onkeydown="if(event.key==='Enter')doLogin()">
      <button class="login-btn" onclick="doLogin()">Entrar</button>
    </div>
    <!-- Formulário Criar Conta -->
    <div id="form-register" style="display:none">
      <input class="login-input" type="text" id="reg-nome" placeholder="Nome completo"
             onkeydown="if(event.key==='Enter')document.getElementById('reg-email').focus()">
      <input class="login-input" type="email" id="reg-email" placeholder="E-mail"
             onkeydown="if(event.key==='Enter')document.getElementById('reg-pw').focus()">
      <input class="login-input" type="password" id="reg-pw" placeholder="Senha (mínimo 6 caracteres)"
             onkeydown="if(event.key==='Enter')doRegister()">
      <button class="login-btn" onclick="doRegister()">Criar Conta</button>
    </div>
  </div>
</div>
<div id="loading-overlay">
  <div class="loading-spinner"></div>
  <div class="loading-text" id="loading-text">Carregando dados...</div>
</div>
<div id="app-root" style="display:none">
"""

HTML_LOGIN_CLOSE = """
</div><!-- /app-root -->
"""

# ── JS Supabase layer ──────────────────────────────────────────────────────────
JS_SUPABASE = f"""
// ── SUPABASE ──────────────────────────────────────────────────────────────────
const {{createClient}}=supabase;
const sb=createClient('{SUPABASE_URL}','{SUPABASE_KEY}');
let currentUser=null;

// ── AUTH HELPERS ──────────────────────────────────────────────────────────────
function showLoginMsg(msg,type='error'){{
  const el=document.getElementById('login-msg');
  if(!el)return;
  el.textContent=msg;el.className='login-msg show '+type;
}}
function clearLoginMsg(){{
  const el=document.getElementById('login-msg');
  if(el){{el.className='login-msg';el.textContent='';}}
}}
function setLoginBtnLoading(btnId,loading,text){{
  const btn=document.getElementById(btnId)||document.querySelector('#form-login .login-btn, #form-register .login-btn');
  if(btn){{btn.disabled=loading;if(text)btn.textContent=loading?'Aguarde...':text;}}
}}
function switchTab(tab){{
  clearLoginMsg();
  document.getElementById('form-login').style.display=tab==='login'?'block':'none';
  document.getElementById('form-register').style.display=tab==='register'?'block':'none';
  document.getElementById('tab-login').className='login-tab'+(tab==='login'?' active':'');
  document.getElementById('tab-register').className='login-tab'+(tab==='register'?' active':'');
}}

async function doLogin(){{
  const email=document.getElementById('li-email')?.value?.trim();
  const pw=document.getElementById('li-pw')?.value;
  if(!email||!pw){{showLoginMsg('Preencha e-mail e senha.');return;}}
  clearLoginMsg();
  const btn=document.querySelector('#form-login .login-btn');
  if(btn){{btn.disabled=true;btn.textContent='Entrando...';}}
  const {{data,error}}=await sb.auth.signInWithPassword({{email,password:pw}});
  if(btn){{btn.disabled=false;btn.textContent='Entrar';}}
  if(error){{
    showLoginMsg(error.message==='Invalid login credentials'?'E-mail ou senha incorretos.':error.message);
    return;
  }}
  currentUser=data.user;
  await bootApp();
}}

async function doRegister(){{
  const nome=document.getElementById('reg-nome')?.value?.trim();
  const email=document.getElementById('reg-email')?.value?.trim();
  const pw=document.getElementById('reg-pw')?.value;
  if(!nome||!email||!pw){{showLoginMsg('Preencha todos os campos.');return;}}
  if(pw.length<6){{showLoginMsg('A senha precisa ter pelo menos 6 caracteres.');return;}}
  clearLoginMsg();
  const btn=document.querySelector('#form-register .login-btn');
  if(btn){{btn.disabled=true;btn.textContent='Criando conta...';}}
  const {{data,error}}=await sb.auth.signUp({{email,password:pw,options:{{data:{{full_name:nome}}}}}});
  if(btn){{btn.disabled=false;btn.textContent='Criar Conta';}}
  if(error){{showLoginMsg(error.message);return;}}
  // Se confirmação de email desabilitada no Supabase, já faz login direto
  if(data.session){{
    currentUser=data.user;
    await bootApp();
  }} else {{
    showLoginMsg('Conta criada! Verifique seu e-mail e clique no link de confirmação para ativar.','success');
  }}
}}

async function doLogout(){{
  await sb.auth.signOut();
  currentUser=null;
  document.getElementById('app-root').style.display='none';
  document.getElementById('login-root').style.display='flex';
  clearLoginMsg();
}}

async function checkAuth(){{
  const {{data:{{session}}}}=await sb.auth.getSession();
  if(!session){{
    document.getElementById('login-root').style.display='flex';
    return;
  }}
  currentUser=session.user;
  await bootApp();
}}

async function bootApp(){{
  document.getElementById('login-root').style.display='none';
  document.getElementById('loading-overlay').style.display='flex';
  document.getElementById('loading-text').textContent='Carregando dados...';
  try{{
    await loadFromSupabase();
    document.getElementById('loading-overlay').style.display='none';
    document.getElementById('app-root').style.display='block';
    go('dashboard');
  }}catch(e){{
    document.getElementById('loading-overlay').style.display='none';
    document.getElementById('login-root').style.display='flex';
    showLoginMsg('Erro ao carregar: '+(e.message||String(e)));
  }}
}}

// ── LOAD FROM SUPABASE ────────────────────────────────────────────────────────
async function loadFromSupabase(){{
  const results=await Promise.all([
    sb.from('redes').select('*').order('nome'),
    sb.from('escolas').select('*').eq('ativa',true).order('nome'),
    sb.from('documentos').select('*'),
    sb.from('processos_sei').select('*').order('created_at',{{ascending:false}}),
    sb.from('andamentos').select('*').order('data'),
    sb.from('checklist_items').select('*'),
    sb.from('tarefas').select('*').order('prazo'),
    sb.from('financeiro').select('*').order('data_vencimento'),
    sb.from('contatos').select('*').order('nome'),
    sb.from('usuarios_app').select('*').eq('ativo',true),
    sb.from('etaps').select('*'),
    sb.from('etap_membros').select('*'),
    sb.from('etap_publicacoes_do').select('*'),
    sb.from('etap_processos_vinculados').select('*'),
    sb.from('auditorias').select('*').order('data',{{ascending:false}}),
    sb.from('auditoria_items').select('*'),
    sb.from('legislacoes').select('*').order('data',{{ascending:false}}),
    sb.from('modelos_anexos').select('*').order('titulo'),
    sb.from('tipos_processo').select('*').order('ordem'),
  ]);

  results.forEach(r=>{{if(r.error)throw r.error;}});
  const [redes,escolas,docs,procs,ands,chkItems,tarefas,fin,contatos,
         usuarios,etapsList,membros,dosPublic,etapProcsVinc,
         auditorias,audItems,legislacoes,modelos,tiposProc]=results.map(r=>r.data||[]);

  DB.redes=redes;
  const redeMap={{}};redes.forEach(r=>redeMap[r.id]=r.nome);
  const escolaMap={{}};
  escolas.forEach(e=>{{e.rede=redeMap[e.rede_id]||'';escolaMap[e.id]=e;}});

  const allDocs=docs.map(d=>{{
    const e=escolaMap[d.escola_id]||{{}};
    return{{...d,escola:e.nome||'',rede:e.rede||'',estado:e.estado||''}};
  }});
  DB.docs=allDocs;

  const docsWithSt=allDocs.map(d=>{{...d,_s:statusFromDoc(d)}});
  DB.schools=escolas.map(e=>{{
    const sd=docsWithSt.filter(d=>d.escola_id===e.id);
    return{{...e,total_docs:sd.length,ok_docs:sd.filter(d=>d._s==='ok').length,
      a_vencer:sd.filter(d=>d._s==='a_vencer').length,
      criticos:sd.filter(d=>['vencido','pendente'].includes(d._s)).length}};
  }});

  const andByProc={{}},chkByProc={{}};
  ands.forEach(a=>{{(andByProc[a.processo_id]||(andByProc[a.processo_id]=[])).push(a);}});
  chkItems.forEach(i=>{{(chkByProc[i.processo_id]||(chkByProc[i.processo_id]=[])).push(i);}});

  DB.procs=procs.map(p=>{{
    const e=escolaMap[p.escola_id]||{{}};
    return{{...p,escola:e.nome||'',rede:e.rede||'',
      andamentos:andByProc[p.id]||[],checklist_items:chkByProc[p.id]||[]}};
  }});

  DB.tarefas=tarefas;
  DB.financeiro=fin;
  DB.contatos=contatos;
  DB.usuarios=usuarios;
  DB.arquivos=[];
  DB.tipos_processo=tiposProc.map(t=>t.nome);
  DB.legislacoes=legislacoes;
  DB.modelos_anexos=modelos;

  const memByEtap={{}},doByEtap={{}},pvByEtap={{}};
  membros.forEach(m=>{{(memByEtap[m.etap_id]||(memByEtap[m.etap_id]=[])).push(m);}});
  dosPublic.forEach(d=>{{(doByEtap[d.etap_id]||(doByEtap[d.etap_id]=[])).push(d);}});
  etapProcsVinc.forEach(ep=>{{(pvByEtap[ep.etap_id]||(pvByEtap[ep.etap_id]=[])).push(ep.processo_id);}});
  DB.etaps=etapsList.map(e=>{{
    const escola=escolaMap[e.escola_id]||{{}};
    return{{...e,escola:escola.nome||e.escola||'',rede:escola.rede||e.rede||'',
      membros:memByEtap[e.id]||[],publicacoes_do:doByEtap[e.id]||[],
      processos_vinculados:pvByEtap[e.id]||[]}};
  }});

  const aiByAud={{}};
  audItems.forEach(i=>{{(aiByAud[i.auditoria_id]||(aiByAud[i.auditoria_id]=[])).push(i);}});
  DB.auditorias=auditorias.map(a=>{{
    const e=escolaMap[a.escola_id]||{{}};
    return{{...a,escola:e.nome||a.escola||'',rede:e.rede||a.rede||'',
      items:aiByAud[a.id]||[]}};
  }});
}}

// ── SUPABASE HELPERS ──────────────────────────────────────────────────────────
async function sbInsert(table,data){{
  const r=await sb.from(table).insert(data).select().single();
  if(r.error)throw r.error;
  return r.data;
}}
async function sbUpdate(table,data,id){{
  const r=await sb.from(table).update(data).eq('id',id);
  if(r.error)throw r.error;
}}
async function sbDelete(table,id){{
  const r=await sb.from(table).delete().eq('id',id);
  if(r.error)throw r.error;
}}
async function sbUpsert(table,data){{
  const r=await sb.from(table).upsert(data).select().single();
  if(r.error)throw r.error;
  return r.data;
}}

// Reload tudo e re-renderizar
async function reload(){{
  await loadFromSupabase();
  render();
}}

// ── OVERRIDE save() ───────────────────────────────────────────────────────────
// Mantém localStorage como cache local
function save(){{
  try{{localStorage.setItem('rg_v3',JSON.stringify(DB));}}catch(e){{}}
}}

// ── FILE STORAGE (Supabase Storage) ───────────────────────────────────────────
async function uploadToStorage(bucket,path,file){{
  const {{data,error}}=await sb.storage.from(bucket).upload(path,file,{{upsert:true}});
  if(error)throw error;
  return data.path;
}}
async function getSignedUrl(bucket,path,seconds=3600){{
  const {{data,error}}=await sb.storage.from(bucket).createSignedUrl(path,seconds);
  if(error)throw error;
  return data.signedUrl;
}}
async function deleteFromStorage(bucket,path){{
  await sb.storage.from(bucket).remove([path]);
}}

// Override arquivo functions para usar Supabase Storage
async function storeFileContent(id,dataURL){{
  // Mantém IndexedDB como cache local também
  try{{
    const db=await openFileDB();
    await new Promise((res,rej)=>{{const tx=db.transaction('files','readwrite');
      tx.objectStore('files').put({{id,dataURL}});tx.oncomplete=res;tx.onerror=rej;}});
  }}catch(e){{}}
}}
async function loadFileContent(id){{
  // Tenta IndexedDB local primeiro
  try{{
    const db=await openFileDB();
    const r=await new Promise((res,rej)=>{{const tx=db.transaction('files','readonly');
      const req=tx.objectStore('files').get(id);
      req.onsuccess=e=>res(e.target.result?.dataURL||null);req.onerror=rej;}});
    if(r)return r;
  }}catch(e){{}}
  return null;
}}

// ── OVERRIDE SAVE FUNCTIONS ───────────────────────────────────────────────────
// Documenta salvamento
const _origSaveDoc=saveDoc;
saveDoc=async function(id){{
  const tipo=document.getElementById('ef-tipo')?.value;
  const status_=document.getElementById('ef-status')?.value;
  const data_=document.getElementById('ef-data')?.value;
  const obs_=document.getElementById('ef-obs')?.value?.trim();
  const sit_=document.getElementById('ef-situacao')?.value||null;
  const proto_=document.getElementById('ef-protocolo')?.value?.trim()||null;
  const dtProto_=document.getElementById('ef-dt-protocolo')?.value||null;
  if(!tipo){{showToast('Selecione o tipo de documento','error');return;}}
  try{{
    await sbUpdate('documentos',{{tipo,status:status_,data_vencimento:data_||null,
      observacoes:obs_||null,situacao:sit_,numero_protocolo:proto_,data_protocolo:dtProto_||null}},id);
    closeModal();await reload();showToast('Documento salvo!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origAddDoc=addDoc;
addDoc=async function(){{
  const selE=document.getElementById('nd-escola');
  const escolaId=parseInt(selE?.value)||null;
  const selOpt=selE?.options[selE.selectedIndex];
  const tipoSel=document.getElementById('nd-tipo')?.value;
  const tipo=tipoSel==='_custom'?document.getElementById('nd-custom')?.value?.trim():tipoSel;
  const status_=document.getElementById('nd-status')?.value||'desconhecido';
  const data_=document.getElementById('nd-data')?.value||null;
  const obs_=document.getElementById('nd-obs')?.value?.trim()||null;
  if(!escolaId||!tipo){{showToast('Preencha escola e tipo','error');return;}}
  try{{
    await sbInsert('documentos',{{escola_id:escolaId,tipo,status:status_,data_vencimento:data_,observacoes:obs_}});
    closeModal();await reload();showToast('Documento adicionado!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origDeleteDoc=deleteDoc;
deleteDoc=async function(id){{
  if(!confirm('Excluir este documento?'))return;
  try{{
    await sbDelete('documentos',id);await reload();showToast('Documento excluído','error');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origSaveProc=saveProc;
saveProc=async function(id){{
  const num=document.getElementById('ep-num')?.value?.trim();
  if(!num){{showToast('Preencha o número','error');return;}}
  const selE=document.getElementById('ep-escola');
  const escolaId=parseInt(selE?.value)||null;
  const selOpt=selE?.options[selE?.selectedIndex];
  const data_={{numero:num,escola_id:escolaId,
    tipo_processo:document.getElementById('ep-tipo')?.value||null,
    responsavel:document.getElementById('ep-resp')?.value||null,
    forma_exigencia:document.getElementById('ep-forma')?.value?.trim()||null,
    data_recebimento:document.getElementById('ep-rec')?.value?.trim()||null,
    status:document.getElementById('ep-status')?.value||'aberto',
    prazo:document.getElementById('ep-prazo')?.value?.trim()||null,
    observacoes:document.getElementById('ep-obs')?.value?.trim()||null}};
  try{{
    if(id>0){{await sbUpdate('processos_sei',data_,id);}}
    else{{await sbInsert('processos_sei',data_);}}
    closeModal();await reload();showToast('Processo salvo!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origDeleteProc=deleteProc;
deleteProc=async function(id){{
  if(!confirm('Excluir este processo?'))return;
  try{{
    await sbDelete('processos_sei',id);await reload();showToast('Processo excluído','error');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origAddAndamento=addAndamento;
addAndamento=async function(procId){{
  const txt=document.getElementById('novo-and')?.value?.trim();
  const dt=document.getElementById('novo-and-data')?.value||todayISO();
  if(!txt){{showToast('Digite o andamento','error');return;}}
  try{{
    await sbInsert('andamentos',{{processo_id:procId,data:dt,texto:txt,autor:DB.usuarios[0]?.nome||'Usuário'}});
    await reload();openProcDetail(procId);showToast('Andamento registrado!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origToggleChkItem=toggleChkItem;
toggleChkItem=async function(procId,itemId,done){{
  try{{
    await sbUpdate('checklist_items',{{done}},itemId);
    await loadFromSupabase();openProcDetail(procId);
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origAddChkItem=addChkItem;
addChkItem=async function(procId){{
  const input=document.getElementById('chk-new-'+procId);
  const texto=(input?.value||'').trim();
  if(!texto){{showToast('Digite o item','error');return;}}
  try{{
    await sbInsert('checklist_items',{{processo_id:procId,texto,done:false,obs:''}});
    await loadFromSupabase();openProcDetail(procId);showToast('Item adicionado!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origDeleteChkItem=deleteChkItem;
deleteChkItem=async function(procId,itemId){{
  try{{
    await sbDelete('checklist_items',itemId);await loadFromSupabase();openProcDetail(procId);
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origSaveTarefa=saveTarefa;
saveTarefa=async function(id){{
  const titulo=document.getElementById('ta-titulo')?.value?.trim();
  if(!titulo){{showToast('Título é obrigatório','error');return;}}
  const escolaEl=document.getElementById('ta-escola');
  const escola=escolaEl?.value||null;
  const escolaId=DB.schools.find(s=>s.nome===escola)?.id||null;
  const data_={{titulo,descricao:document.getElementById('ta-desc')?.value?.trim()||null,
    responsavel:document.getElementById('ta-resp')?.value||null,
    prioridade:document.getElementById('ta-prio')?.value||'media',
    escola,escola_id:escolaId,categoria:document.getElementById('ta-cat')?.value||null,
    prazo:document.getElementById('ta-prazo')?.value||null,
    status:document.getElementById('ta-status')?.value||'pendente',
    observacoes:document.getElementById('ta-obs')?.value?.trim()||null}};
  try{{
    if(id>0){{await sbUpdate('tarefas',data_,id);}}
    else{{await sbInsert('tarefas',{{...data_,criada_em:todayISO()}});}}
    closeModal();await reload();showToast('Tarefa salva!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origDeleteTarefa=deleteTarefa;
deleteTarefa=async function(id){{
  if(!confirm('Excluir esta tarefa?'))return;
  try{{await sbDelete('tarefas',id);await reload();showToast('Tarefa excluída','error');}}
  catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origSaveFin=saveFin;
saveFin=async function(id){{
  const desc=document.getElementById('fi-desc')?.value?.trim();
  const cat=document.getElementById('fi-cat')?.value;
  if(!desc||!cat){{showToast('Preencha descrição e categoria','error');return;}}
  const selE=document.getElementById('fi-escola');
  const escolaNome=selE?.value||null;
  const escolaId=DB.schools.find(s=>s.nome===escolaNome)?.id||null;
  const valorStr=document.getElementById('fi-valor')?.value?.replace(/\\./g,'').replace(',','.')||'0';
  const valor=parseFloat(valorStr)||0;
  if(valor<=0){{showToast('Informe um valor válido','error');return;}}
  const data_={{descricao:desc,categoria:cat,escola:escolaNome,escola_id:escolaId,
    orgao:document.getElementById('fi-orgao')?.value?.trim()||null,
    responsavel:document.getElementById('fi-resp')?.value||null,
    valor,data_vencimento:document.getElementById('fi-dvenc')?.value||null,
    data_pagamento:document.getElementById('fi-dpag')?.value||null,
    status:document.getElementById('fi-status')?.value||'pendente',
    forma_pagamento:document.getElementById('fi-forma')?.value||null,
    observacoes:document.getElementById('fi-obs')?.value?.trim()||null}};
  try{{
    if(id>0){{await sbUpdate('financeiro',data_,id);}}
    else{{await sbInsert('financeiro',data_);}}
    closeModal();await reload();showToast('Lançamento salvo!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origDeleteFin=deleteFin;
deleteFin=async function(id){{
  if(!confirm('Excluir este lançamento?'))return;
  try{{await sbDelete('financeiro',id);await reload();showToast('Lançamento excluído','error');}}
  catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origSaveContato=saveContato;
saveContato=async function(id){{
  const nome=document.getElementById('ct-nome')?.value?.trim();
  if(!nome){{showToast('Nome é obrigatório','error');return;}}
  const data_={{nome,cargo:document.getElementById('ct-cargo')?.value||null,
    regional:document.getElementById('ct-regional')?.value||null,
    escola_vinculada:document.getElementById('ct-escola')?.value||null,
    telefone:document.getElementById('ct-tel')?.value?.trim()||null,
    email:document.getElementById('ct-email')?.value?.trim()||null,
    observacoes:document.getElementById('ct-obs')?.value?.trim()||null}};
  try{{
    if(id>0){{await sbUpdate('contatos',data_,id);}}
    else{{await sbInsert('contatos',data_);}}
    closeModal();await reload();showToast('Contato salvo!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origDeleteContato=deleteContato;
deleteContato=async function(id){{
  if(!confirm('Excluir este contato?'))return;
  try{{await sbDelete('contatos',id);await reload();showToast('Contato excluído','error');}}
  catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origSaveUsuario=saveUsuario;
saveUsuario=async function(id){{
  const nome=document.getElementById('us-nome')?.value?.trim();
  if(!nome){{showToast('Nome é obrigatório','error');return;}}
  const data_={{nome,cargo:document.getElementById('us-cargo')?.value?.trim()||null,
    email:document.getElementById('us-email')?.value?.trim()||null,
    setor:document.getElementById('us-setor')?.value?.trim()||null,
    ativo:document.getElementById('us-ativo')?.value==='1'}};
  try{{
    if(id>0){{await sbUpdate('usuarios_app',data_,id);}}
    else{{await sbInsert('usuarios_app',data_);}}
    closeModal();await reload();showToast('Usuário salvo!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origDeleteUsuario=deleteUsuario;
deleteUsuario=async function(id){{
  if(DB.usuarios.length<=1){{showToast('É necessário ao menos 1 usuário','error');return;}}
  if(!confirm('Excluir este usuário?'))return;
  try{{await sbDelete('usuarios_app',id);await reload();showToast('Usuário removido','error');}}
  catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origSaveEscola=saveEscola;
saveEscola=async function(id){{
  const nome=document.getElementById('es-nome')?.value?.trim();
  if(!nome){{showToast('Nome é obrigatório','error');return;}}
  const censo=document.getElementById('es-censo')?.value?.trim().replace(/\\D/g,'')||null;
  const redeEl=document.getElementById('es-rede');
  let redeNome=redeEl?.value||'';
  let redeId=null;
  if(redeNome==='__nova__'){{
    const novaNome=document.getElementById('es-rede-nova')?.value?.trim();
    if(!novaNome){{showToast('Digite o nome da nova rede','error');return;}}
    redeNome=novaNome;
    try{{const r=await sbInsert('redes',{{nome:novaNome}});redeId=r.id;}}catch(e){{}}
  }}else{{
    redeId=DB.redes.find(r=>r.nome===redeNome)?.id||null;
  }}
  const statusU=document.querySelector('input[name="es-status-u"]:checked')?.value||'em_funcionamento';
  const data_={{nome,rede_id:redeId,
    cnpj:document.getElementById('es-cnpj')?.value?.trim()||null,
    inscricao_municipal:document.getElementById('es-insc')?.value?.trim()||null,
    codigo_censo:censo||null,status_unidade:statusU,
    estado:document.getElementById('es-estado')?.value||'RJ',
    o_que_funciona:document.getElementById('es-funciona')?.value?.trim()||null,
    observacoes:document.getElementById('es-obs')?.value?.trim()||null,ativa:true}};
  try{{
    if(id>0){{await sbUpdate('escolas',data_,id);closeModal();await reload();openEscolaDrawer(id);showToast('Escola atualizada!');}}
    else{{await sbInsert('escolas',data_);closeModal();await reload();showToast('Escola cadastrada!');}}
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origDeleteEscola=deleteEscola;
deleteEscola=async function(id){{
  const s=DB.schools.find(x=>x.id===id);if(!s)return;
  if(!confirm('Excluir "'+s.nome+'" e todos os dados vinculados?'))return;
  try{{await sbDelete('escolas',id);closeDrawer();await reload();showToast('Escola excluída','error');}}
  catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origSaveLeg=saveLeg;
saveLeg=async function(id){{
  const titulo=document.getElementById('lg-titulo')?.value?.trim();
  const orgao=document.getElementById('lg-orgao')?.value;
  const tipo=document.getElementById('lg-tipo')?.value;
  if(!titulo||!orgao||!tipo){{showToast('Preencha título, órgão e tipo','error');return;}}
  const data_={{titulo,orgao,tipo,
    numero:document.getElementById('lg-num')?.value?.trim()||null,
    data:document.getElementById('lg-data')?.value||null,
    ementa:document.getElementById('lg-ementa')?.value?.trim()||null,
    link_oficial:document.getElementById('lg-link')?.value?.trim()||null}};
  try{{
    if(id>0){{await sbUpdate('legislacoes',data_,id);}}
    else{{await sbInsert('legislacoes',data_);}}
    closeModal();await reload();showToast('Legislação salva!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

const _origSaveModelo=saveModelo;
saveModelo=async function(id){{
  const titulo=document.getElementById('mo-titulo')?.value?.trim();
  const cat=document.getElementById('mo-cat')?.value;
  if(!titulo||!cat){{showToast('Preencha título e categoria','error');return;}}
  const data_={{titulo,categoria:cat,
    versao:document.getElementById('mo-versao')?.value?.trim()||null,
    descricao:document.getElementById('mo-desc')?.value?.trim()||null,
    instrucoes:document.getElementById('mo-inst')?.value?.trim()||null}};
  try{{
    if(id>0){{await sbUpdate('modelos_anexos',data_,id);}}
    else{{await sbInsert('modelos_anexos',data_);}}
    closeModal();await reload();showToast('Modelo salvo!');
  }}catch(e){{showToast('Erro: '+(e.message||e),'error');}}
}};

// ── EXPORTAR DATA (Supabase) ──────────────────────────────────────────────────
function exportData(){{
  const blob=new Blob([JSON.stringify(DB,null,2)],{{type:'application/json'}});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='regulareduc_backup_'+todayISO()+'.json';a.click();
  showToast('Backup exportado!');
}}
function resetData(){{
  showToast('Para resetar use o painel Supabase → Table Editor','info');
}}

// ── INIT ──────────────────────────────────────────────────────────────────────
// (substitui go('dashboard') do final do script original)
checkAuth();
"""

# ── BUILD ─────────────────────────────────────────────────────────────────────
def build():
    import re

    # Ler o HTML atual
    with open('regulareduc.html', encoding='utf-8') as f:
        html = f.read()

    # 1. Adicionar Supabase CDN no <head>
    html = html.replace(
        '<script src="https://unpkg.com/lucide@0.263.1/dist/umd/lucide.min.js"></script>',
        '<script src="https://unpkg.com/lucide@0.263.1/dist/umd/lucide.min.js"></script>\n'
        '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'
    )

    # 2. Adicionar CSS login no bloco <style>
    html = html.replace('</style>', CSS_LOGIN + '\n</style>', 1)

    # 3. Adicionar botão logout no header (após o sino de notificações)
    html = html.replace(
        '</div>\n</div>\n\n<div class="main"',
        '</div>\n'
        '<button class="btn-ic" onclick="doLogout()" title="Sair" style="color:var(--red)">\n'
        '  <i data-lucide="log-out" style="width:16px;height:16px"></i>\n'
        '</button>\n'
        '</div>\n</div>\n\n<div class="main"'
    )

    # 4. Envolver o conteúdo do body com login-root + app-root
    # Substituir o início do body content
    html = html.replace('<div class="sb">', HTML_LOGIN + '<div class="sb">', 1)

    # Encontrar onde o HTML principal termina (antes do </body>)
    # Adicionar fechamento do app-root e o script Supabase
    html = html.replace(
        '<div class="toasts" id="toasts"></div>\n<div id="modal-root"></div>\n<div id="drawer-root"></div>',
        '<div class="toasts" id="toasts"></div>\n<div id="modal-root"></div>\n<div id="drawer-root"></div>\n' + HTML_LOGIN_CLOSE
    )

    # 5. Remover "go('dashboard');" do final do script e adicionar o JS do Supabase
    # O script original termina com: go('dashboard');
    html = html.replace("go('dashboard');\n\"\"\"", "// Supabase init handled below\n\"\"\"")

    # 6. Adicionar o bloco JS do Supabase ANTES do </script> final
    html = html.replace('</script>\n</body>', JS_SUPABASE + '\n</script>\n</body>', 1)

    with open('regulareduc_supabase.html', 'w', encoding='utf-8') as f:
        f.write(html)

    size_kb = len(html) // 1024
    print(f'Gerado: regulareduc_supabase.html ({size_kb} KB)')
    return html

if __name__ == '__main__':
    build()
