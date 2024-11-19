from src.data.db_conn import db_connection, par_dbType
from src.utils import *
from mysql.connector import Error
from prettytable import PrettyTable

def contato_incluir(nome, email, telefone, documento):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "insert into contato(nome, email, telefone, documento) values (%s, %s, %s, %s)"
        query = dbms_mark_replacer(par_dbType, query)
        values = (nome, email, telefone, documento)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def contato_alterar(documento, nome, email, telefone):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "update contato set nome = %s, email = %s, telefone = %s where documento = %s"
        query = dbms_mark_replacer(par_dbType, query)
        values = (nome, email, telefone, documento)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def contato_excluir(documento):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "delete from contato where documento = %s"
        query = dbms_mark_replacer(par_dbType, query)
        values = (documento)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao excluir dados: {e}")
    finally:
        cursor.close()

def contato_listar():
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "select documento, nome, email, telefone from contato order by criado_em"
        query = dbms_mark_replacer(par_dbType, query)
        cursor.execute(query)
        rows = cursor.fetchall()
        table = PrettyTable()
        table.title = "*** Appointment Manager - Contatos ***"
        table.field_names = ["Documento", "Nome", "Email", "Telefone"]
        table.add_rows(rows)
        table.align = "l"
        print(table)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        conn.close()
