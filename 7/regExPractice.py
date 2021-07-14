import re

with open("7\mnsz_minta.sima",encoding="utf-8") as f:
  fString = str(f.readlines())
  reIter = re.finditer(r"\b(\w)\w+\s\1\w+\s\1\w+\b", fString)
print([m.group() for m in reIter])

exit()

with open("7\mnsz_minta.sima", encoding="utf-8") as f:
  outF = re.sub(r" ([,!.?;])", r"\1", "".join(f.readlines()))

with open("7\detokenizált.txt", "w", encoding="utf-8") as f:
  f.write(outF)

exit()

# match = re.search(r"\b(\w)\w+\s\1\w+\s\1\w+\b", "szegény szamár szónokol, és ezért hamar hárommá hull")
# print(match.group(0))
# print(re.findall("\w\w(?:\w)\w\s", "ello bello trello"))
print(re.findall(r"(\b(\w)\w+\s\2\w+\s\2\w+\b)", "szegény szamár szónokol, és ezért hamar hárommá hull"))

# m = re.finditer(r"\b(\w)\w+\s\1\w+\s\1\w+\b", "szegény szamár szónokol, és ezért hamar hárommá hull")
# print(m.__next__())
# print(m.__next__())
# print(m.__next__())
