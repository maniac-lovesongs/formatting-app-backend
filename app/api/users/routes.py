from app.api.users import bp
from app.models.user import User
from app.models.role import Role

###################################################################
@bp.route('/all', methods=["GET"])
def all():
    allUsers = [user.to_json() for user in User.query.all()]
    return allUsers
###################################################################
@bp.route('/view/by_username/<u>', methods=["GET"])
def viewByUsername(u):
    temp_user = User.query.filter_by(username=u).first()
    if temp_user:
        return {"user": temp_user.to_json(), "exists": True}
    return {"user": u, "exists": False}
###################################################################
@bp.route('/view/by_email/<u>', methods=["GET"])
def viewByEmail(u):
    temp_user = User.query.filter_by(email=u).first()
    if temp_user:
        return {"user": temp_user.to_json(), "exists": True}
    return {"user": u, "exists": False}
###################################################################
@bp.route('/view/by_id/<u>', methods=["GET"])
def viewById(u):
    temp_user = User.query.filter_by(id=u).first()
    if temp_user:
        return {"user": temp_user.to_json(), "exists": True}
    return {"user": u, "exists": False}
###################################################################
@bp.route('/view/by_role/<r>', methods=["GET"])
def viewByRole(r):
    temp_users = [user.to_json() for user in User.query.filter_by(role_id=r).all()]
    temp_role = Role.query.filter_by(id=r).first()
    return {"users":temp_users, "role": temp_role.to_json()}
