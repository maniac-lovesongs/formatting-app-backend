from app import models as m
from app import db,app
from app import font_creator
from app import fonts

app.app_context().push()

all_fonts = font_creator.makeFonts(fonts.font_pairs)
pos_styles = {"normal": [False, False], 
              "italic": [False,True], 
              "bold": [True, False], 
              "bold italic": [True,True]}

### Initialize styles #############################
for style in list(pos_styles.keys()):
    with app.app_context():
        style_exists = m.Style.query.filter_by(name=style).first()
        if not style_exists: 
            temp_style = m.Style(name=style, isBold=pos_styles[style][0], isItalic=pos_styles[style][1])
            db.session.add(temp_style)
            db.session.commit()


for name in list(all_fonts.keys()):
    with app.app_context():
        font_exists = m.Font.query.filter_by(name=name).first()
        if not font_exists: 
            font = all_fonts[name]
            styles = []
            style_font_pairs = []
            for style in font["styles"].keys():
                if font["styles"][style] != None:
                    styles.append(style)
                    style_font_pairs.append((name,style))

            temp_font = m.Font(name=name, styles=str(",".join(styles)))
            db.session.add(temp_font)
            db.session.commit()

            for sfp in style_font_pairs:
                f = m.Font.query.filter_by(name=sfp[0]).first()
                s = m.Style.query.filter_by(name=sfp[1]).first()
                p = m.StyleFontPair(font_id=f.id, style_id=s.id)
                db.session.add(p)
            db.session.commit()
        else:
            font_data = all_fonts[name]
            for style in font_data["styles"].keys():
                if font_data["styles"][style]:
                    chars = font_data["styles"][style]
                    #print(chars)
                    for ch in chars: 
                        value = chars[ch]["value"]
                        sym = chars[ch]["symbol"]
                        st = m.Style.query.filter_by(name=style).first()
                        f = font_exists
                        p = m.StyleFontPair.query.filter_by(style_id=st.id, font_id=f.id).first()
                        ch_exists = m.InstaChar.query.filter_by(symbol=ch, value=value, style_id=st.id, font_id=f.id, style_font_pair_id=p.id).first()
                        if not ch_exists:
                            temp_ch = m.InstaChar(symbol=sym, value=value, style_id=st.id, font_id=f.id, style_font_pair_id=p.id)
                            db.session.add(temp_ch)
                    db.session.commit()