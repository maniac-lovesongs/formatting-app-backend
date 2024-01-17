from app.auth import bp
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User

@bp.route('/')
def index():
    return 'This is The Auth Blueprint'