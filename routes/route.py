from flask import Blueprint,render_template
from dados.dado import lista_post

posts = lista_post

rotas = Blueprint('rotas', __name__)

@rotas.route('/posts',methods = ['GET'])
def get_name():
      return render_template('index.html',Post=posts)


