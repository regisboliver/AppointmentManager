from src.utils import *
from src.data.contato import contato_listar, contato_incluir, contato_alterar, contato_excluir
from src.data.profissional import profissional_listar, profissional_incluir, profissional_alterar, profissional_excluir
from src.data.agendamentos import agendamentos_listar, agendamentos_incluir, agendamentos_alterar, agendamentos_excluir

def main_menu():
  start_menu()
  print("1. Gerenciar Contatos")
  print("2. Gerenciar Profissionais")
  print("3. Gerenciar Agendamentos")
  print("4. Sair")

  opcao = int(input("Digite a opção desejada: "))

  if opcao == 1:
    contato_menu()
  elif opcao == 2:
    profissional_menu()
  elif opcao == 3:
    agendamentos_menu()
  elif opcao == 4:
    exit()

def start_menu():
  clear_term()
  print("*** Appointment Manager ***")
  print("---------------------------")

def end_menu(current_menu):
  print("Pressione ENTER para continuar...")
  input()
  match current_menu:
    case "contato":
      contato_menu()
    case "profissional":
      profissional_menu()
    case "agendamentos":
      agendamentos_menu()

# contatos
def contato_menu():
  start_menu()
  print("Gerenciar Contatos")
  print("1. Listar Contatos")
  print("2. Incluir Contato")
  print("3. Alterar Contato")
  print("4. Excluir Contato")
  print("5. Voltar")

  opcao = int(input("Digite a opção desejada: "))

  if opcao == 1:
    contato_listar_menu()
  elif opcao == 2:
    contato_incluir_menu()
  elif opcao == 3:
    contato_alterar_menu()
  elif opcao == 4:
    contato_excluir_menu()
  elif opcao == 5:
    main_menu()

def contato_incluir_menu():
  start_menu()
  print("Por favor, insira os dados do contato:")
  nome = input("Nome: ")
  email = input("Email: ")
  telefone = input("Telefone: ")
  documento = input("Documento: ")
  contato_incluir(nome, email, telefone, documento)
  print("Contato incluído com sucesso!")
  end_menu("contato")

def contato_alterar_menu():
  start_menu()
  print("Por favor, insira os novos dados do contato:")
  documento = input("Documento: ")
  nome = input("Nome: ")
  email = input("Email: ")
  telefone = input("Telefone: ")
  contato_alterar(documento, nome, email, telefone)
  print("Contato alterado com sucesso!")
  end_menu("contato")

def contato_excluir_menu():
  start_menu()
  print("Por favor, insira o id do contato a ser excluído:")
  documento = input("Documento: ")
  contato_excluir(documento)
  print("Contato excluído com sucesso!")
  end_menu("contato")

def contato_listar_menu():
  clear_term()
  contato_listar()
  print("Contatos listados com sucesso!")
  end_menu("contato")

# profissionais
def profissional_menu():
  start_menu()
  print("Gerenciar Profissionais")
  print("1. Listar Profissionais")
  print("2. Incluir Profissional")
  print("3. Alterar Profissional")
  print("4. Excluir Profissional")
  print("5. Voltar")

  opcao = int(input("Digite a opção desejada: "))

  if opcao == 1:
    profissional_listar_menu()
  elif opcao == 2:
    profissional_incluir_menu()
  elif opcao == 3:
    profissional_alterar_menu()
  elif opcao == 4:
    profissional_excluir_menu()
  elif opcao == 5:
    main_menu()

def profissional_incluir_menu():
  start_menu()
  print("Incluir Profissional")
  nome = input("Nome: ")
  registro = input("Registro: ")
  sala = input("Sala: ")
  especialidade = input("Especialidade: ")
  profissional_incluir(nome, registro, sala, especialidade)
  print("Profissional incluído com sucesso!")
  end_menu("profissional")

def profissional_alterar_menu():
  start_menu()
  print("Alterar Profissional")
  registro = int(input("Registro: "))
  nome = input("Nome: ")
  sala = input("Sala: ")
  especialidade = input("Especialidade: ")
  profissional_alterar(registro, nome, sala, especialidade)
  print("Profissional alterado com sucesso!")
  end_menu("profissional")

def profissional_excluir_menu():
  start_menu()
  print("Excluir Profissional") 
  registro = int(input("Registro: "))
  profissional_excluir(registro)
  print("Profissional excluído com sucesso!")
  end_menu("profissional")

def profissional_listar_menu():
  clear_term()
  profissional_listar()
  print("Profissionais listados com sucesso!")
  end_menu("profissional")

# agendamentos
def agendamentos_menu():
  start_menu()
  print("Gerenciar Agendamentos")
  print("1. Listar Agendamentos")
  print("2. Incluir Agendamento")
  print("3. Alterar Agendamento")
  print("4. Excluir Agendamento")
  print("5. Voltar")

  opcao = int(input("Digite a opção desejada: "))

  if opcao == 1:
    agendamentos_listar_menu()
  elif opcao == 2:
    agendamentos_incluir_menu()
  elif opcao == 3:
    agendamentos_alterar_menu()
  elif opcao == 4:
    agendamentos_excluir_menu()
  elif opcao == 5:
    main_menu()

def agendamentos_incluir_menu():
  start_menu()
  print("Incluir Agendamento") 
  contato_id = int(input("Contato Id: ")) 
  profissional_id = int(input("Profissional Id: ")) 
  data = input("Data: ") 
  duracao = input("Duracao: ") 
  agendamentos_incluir(contato_id, profissional_id, data, duracao)
  print("Agendamento incluído com sucesso!")
  end_menu("agendamento")

def agendamentos_alterar_menu():
  start_menu()
  print("Alterar Agendamento")
  id = int(input("Id: "))
  contato_id = int(input("Contato Id: "))
  profissional_id = int(input("Profissional Id: "))
  data = input("Data: ")
  duracao = input("Duracao: ")
  agendamentos_alterar(id, contato_id, profissional_id, data, duracao)
  print("Agendamento alterado com sucesso!")
  end_menu("agendamento")

def agendamentos_excluir_menu():
  start_menu()
  print("Excluir Agendamento")
  id = int(input("Id: "))
  agendamentos_excluir(id)
  print("Agendamento excluído com sucesso!")
  end_menu("agendamento")

def agendamentos_listar_menu():
    start_menu()
    agendamentos_listar()
    print("Agendamentos listados com sucesso!")
    end_menu("agendamento")
