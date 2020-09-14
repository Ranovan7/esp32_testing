import os

from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, current_user
from flask_cors import CORS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = f"{os.getcwd()}/apps/static/images/test"
CORS(app)
socketio = SocketIO(app, async_mode='eventlet')

app_settings = os.environ.get(
    'APP_SETTINGS',
    'project.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
# db = SQLAlchemy(app)
# login = LoginManager(app)
# login.login_view = 'login'


# @app.context_processor
# def always_on():
#     return dict(user=current_user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('master/404.html')

from project.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from project.application.main import bp as main_bp
app.register_blueprint(main_bp, url_prefix='')

import project.socket
