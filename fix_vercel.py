"""Desabilita proteção de autenticação do Vercel e configura domínio público."""
import requests, json

TOKEN      = "COLE_SEU_TOKEN_AQUI"   # vercel.com → Settings → Tokens
PROJECT_ID = "prj_IzjniC0Zqbepey95Dx52hw3jp1QJ"
DEPLOY_ID  = "dpl_F873RSz7xVCFfbrXJUfipAWQCf5T"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type":  "application/json",
}

print("=== Corrigindo configurações do projeto Vercel ===\n")

# 1. Desabilitar proteção de autenticação (SSO/Password protection)
print("1. Desabilitando deployment protection...")
r = requests.patch(
    f"https://api.vercel.com/v9/projects/{PROJECT_ID}",
    headers=headers,
    json={
        "ssoProtection": None,
        "passwordProtection": None,
        "trustedIps": None,
        "autoExposeSystemEnvs": True,
    }
)
print(f"   Status: {r.status_code}")
if r.status_code == 200:
    print("   OK — proteção desabilitada")
else:
    print(f"   Resposta: {r.text[:200]}")

# 2. Verificar estado do deploy
print("\n2. Verificando estado do deploy...")
r2 = requests.get(
    f"https://api.vercel.com/v13/deployments/{DEPLOY_ID}",
    headers=headers
)
if r2.status_code == 200:
    data = r2.json()
    state  = data.get("readyState", "unknown")
    url    = data.get("url", "")
    alias  = data.get("alias", [])
    print(f"   Estado: {state}")
    print(f"   URL:    https://{url}")
    if alias:
        print(f"   Alias:  https://{alias[0]}")
else:
    print(f"   Erro: {r2.text[:200]}")

# 3. Listar aliases do projeto
print("\n3. Verificando aliases do projeto...")
r3 = requests.get(
    f"https://api.vercel.com/v9/projects/{PROJECT_ID}/domains",
    headers=headers
)
if r3.status_code == 200:
    domains = r3.json().get("domains", [])
    for d in domains:
        print(f"   {d.get('name')} — {d.get('verified')}")
else:
    print(f"   {r3.text[:200]}")

# 4. Promover deploy para produção se necessário
print("\n4. Promovendo deploy para produção...")
r4 = requests.post(
    f"https://api.vercel.com/v9/projects/{PROJECT_ID}/promote/{DEPLOY_ID}",
    headers=headers
)
print(f"   Status: {r4.status_code} — {r4.text[:150]}")

print("\n=== LINKS FINAIS ===")
print(f"Dashboard: https://vercel.com/brunna-miranda/regulareduc")
print(f"App:       https://regulareduc-brunnamiranda.vercel.app")
