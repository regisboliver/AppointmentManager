// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table contato {
  id char(36) [primary key, default: `UUID()`]
  criado_em timestamp [default: `CURRENT_TIMESTAMP`]
  modificado_em datetime [default: null]
  nome varchar (50) [not null, unique]
  email varchar (50) [not null, unique]
  telefone varchar (20) [not null, unique]
  documento varchar (14) [not null, unique]
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
  id char(36) [primary key, default: `UUID()`]
  criado_em timestamp [default: `CURRENT_TIMESTAMP`]
  modificado_em datetime [default: null]
  nome varchar (50) [not null, unique]
  registro integer [not null, unique]
  sala varchar (20) [not null]
  especialidade varchar (20) [not null]
  indisponibilidade varchar (20)
}

Table agendamentos {
  id char(36) [primary key, default: `UUID()`]
  criado_em timestamp [default: `CURRENT_TIMESTAMP`]
  modificado_em datetime [default: null]
  codigo integer [not null, unique]
  contato_id char(32) [not null]
  profissional_id char(32) [not null]
  data datetime [not null]
  duracao integer [not null]
  observacao varchar [default: null]
}

Ref: agendamentos.contato_id > contato.id

Ref: agendamentos.profissional_id > profissional.id
