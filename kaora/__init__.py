from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from kaora import app

ENV = "prod"
if ENV == "prod":
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgres://nhbshaqbygmaef:67039998f60f17f686c2e841b6eb62c86d3f582ef4ff9237ffb1729f70ef7dc2@ec2-3-213-76-170.compute-1.amazonaws.com:5432/d1fsdabj56c882'
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://postgres:postgres@localhost/flasksql'

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
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
