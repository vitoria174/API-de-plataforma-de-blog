import mysql.connector

# Conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="albuquerqu",
        database="blog_pessoal"
      )
      