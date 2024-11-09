# dependencias
# pip install mysql-connector-python
# pip install pyodbc

# parametros
par_dbType = "mysql" # mysql, mssql, sqlite3
par_mysqlHost = "localhost"
par_mysqlUser = "appmgr"
par_mysqlPassword = "masterkey"
par_mysqlDatabase = "appmgr"
par_mssqlHost = "regisboliver-fatec.database.windows.net"
par_mssqlUser = "master"
par_mssqlPassword = "9mLePk^Y#2asSFfx7yl4"
par_mssqlDatabase = "pin_appmgr"
#par_sqlite3Host = "src/data/appmgr.db"
par_sqlite3Host = "appmgr.db"

def db_connection(dbType = par_dbType):

    dbData = db_data(dbType)
    print("[db_conn] db_connection_multi() - Database data:", dbData)

    match dbData["dbType"]:
        case "mysql":
            import mysql.connector
            from mysql.connector import Error
            try:
                connection = mysql.connector.connect(
                    host=     dbData["dbHost"],
                    user=     dbData["dbUser"],
                    password= dbData["dbPassword"],
                    database= dbData["dbName"]
                )
                if connection.is_connected():
                    print("[db_conn] db_connection_multi() - Successfully connected to the database (MySQL).")
                    return connection
            except Error as e:
                print(f"[db_conn] db_connection_multi() - Error while connecting to MySQL: {e}")
                return None

        case "mssql":
            import pyodbc
            try:
                connection = pyodbc.connect(
                    "Driver={SQL Server};"
                    "Server={"   + dbData["dbHost"]     + "};"
                    "UID={"      + dbData["dbUser"]     + "};"
                    "PWD={"      + dbData["dbPassword"] + "};"
                    "Database={" + dbData["dbName"]     + "};"
                )
                if connection:
                    print("[db_conn] db_connection_multi() - Successfully connected to the database (MSSQL).")
                    return connection
            except pyodbc.Error as e:
                print(f"[db_conn] db_connection_multi() - Error while connecting to MSSQL: {e}")
                return None

        case "sqlite3":
            import sqlite3
            from sqlite3 import Error
            try:
                connection = sqlite3.connect(dbData["dbHost"])
                if connection:
                    print("[db_conn] db_connection_multi() - Successfully connected to the database (SQLite3).")
                    return connection
            except sqlite3.Error as e:
                print(f"[db_conn] db_connection_multi() - Error while connecting to SQLite3: {e}")
                return None

        case _:
            return None

def db_data(dbType):
    match dbType:
        case "mysql":
            dbHost =     par_mysqlHost
            dbUser =     par_mysqlUser
            dbPassword = par_mysqlPassword
            dbName =     par_mysqlDatabase

        case "mssql":
            dbHost =     par_mssqlHost
            dbUser =     par_mssqlUser
            dbPassword = par_mssqlPassword
            dbName =     par_mssqlDatabase

        case "sqlite3":
            dbHost =     par_sqlite3Host
            dbUser =     'null'
            dbPassword = 'null'
            dbName =     'null'
        case _:
            print("[db_conn] db_data() - Invalid database type.")
            return None
    
    # dbData = (dbType, dbHost, dbUser, dbPassword, dbName)
    dbData = {"dbType": dbType, "dbHost": dbHost, "dbUser": dbUser, "dbPassword": dbPassword, "dbName": dbName}

    print("[db_conn] db_data() - Database data:", dbData)

    return dbData