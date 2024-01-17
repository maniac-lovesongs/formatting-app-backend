from flask import Blueprint

bp = Blueprint('styles', __name__)

from app.api.styles import routes