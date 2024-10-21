from src.data.db_conn import db_connection
from mysql.connector import Error

def profissional_incluir(nome, sala, especialidade):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "insert into profissional(nome, sala, especialidade) values (%s, %s, %s)"
        values = (nome, sala, especialidade)
        cursor.execute(query, values)
        db_connection().commit()
        print("insert OK")
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def profissional_alterar(id, nome, sala, especialidade):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "update profissional set nome = %s, sala = %s, especialidade = %s where id = %s"
        values = (nome, sala, especialidade, id)
        cursor.execute(query, values)
        db_connection().commit()
        print("update OK")
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def profissional_excluir(id):
    try:
        conn = db_connection()
        cursor = conn.cursor()
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
        conn = db_connection()
        cursor = conn.cursor()
        query = "select * from profissional"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        cursor.close()
