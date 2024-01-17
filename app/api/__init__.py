from flask import Blueprint

bp = Blueprint('api', __name__)

# Child blueprints
from app.api.fonts import bp as fonts_bp
bp.register_blueprint(fonts_bp, url_prefix="/fonts")

from app.api.styles import bp as styles_bp
bp.register_blueprint(styles_bp, url_prefix="/styles")

from app.api import routes