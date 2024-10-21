import os

def start_menu():
  clear_term()
  print("*** Appointment Manager ***")
  print("---------------------------")

def clear_term():
  os.system('cls' if os.name == 'nt' else 'clear')

def end_menu():
  print("Pressione ENTER para continuar...")
  input()