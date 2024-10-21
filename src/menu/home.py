from src.utils import start_menu
from src.menu.contato import *
from src.menu.profissional import *
from src.menu.agendamentos import *

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