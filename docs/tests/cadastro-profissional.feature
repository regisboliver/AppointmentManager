Funcionalidade: Cadastro de profissionais

  Como usuário
  Eu quero gerenciar os profissionais

    O cadastro de profissionais serve para listagem, inclusão, edição e exclusão de profissionais

    Cenário: Listar profissionais
      Dado que eu tenha profissionais cadastrados
      E eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de profissionais
      E acessar a opção de listar profissionais
      Então deve ser exibida uma tabela com os profissionais cadastrados

    Cenário: Incluir profissional
      Dado que eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de profissionais
      E acessar a opção de incluir profissional
      E preencher os campos do profissional
      Então o profissional deve ser cadastrado com sucesso
      E o profissional deve estar na lista de profissionais cadastrados

    Cenário: Editar profissional
      Dado que eu tenho um profissional cadastrado
      E eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de profissionais
      E acessar a opção de editar profissional
      E preencher os campos do profissional
      Então o profissional deve ser editado com sucesso
      E o profissional deve estar na lista de profissionais cadastrados com os dados atualizados

    Cenário: Excluir profissional
      Dado que eu tenho um profissional cadastrado
      E eu esteja acessando a aplicação
      Quando eu acessar o gerenciamento de profissionais
      E acessar a opção de excluir profissional
      Então o profissional deve ser excluído com sucesso
      E o profissional não deve estar na lista de profissionais cadastrados
