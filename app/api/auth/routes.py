from flask import  redirect,request 
from flask_login import current_user, login_user, logout_user
import json
from app.models.user import User
from app.api.auth import bp

###################################################################
@bp.route('/', methods=["GET"])
def index():
    return "This is the index of api.auth"