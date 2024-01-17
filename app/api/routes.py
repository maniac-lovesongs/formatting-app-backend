from app.api import bp


@bp.route('/')
def index():
    return 'This is The API Blueprint'