from app.api.roles import bp
from app.models.role import Role

###################################################################
@bp.route('/')
def index():
    return 'This is The Role Blueprint'
###################################################################
@bp.route('/all', methods=["GET"])
def all():
    allRoles = [role.to_json() for role in Role.query.all()]
    return allRoles
###################################################################
@bp.route('/view/by_name/<r>', methods=["GET"])
def viewByName(r):
    temp_role = Role.query.filter_by(name=r).first()
    if temp_role:
        return {"role": temp_role.to_json(), "exists": True}
    return {"role": r, "exists": False}
###################################################################
@bp.route('/view/by_id/<r>', methods=["GET"])
def viewById(r):
    temp_role = Role.query.filter_by(id=r).first()
    if temp_role:
        return {"role": temp_role.to_json(), "exists": True}
    return {"role": r, "exists": False}