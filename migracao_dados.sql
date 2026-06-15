-- =============================================
-- MIGRAÇÃO: SQLite → Supabase
-- Execute no SQL Editor do Supabase (Dashboard > SQL Editor)
-- =============================================

-- 1. REDES
INSERT INTO redes (nome) VALUES
  ('QI'),
  ('QI Metropolitano'),
  ('Escolas Integradas'),
  ('Ao Cubo'),
  ('Matriz'),
  ('Global Tree'),
  ('CLV'),
  ('Americano'),
  ('União'),
  ('Raiz Educação'),
  ('Apogeu'),
  ('Outras')
ON CONFLICT DO NOTHING RETURNING id, nome;

-- 2. ESCOLAS
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI - Gabizo', (SELECT id FROM redes WHERE nome = 'QI' LIMIT 1), '86.704.160/0001-37', '0173133-5',
          'RJ', 'UNIDADE FECHADA - HOJE É MATRIZ TIJUCA', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI - Ibituruna', (SELECT id FROM redes WHERE nome = 'QI' LIMIT 1), '86.704.160/0002-18', '0163873-4',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI - Botafogo', (SELECT id FROM redes WHERE nome = 'QI' LIMIT 1), '86.704.160/0003-07', '0198388-1',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI - Freguesia', (SELECT id FROM redes WHERE nome = 'QI' LIMIT 1), '86.704.160/0005-60', '0283803-6',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI - Rio 2', (SELECT id FROM redes WHERE nome = 'QI' LIMIT 1), '86.704.160/0008-03', '1307765-7            126457-1',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI - Recreio (Escolas Integradas)', (SELECT id FROM redes WHERE nome = 'QI' LIMIT 1), '07.499.961/0001-31', '0381637-0',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI - Rio 2 Expansão', (SELECT id FROM redes WHERE nome = 'QI' LIMIT 1), '86.704.160/0013-70', '1508610-6',
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI - Freeway', (SELECT id FROM redes WHERE nome = 'QI' LIMIT 1), '86.704.160/0014-51', '1549784-0',
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI Metropolitano - Lopes 72', (SELECT id FROM redes WHERE nome = 'QI Metropolitano' LIMIT 1), '33.590.308/0001-93', '0002365-5',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI Metropolitano - Jacinto 81', (SELECT id FROM redes WHERE nome = 'QI Metropolitano' LIMIT 1), '33.590.308/0002-74', '0002366-3',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('QI Recreio', (SELECT id FROM redes WHERE nome = 'Escolas Integradas' LIMIT 1), '07.499.961/0001-31', '0381637-0',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Konder', (SELECT id FROM redes WHERE nome = 'Escolas Integradas' LIMIT 1), '07.499.961/0002-12', '1350706-6',
          'RJ', 'UNIDADE FECHADA', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Sá Pereira', (SELECT id FROM redes WHERE nome = 'Escolas Integradas' LIMIT 1), '07.499.961/0003-01', '1162455-3',
          'RJ', 'Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Capistrano', (SELECT id FROM redes WHERE nome = 'Escolas Integradas' LIMIT 1), '07.499.961/0006-46', '0039249-9',
          'RJ', 'Creche e Educação Infantil', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('SAP', (SELECT id FROM redes WHERE nome = 'Escolas Integradas' LIMIT 1), '07.499.961/0007-27', '1269447-4 - Inscrição Principal',
          'RJ', 'Educação Infantil, Ensino Fundamental, Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Cubo Global Bosque Marapendi', (SELECT id FROM redes WHERE nome = 'Ao Cubo' LIMIT 1), '23.075.186/0002-24', '667511-5',
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Ao Cubo Botafogo', (SELECT id FROM redes WHERE nome = 'Ao Cubo' LIMIT 1), '23.075.186/0005-77', '12683162',
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Ao Cubo Barra I - Rodolfo Amoedo', (SELECT id FROM redes WHERE nome = 'Ao Cubo' LIMIT 1), '23.075.186/0002-24', '0667511-5;        1275256-3 (verificar)',
          'RJ', 'UNIDADE FECHADA - TRANSFERIDA PARA ABM', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Ao Cubo Ipanema', (SELECT id FROM redes WHERE nome = 'Ao Cubo' LIMIT 1), '23.075.186/0003-05', '10224020',
          'RJ', 'UNIDADE FECHADA', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Ao Cubo Tijuca (Professor Gabizo)', (SELECT id FROM redes WHERE nome = 'Ao Cubo' LIMIT 1), '23.075.186/0004-96', '1026699-8',
          'RJ', 'UNIDADE FECHADA', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Ao Cubo (Professor Gabizo)', (SELECT id FROM redes WHERE nome = 'Ao Cubo' LIMIT 1), '23.075.186/0001-43', '0661292-0 (José Higino 276)',
          'RJ', 'UNIDADE FECHADA', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Ao Cubo Recreio', (SELECT id FROM redes WHERE nome = 'Ao Cubo' LIMIT 1), '23.075.186/0006-58', '14731741',
          'RJ', 'UNIDADE FECHADA', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Ao Cubo (Sede Freeway)', (SELECT id FROM redes WHERE nome = 'Ao Cubo' LIMIT 1), '23.075.186/0009-09', '1553808-2',
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Rocha Miranda', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0001-54', '1389810-3',
          'RJ', 'Fundamental II; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Campo Grande', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0002-35', '1269448-2',
          'RJ', 'Fundamental II; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Nova Iguaçu', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0003-16', '592242',
          'RJ', 'Fundamental II; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Bangu', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0004-05', '1269451-2',
          'RJ', 'Fundamental II; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Caxias', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0006-69', '28336302000669',
          'RJ', 'Fundamental II; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Taquara', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0005-88', '1151686-6',
          'RJ', 'Fundamental II; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - São João de Meriti', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0008-20', '20202202127',
          'RJ', 'Fundamental II; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Madureira', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0009-01', 'Não Possui',
          'RJ', 'Fundamental II; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Retiro dos Artistas', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0010-45', '1565868-1',
          'RJ', 'Ensino Fundamental; Ensino Médio e Pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Tijuca', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0012-07', '1565074-5',
          'RJ', 'Fundamental II (9º ano), Ensino Médio e pré-vestibular', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz - Sede Administrativa Freeway', (SELECT id FROM redes WHERE nome = 'Matriz' LIMIT 1), '28.336.302/0013-98', '1548899-9',
          'RJ', 'Não se aplica', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree - Rio 2', (SELECT id FROM redes WHERE nome = 'Global Tree' LIMIT 1), '28.734.505/0001-07', '1075111-0',
          'RJ', 'Creche e pré-escola', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree - Recreio', (SELECT id FROM redes WHERE nome = 'Global Tree' LIMIT 1), '28.734.505/0002-80', '1267362-0',
          'RJ', 'Creche e pré-escola', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree - Rio 2 anexo', (SELECT id FROM redes WHERE nome = 'Global Tree' LIMIT 1), '28.734.505/0003-60', 'Não possui',
          'RJ', 'Creche e pré-escola', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree -  Península', (SELECT id FROM redes WHERE nome = 'Global Tree' LIMIT 1), '28.734.505/0004-41', '1428216-5',
          'RJ', 'Creche e pré-escola', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree - ABM', (SELECT id FROM redes WHERE nome = 'Global Tree' LIMIT 1), '28.734.505/0005-22', 'Não possui',
          'RJ', 'Creche e pré-escola', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree - Sede Administrativa Freeway', (SELECT id FROM redes WHERE nome = 'Global Tree' LIMIT 1), '28.734.505/0006-03', '1553585-7',
          'RJ', 'Não se aplica', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('ALFA - IPA', (SELECT id FROM redes WHERE nome = 'CLV' LIMIT 1), '09.262.835/0001-94', '23641320',
          'MG', '1.Educação Infantil
2.Ensino Fundamental Anos Iniciais
3.Ensino Fundamental Anos Finais
4.Ensino Médio
5.Turno Integral Bilíngue', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('BETA', (SELECT id FROM redes WHERE nome = 'CLV' LIMIT 1), '09.262.835/0002-75', '51506726',
          'MG', '1.Educação Infantil
2.Ensino Fundamental Anos Iniciais
3.Ensino Fundamental Anos Finais
4.Ensino Médio
5.Turno Integral Bilíngue', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('GAMA', (SELECT id FROM redes WHERE nome = 'CLV' LIMIT 1), '38.376.734/0001-42 (CILV)', '6900210',
          'MG', '1.Educação Infantil
2.Ensino Fundamental Anos Iniciais
3.Ensino Fundamental Anos Finais
4.Ensino Médio
5.Turno Integral Bilíngue', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz', (SELECT id FROM redes WHERE nome = 'Americano' LIMIT 1), '58.232.918/0001-46', '87640520',
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz', (SELECT id FROM redes WHERE nome = 'União' LIMIT 1), '58.241.128/0001-27', NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('CSC RIO', (SELECT id FROM redes WHERE nome = 'Raiz Educação' LIMIT 1), '21.219.576/0001-14', '1028824-0',
          'RJ', 'CSC', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('CSC JF', (SELECT id FROM redes WHERE nome = 'Raiz Educação' LIMIT 1), '21.219.576/0002-03', '208.727/00-0',
          'RJ', 'CSC', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('APOGEU ESPACO MAGICO', (SELECT id FROM redes WHERE nome = 'Apogeu' LIMIT 1), '25.788.092/0001-47', '51964007.0',
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('APOGEU SANTO ANTÔNIO I', (SELECT id FROM redes WHERE nome = 'Apogeu' LIMIT 1), '25.788.092/0002-28', '185258000.0',
          'MG', '1. Ensino Fundamental           2. Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('APOGEU BENFICA', (SELECT id FROM redes WHERE nome = 'Apogeu' LIMIT 1), '25.788.092/0003-09', '185260004.0',
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('APOGEU SANTO ANTÔNIO II', (SELECT id FROM redes WHERE nome = 'Apogeu' LIMIT 1), '25.788.092/0004-90', '185261000.0',
          'MG', '1. Ensino Médio                                 2. Curso pré-vestibular            3. Preparatório militar', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('APOGEU JARDIM NORTE', (SELECT id FROM redes WHERE nome = 'Apogeu' LIMIT 1), '25.788.092/0005-70', '185263003.0',
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('CENTRO EDUCACIONAL ESPAÇO MÁGICO', (SELECT id FROM redes WHERE nome = 'Apogeu' LIMIT 1), '25.788.092/0006-51', '192912003.0',
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('APOGEU CIDADE ALTA', (SELECT id FROM redes WHERE nome = 'Apogeu' LIMIT 1), '25.788.092/0007-32', '890245649.0',
          'MG', '1. Educação infantil (maternal à pré escola II)        2. Ensino Fundamental             3. Ensino Médio (1ª série apenas)', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('REDE DE ENSINO APOGEU LTDA', (SELECT id FROM redes WHERE nome = 'Apogeu' LIMIT 1), '25.788.092/0008-13', NULL,
          'MG', '1. Berçario                                   2. Ensino Infantil                         3. Ensino Fundamental            4.Ensino Médio', NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Apogeu Espaço Mágico', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Apogeu Global School', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Apogeu Santo Antônio I', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Apogeu Santo Antônio II', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Apogeu Zona Norte', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Saber Mais (Sarah Dawsey JF)', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'MG', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Bom Tempo', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Cubo Global School Barra', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Cubo Global School Botafogo', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree Barra Marapendi', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree Barra Península', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree Recreio', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Global Tree Rio 2', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Taquara', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz São João de Meriti', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Rocha Miranda', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Nova Iguaçu', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Madureira', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Caxias', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Campo Grande', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Bangu', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Tijuca', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Matriz Retiro dos Artistas', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Qi Botafogo', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Qi Freguesia', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Qi Rio 2', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Qi Tijuca', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RJ', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Americano', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RS', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('CLV Alfa', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RS', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('CLV Beta', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RS', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('CLV Gama', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RS', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('União', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RS', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Unificado Ramiro', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RS', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;
INSERT INTO escolas (nome, rede_id, cnpj, inscricao_municipal, estado, o_que_funciona, observacoes, ativa)
  VALUES ('Unificado Zona Sul', (SELECT id FROM redes WHERE nome = 'Outras' LIMIT 1), NULL, NULL,
          'RS', NULL, NULL, TRUE)
ON CONFLICT DO NOTHING;

-- 3. TIPOS DE DOCUMENTOS
INSERT INTO tipos_documentos (nome, alerta_dias) VALUES
  ('Licença Sanitária', 60),
  ('Ato Autorizativo - Sec. Educação', 365),
  ('PAA', 365),
  ('ETAP', 365),
  ('Habite-se', 60),
  ('Corpo de Bombeiros', 365),
  ('Alvará de Funcionamento', 365),
  ('Vigilância Sanitária', 365),
  ('Regimento Interno', 365),
  ('PPP', 365)
ON CONFLICT (nome) DO NOTHING;

-- 4. DOCUMENTOS
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Gabizo' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim.                   Vencimento: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Gabizo' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'ok', NULL, 'Sim')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Gabizo' LIMIT 1), 'PAA',
          'pendente', NULL, 'Não')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Gabizo' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Ibituruna' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim.                   Vencimento: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Ibituruna' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2011-03-29', 'Sim, publicado no DO de 29/03/2011 para ensino fundamental')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Ibituruna' LIMIT 1), 'PAA',
          'ok', NULL, 'Sim')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Ibituruna' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Botafogo' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim.                   Vencimento: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Botafogo' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2010-10-01', 'Sim. Autorização para Ensino Fundamental do 6º ao 9º publicado no DO em 01/10/2010.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Botafogo' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Botafogo' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Freguesia' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim.                   Vencimento: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Freguesia' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2023-07-11', 'Sim. Autorização para Ensino Fundamental e Ensino Médio publicado no DO em 11/07/2023.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Freguesia' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Freguesia' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Rio 2' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim.                   Vencimento: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Rio 2' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'a_vencer', NULL, 'Tem parecer autorizativo para Ensino Fundamental emitido em 01/04/2024. Aguardando publicação em DO')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Rio 2' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Rio 2' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Recreio (Escolas Integradas)' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim.                   Vencimento: 30/04/2025 na IM: 12716982')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Recreio (Escolas Integradas)' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2010-06-23', 'Sim. Ensino fundamental publicado em 23/06/2010 e Ensino Fundamental anos finais e Ensino Médio publicado em 04/12/2007.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Recreio (Escolas Integradas)' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Recreio (Escolas Integradas)' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Rio 2 Expansão' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim.                   Vencimento: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Rio 2 Expansão' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Rio 2 Expansão' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Rio 2 Expansão' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Freeway' LIMIT 1), 'Licença Sanitária',
          'pendente', NULL, 'Não possui')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Freeway' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Freeway' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI - Freeway' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Lopes 72' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Vencimento em 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Lopes 72' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Lopes 72' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Lopes 72' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Jacinto 81' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Vencimento em 30/04/2025 na IM : 23671')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Jacinto 81' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Jacinto 81' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Jacinto 81' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Recreio' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Vencimento em 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Recreio' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2010-06-23', 'Sim. Ensino fundamental publicado em 23/06/2010 e Ensino Fundamental anos finais e Ensino Médio publicado em 04/12/2007.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Recreio' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'QI Recreio' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Konder' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Konder' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Konder' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Konder' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Sá Pereira' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Vencimento em 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Sá Pereira' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2022-02-17', 'Sim. Ensino Médio com parecer favorável emitido em 17/02/2022. Fundamental I  e II com parecer favorável em 17/02/2022')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Sá Pereira' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Sá Pereira' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Capistrano' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Vencimento em 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Capistrano' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2024-09-16', 'Sim, o parecer de funcionamento é antigo e possui, publicado no DO, a alteração de mantença para Escolas Integradas em 16/09/2024')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Capistrano' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Capistrano' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'SAP' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Vencimento em 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'SAP' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2022-03-17', 'Sim. Fundamental I e II publicado no DO em 17/03/2022')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'SAP' LIMIT 1), 'PAA',
          'ok', NULL, 'Sim, desde 2024')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'SAP' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Cubo Global Bosque Marapendi' LIMIT 1), 'Licença Sanitária',
          'pendente', NULL, 'Não possui')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Cubo Global Bosque Marapendi' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, 'Está com processo de alteração de endereço na SEEDUC')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Cubo Global Bosque Marapendi' LIMIT 1), 'PAA',
          'ok', NULL, 'Sim, desde 2023')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Cubo Global Bosque Marapendi' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Botafogo' LIMIT 1), 'Licença Sanitária',
          'ok', NULL, 'Sim. Vencimento em 30/04/25')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Botafogo' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, 'O parecer favorável é do endereço Bambina, 126 para Ensino Médio e Fundamental.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Botafogo' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Botafogo' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Barra I - Rodolfo Amoedo' LIMIT 1), 'Licença Sanitária',
          'ok', NULL, 'Sim. Vencimento em 30/04/25 na IM 6675115')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Barra I - Rodolfo Amoedo' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Barra I - Rodolfo Amoedo' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Barra I - Rodolfo Amoedo' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Ipanema' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Ipanema' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Ipanema' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Ipanema' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Tijuca (Professor Gabizo)' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Tijuca (Professor Gabizo)' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Tijuca (Professor Gabizo)' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Tijuca (Professor Gabizo)' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo (Professor Gabizo)' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo (Professor Gabizo)' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo (Professor Gabizo)' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo (Professor Gabizo)' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Recreio' LIMIT 1), 'Licença Sanitária',
          'ok', NULL, 'Sim. Vencimento em 30/04/25')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Recreio' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Recreio' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo Recreio' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo (Sede Freeway)' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo (Sede Freeway)' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo (Sede Freeway)' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Ao Cubo (Sede Freeway)' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Rocha Miranda' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Validade: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Rocha Miranda' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'pendente', NULL, 'Não. Ato autorizativo é de 1970 e o processo de transferência de mantença não saiu')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Rocha Miranda' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Rocha Miranda' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Campo Grande' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Validade: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Campo Grande' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'a_vencer', NULL, 'Parecer favorável de Ensino Fundamental anos finais e médio aguardando liberação do alvará')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Campo Grande' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Campo Grande' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Nova Iguaçu' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-03-19', 'Sim. Validade: 19/03/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Nova Iguaçu' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2023-06-19', 'Sim, ato de 19/06/2023 para ensino fundamental anos finais.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Nova Iguaçu' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Nova Iguaçu' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Bangu' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Validade: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Bangu' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'ok', NULL, 'Sim, ato de 9/12/2019 autorizando ensino fundamental anos finais e ensino médio.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Bangu' LIMIT 1), 'PAA',
          'ok', NULL, 'Sim')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Bangu' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Caxias' LIMIT 1), 'Licença Sanitária',
          'pendente', NULL, 'Não possui')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Caxias' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2023-03-06', 'Sim,  publicado no DO de 06/03/2023 autorizando ensino fundamental anos iniciais.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Caxias' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Caxias' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Taquara' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Validade: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Taquara' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2023-06-19', 'Sim, publicado no DO em 19/06/2023 autorização para ensino fundamental anos finais e médio.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Taquara' LIMIT 1), 'PAA',
          'ok', NULL, 'Sim.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Taquara' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - São João de Meriti' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, 'Tem processo para certidão de 2023.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - São João de Meriti' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2021-11-29', 'Sim, publicado em DO em 29/11/2021 para oferta de ensino médio')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - São João de Meriti' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - São João de Meriti' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Madureira' LIMIT 1), 'Licença Sanitária',
          'pendente', NULL, 'Não possui')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Madureira' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2024-03-15', 'Sim, publicado em 15/03/2024 para oferta de ensino fundamental anos finais e ensino médio.')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Madureira' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Madureira' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Retiro dos Artistas' LIMIT 1), 'Licença Sanitária',
          'vencido', '2026-04-30', 'Sim. Vencimento em 30/04/2026')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Retiro dos Artistas' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, 'Em processo')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Retiro dos Artistas' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Retiro dos Artistas' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Tijuca' LIMIT 1), 'Licença Sanitária',
          'vencido', '2026-04-30', 'Sim. Vencimento em 30/04/2026')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Tijuca' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, 'Em processo')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Tijuca' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Tijuca' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Sede Administrativa Freeway' LIMIT 1), 'Licença Sanitária',
          'pendente', NULL, 'Não Possui')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Sede Administrativa Freeway' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Sede Administrativa Freeway' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz - Sede Administrativa Freeway' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Rio 2' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Validade: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Rio 2' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2018-09-21', 'Sim, parecer favorável de 21/09/2018')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Rio 2' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Rio 2' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Recreio' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Validade: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Recreio' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2019-12-09', 'Sim, publicado no DO em 09/12/2019 na modalidade creche e pré-escola')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Recreio' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Recreio' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Rio 2 anexo' LIMIT 1), 'Licença Sanitária',
          'pendente', NULL, 'Não possui')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Rio 2 anexo' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Rio 2 anexo' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Rio 2 anexo' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree -  Península' LIMIT 1), 'Licença Sanitária',
          'vencido', '2025-04-30', 'Sim. Validade: 30/04/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree -  Península' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'vencido', '2023-09-19', 'Sim, parecer autorizativo de 19/09/2023')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree -  Península' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree -  Península' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - ABM' LIMIT 1), 'Licença Sanitária',
          'pendente', NULL, 'Não possui')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - ABM' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, 'Em processo na SEEDUC')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - ABM' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - ABM' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Sede Administrativa Freeway' LIMIT 1), 'Licença Sanitária',
          'pendente', NULL, 'Não possui')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Sede Administrativa Freeway' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Sede Administrativa Freeway' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Global Tree - Sede Administrativa Freeway' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'ALFA - IPA' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'ALFA - IPA' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'ALFA - IPA' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'ALFA - IPA' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'BETA' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, 'Vencido desde 2019')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'BETA' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'BETA' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'BETA' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'GAMA' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'GAMA' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'GAMA' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'GAMA' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CSC RIO' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, 'Em processo de licença - Deverá ser concluído até 24/03/2025')
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CSC RIO' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CSC RIO' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CSC RIO' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CSC JF' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CSC JF' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CSC JF' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CSC JF' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU ESPACO MAGICO' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU ESPACO MAGICO' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU ESPACO MAGICO' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU ESPACO MAGICO' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU SANTO ANTÔNIO I' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU SANTO ANTÔNIO I' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU SANTO ANTÔNIO I' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU SANTO ANTÔNIO I' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU BENFICA' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU BENFICA' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU BENFICA' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU BENFICA' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU SANTO ANTÔNIO II' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU SANTO ANTÔNIO II' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU SANTO ANTÔNIO II' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU SANTO ANTÔNIO II' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU JARDIM NORTE' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU JARDIM NORTE' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU JARDIM NORTE' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU JARDIM NORTE' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CENTRO EDUCACIONAL ESPAÇO MÁGICO' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CENTRO EDUCACIONAL ESPAÇO MÁGICO' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CENTRO EDUCACIONAL ESPAÇO MÁGICO' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'CENTRO EDUCACIONAL ESPAÇO MÁGICO' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU CIDADE ALTA' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU CIDADE ALTA' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU CIDADE ALTA' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'APOGEU CIDADE ALTA' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'REDE DE ENSINO APOGEU LTDA' LIMIT 1), 'Licença Sanitária',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'REDE DE ENSINO APOGEU LTDA' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'REDE DE ENSINO APOGEU LTDA' LIMIT 1), 'PAA',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'REDE DE ENSINO APOGEU LTDA' LIMIT 1), 'ETAP',
          'desconhecido', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz Retiro dos Artistas' LIMIT 1), 'Habite-se',
          'a_vencer', NULL, NULL)
ON CONFLICT DO NOTHING;
INSERT INTO documentos (escola_id, tipo, status, data_vencimento, observacoes)
  VALUES ((SELECT id FROM escolas WHERE nome = 'Matriz Retiro dos Artistas' LIMIT 1), 'Ato Autorizativo - Sec. Educação',
          'a_vencer', NULL, NULL)
ON CONFLICT DO NOTHING;

-- 5. PROCESSOS SEI
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 120001/012188/2021', (SELECT id FROM escolas WHERE nome = 'QI - Recreio (Escolas Integradas)' LIMIT 1), 'Oficio 00.40/2025 - exigências',
          'recebido por email em 14/04/2025 às 14:34', 'Solicitamos dilação de prazo em 24/04 por e-mail e 29/04 por oficio', 'aberto', 'Responder  em 16/04')
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030038/006324/2023', (SELECT id FROM escolas WHERE nome = 'QI - Recreio (Escolas Integradas)' LIMIT 1), 'exigência',
          'recebido por email em 01/04/2025 às 17:36', 'Enviado resposta em 13/05 solicitando 15 dias para resposta.', 'cumprido', 'responder até 23/04')
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030001/063541/2024', NULL, 'E-mail com exigência',
          'recebido por e-mail em 27/03/2025 às 09:57', 'respondido em 24/04 por e-mail', 'cumprido', NULL)
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030001/049892/2024', NULL, 'E-mail com exigência',
          'recebido por e-mail em 27/03/2025 às 09:08', 'e-mail solicitando prorrogação de prazo em 25/04', 'aberto', 'responder até 16/04')
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030001/037451/2024', NULL, 'E-mail com exigência',
          'recebido por e-mail em 26/03/2025 às 11:26', 'respondido em 04/04 por e-mail com a documentação', 'cumprido', NULL)
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 12001/012188/2021', (SELECT id FROM escolas WHERE nome = 'QI - Recreio (Escolas Integradas)' LIMIT 1), 'Oficio 026/2025',
          'recebido por e-mail em 26/03/2025 às 08:00', 'Prazo de 10 dias - Cumprido em 04/04/2025 às 19:08', 'cumprido', NULL)
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030001/072843/2024', (SELECT id FROM escolas WHERE nome = 'QI - Recreio (Escolas Integradas)' LIMIT 1), 'E-mail com indeferimento',
          'recebido por e-mail em 30/01/2025', 'Precisamos ver o que trata e protocolar novamente', 'aberto', 'Processo Matriz - Retiro')
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030001/054140/2024', (SELECT id FROM escolas WHERE nome = 'Matriz Taquara' LIMIT 1), 'ETAP - Email com exigência',
          'recebido por e-mail em 13/11/2024 às 21:26', 'Questionamento em 21/11/2024 às 12:11', 'aberto', NULL)
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030001/038302/2024', (SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Lopes 72' LIMIT 1), NULL,
          'Cadeia de e-mail de 22/11/2024 às 13:14', 'Não há e-mail com exigÊncia. Precisamos retomar o processo', 'aberto', 'Responder até 30/05')
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030001/057170/2024', (SELECT id FROM escolas WHERE nome = 'QI Metropolitano - Lopes 72' LIMIT 1), 'E-mail com exigência',
          'recebido por e-mail em 02/12/2024 às 16:20', 'Não há e-mail com exigÊncia. Precisamos retomar o processo', 'aberto', 'Verificar se está arquivado e pedir o desarquivamento com os documentos até 30/05')
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030038/004995/2023', NULL, 'e-mail com exigência',
          'recebido por e-mail em 24/03/2025', 'cumprido por email em 27/03/2025 às 15:11', 'cumprido', NULL)
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('Processo SEI 030001/073867/2024', (SELECT id FROM escolas WHERE nome = 'QI - Gabizo' LIMIT 1), 'e-mail com exigência',
          'recebido por e-mail em 07/05/2025', 'Cumprir exigência até 30/05/2025', 'aberto', 'email enviado em 05/06/2025.')
ON CONFLICT DO NOTHING;
INSERT INTO processos_sei (numero, escola_id, forma_exigencia, data_recebimento, prazo, status, observacoes)
  VALUES ('SEI-030001/058320/2024', (SELECT id FROM escolas WHERE nome = 'Ao Cubo Botafogo' LIMIT 1), 'e-mail com exigência',
          'recebido por e-mail em 29/05/2025', 'email enviado em 05/06/2025 solicitando acesso ao processo', 'cumprido', 'Aguardar retorno até 16/06/2025')
ON CONFLICT DO NOTHING;

-- 6. TIPOS DE PROCESSO
INSERT INTO tipos_processo (nome, ordem) VALUES
  ('Autorização de Funcionamento', 1),
  ('Renovação de Autorização', 2),
  ('Renovação de Alvará', 3),
  ('Renovação — Licença Sanitária', 4),
  ('AVCB — Corpo de Bombeiros', 5),
  ('Laudo Técnico CREA', 6),
  ('Habite-se', 7),
  ('Transferência de Mantenedora', 8),
  ('Recredenciamento MEC', 9),
  ('Censo Escolar INEP', 10),
  ('Regularização Fiscal', 11),
  ('Processo Administrativo', 12),
  ('Outro', 13)
ON CONFLICT DO NOTHING;

-- 7. USUÁRIO PADRÃO DA PLATAFORMA
-- Execute após criar o usuário no Supabase Authentication:
INSERT INTO usuarios_app (nome, cargo, email, setor, ativo)
  VALUES ('Brunna Miranda', 'Gestora Regulatória', 'brunna@raiz.edu.br', 'Regulatório', TRUE)
ON CONFLICT DO NOTHING;

-- =============================================
-- MIGRAÇÃO CONCLUÍDA
-- 12 redes | 89 escolas | 222 documentos | 13 processos
-- =============================================