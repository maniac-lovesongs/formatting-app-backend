from typing import Optional
from app import db
from app.models.base import Base

class Role(Base):
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Role %r>' % self.name
    
    def to_json(self):
        return {"name": self.name, "description": self.description}