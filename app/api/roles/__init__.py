from flask import Blueprint

bp = Blueprint('roles', __name__)

from app.api.roles import routes