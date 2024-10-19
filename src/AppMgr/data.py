# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

def db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # change to your host
            user='pin',  # change to your username
            password='pin',  # change to your password
            database='pin'  # change to your database name
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
    
db_connection()

def contato_incluir(nome, email, telefone, documento, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_uf, endereco_cep, endereco_complemento, observacao):
    try:
        cursor = db_connection().cursor()
        query = "insert into contato(nome, email, telefone, documento, \
            endereco_rua, \
            endereco_bairro, \
            endereco_cidade, \
            endereco_uf, \
            endereco_cep, \
            endereco_complemento, \
            observacao) \
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nome, email, telefone, documento, \
            endereco_rua, \
            endereco_bairro, \
            endereco_cidade, \
            endereco_uf, \
            endereco_cep, \
            endereco_complemento, \
            observacao)
        cursor.execute(query, values)
        db_connection().commit()
        print("insert OK")
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def contato_alterar(id, nome, email, telefone, documento, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_uf, endereco_cep, endereco_complemento, observacao):
    try:
        cursor = db_connection().cursor()
        query = "update contato set nome = %s, email = %s, telefone = %s, documento = %s, \
            endereco_rua = %s, \
            endereco_numero = %s, \
            endereco_bairro = %s, \
            endereco_cidade = %s, \
            endereco_uf = %s, \
            endereco_cep = %s, \
            endereco_complemento = %s, \
            observacao = %s \
            where id = %s"
        values = (nome, email, telefone, documento, \
            endereco_rua, \
            endereco_bairro, \
            endereco_cidade, \
            endereco_uf, \
            endereco_cep, \
            endereco_complemento, \
            observacao, \
            id)
        cursor.execute(query, values)
        db_connection().commit()
        print("update OK")
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def contato_excluir(id):
    try:
        cursor = db_connection().cursor()
        query = "delete from contato where id = %s"
        values = (id,)
        cursor.execute(query, values)
        db_connection().commit()
        print("delete OK")
    except Error as e:
        print(f"erro ao excluir dados: {e}")
    finally:
        cursor.close()


## TO-DO ajustar
def contato_listar():
    try:
        cursor = db_connection().cursor()
        query = "select * from contato"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        cursor.close()

def profissional_incluir(nome, sala, especialidade, indisponibilidade):
    try:
        cursor = db_connection().cursor()
        query = "insert into profissional(nome, sala, especialidade, indisponibilidade) values (%s, %s, %s, %s)"
        values = (nome, sala, especialidade, indisponibilidade)
        cursor.execute(query, values)
        db_connection().commit()
        print("insert OK")
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def profissional_alterar(id, nome, sala, especialidade, undisponibilidade):
    try:
        cursor = db_connection().cursor()
        query = "update profissional set nome = %s, sala = %s, especialidade = %s, undisponibilidade = %s where id = %s"
        values = (nome, sala, especialidade, undisponibilidade, id)
        cursor.execute(query, values)
        db_connection().commit()
        print("update OK")
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def profissional_excluir(id):
    try:
        cursor = db_connection().cursor()
        query = "delete from profissional where id = %s"
        values = (id,)
        cursor.execute(query, values)
        db_connection().commit()
        print("delete OK")
    except Error as e:
        print(f"erro ao excluir dados: {e}")
    finally:
        cursor.close()

## TO-DO ajustar
def profissional_listar():
    try:
        cursor = db_connection().cursor()
        query = "select * from profissional"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        cursor.close()

def agendamentos_incluir(contato_id, profissional_id, data, duracao, observacao):
    try:
        cursor = db_connection().cursor()
        query = "insert into agendamentos(contato_id, profissional_id, data, duracao, observacao) values (%s, %s, %s, %s, %s)"
        values = (contato_id, profissional_id, data, duracao, observacao)
        cursor.execute(query, values)
        db_connection().commit()
        print("insert OK")
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def agendamentos_alterar(id, contato_id, profissional_id, data, duracao, observacao):
    try:
        cursor = db_connection().cursor()
        query = "update agendamentos set contato_id = %s, profissional_id = %s, data = %s, duracao = %s, observacao = %s where id = %s" 
        values = (contato_id, profissional_id, data, duracao, observacao, id)
        cursor.execute(query, values)
        db_connection().commit()
        print("update OK")
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def agendamentos_excluir(id):
    try:
        cursor = db_connection().cursor()
        query = "delete from agendamentos where id = %s"
        values = (id,)
        cursor.execute(query, values)
        db_connection().commit()
        print("delete OK")
    except Error as e:
        print(f"erro ao excluir dados: {e}")
    finally:
        cursor.close()


## TO-DO ajustar
def agendamentos_listar():
    try:
        cursor = db_connection().cursor()
        query = "select * from agendamentos"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        cursor.close()
        