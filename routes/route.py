from flask import Blueprint,render_template, request, redirect,url_for,jsonify
from dados.dado import lista_post

posts = lista_post

rotas = Blueprint('rotas', __name__)

@rotas.route('/posts',methods = ['GET','POST'])
def get_name():
      if request.method == 'POST':
            id = len(posts)+1
            titulo = request.form.get('titulo')
            descricao = request.form.get('descricao')
            novo_post = {'id':id,'titulo':titulo,'descricao':descricao}
            posts.append(novo_post)
            
            return jsonify(posts)
            
      return jsonify(posts)

@rotas.route('/post/<int:id>', methods = ['GET'])
def get_id(id):
      id = request.args.get(id)
      for i in posts:
            if i['id'] == id:
                  return jsonify(i)
            
