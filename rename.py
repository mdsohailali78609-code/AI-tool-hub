with open("c:/antigravity/script.js", "r", encoding="utf-8") as f:
    txt = f.read()

txt = txt.replace('category: "Education"', 'category: "Study"')

with open("c:/antigravity/script.js", "w", encoding="utf-8") as f:
    f.write(txt)
