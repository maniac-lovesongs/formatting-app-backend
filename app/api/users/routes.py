from app.api.users import bp
from app.models.user import User

###################################################################
@bp.route('/')
def index():
    return 'This is The User Blueprint'