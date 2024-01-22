from app.api import bp
from app.models.style_font_pair import StyleFontPair
from app.models.font import Font
from app.models.user import User
from app.models.role import Role

@bp.route('/')
def index():
    return 'This is The API Blueprint'

@bp.route("/all")
def allCounts():
    allUsers = User.query.all()
    allRoles = Role.query.all()
    allFonts = Font.query.all()
    allCharacterSets = StyleFontPair.query.all()
    return {"Users": len(allUsers), "Roles": len(allRoles), "Fonts": len(allFonts), "Character Sets": len(allCharacterSets)}