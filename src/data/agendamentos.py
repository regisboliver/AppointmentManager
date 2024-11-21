from datetime import datetime
from prettytable import PrettyTable

from src.utils import *
from src.data.db_conn import db_connection, par_dbType
if par_dbType == "mssql": from pyodbc import Error
if par_dbType == "mysql": from mysql.connector import Error

def agendamentos_incluir(contato_doc, profissional_registro, data, hora, duracao):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        contato_id = contato_buscar_id(contato_doc)
        profissional_id = profissional_buscar_id(profissional_registro)
        codigo = agendamentos_buscar_ultimo_codigo() + 1
        date = datetime.strptime(data + " " + hora, "%d/%m/%Y %H:%M")
        date = date.strftime("%Y-%m-%d %H:%M:00")
        query = "insert into agendamentos (codigo, contato_id, profissional_id, data, duracao) values (%s, %s, %s, %s, %s)"
        query = dbms_mark_replacer(par_dbType, query)
        values = (codigo, contato_id, profissional_id, date, duracao)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def agendamentos_alterar(codigo, contato_doc, profissional_registro, data, hora, duracao):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        contato_id = contato_buscar_id(contato_doc)
        profissional_id = profissional_buscar_id(profissional_registro)
        date = datetime.strptime(data + " " + hora, "%d/%m/%Y %H:%M")
        date = date.strftime("%Y-%m-%d %H:%M:00")
        query = "update agendamentos set contato_id = %s, profissional_id = %s, data = %s, duracao = %s where codigo = %s"
        query = dbms_mark_replacer(par_dbType, query)
        values = (contato_id, profissional_id, date, duracao, codigo)
        print('var values: ', values)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def agendamentos_excluir(codigo):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "delete from agendamentos where codigo = %s"
        query = dbms_mark_replacer(par_dbType, query)
        values = (codigo,)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"erro ao excluir dados: {e}")
    finally:
        cursor.close()

def agendamentos_listar():
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "select format(a.data, 'dd/MM/yyyy HH:mm') \"data\", concat(a.duracao, ' minutos') \"duracao\", concat('#', a.codigo) \"codigo\", c.nome \"paciente\", p.nome \"profissional\" \
                from agendamentos a \
                inner join profissional p on a.profissional_id = p.id \
                inner join contato c on a.contato_id = c.id \
                where a.data >= dateadd(hour, -3, getdate()) \
                order by a.data, a.codigo;"
        cursor.execute(query)
        rows = cursor.fetchall()
        table = PrettyTable()
        table.title = "*** Appointment Manager - Agendamentos ***"
        table.field_names = ["Data", "Duracao", "Codigo", "Paciente", "Profissional"]
        table.add_rows(rows)
        table.align = "l"
        print(table)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        cursor.close()

def contato_buscar_id(contato_doc):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "select id from contato where documento = %s"
        query = dbms_mark_replacer(par_dbType, query)
        values = (contato_doc,)
        cursor.execute(query, values)
        row = cursor.fetchone()
        return row[0]
    except Error as e:
        print(f"erro ao buscar dados: {e}")
    finally:
        cursor.close()

def profissional_buscar_id(profissional_registro):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "select id from profissional where registro = %s"
        query = dbms_mark_replacer(par_dbType, query)
        values = (profissional_registro,)
        cursor.execute(query, values)
        row = cursor.fetchone()
        return row[0]
    except Error as e:
        print(f"erro ao buscar dados: {e}")
    finally:
        cursor.close()

def agendamentos_buscar_ultimo_codigo():
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "select max(codigo) from agendamentos"
        cursor.execute(query)
        row = cursor.fetchone()
        return row[0]
    except Error as e:
        print(f"erro ao buscar dados: {e}")
    finally:
        cursor.close()