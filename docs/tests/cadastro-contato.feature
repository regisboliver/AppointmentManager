Funcionalidade: Cadastro de contatos

  Como usuário
  Eu quero gerenciar os contatos

    O cadastro de contatos serve para listagem, inclusão, edição e exclusão de contatos

    Cenário: Listar contatos
      Dado que eu tenho contatos cadastrados
      E eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de contatos
      E acessar a opção de listar contatos
      Então deve ser exibida uma tabela com os contatos cadastrados

    Cenário: Incluir contato
      Dado que eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de contatos
      E acessar a opção de incluir contato
      E preencher os campos do contato
      Então o contato deve ser cadastrado com sucesso
      E o contato deve estar na lista de contatos cadastrados

    Cenário: Editar contato
      Dado que eu tenho um contato cadastrado
      E eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de contatos
      E acessar a opção de editar contato
      E preencher os campos do contato
      Então o contato deve ser editado com sucesso
      E o contato deve estar na lista de contatos cadastrados com os dados atualizados

    Cenário: Excluir contato
      Dado que eu tenho um contato cadastrado
      E eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de contatos
      E acessar a opção de excluir contato
      Então o contato deve ser excluído com sucesso
      E o contato não deve estar na lista de contatos cadastrados
