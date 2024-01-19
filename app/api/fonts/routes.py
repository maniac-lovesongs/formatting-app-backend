from flask import render_template, request, url_for, redirect,request 
import json
from app.models.font import Font
from app.api.fonts import bp
from app.api.fonts.utils import process_name

###################################################################
@bp.route('/')
def index():
    return 'This is The Font Blueprint'
###################################################################
@bp.route('/all', methods=["GET"])
def all():
    fonts = [f.to_json() for f in Font.query.all()]
    return {"fonts": fonts}
###################################################################
@bp.route('/<f>/exists', methods=["GET"])
def exists(f):
    f_name = process_name(f)
    temp_font = Font.query.filter_by(name=f_name).first()
    if temp_font:
        return {"font": temp_font.to_json(), "exists": True}
    return {"font": f_name, "exists": False}
###################################################################
@bp.route('/<f>/hasStyle/<s>', methods=["GET"])
def hasStyle(f,s):
    f_name = process_name(f)
    s_name = ' '.join(s.split("_"))
    temp_font = Font.query.filter_by(name=f_name).first()
    if temp_font: 
        return {"font": temp_font.to_json(), 
                "style": s_name, 
                "hasStyle": temp_font.hasStyle(s_name)}
    
    return {"error": "The font you requested does not exist"}
###################################################################