from flask import Flask
from app.config.config import config
from app.extensions import database, auth

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    database.init_app(app)
    auth.init_app(app)

    # Register blueprints
    from app.api.v1.routes import api as api_blueprint
    from app.main.views import main as main_blueprint
    
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    app.register_blueprint(main_blueprint)

    return app