// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table contato {
  id char(32) [primary key, default: `UUID()`]
  criado_em timestamp [default: `CURRENT_TIMESTAMP`]
  nome varchar (50) [not null]
  email varchar (50) [not null]
  telefone varchar (20) [not null]
  documento varchar (14) [default: null]
  endereco_rua varchar (50) [default: null]
  endereco_numero varchar (10) [default: null]
  endereco_bairro varchar (50) [default: null]
  endereco_cidade varchar (50) [default: null]
  endereco_uf varchar (2) [default: null]
  endereco_cep varchar (8) [default: null]
  endereco_complemento varchar (50) [default: null]
  observacao varchar [default: null]
}

Table profissional {
  id char(32) [primary key, default: `UUID()`]
  criado_em timestamp [default: `CURRENT_TIMESTAMP`]
  nome varchar (50) [not null]
  sala varchar (20) [not null]
  especialidade varchar (20) [not null]
  indisponibilidade varchar (20)
}

Table agendamentos {
  id char(32) [primary key, default: `UUID()`]
  criado_em timestamp [default: `CURRENT_TIMESTAMP`]
  contato_id char(32) [not null]
  profissional_id char(32) [not null]
  data datetime [not null]
  duracao integer [not null]
  observacao varchar [default: null]
}

Ref: agendamentos.contato_id > contato.id

Ref: agendamentos.profissional_id > profissional.id
