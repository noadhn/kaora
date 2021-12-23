from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['APPLICATION_ROOT'] = False
app.config['OAUTHLIB_INSECURE_TRANSPORT'] = True
app.config['UPLOAD_FOLDER'] = '/Users/noadhn/Desktop/temp/kaora/static/images/new-products'
app.config["ALLOWED_EXTENSIONS"] = ['png', 'jpg', 'jpeg']

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from kaora import routes
