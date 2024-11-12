from src.utils import start_menu, end_menu
from src.menu.home import *
from src.data.contato import contato_incluir, contato_alterar, contato_excluir, contato_listar

def contato_incluir_menu():
  start_menu()
  print("Por favor, insira os dados do contato:")
  nome = input("Nome: ")
  email = input("Email: ")
  telefone = input("Telefone: ")
  documento = input("Documento: ")
  contato_incluir(nome, email, telefone, documento)
  print("Contato incluído com sucesso!")
  end_menu()
  contato_menu()

def contato_alterar_menu():
  start_menu()
  print("Por favor, insira os novos dados do contato:")
  id = int(input("Id: ")) 
  nome = input("Nome: ")
  email = input("Email: ")
  telefone = input("Telefone: ")
  documento = input("Documento: ")
  contato_alterar(id, nome, email, telefone, documento)
  print("Contato alterado com sucesso!")
  end_menu()
  contato_menu()

def contato_excluir_menu():
  start_menu()
  print("Por favor, insira o id do contato a ser excluído:")
  id = int(input("Id: "))
  contato_excluir(id)
  print("Contato excluído com sucesso!")
  end_menu()
  contato_menu()

def contato_listar_menu():
  start_menu()
  contato_listar()
  print("Contatos listados com sucesso!")
  end_menu()
  contato_menu()