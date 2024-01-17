from flask import Flask
from config import Config
from app.extensions import db, migrate, login

def create_app(config_class=Config):
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Flask extensions
    #cors = CORS(app)
    db.init_app(app)
    migrate.init_app(app,db)

    login.init_app(app)
    login.login_view = 'auth.login'

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
