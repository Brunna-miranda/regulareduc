with open('regulareduc_supabase.html', encoding='utf-8') as f:
    content = f.read()

checks = [
    ('Supabase CDN', 'supabase-js@2'),
    ('login-root', 'login-root'),
    ('checkAuth', 'checkAuth'),
    ('doLogin', 'doLogin'),
    ('loadFromSupabase', 'loadFromSupabase'),
    ('bootApp', 'bootApp'),
    ('doLogout', 'doLogout'),
    ('app-root div', 'id="app-root"'),
    ('loading-overlay', 'loading-overlay'),
    ('sbInsert helper', 'sbInsert'),
    ('sbUpdate helper', 'sbUpdate'),
    ('Supabase URL embutida', 'ruirdarbiftvnducmfxt'),
]
print('=== VERIFICACAO DO HTML ===')
for label, search in checks:
    found = search in content
    status = 'OK  ' if found else 'FALTA'
    print(f'  {status} {label}')
print(f'\nTamanho: {len(content)//1024} KB')

# Verificar se login-root fecha antes de app-root abre
lr_pos = content.find('id="login-root"')
ar_pos = content.find('id="app-root"')
print(f'\nPosicao login-root: {lr_pos}')
print(f'Posicao app-root: {ar_pos}')
print(f'Ordem correta (login antes de app): {lr_pos < ar_pos}')
