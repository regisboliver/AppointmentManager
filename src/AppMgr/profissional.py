from AppMgr.data import profissional_incluir, profissional_alterar, profissional_excluir, profissional_listar

def profissional_incluir_menu():
  print("Incluir Profissional")
  nome = input("Nome: ")
  sala = input("Sala: ")
  especialidade = input("Especialidade: ")
  profissional_incluir(nome, sala, especialidade)
  print("Profissional incluído com sucesso!")

def profissional_alterar_menu():
  print("Alterar Profissional")
  id = int(input("Id: "))
  nome = input("Nome: ")
  sala = input("Sala: ")
  especialidade = input("Especialidade: ")
  profissional_alterar(id, nome, sala, especialidade)
  print("Profissional alterado com sucesso!")

def profissional_excluir_menu():
  print("Excluir Profissional") 
  id = int(input("Id: "))
  profissional_excluir(id)
  print("Profissional excluído com sucesso!")

def profissional_listar_menu():
  profissional_listar()
  print("Profissionais listados com sucesso!")