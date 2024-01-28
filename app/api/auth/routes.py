from flask import  make_response,request 
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db
from app.models.login_cookie import LoginCookie
from app.api.auth import bp
import string
import secrets
import time

###################################################################
# Define a function
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a secure string
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

###################################################################
@bp.route('/', methods=["GET"])
def index():
    return "This is the index of api.auth"

@bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.json["username"]
        password = request.json["password"]
        user = User.query.filter_by(username=username).first()
        if not user: 
            return {"login": False, "error": "User " + username + " does not exist"}
        else: 
            if not user.check_password(password):
                return {"login": False, "error": "Incorrect password"}
        
        if user and user.check_password(password):
            login_user(user)

            # Generate the cookie
            randomString = generate_random_string(120)
            # Generate an expiration date a week from now 
            numberOfSecsInAWeek = 604800
            expiration = int(time.time()) + numberOfSecsInAWeek
            cookieKey = "instastylr"
            cookies = [{"value": randomString, "key": cookieKey, "expiration": expiration},
                       {"value": username, "key": "instastylr_user", "expiration": expiration}]
            resp = make_response({"login": True, "user": user.to_json(), "cookies": cookies })
            login_cookie = LoginCookie(username=username,cookie=randomString,expiration=expiration,user_id=user.id)
            db.session.add(login_cookie)
            db.session.commit()
            return resp
    return {"error": "This endpoint only accepts POST requests"}