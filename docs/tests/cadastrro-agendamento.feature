Funcionalidade: Cadastro de agendamentos

  Como usuário
  Eu quero gerenciar os agendamentos

    O cadastro de agendamentos serve para listagem, inclusão, edição e exclusão de agendamentos

    Cenário: Listar agendamentos
      Dado que eu tenha agendamentos cadastrados
      E eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de agendamentos
      E acessar a opção de listar agendamentos
      Então deve ser exibida uma tabela com os agendamentos cadastrados

    Cenário: Incluir agendamento
      Dado que eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de agendamentos
      E acessar a opção de incluir agendamento
      E preencher os campos do agendamento
      Então o agendamento deve ser cadastrado com sucesso
      E o agendamento deve estar na lista de agendamentos cadastrados

    Cenário: Editar agendamento
      Dado que eu tenho um agendamento cadastrado
      E eu esteja acessando a aplicação 
      Quando eu acessar o gerenciamento de agendamentos
      E acessar a opção de editar agendamento
      E preencher os campos do agendamento
      Então o agendamento deve ser editado com sucesso
      E o agendamento deve estar na lista de agendamentos cadastrados com os dados atualizados

    Cenário: Excluir agendamento
      Dado que eu tenho um agendamento cadastrado
      E eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de agendamentos
      E acessar a opção de excluir agendamento
      Então o agendamento deve ser excluído com sucesso
      E o agendamento não deve estar na lista de agendamentos cadastrados
