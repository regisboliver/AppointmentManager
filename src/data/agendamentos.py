from src.data.db_conn import db_connection
from mysql.connector import Error

def agendamentos_incluir(contato_id, profissional_id, data, duracao):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "insert into agendamentos(contato_id, profissional_id, data, duracao) values (%s, %s, %s, %s)"
        values = (contato_id, profissional_id, data, duracao)
        cursor.execute(query, values)
        db_connection().commit()
        print("insert OK")
    except Error as e:
        print(f"erro ao inserir dados: {e}")
    finally:
        cursor.close()

def agendamentos_alterar(id, contato_id, profissional_id, data, duracao):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = "update agendamentos set contato_id = %s, profissional_id = %s, data = %s, duracao = %s where id = %s" 
        values = (contato_id, profissional_id, data, duracao, id)
        cursor.execute(query, values)
        db_connection().commit()
        print("update OK")
    except Error as e:
        print(f"erro ao alterar dados: {e}")
    finally:
        cursor.close()

def agendamentos_excluir(id):
    try:
        conn = db_connection()
        cursor = conn.cursor()
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
        conn = db_connection()
        cursor = conn.cursor()
        query = "select * from agendamentos"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"erro ao listar dados: {e}")
    finally:
        cursor.close()
