from datetime import date

data = date.today()
print(data)
lista_post =[
      {     'id':1,
            'data':str(data),
            'titulo':'post',
            'descricao':'Primeiro post ',
            'tag':'api''flask'
      },
      {
            'id':2,
            'data':'2025-04-19',
            'titulo':'Teste de post',
            'descricao':'Segundo teste',
            'tag':'teste'
      },
      {
            'id':3,
            'data':str(data),
            'titulo':'Finalizando teste',
            'descricao':'final'
      }
]
