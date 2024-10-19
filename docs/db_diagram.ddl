// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table contato {
  id integer [primary key]
  criado_em timestamp
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
  id integer [primary key]
  criado_em timestamp
  nome varchar (50) [not null]
  sala varchar (20) [not null]
  especialidade varchar (20) [not null]
  indisponibilidade varchar (20)
}

Table agendamentos {
  id integer [primary key]
  criado_em timestamp
  contato_id integer [not null]
  profissional_id integer [not null]
  data datetime [not null]
  duracao integer [not null]
  observacao varchar [default: null]
}

Ref: agendamentos.contato_id > contato.id

Ref: agendamentos.profissional_id > profissional.id
