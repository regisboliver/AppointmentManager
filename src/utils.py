import os

def clear_term():
  os.system('cls' if os.name == 'nt' else 'clear')

def dbms_mark_replacer(dbType, queryText):
  match dbType:
    case "mysql":
      return queryText
    case "mssql":
      queryText = queryText.replace("%s", "?")
      return queryText
    case "sqlite3":
      return queryText
    case _:
      return "dbType não informado."
