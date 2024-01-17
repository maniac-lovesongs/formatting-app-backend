from typing import Optional
from app import db
from app.models.base import Base

class Style(Base):
    name = db.Column(db.String(80), unique=True, nullable=False, default="normal")
    isBold = db.Column(db.Boolean, nullable=False, default=False)
    isItalic = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Style %r>' % self.name
    
    def to_json(self):
        return {"id": self.id, "name": self.name, "isBold": self.isBold, "isItalic": self.isItalic}