from typing import Optional
from app.extensions import db, login
from app.models.base import Base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin,Base):
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    def to_json(self):        
        return {"username": self.username,
                "id": self.id, 
                "role_id": self.role_id,
                "email": self.email}