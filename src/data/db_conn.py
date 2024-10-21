# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

def db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='appmgr',
            password='masterkey',
            database='appmgr'
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
