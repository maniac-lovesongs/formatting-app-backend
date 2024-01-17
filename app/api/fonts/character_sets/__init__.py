from flask import Blueprint

bp = Blueprint('characterSets', __name__)

from app.api.fonts.character_sets import routes