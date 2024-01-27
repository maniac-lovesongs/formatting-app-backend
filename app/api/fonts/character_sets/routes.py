from app.api.fonts.character_sets import bp
from app.models.font import Font
from app.models.style import Style 
from app.models.insta_char import InstaChar
from app.api.fonts.utils import process_name as font_pn 
from app.api.styles.utils import process_name as style_pn


@bp.route('/font/<f>/style/<s>')
def getCharacterSet(f,s):
    f_name = font_pn(f)
    s_name = style_pn(s)

    # Lookup font
    font = Font.query.filter_by(name=f_name).first()
    if not font:
        return {"error": "Font " + f_name + " does not exist"}
    
    if not font.hasStyle(s_name):
        return {"error": "Font '" + f_name + "' does not have style '" + s_name + "'"}

    # Lookup style
    style = Style.query.filter_by(name=s_name).first()
    if not style: 
        return {"error": "Style " + s_name + " does not exist"}


    c_set = InstaChar.query.filter_by(font_id=font.id, style_id=style.id).all()
    c_set = {k["value"]: k for k in [c.to_json() for c in c_set]}
    return {"characters": c_set, 
            "font": f_name, 
            "availableStyles": font.styles.split(","),
            "styleInfo": style.to_json(),
            "style": s_name,
            "font_id": font.id, 
            "style_id": style.id}