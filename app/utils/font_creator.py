import math

base_full = list(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
base_no_nums = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
base_only_lowercase = list("abcdefghijklmnopqrstuvwxyz")
base_only_uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def getNumCharsPerSym(alpha, base):
  base_len = len(base)
  num_chars_per_symbol = len(alpha) / base_len
  (frac, whole) = math.modf(num_chars_per_symbol)
  return (frac, whole)


def splitStringIntoChunks(string, n):
  return [string[i:i + n] for i in range(0, len(string), n)]


def makeCharacterSet(base, alpha):
  (frac, whole) = getNumCharsPerSym(alpha, base)
  if frac == 0.0:
    alpha_split = splitStringIntoChunks(alpha, int(whole))
  pairs = {x: {'value': x, 'symbol': y} for (x, y) in zip(base, alpha_split)}
  return pairs


def makeFontComp(name, styles):
  (normal_pairs, italic_pairs, bold_pairs, bold_italic_pairs) = (None, None,
                                                                 None, None)
  if 'normal' in styles:
    normal_pairs = makeCharacterSet(styles['normal']['base'],
                                    styles['normal']['characters'])
  if 'italic' in styles:
    italic_pairs = makeCharacterSet(styles['italic']['base'],
                                    styles['italic']['characters'])
  if 'bold' in styles:
    bold_pairs = makeCharacterSet(styles['bold']['base'],
                                  styles['bold']['characters'])
  if 'bold italic' in styles:
    bold_italic_pairs = makeCharacterSet(styles['bold italic']['base'],
                                         styles['bold italic']['characters'])

  return {
      'font': name,
      'styles': {
          'normal': normal_pairs,
          'italic': italic_pairs,
          'bold': bold_pairs,
          'bold italic': bold_italic_pairs
      }
  }


def makeFonts(font_pairs):
  fonts = {}
  for (name, styles) in font_pairs:
    fonts[name] = makeFontComp(name, styles)
  return fonts
