from flask import render_template, request, url_for, redirect,request 
import json
from flask_cors import cross_origin
from app.models.font import Font
from app.api.fonts import bp
from app.api.fonts.utils import process_name


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
@bp.route('/by_id/<f>', methods=["GET"])
def getById(f):
    #f_name = process_name(f)
    temp_font = Font.query.filter_by(id=f).first()
    if temp_font:
        return {"font": temp_font.to_json()}
    return {"font": f, "exists": False}
###################################################################
@bp.route('/by_name/<f>', methods=["GET"])
def getByName(f):
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