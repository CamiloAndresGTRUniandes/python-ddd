import os
from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask import Flask
from seedwork.infrastructure.utils import database_connection_string


basedir = os.path.abspath(os.path.dirname(__file__))

def register_handlers():
    import modules.property.application

def import_alchemy_models():
    import modules.property.infrastructure.dto

def start_consumer():
    # import threading
    # import modules.property.infrastructure.consumer as property
    ...

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_connection_string()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    from config.db import init_db
    init_db(app)

    from config.db import db

    import_alchemy_models()
    register_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            start_consumer()

     # Importa Blueprints
    from . import property
    # Registro de Blueprints
    app.register_blueprint(property.bp)
    from flask_swagger import swagger
    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app