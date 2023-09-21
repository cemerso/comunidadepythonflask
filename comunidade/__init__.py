from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os



database = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = '8e8ac9fb778d7f6111c87ddcc9f9a5fa'

if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #Aqui é a função que vai direcionar ele para a pagina que você quer
login_manager.login_message = 'Por favor, faça o login para acessar esta página.'
login_manager.login_message_category = 'alert-info'


from comunidade import routes


