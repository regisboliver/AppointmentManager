# Appointment Manager

## Descrição

A aplicação tem o objetivo de gerenciar agendamentos. Para isso, devemos antes realizar o cadastro de contatos e profissionais.

Existe um menu onde você poderá percorrer as opções de contato, profissional e agendamentos, sendo elas: listar, incluir, alterar e excluir.

## Instalação

> É necessário ter o Python 3.12 ou superior instalado.

Para instalação do projeto, basta clonar o repositório e executar o comando `pip install -r requirements.txt`.

Verificar se os dados de acesso ao banco de dados estão corretos em `src/data/db_conn.py`, de acordo com o SGBD utilizado.

Após todas as dependências serem instaladas e informações de conexão com o banco de dados estarem corretas, basta executar o comando `python .` na raiz do projeto.

## Uso

A interface da aplicação é um menu básico que permite realizar funções como listar, incluir, alterar e excluir contatos, profissionais e agendamentos. Para isso, basta navegar pelo menu e escolher a opção desejada.

Para a criação de um agendamento, é necessário que o contato e o profissional sejam previamente cadastrados, e você deve saber o número de documento do contato e o registro do profissional.

## Contribuição

Agradecimentos ao professor Wagner Luiz de Andrade Júnior pela orientação e auxílio na construção do projeto.

## Licença

O projeto pode ser reproduzido sem restrições, desde que o autor seja citado.
