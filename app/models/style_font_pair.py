from typing import Optional
from app import db
from app.models.base import Base

class StyleFontPair(Base):
    font_id = db.Column(db.Integer, db.ForeignKey('font.id'))
    style_id = db.Column(db.Integer, db.ForeignKey('style.id'))

    def __repr__(self):
        return '<StyleFontPair font_id=' + self.font_id + ', style_id=' + self.style_id + ">"