import re

def kodfuggveny(szoveg, szotar, kodolt=""):

  minta=r"|".join(reversed(list(szotar)))
  if len(szoveg) == 0:
    return kodolt
  else:
    szoveg_lower = szoveg.lower()
    m = re.match(minta, szoveg_lower)
    next_char = szoveg_lower[0] if not m else m.group(0)
    try:
      kodolt += szotar[next_char] if szoveg[0].islower() else szotar[next_char].capitalize()
    except KeyError:
      kodolt += next_char
    szoveg = szoveg[len(next_char):]
    return kodfuggveny(szoveg, szotar, kodolt)

# Example usage:

szotar = { 'a':'ny', 'á':'o', 'b':'ó', 'c':'ö', 'cs':'ő', 'd':'p', 'dz':'q', 'dzs':'r', 'e':'s', 'é':'sz', 'f':'t', 'g':'ty', 'gy':'u', 'h':'ú', 'i':'ü', 'í':'ű', 'j':'v', 'k':'w', 'l':'x', 'ly':'y', 'm':'z', 'n':'zs', 'ny':'a', 'o':'á', 'ó':'b', 'ö':'c', 'ő':'cs', 'p':'d', 'q':'dz', 'r':'dzs', 's':'e', 'sz':'é', 't':'f', 'ty':'g', 'u':'gy', 'ú':'h', 'ü':'i', 'ű':'í', 'v':'j', 'w':'k', 'x':'l', 'y':'ly', 'z':'m', 'zs':'n' }
kodolt_szoveg = kodfuggveny("Csacska. Dzsakarta", szotar)
print(kodolt_szoveg)
dekodolt_szoveg = kodfuggveny(kodolt_szoveg, szotar)
print(dekodolt_szoveg)