TITLE = "heyden-formulae-graece"
# Heyden Formulae Latine
SRC = f"{TITLE}.txt"
DEST = f"{TITLE}.html"

HEADER = f"""\
<!DOCTYPE html>
<html lang="grc">
<head>
<title>Αἱ τῶν Παιδῶν Ὁμιλίαι τε καὶ Φράσεις Σεβάλδου τοῦ Εὐδένος</title>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css?family=Noto+Serif:400,700&amp;subset=greek,greek-ext" rel="stylesheet">
<link href="style.css" rel="stylesheet">
</head>
<body>
<div class="container">
<nav>&#x2191; <a href="./">heyden-formulae</a></nav>
<h1 lang="en">Sebald Heyden Fōrmulae Colloquiōrum Puerīlium</h1>
<h1>Αἱ τῶν Παιδῶν Ὁμιλίαι τε καὶ Φράσεις Σεβάλδου τοῦ Εὐδένος</h1>
<h1 lang="en">translated by Martin Ruland the Elder (1556)</h1>
<h1 lang="en">edited by Fergus Walsh</h1>
"""

FOOTER = """\
</div>
</body>
</html>
"""

with open(SRC, encoding = "utf-8") as f:
    with open(DEST, "w", encoding = "utf-8") as g:
        prev_section = None
        prev_subsection = None
        print(HEADER, file=g)
        for line in f:
            parts = line.strip().split(maxsplit=1)
            ref = parts[0].split(".")
            section, subsection = ref
            if section.isnumeric() == False:
                if subsection == "0":
                    print(f"""    <h2 class="section_title">{parts[1]}</h2>""", file=g)
                elif subsection != "0":
                    print(f"""<p>{parts[1]}</p>""", file=g)
            else:
                if subsection == "t":
                    print(f"""    <h2 class="section_title">{parts[1]}</h2>""", file=g)
                elif subsection == "p":
                    print(f"""    <h3 class="personae">{parts[1]}</h3>""", file=g)
                else:
                    print(f"""<p>{parts[1]}</p>""", file=g)
        print(FOOTER, file=g)                    