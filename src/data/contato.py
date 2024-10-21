from src.data.db_conn import db_connection
from mysql.connector import Error

def contato_incluir(nome, email, telefone, documento):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "insert into contato(nome, email, telefone, documento) \
            values (%s, %s, %s, %s)"
        values = (nome, email, telefone, documento)
        cursor.execute(query, values)
        db_connection().commit()
        print("insert OK")
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def contato_alterar(id, nome, email, telefone, documento):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "update contato set nome = %s, email = %s, telefone = %s, documento = %s, \
            where id = %s"
        values = (nome, email, telefone, documento, id)
        cursor.execute(query, values)
        db_connection().commit()
        print("update OK")
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def contato_excluir(id):
    try:
        conn = db_connection()
        cursor = conn.cursor()
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
        conn = db_connection()
        cursor = conn.cursor()
        query = "select concat('- Id: ', id, ', Nome: ', nome, ', Email: ', email, ', Telefone: ', telefone, ', Documento: ', documento) from contato"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        conn.close()
