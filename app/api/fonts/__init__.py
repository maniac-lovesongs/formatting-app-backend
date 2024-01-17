from flask import Blueprint

bp = Blueprint('fonts', __name__)

# Child blueprints
from app.api.fonts.character_sets import bp as cs_bp
bp.register_blueprint(cs_bp, url_prefix="/character_sets")


from app.api.fonts import routes