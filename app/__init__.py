from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from instance.config import app_config

db = SQLAlchemy()


def create_app():
    from api.employees import api_blueprint
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.register_blueprint(api_blueprint)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/')
    def home():
        return 'Welcome to employees api'

    return app

