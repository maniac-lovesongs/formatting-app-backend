from app.api.roles import bp
from app.models.role import Role

###################################################################
@bp.route('/')
def index():
    return 'This is The Role Blueprint'