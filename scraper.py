from bs4 import BeautifulSoup
import requests
import re
import json

# Strengjamedhondlun
# Vid skiptum ut kommum fyrir punkta og fellum prosentumerki.
# I stad thess ad nota replace().replace()-kedju gerum vid thad
# i single pass.
def stripNum(text, conds):
	rep = dict((re.escape(key), val) for key, val in conds.iteritems())
	pattern = re.compile("|".join(rep.keys()))
	return pattern.sub(lambda m: rep[re.escape(m.group(0))], text)


req = requests.get("http://sedlabanki.is/")

dom = req.text
soup = BeautifulSoup(dom)

lysing = soup.findAll("div", { "class" : "lysing-small" })

# Breytum kommum i punkta, og fjarlaegjum prosentumerki.
conds = {",": ".", "%": ""}
for l in lysing:
	sedlabanki = [stripNum(s, conds) for s in re.findall(r'\d{0,2},\d{0,2}\%', str(l))]

out = {"nuverandi": float(sedlabanki[0])/100.0, "markmid": float(sedlabanki[1])/100.0)}

with open('json/verdbolga.json', 'w') as outfile:
 	json.dump(out, outfile)