# Appointment Manager

## Descrição

### Frontend

#### cadastro contato

- nome
- documento
- email
- telefone
- endereço
  - rua
  - numero
  - bairro
  - cidade
  - estado
  - cep
  - complemento
- observação
- agendamentos

#### cadastro agendamento

- contato
- data
- horário

#### acompanhamento agendamentos

- datas
- agendamentos
  - contato
  - horário

### Database

contato

- id
- nome
- documento
- email
- telefone
- endereco_rua
- endereco_numero
- endereco_bairro
- endereco_cidade
- endereco_estado
- endereco_cep
- endereco_complemento
- observacao

profissional

- id
- nome
- sala
- especialidade
- indisponibilidade

agendamentos

- id
- contato_id
- profissional_id
- data
- horario
- observacao

id
nome
documento
email
telefone
endereco_rua
endereco_numero
endereco_bairro
endereco_cidade
endereco_estado
endereco_cep
endereco_complemento
observacao