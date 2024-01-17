from app import font_creator
main = font_creator

fraktur = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷օյշՅկՏճԴՑգ"
    },
    "bold": {
        "base": main.base_no_nums,
        "characters": "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"
    }
}

glitch = {
    "normal": {
        "characters": "ᏗᏰፈᎴᏋᎦᎶᏂᎥᏠᏦᏝᎷᏁᎧᎮᎤᏒᏕᏖᏬᏉᏇጀᎩፚᏗᏰፈᎴᏋᎦᎶᏂᎥᏠᏦᏝᎷᏁᎧᎮᎤᏒᏕᏖᏬᏉᏇጀᎩፚ",
        "base": main.base_no_nums
    }
}
sans_serif = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    },
    "bold": {
        "base":
        main.base_full,
        "characters":
        "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
    },
    "italic": {
        "base": main.base_no_nums,
        "characters": "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"
    },
    "bold italic": {
        "base": main.base_no_nums,
        "characters": "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯"
    }
}
script = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
    },
    "bold": {
        "base": main.base_no_nums,
        "characters": "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"
    },
}
serif = {
    "bold": {
        "base":
        main.base_full,
        "characters":
        "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
    },
    "bold italic": {
        "base": main.base_no_nums,
        "characters": "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"
    },
}
bubbles = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓪①②③④⑤⑥⑦⑧⑨"
    }
}
dark_bubbles = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩⓿➊➋➌➍➎➏➐➑➒"
    }
}
mono = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"
    }
}
tuxedo = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "🅰Ⓑ🅲Ⓓ🅴Ⓕ🅶Ⓗ🅸Ⓙ🅺Ⓛ🅼Ⓝ🅾Ⓟ🆀Ⓡ🆂Ⓣ🆄Ⓥ🆆Ⓧ🆈Ⓩ🅰Ⓑ🅲Ⓓ🅴Ⓕ🅶Ⓗ🅸Ⓙ🅺Ⓛ🅼Ⓝ🅾Ⓟ🆀Ⓡ🆂Ⓣ🆄Ⓥ🆆Ⓧ🆈Ⓩ0①2③4⑤6⑦8⑨"
    }
}
aesthetic = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ０１２３４５６７８９"
    }
}
silicon = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
    }
}
underline = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "A͟B͟C͟D͟E͟F͟G͟H͟I͟J͟K͟L͟M͟N͟O͟P͟Q͟R͟S͟T͟U͟V͟W͟X͟Y͟Z͟a͟b͟c͟d͟e͟f͟g͟h͟i͟j͟k͟l͟m͟n͟o͟p͟q͟r͟s͟t͟u͟v͟w͟x͟y͟z͟0͟1͟2͟3͟4͟5͟6͟7͟8͟9͟"
    }
}

all_caps = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    }
}

kings_landing = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
    }
}
art_greco = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "ΑВ¢∂ЄƑGНΙנКℓѪИѺΡQЯЅͲЦѴѰΧУZαвċ∂єƒgнιנкℓмησρqяѕтυνωχуz"
    }
}
chroma = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉"
    }
}
strikethrough = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "A̶B̶C̶D̶E̶F̶G̶H̶I̶J̶K̶L̶M̶N̶O̶P̶Q̶R̶S̶T̶U̶V̶W̶X̶Y̶Z̶a̶b̶c̶d̶e̶f̶g̶h̶i̶j̶k̶l̶m̶n̶o̶p̶q̶r̶s̶t̶u̶v̶w̶x̶y̶z̶0̶1̶2̶3̶4̶5̶6̶7̶8̶9̶"
    }
}
slipknot = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ"
    }
}
slicer = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "ȺɃȻĐɆFǤĦƗɈꝀŁMNØⱣꝖɌSŦᵾVWXɎƵȺƀȼđɇfǥħɨɉꝁłmnøᵽꝗɍsŧᵾvwxɏƶ"
    }
}
pound_cake = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "ⱭƁƇƊҼƑƓӇӀJƘlⱮƝƠƤQRՏƬƲVⱲXƳȤąɓƈɗҽƒɠɦíᴊƙƖɱղօƥʠɾʂƭʋⱱⱳxყz"
    }
}

quebec = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "ⱭƁƇƊҼƑƓӇӀJƘlⱮƝƠƤQRՏƬƲVⱲXƳȤɑҍϲժҽƒցհíᴊƙƖʍղօթqɾsեմѵաxყz"
    }
}

wonky = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "ค๒ς๔єŦɠђเןкl๓ภ๏թợгรtยvฬxץzค๒ς๔єŦɠђเןкl๓ภ๏թợгรtยvฬxץz"
    }
}

wiggle_arms = {
    "normal": {
        "base": main.base_only_uppercase,
        "characters": "ᗩᙖᙅᗪᙓᖴᘜᕼIᒍKᒪᙏᑎOᑭᑫᖇSTᙀᐯᙎ᙭Yᘔ"
    }
}

upside_down = {
    "normal": {
        "base": main.base_no_nums,
        "characters": "∀ᙠƆᗡƎℲ⅁HIſ⋊˥WNOԀΌᴚS⊥∩ΛMX⅄Zɐqɔpǝɟɓɥıɾʞlɯuodbɹsʇnʌʍxʎz"
    }
}

icy = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "ꁲꃳꏳꀷꑀꊯꁅꁝ꒐꒑ꈵ꒒ꂵꃔꊿꉣꋠꌅꈜꋖꌈ꒦ꅐꉤꐔꑒꁲꃳꏳꀷꑀꊯꁅꁝ꒐꒑ꈵ꒒ꂵꃔꊿꉣꋠꌅꈜꋖꌈ꒦ꅐꉤꐔꑒꂷꀤꀨꎆꎨꌓꋻꊰꈔꍌ"
    }
}

ringlets = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "αɓ૮∂εƒɠɦเʝҡℓɱɳσρφ૨รƭµѵωאყƶαɓ૮∂εƒɠɦเʝҡℓɱɳσρφ૨รƭµѵωאყƶ੦౹੨੩੫ƼϬԴ੪੧"
    }
}

heart_king = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "♥A♥ ♥B♥ ♥C♥ ♥D♥ ♥E♥ ♥F♥ ♥G♥ ♥H♥ ♥I♥ ♥J♥ ♥K♥ ♥L♥ ♥M♥ ♥N♥ ♥O♥ ♥P♥ ♥Q♥ ♥R♥ ♥S♥ ♥T♥ ♥U♥ ♥V♥ ♥W♥ ♥X♥ ♥Y♥ ♥Z♥ ♥a♥ ♥b♥ ♥c♥ ♥d♥ ♥e♥ ♥f♥ ♥g♥ ♥h♥ ♥i♥ ♥j♥ ♥k♥ ♥l♥ ♥m♥ ♥n♥ ♥o♥ ♥p♥ ♥q♥ ♥r♥ ♥s♥ ♥t♥ ♥u♥ ♥v♥ ♥w♥ ♥x♥ ♥y♥ ♥z♥ ♥0♥ ♥1♥ ♥2♥ ♥3♥ ♥4♥ ♥5♥ ♥6♥ ♥7♥ ♥8♥ ♥9♥ "
    }
}

skullies = {
    "normal": {
        "base":
        main.base_full,
        "characters":
        "☠𝙰☠ ☠𝙱☠ ☠𝙲☠ ☠𝙳☠ ☠𝙴☠ ☠𝙵☠ ☠𝙶☠ ☠𝙷☠ ☠𝙸☠ ☠𝙹☠ ☠𝙺☠ ☠𝙻☠ ☠𝙼☠ ☠𝙽☠ ☠𝙾☠ ☠𝙿☠ ☠𝚀☠ ☠𝚁☠ ☠𝚂☠ ☠𝚃☠ ☠𝚄☠ ☠𝚅☠ ☠𝚆☠ ☠𝚇☠ ☠𝚈☠ ☠𝚉☠ ☠𝚊☠ ☠𝚋☠ ☠𝚌☠ ☠𝚍☠ ☠𝚎☠ ☠𝚏☠ ☠𝚐☠ ☠𝚑☠ ☠𝚒☠ ☠𝚓☠ ☠𝚔☠ ☠𝚕☠ ☠𝚖☠ ☠𝚗☠ ☠𝚘☠ ☠𝚙☠ ☠𝚚☠ ☠𝚛☠ ☠𝚜☠ ☠𝚝☠ ☠𝚞☠ ☠𝚟☠ ☠𝚠☠ ☠𝚡☠ ☠𝚢☠ ☠𝚣☠ ☠𝟶☠ ☠𝟷☠ ☠𝟸☠ ☠𝟹☠ ☠𝟺☠ ☠𝟻☠ ☠𝟼☠ ☠𝟽☠ ☠𝟾☠ ☠𝟿☠ "
    }
}
font_pairs = [("Franktur", fraktur), ("Sans Serif", sans_serif),
              ("Script", script), ("Bubbles", bubbles), ("Serif", serif),
              ("Ringlets", ringlets), ("All Caps", all_caps),
              ("Skullies", skullies), ("Dark Bubbles", dark_bubbles),
              ("Upside Down", upside_down), ("Wiggle Arms", wiggle_arms),
              ("Glitch", glitch),
              ("Heart King", heart_king), ("Wonky", wonky), ("Chroma", chroma),
              ("Art Greco", art_greco), ("Icy", icy), ("Slicer", slicer),
              ("Pound Cake", pound_cake), ("Quebec", quebec),
              ("Strikethrough", strikethrough), ("Slipknot", slipknot),
              ("Kings Landing", kings_landing), ("Mono", mono),
              ("Underline", underline), ("Silicon", silicon),
              ("Aesthetic", aesthetic), ("Tuxedo", tuxedo)]
