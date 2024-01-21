from flask import Blueprint

bp = Blueprint('api', __name__)

# Child blueprints
from app.api.fonts import bp as fonts_bp
bp.register_blueprint(fonts_bp, url_prefix="/fonts")

from app.api.styles import bp as styles_bp
bp.register_blueprint(styles_bp, url_prefix="/styles")

from app.api.users import bp as users_bp
bp.register_blueprint(users_bp, url_prefix="/users")

from app.api.roles import bp as roles_bp
bp.register_blueprint(roles_bp, url_prefix="/roles")

from app.api.auth import bp as auth_bp
bp.register_blueprint(auth_bp, url_prefix="/auth")

from app.api import routes