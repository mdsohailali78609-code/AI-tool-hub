import re
with open("c:/antigravity/script.js", "r", encoding="utf-8") as f:
    txt = f.read()

matches = re.findall(r'category:\s*"(.*?)"', txt)
print(set(matches))
