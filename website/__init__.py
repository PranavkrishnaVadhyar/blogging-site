from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "ldicnawijdidnvoisjdd"
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix = "/") # What ever is written the url prefix is to be added before enterning the route of the function
    app.register_blueprint(auth,url_prefix = "/")
    
    return app  