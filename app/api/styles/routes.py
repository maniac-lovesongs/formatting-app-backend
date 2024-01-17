from app.api.styles import bp
from app.api.styles.utils import process_name
from app.models.style import Style

###################################################################
@bp.route('/')
def index():
    return 'This is The Style Blueprint'
###################################################################
@bp.route('/all')
def all():
    styles = [s.to_json() for s in Style.query.all()]
    return {"styles": styles}
###################################################################
@bp.route("/<s>/exists")
def exists(s):
    s_name = process_name(s)
    temp_style = Style.query.filter_by(name=s_name)
    if temp_style:
        return {"style": temp_style.to_json(), "exists": True}
    return {"style": s_name, "exists": False}
###################################################################