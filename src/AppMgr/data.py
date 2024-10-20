from AppMgr.db_conn import db_connection

def contato_incluir(nome, email, telefone, documento):
    try:
        cursor = db_connection().cursor()
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
        cursor = db_connection().cursor()
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

def profissional_incluir(nome, sala, especialidade):
    try:
        cursor = db_connection().cursor()
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
        cursor = db_connection().cursor()
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

def agendamentos_incluir(contato_id, profissional_id, data, duracao):
    try:
        cursor = db_connection().cursor()
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
        cursor = db_connection().cursor()
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
        