from flask import Flask, jsonify, request
from db import Post

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = True

#retorna todos os posts
@app.route('/post', methods = ['GET'])
def get_post():
      return jsonify( Post )

#cria um novo post
@app.route('/novo_post', methods = ["POST"])
def create_post():
      dados = request.json
      Post.append(dados)
      return jsonify(dados), 201

#retona post por id
@app.route('/post/<int:post_id>', methods = ['GET'])
def get_id(post_id):
      for i in Post:
            if i['id'] == post_id:
                  return jsonify(i)
      return jsonify('Erro, id não existe'), 404


@app.route('/post/update/<int:post_id>', methods = ['PUT'])
def update_post(post_id):
      dados_update = request.json
      
      for i, post in enumerate(Post):
            if post['id'] == post_id:
                  Post[i].update(dados_update)
                  return jsonify(Post[i]), 200
      else:
            return jsonify('id nao existe'), 404

                  

app.run(debug= True)