from typing import Optional
from app.extensions import db
from app.models.base import Base

class Font(Base):
    name = db.Column(db.String(80), unique=True, nullable=False, default="Sans Serif")
    styles = db.Column(db.String(100))

    def __repr__(self):
        return '<Font %r>' % self.name
    
    def hasStyle(self,style):
        return style in self.styles

    def to_json(self):
        styles = [s for s in self.styles.split(",")]
        return {"id": self.id, "name": self.name, "styles": styles}