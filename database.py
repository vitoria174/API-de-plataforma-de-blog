import mysql.connector

db = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "albuquerqu",
      database = "blog_pessoal"
        
)

cursor = db.cursor()

def create_post():
      sql = """   
            INSERT INTO Post (titulo, comentario, categoria, tags, createdata, updatedata) 
            VALUES (%s,%s,%s,%s,%s,%s)
      """
      valor = (
            'segundo post',
            'Criando post de teste',
            'Teste',
            'Aliviada',
            '2025-04-15',
            '2025-04-15'
            )
      cursor.execute(sql,valor)
      db.commit()
      
def read_post():
      cursor.execute('SELECT * FROM Post')
      resultado = cursor.fetchall()
      
      for i in resultado:
            print(i)
      