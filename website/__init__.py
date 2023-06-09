from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
#from werkzeug.utils import secure_filename
#from werkzeug.datastructures import  FileStorage
from flask_login import LoginManager
#from flask_uploads import IMAGES,UploadSet,configure_uploads
#from flask_uploads import *
db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    
    app = Flask(__name__)
    app.secret_key = "your_secret_key" 
    app.config['SECRET_KEY']= 'Naresh Yadav'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
   


    db.init_app(app)
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    from .models import User,Product
    #from models import Product
    create_database(app)
    #photos = UploadSet('photos',IMAGES)
    #configure_uploads(app,photos)
    #patch_request_class(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app) 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
         db.create_all()
        print('Created Database!')