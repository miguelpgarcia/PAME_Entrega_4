from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.funcionario.routes import funcionario_api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    app.register_blueprint(funcionario_api)
    return app