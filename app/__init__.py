from flask import Flask
from config import Config
from app.extensions import db, migrate, login, cors

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

    cors.init_app(app, origins=["http://localhost:3000", "https://localhost:3000"])

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
