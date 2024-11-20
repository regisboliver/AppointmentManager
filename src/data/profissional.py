from prettytable import PrettyTable

from src.utils import *
from src.data.db_conn import db_connection, par_dbType
if par_dbType == "mssql": from pyodbc import Error
if par_dbType == "mysql": from mysql.connector import Error

def profissional_incluir(nome, registro, sala, especialidade):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "insert into profissional(nome, registro, sala, especialidade) values (%s, %s, %s, %s)"
        query = dbms_mark_replacer(par_dbType, query)
        values = (nome, registro, sala, especialidade)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def profissional_alterar(registro, nome, sala, especialidade):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "update profissional set nome = %s, sala = %s, especialidade = %s where registro = %s"
        query = dbms_mark_replacer(par_dbType, query)
        values = (nome, sala, especialidade, registro)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def profissional_excluir(registro):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "delete from profissional where registro = %s"
        query = dbms_mark_replacer(par_dbType, query)
        values = (registro,)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao excluir dados: {e}")
    finally:
        cursor.close()

def profissional_listar():
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "select registro, nome, sala, especialidade from profissional order by criado_em"
        cursor.execute(query)
        rows = cursor.fetchall()
        table = PrettyTable()
        table.title = "*** Appointment Manager - Profissionais ***"
        table.field_names = ["Registro", "Nome", "Sala", "Especialidade"]
        table.add_rows(rows)
        table.align = "l"
        print(table)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        cursor.close()
