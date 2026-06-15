"""
Deploy automático no Vercel via API REST.
Execute: python -X utf8 deploy_vercel.py
"""
import requests, base64, json, sys
from pathlib import Path

VERCEL_TOKEN = "COLE_SEU_TOKEN_AQUI"   # vercel.com → Settings → Tokens
PROJECT_NAME = "regulareduc"
FILE_PATH    = Path("index.html")

def main():
    if "COLE_AQUI" in VERCEL_TOKEN:
        print("Configure VERCEL_TOKEN antes de rodar!")
        return

    headers = {
        "Authorization": f"Bearer {VERCEL_TOKEN}",
        "Content-Type":  "application/json",
    }

    print("Lendo arquivo HTML...")
    content = FILE_PATH.read_text(encoding="utf-8")
    content_b64 = base64.b64encode(content.encode("utf-8")).decode()

    # Verificar/criar projeto
    print("Verificando projeto no Vercel...")
    r = requests.get("https://api.vercel.com/v9/projects?limit=20", headers=headers)
    projects = r.json().get("projects", [])
    project = next((p for p in projects if p["name"] == PROJECT_NAME), None)
    project_id = project["id"] if project else None

    if not project_id:
        print("Criando projeto...")
        r = requests.post("https://api.vercel.com/v10/projects", headers=headers,
            json={"name": PROJECT_NAME, "framework": None})
        if r.status_code not in (200, 201):
            print(f"Erro ao criar projeto: {r.text}")
            return
        project_id = r.json()["id"]
        print(f"  Projeto criado: {project_id}")

    # Fazer deploy
    print("Iniciando deploy...")
    payload = {
        "name":    PROJECT_NAME,
        "files": [
            {"file": "index.html",  "data": content_b64,  "encoding": "base64"},
            {"file": "vercel.json", "data": base64.b64encode(
                Path("vercel.json").read_bytes()).decode(), "encoding": "base64"},
        ],
        "projectSettings": {"framework": None, "outputDirectory": "."},
        "target": "production",
    }
    r = requests.post("https://api.vercel.com/v13/deployments", headers=headers, json=payload)

    if r.status_code not in (200, 201):
        print(f"Erro no deploy: {r.status_code} — {r.text[:300]}")
        return

    data = r.json()
    deploy_id  = data.get("id", "")
    deploy_url = data.get("url", "")
    alias      = data.get("alias", [])

    print(f"\n{'='*50}")
    print(f"Deploy iniciado!")
    print(f"  ID:  {deploy_id}")
    print(f"  URL: https://{deploy_url}")
    if alias:
        print(f"  URL produção: https://{alias[0]}")
    print(f"{'='*50}")
    print("\nAcompanhe em: https://vercel.com/dashboard")

if __name__ == "__main__":
    main()
