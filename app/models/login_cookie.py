from typing import Optional
from app.extensions import db, login
from app.models.base import Base

class LoginCookie(Base):
    username = db.Column(db.String(80), unique=True, nullable=False)
    cookie = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expiration = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<LoginCookies %r>' % self.username
    
    def to_json(self):        
        return {"username": self.username,
                "id": self.id, 
                "user_id": self.user_id,
                "cookie": self.cookie}