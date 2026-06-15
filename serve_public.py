"""
Inicia servidor local + túnel ngrok para compartilhar a plataforma publicamente.
Execute: python serve_public.py
"""
import http.server
import threading
import sys
import os

PORT = 8080
ARQUIVO = "regulareduc.html"
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.path = f"/{ARQUIVO}"
        super().do_GET()
    def log_message(self, fmt, *args):
        pass  # silencia logs

def start_server():
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    print("Iniciando servidor local...")
    t = threading.Thread(target=start_server, daemon=True)
    t.start()
    print(f"Servidor rodando em http://localhost:{PORT}")

    try:
        from pyngrok import ngrok, conf
        print("Criando túnel público via ngrok...")
        tunnel = ngrok.connect(PORT, "http")
        url = tunnel.public_url
        print("\n" + "="*60)
        print("  LINK PÚBLICO PARA COMPARTILHAR:")
        print(f"  {url}")
        print("="*60)
        print("\nCompartilhe este link. Válido enquanto esta janela estiver aberta.")
        print("Pressione Ctrl+C para encerrar.\n")
        try:
            ngrok.get_ngrok_process().proc.wait()
        except KeyboardInterrupt:
            ngrok.kill()
    except Exception as e:
        print(f"Erro no túnel: {e}")
        print(f"\nAcesso local: http://localhost:{PORT}")
        print("Para link público, acesse: https://app.netlify.com/drop")
        print("e arraste o arquivo: C:\\claude\\regulatorio-platform\\regulareduc.html")
        input("\nPressione Enter para encerrar...")
