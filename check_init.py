with open('regulareduc_supabase.html', encoding='utf-8') as f:
    c = f.read()

# Verificar se checkAuth() está no final do script (como init)
script_end = c.rfind('</script>')
last_500 = c[script_end-500:script_end]
print("=== FINAL DO SCRIPT ===")
print(last_500[-300:])
print()

# Verificar se existe go('dashboard') como chamada de init solta (não dentro de função)
import re
count = len(re.findall(r"go\('dashboard'\)", c))
print(f"Ocorrencias de go('dashboard'): {count}")
count2 = c.count('checkAuth()')
print(f"Ocorrencias de checkAuth(): {count2}")
