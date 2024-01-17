from app.user import bp

@bp.route('/')
def index():
    return 'This is The User Blueprint'