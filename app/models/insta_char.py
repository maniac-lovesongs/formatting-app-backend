from typing import Optional
from app import db
from app.models.base import Base

class InstaChar(Base):
    value = db.Column(db.String(1), nullable=False, default="")
    symbol = db.Column(db.BLOB(), nullable=False, default="")
    font_id = db.Column(db.Integer, db.ForeignKey('font.id'))
    style_id = db.Column(db.Integer, db.ForeignKey('style.id'))
    style_font_pair_id = db.Column(db.Integer, db.ForeignKey('style_font_pair.id'))

    def to_json(self):
        return {"value": self.value, 
                "symbol": self.symbol.decode("utf-8"), 
                "id": self.id,
                "font_id": self.font_id, 
                "style_id": self.style_id}

    def __repr__(self):
        sym = self.symbol.decode("utf-8")
        return '<InstaChar value=' + self.value + ', symbol=' + sym + '>'