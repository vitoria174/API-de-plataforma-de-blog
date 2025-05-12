from flask import Blueprint, request,jsonify
from dados.dado import lista_post

posts = lista_post

rotas = Blueprint('rotas', __name__)

@rotas.route('/posts',methods = ['GET','POST'])
def get_name():
      if request.method == 'POST':
            dados = request.get_json()
            id = len(posts)+1
            data = dados.get('data')
            titulo = dados.get('titulo')
            descricao = dados.get('descricao')
            tag = dados.get('tag')
            
            novo_post = {'id':id,'data':data,'titulo':titulo,'descricao':descricao,'tag':tag}
            posts.append(novo_post)
            
            return jsonify(novo_post), 201
            
      return jsonify(posts), 200

@rotas.route('/posts/<int:id>', methods = ['GET'])
def get_id(id):
      
      for i in posts:
            if i['id'] == id:
                  return jsonify(i), 200
      return jsonify({'mensagem':'solicitacao nao encontrada'}), 404

@rotas.route('/posts/data/<data>',methods=['GET'])
def get_data(data):
      for j in posts:
            if j.get('data')==data:
                  return jsonify(j), 200
      return jsonify({'Mensagem':'Erro data nao encontrada'}), 404

@rotas.route('/posts/tag/<tag>', methods=['GET'])
def get_tag(tag):
      for busca_tag in posts:
            if busca_tag.get('tag') == tag:
                  return jsonify(busca_tag), 200
      return jsonify ({'mensagem':'Tag nao encontrada'}), 404
        
@rotas.route('/posts/<int:id>', methods=['PUT'])
def update(id):
      dados=request.get_json()
      
      for i in posts:
            if i['id'] == id:
                 i['titulo']=dados.get('titulo',i['titulo'])
                 i['descricao']=dados.get('descricao', i['descricao'])
                 return jsonify(i), 200
      return jsonify({'mensagem':'Id nao encontrada'}), 404

@rotas.route('/posts/<int:id>', methods=['DELETE'])
def delete(id):
      for i, post in enumerate(posts):
            if post['id']==id:
                  del posts[i]
                  
            return jsonify({'mensagem':'Post deletado com sucesso'}), 201
      return jsonify({'mensagem':'POst nao encontrado'}), 404
