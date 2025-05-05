from flask import Flask
from routes.route import rotas

app = Flask(__name__)
app.register_blueprint(rotas, url_prefix = '/api')

if __name__ == '__main__':
      app.run(debug=True)