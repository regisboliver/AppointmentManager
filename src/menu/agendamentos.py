from src.utils import start_menu
from src.data.agendamentos import agendamentos_incluir, agendamentos_alterar, agendamentos_excluir, agendamentos_listar

def agendamentos_incluir_menu():
  start_menu()
  print("Incluir Agendamento") 
  contato_id = int(input("Contato Id: ")) 
  profissional_id = int(input("Profissional Id: ")) 
  data = input("Data: ") 
  duracao = input("Duracao: ") 
  agendamentos_incluir(contato_id, profissional_id, data, duracao)
  print("Agendamento incluído com sucesso!")

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

def agendamentos_excluir_menu():
  start_menu()
  print("Excluir Agendamento")
  id = int(input("Id: "))
  agendamentos_excluir(id)
  print("Agendamento excluído com sucesso!")

def agendamentos_listar_menu():
  start_menu()
  agendamentos_listar()
  print("Agendamentos listados com sucesso!")