-- =============================================================================
-- SCHEMA: Sistema de Gestão Regulatória Escolar
-- Target:  Supabase / PostgreSQL
-- Gerado:  2026-06-12
-- =============================================================================
-- Instruções de uso:
--   1. Abra o SQL Editor no painel do Supabase
--   2. Cole todo o conteúdo deste arquivo
--   3. Execute (Run)
-- =============================================================================


-- -----------------------------------------------------------------------------
-- EXTENSÕES
-- -----------------------------------------------------------------------------
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


-- =============================================================================
-- TABELAS
-- =============================================================================


-- -----------------------------------------------------------------------------
-- 1. redes
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS redes (
    id          BIGSERIAL    PRIMARY KEY,
    nome        TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);


-- -----------------------------------------------------------------------------
-- 2. escolas
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS escolas (
    id                    BIGSERIAL    PRIMARY KEY,
    nome                  TEXT         NOT NULL,
    rede_id               BIGINT       REFERENCES redes(id) ON DELETE SET NULL,
    cnpj                  TEXT,
    inscricao_municipal   TEXT,
    estado                TEXT,
    o_que_funciona        TEXT,
    observacoes           TEXT,
    ativa                 BOOLEAN      NOT NULL DEFAULT TRUE,
    status_unidade        TEXT,
    codigo_censo          TEXT,
    created_at            TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at            TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_escolas_rede_id ON escolas(rede_id);
CREATE INDEX IF NOT EXISTS idx_escolas_ativa   ON escolas(ativa);


-- -----------------------------------------------------------------------------
-- 3. tipos_documentos
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tipos_documentos (
    id          BIGSERIAL    PRIMARY KEY,
    nome        TEXT         NOT NULL UNIQUE,
    alerta_dias INT          NOT NULL DEFAULT 30,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);


-- -----------------------------------------------------------------------------
-- 4. documentos
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS documentos (
    id                BIGSERIAL    PRIMARY KEY,
    escola_id         BIGINT       NOT NULL REFERENCES escolas(id) ON DELETE CASCADE,
    tipo              TEXT         NOT NULL,
    status            TEXT,
    situacao          TEXT,
    data_vencimento   DATE,
    observacoes       TEXT,
    numero_protocolo  TEXT,
    data_protocolo    DATE,
    created_at        TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at        TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_documentos_escola_id       ON documentos(escola_id);
CREATE INDEX IF NOT EXISTS idx_documentos_status          ON documentos(status);
CREATE INDEX IF NOT EXISTS idx_documentos_data_vencimento ON documentos(data_vencimento);


-- -----------------------------------------------------------------------------
-- 5. tipos_processo
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tipos_processo (
    id          BIGSERIAL    PRIMARY KEY,
    nome        TEXT         NOT NULL UNIQUE,
    ordem       INT          NOT NULL DEFAULT 0,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);


-- -----------------------------------------------------------------------------
-- 6. processos_sei
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS processos_sei (
    id               BIGSERIAL    PRIMARY KEY,
    escola_id        BIGINT       NOT NULL REFERENCES escolas(id) ON DELETE CASCADE,
    numero           TEXT,
    tipo_processo    TEXT,
    forma_exigencia  TEXT,
    data_recebimento DATE,
    prazo            DATE,
    status           TEXT,
    responsavel      TEXT,
    observacoes      TEXT,
    created_at       TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at       TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_processos_sei_escola_id ON processos_sei(escola_id);
CREATE INDEX IF NOT EXISTS idx_processos_sei_status    ON processos_sei(status);


-- -----------------------------------------------------------------------------
-- 7. andamentos
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS andamentos (
    id          BIGSERIAL    PRIMARY KEY,
    processo_id BIGINT       NOT NULL REFERENCES processos_sei(id) ON DELETE CASCADE,
    data        DATE,
    texto       TEXT,
    autor       TEXT,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_andamentos_processo_id ON andamentos(processo_id);


-- -----------------------------------------------------------------------------
-- 8. checklist_items
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS checklist_items (
    id          BIGSERIAL    PRIMARY KEY,
    processo_id BIGINT       NOT NULL REFERENCES processos_sei(id) ON DELETE CASCADE,
    texto       TEXT         NOT NULL,
    done        BOOLEAN      NOT NULL DEFAULT FALSE,
    obs         TEXT,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_checklist_items_processo_id ON checklist_items(processo_id);


-- -----------------------------------------------------------------------------
-- 9. tarefas
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tarefas (
    id          BIGSERIAL    PRIMARY KEY,
    titulo      TEXT         NOT NULL,
    descricao   TEXT,
    responsavel TEXT,
    escola      TEXT,
    escola_id   BIGINT       REFERENCES escolas(id) ON DELETE SET NULL,
    categoria   TEXT,
    prioridade  TEXT,
    prazo       DATE,
    status      TEXT,
    observacoes TEXT,
    criada_em   DATE         DEFAULT CURRENT_DATE,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_tarefas_escola_id ON tarefas(escola_id);
CREATE INDEX IF NOT EXISTS idx_tarefas_status    ON tarefas(status);
CREATE INDEX IF NOT EXISTS idx_tarefas_prazo     ON tarefas(prazo);


-- -----------------------------------------------------------------------------
-- 10. financeiro
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS financeiro (
    id              BIGSERIAL       PRIMARY KEY,
    descricao       TEXT            NOT NULL,
    categoria       TEXT,
    escola          TEXT,
    escola_id       BIGINT          REFERENCES escolas(id) ON DELETE SET NULL,
    orgao           TEXT,
    responsavel     TEXT,
    valor           NUMERIC(15, 2),
    data_vencimento DATE,
    data_pagamento  DATE,
    status          TEXT,
    forma_pagamento TEXT,
    observacoes     TEXT,
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_financeiro_escola_id       ON financeiro(escola_id);
CREATE INDEX IF NOT EXISTS idx_financeiro_status          ON financeiro(status);
CREATE INDEX IF NOT EXISTS idx_financeiro_data_vencimento ON financeiro(data_vencimento);


-- -----------------------------------------------------------------------------
-- 11. contatos
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS contatos (
    id               BIGSERIAL    PRIMARY KEY,
    nome             TEXT         NOT NULL,
    cargo            TEXT,
    regional         TEXT,
    escola_vinculada TEXT,
    telefone         TEXT,
    email            TEXT,
    observacoes      TEXT,
    created_at       TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at       TIMESTAMPTZ  NOT NULL DEFAULT now()
);


-- -----------------------------------------------------------------------------
-- 12. usuarios_app
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios_app (
    id          UUID         PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    nome        TEXT         NOT NULL,
    cargo       TEXT,
    email       TEXT         NOT NULL,
    setor       TEXT,
    ativo       BOOLEAN      NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now()
);


-- -----------------------------------------------------------------------------
-- 13. etaps
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS etaps (
    id               BIGSERIAL    PRIMARY KEY,
    escola_id        BIGINT       REFERENCES escolas(id) ON DELETE SET NULL,
    escola           TEXT,
    rede             TEXT,
    versao           TEXT,
    data_elaboracao  DATE,
    data_protocolo   DATE,
    numero_protocolo TEXT,
    status           TEXT,
    data_aprovacao   DATE,
    obs              TEXT,
    created_at       TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at       TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_etaps_escola_id ON etaps(escola_id);
CREATE INDEX IF NOT EXISTS idx_etaps_status    ON etaps(status);


-- -----------------------------------------------------------------------------
-- 14. etap_membros
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS etap_membros (
    id        BIGSERIAL    PRIMARY KEY,
    etap_id   BIGINT       NOT NULL REFERENCES etaps(id) ON DELETE CASCADE,
    nome      TEXT         NOT NULL,
    cargo     TEXT,
    registro  TEXT,
    art       TEXT,
    telefone  TEXT,
    email     TEXT,
    obs       TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_etap_membros_etap_id ON etap_membros(etap_id);


-- -----------------------------------------------------------------------------
-- 15. etap_publicacoes_do
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS etap_publicacoes_do (
    id               BIGSERIAL    PRIMARY KEY,
    etap_id          BIGINT       NOT NULL REFERENCES etaps(id) ON DELETE CASCADE,
    tipo             TEXT,
    data_publicacao  DATE,
    numero_do        TEXT,
    pagina           TEXT,
    link             TEXT,
    obs              TEXT,
    created_at       TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at       TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_etap_pub_do_etap_id ON etap_publicacoes_do(etap_id);


-- -----------------------------------------------------------------------------
-- 16. etap_processos_vinculados
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS etap_processos_vinculados (
    etap_id     BIGINT  NOT NULL REFERENCES etaps(id) ON DELETE CASCADE,
    processo_id BIGINT  NOT NULL REFERENCES processos_sei(id) ON DELETE CASCADE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (etap_id, processo_id)
);

CREATE INDEX IF NOT EXISTS idx_etap_proc_vinc_processo_id ON etap_processos_vinculados(processo_id);


-- -----------------------------------------------------------------------------
-- 17. auditorias
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS auditorias (
    id         BIGSERIAL    PRIMARY KEY,
    escola_id  BIGINT       REFERENCES escolas(id) ON DELETE SET NULL,
    escola     TEXT,
    rede       TEXT,
    data       DATE,
    auditor    TEXT,
    status     TEXT,
    obs_geral  TEXT,
    score      INT,
    created_at TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_auditorias_escola_id ON auditorias(escola_id);
CREATE INDEX IF NOT EXISTS idx_auditorias_status    ON auditorias(status);


-- -----------------------------------------------------------------------------
-- 18. auditoria_items
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS auditoria_items (
    id           BIGSERIAL    PRIMARY KEY,
    auditoria_id BIGINT       NOT NULL REFERENCES auditorias(id) ON DELETE CASCADE,
    cat          TEXT,
    item         TEXT,
    resultado    TEXT,
    obs          TEXT,
    created_at   TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at   TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_auditoria_items_auditoria_id ON auditoria_items(auditoria_id);


-- -----------------------------------------------------------------------------
-- 19. legislacoes
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS legislacoes (
    id            BIGSERIAL    PRIMARY KEY,
    titulo        TEXT         NOT NULL,
    orgao         TEXT,
    tipo          TEXT,
    numero        TEXT,
    data          DATE,
    ementa        TEXT,
    link_oficial  TEXT,
    arquivo_path  TEXT,
    arquivo_nome  TEXT,
    created_at    TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at    TIMESTAMPTZ  NOT NULL DEFAULT now()
);


-- -----------------------------------------------------------------------------
-- 20. modelos_anexos
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS modelos_anexos (
    id           BIGSERIAL    PRIMARY KEY,
    titulo       TEXT         NOT NULL,
    categoria    TEXT,
    versao       TEXT,
    descricao    TEXT,
    instrucoes   TEXT,
    arquivo_path TEXT,
    arquivo_nome TEXT,
    created_at   TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at   TIMESTAMPTZ  NOT NULL DEFAULT now()
);


-- =============================================================================
-- TRIGGERS: updated_at automático
-- =============================================================================

CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$;

-- Macro para criar trigger em cada tabela
DO $$
DECLARE
    t TEXT;
    tabelas TEXT[] := ARRAY[
        'redes', 'escolas', 'tipos_documentos', 'documentos',
        'tipos_processo', 'processos_sei', 'andamentos', 'checklist_items',
        'tarefas', 'financeiro', 'contatos', 'usuarios_app',
        'etaps', 'etap_membros', 'etap_publicacoes_do',
        'auditorias', 'auditoria_items', 'legislacoes', 'modelos_anexos'
    ];
BEGIN
    FOREACH t IN ARRAY tabelas LOOP
        EXECUTE format(
            'DROP TRIGGER IF EXISTS trg_%s_updated_at ON %I;
             CREATE TRIGGER trg_%s_updated_at
             BEFORE UPDATE ON %I
             FOR EACH ROW EXECUTE FUNCTION set_updated_at();',
            t, t, t, t
        );
    END LOOP;
END;
$$;


-- =============================================================================
-- ROW LEVEL SECURITY (RLS)
-- =============================================================================

-- Habilitar RLS em todas as tabelas
ALTER TABLE redes                      ENABLE ROW LEVEL SECURITY;
ALTER TABLE escolas                    ENABLE ROW LEVEL SECURITY;
ALTER TABLE tipos_documentos           ENABLE ROW LEVEL SECURITY;
ALTER TABLE documentos                 ENABLE ROW LEVEL SECURITY;
ALTER TABLE tipos_processo             ENABLE ROW LEVEL SECURITY;
ALTER TABLE processos_sei              ENABLE ROW LEVEL SECURITY;
ALTER TABLE andamentos                 ENABLE ROW LEVEL SECURITY;
ALTER TABLE checklist_items            ENABLE ROW LEVEL SECURITY;
ALTER TABLE tarefas                    ENABLE ROW LEVEL SECURITY;
ALTER TABLE financeiro                 ENABLE ROW LEVEL SECURITY;
ALTER TABLE contatos                   ENABLE ROW LEVEL SECURITY;
ALTER TABLE usuarios_app               ENABLE ROW LEVEL SECURITY;
ALTER TABLE etaps                      ENABLE ROW LEVEL SECURITY;
ALTER TABLE etap_membros               ENABLE ROW LEVEL SECURITY;
ALTER TABLE etap_publicacoes_do        ENABLE ROW LEVEL SECURITY;
ALTER TABLE etap_processos_vinculados  ENABLE ROW LEVEL SECURITY;
ALTER TABLE auditorias                 ENABLE ROW LEVEL SECURITY;
ALTER TABLE auditoria_items            ENABLE ROW LEVEL SECURITY;
ALTER TABLE legislacoes                ENABLE ROW LEVEL SECURITY;
ALTER TABLE modelos_anexos             ENABLE ROW LEVEL SECURITY;

-- -----------------------------------------------------------------------------
-- Políticas: usuários autenticados têm acesso total (SELECT/INSERT/UPDATE/DELETE)
-- Uma política ALL simplifica o SQL e é equivalente a criar 4 separadas.
-- -----------------------------------------------------------------------------

DO $$
DECLARE
    t TEXT;
    tabelas TEXT[] := ARRAY[
        'redes', 'escolas', 'tipos_documentos', 'documentos',
        'tipos_processo', 'processos_sei', 'andamentos', 'checklist_items',
        'tarefas', 'financeiro', 'contatos', 'usuarios_app',
        'etaps', 'etap_membros', 'etap_publicacoes_do', 'etap_processos_vinculados',
        'auditorias', 'auditoria_items', 'legislacoes', 'modelos_anexos'
    ];
BEGIN
    FOREACH t IN ARRAY tabelas LOOP
        EXECUTE format(
            'DROP POLICY IF EXISTS "authenticated_all" ON %I;
             CREATE POLICY "authenticated_all" ON %I
             FOR ALL
             TO authenticated
             USING (true)
             WITH CHECK (true);',
            t, t
        );
    END LOOP;
END;
$$;


-- =============================================================================
-- STORAGE BUCKETS
-- =============================================================================
-- Nota: INSERT INTO storage.buckets é a forma correta no Supabase.
-- Os buckets são criados como privados (public = false) e o acesso
-- é controlado pelas políticas abaixo (apenas usuários autenticados).

INSERT INTO storage.buckets (id, name, public)
VALUES
    ('arquivos-escolas', 'arquivos-escolas', false),
    ('legislacoes-docs',  'legislacoes-docs',  false),
    ('modelos-docs',      'modelos-docs',      false)
ON CONFLICT (id) DO NOTHING;

-- Políticas de Storage — SELECT (download)
CREATE POLICY "arquivos-escolas: authenticated select"
ON storage.objects FOR SELECT
TO authenticated
USING (bucket_id = 'arquivos-escolas');

CREATE POLICY "legislacoes-docs: authenticated select"
ON storage.objects FOR SELECT
TO authenticated
USING (bucket_id = 'legislacoes-docs');

CREATE POLICY "modelos-docs: authenticated select"
ON storage.objects FOR SELECT
TO authenticated
USING (bucket_id = 'modelos-docs');

-- Políticas de Storage — INSERT (upload)
CREATE POLICY "arquivos-escolas: authenticated insert"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (bucket_id = 'arquivos-escolas');

CREATE POLICY "legislacoes-docs: authenticated insert"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (bucket_id = 'legislacoes-docs');

CREATE POLICY "modelos-docs: authenticated insert"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (bucket_id = 'modelos-docs');

-- Políticas de Storage — UPDATE
CREATE POLICY "arquivos-escolas: authenticated update"
ON storage.objects FOR UPDATE
TO authenticated
USING (bucket_id = 'arquivos-escolas');

CREATE POLICY "legislacoes-docs: authenticated update"
ON storage.objects FOR UPDATE
TO authenticated
USING (bucket_id = 'legislacoes-docs');

CREATE POLICY "modelos-docs: authenticated update"
ON storage.objects FOR UPDATE
TO authenticated
USING (bucket_id = 'modelos-docs');

-- Políticas de Storage — DELETE
CREATE POLICY "arquivos-escolas: authenticated delete"
ON storage.objects FOR DELETE
TO authenticated
USING (bucket_id = 'arquivos-escolas');

CREATE POLICY "legislacoes-docs: authenticated delete"
ON storage.objects FOR DELETE
TO authenticated
USING (bucket_id = 'legislacoes-docs');

CREATE POLICY "modelos-docs: authenticated delete"
ON storage.objects FOR DELETE
TO authenticated
USING (bucket_id = 'modelos-docs');


-- =============================================================================
-- SEED: 10 Tipos de Documento padrão
-- =============================================================================

INSERT INTO tipos_documentos (nome, alerta_dias) VALUES
    ('Licença Sanitária',          60),
    ('Ato Autorizativo',           90),
    ('PAA',                        30),
    ('ETAP',                       30),
    ('Habite-se',                 180),
    ('Corpo de Bombeiros',         60),
    ('Alvará de Funcionamento',    60),
    ('Vigilância Sanitária',       60),
    ('Regimento Interno',         180),
    ('PPP',                        30)
ON CONFLICT (nome) DO NOTHING;


-- =============================================================================
-- FIM DO SCRIPT
-- =============================================================================
