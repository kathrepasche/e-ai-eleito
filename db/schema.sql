-- E aí, Eleito? — esquema inicial (Supabase / Postgres)
-- Princípio: guardar o mínimo. Nunca registrar em quem a pessoa votou.
-- O login é feito pelo Supabase Auth (link mágico); auth.users guarda o e-mail.

create table if not exists perfis (
  id uuid primary key references auth.users(id) on delete cascade,
  nome text,
  uf char(2),
  todas_pautas boolean not null default false,
  recebe_email boolean not null default true,
  criado_em timestamptz not null default now()
);

create table if not exists politicos (
  id text primary key,            -- ex.: dep-204554, sen-5672, pres
  nome text not null,
  cargo text not null check (cargo in ('dep', 'sen', 'pres')),
  partido text,
  uf char(2),
  email text,
  telefone text,
  redes jsonb default '{}'::jsonb,
  atualizado_em timestamptz not null default now()
);

create table if not exists seguidos (
  usuario_id uuid references perfis(id) on delete cascade,
  politico_id text references politicos(id),
  desde timestamptz not null default now(),
  primary key (usuario_id, politico_id)
);

create table if not exists pautas_usuario (
  usuario_id uuid references perfis(id) on delete cascade,
  pauta text not null,
  primary key (usuario_id, pauta)
);

create table if not exists cargos_ocultos (
  usuario_id uuid references perfis(id) on delete cascade,
  cargo text not null,
  primary key (usuario_id, cargo)
);

-- Conteúdo público (o mesmo para todos)
create table if not exists votacoes (
  id text primary key,            -- ex.: camara-2440000-12
  casa text not null check (casa in ('camara', 'senado')),
  data date not null,
  descricao_oficial text,
  frase_simples text,             -- escrita com IA e revisada por uma pessoa
  o_que_muda text,
  a_favor_diz text,
  contra_diz text,
  pauta text,
  resultado text,
  nominal boolean not null default true,
  fonte text not null,
  revisado boolean not null default false
);

create table if not exists votos (
  votacao_id text references votacoes(id) on delete cascade,
  politico_id text references politicos(id),
  voto text not null check (voto in ('sim', 'nao', 'abst', 'falta', 'obstrucao', 'art17')),
  primary key (votacao_id, politico_id)
);

create table if not exists decisoes_presidente (
  id text primary key,
  data date not null,
  tipo text not null check (tipo in ('sancao', 'veto', 'mp', 'decreto')),
  frase_simples text,
  pauta text,
  votacao_id text references votacoes(id),
  fonte text not null
);

-- Segurança: cada pessoa só lê e altera os próprios dados.
alter table perfis enable row level security;
alter table seguidos enable row level security;
alter table pautas_usuario enable row level security;
alter table cargos_ocultos enable row level security;

create policy "dono_perfil" on perfis for all using (auth.uid() = id) with check (auth.uid() = id);
create policy "dono_seguidos" on seguidos for all using (auth.uid() = usuario_id) with check (auth.uid() = usuario_id);
create policy "dono_pautas" on pautas_usuario for all using (auth.uid() = usuario_id) with check (auth.uid() = usuario_id);
create policy "dono_ocultos" on cargos_ocultos for all using (auth.uid() = usuario_id) with check (auth.uid() = usuario_id);

-- Conteúdo público: leitura aberta; escrita só pelo coletor (chave de serviço).
alter table politicos enable row level security;
alter table votacoes enable row level security;
alter table votos enable row level security;
alter table decisoes_presidente enable row level security;
create policy "leitura_publica" on politicos for select using (true);
create policy "leitura_publica" on votacoes for select using (revisado);
create policy "leitura_publica" on votos for select using (true);
create policy "leitura_publica" on decisoes_presidente for select using (true);

-- Apagar a conta (LGPD): apagar o usuário em auth.users remove tudo em cascata.
