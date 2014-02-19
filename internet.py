#!/usr/bin/python

import cgi
import cgitb
from lan import *
from reikningur import *
import json

cgitb.enable()

lanalisti = []
reikningar = []

results = {}
jsonstring = ""
decoded = ""

verdbolga = 0.04
verdtryggt = True

arguments = cgi.FieldStorage()

print "Content-Type: text/json;charset=utf-8;\n"

try:
	jsonstring = arguments["jsonstring"].value
except:
	print "No params"
try:
	decoded = json.loads(jsonstring)
except:
	print "JSON syntax error"
else:

	# Lesum oll gildi ut ur JSON
	for lanid in decoded["lan"]:
		nafn = lanid["nafn"]
		vextir = lanid["vextir"]
		verdtr = lanid["verdtr"]
		lengd = lanid["lengd"]
		haus = lanid["haus"]
		lanid = lan(nafn, float(vextir), float(verdtr), int(lengd), float(haus), verdbolga)
		lanalisti.append(lanid)

	greidslugeta = decoded["spar"]["greidslugeta"]
	hvenaer = decoded["spar"]["hvenaer"]

	results["sparnadurVaxtagrodi"] = []

	for reikningurinn in decoded["reikn"]:

		nafn = reikningurinn["reikningur"]
		vextir = reikningurinn["vextir"]
		reikningar.append(reikningur(nafn, float(vextir), float(verdtryggt), verdbolga))
		sparnadurVaxtagrodiResult = sparnadurVaxtagrodi(float(greidslugeta), float(vextir), verdbolga)
		results["sparnadurVaxtagrodi"].append({"nafn" : nafn, "vextir" : float(vextir), "sparnadur" : sparnadurVaxtagrodiResult})

	results["lanVenjulega"] = []
	results["lanAukalega"] = []

	for lanid in lanalisti:
		lanVenjulegaResult = lanVenjulega(lanid)
		lanAukalegaResult = lanAukalega(lanid, float(greidslugeta))

		results["lanVenjulega"].append({"nafn": lanid.nafn, "val": lanVenjulegaResult})
		results["lanAukalega"].append({"nafn": lanid.nafn, "val" : lanAukalegaResult})

	maxReikningarResult = maxReikningar(reikningar)
	maxLanResult = maxLan(lanalisti)
	maxAlltResult = maxAllt(maxReikningarResult, maxLanResult[0])

	results["maxReikningar"] = { "nafn": maxReikningarResult.nafn, "vextir" : maxReikningarResult.vextir}
	results["maxLan"] = maxLanResult[0].nafn
	results["maxAllt"] = maxAlltResult.nafn

	bestaGreidsluskiptingLanaResult = bestaGreidsluskiptingLana(lanalisti, float(greidslugeta), int(hvenaer))

	results["bestaGreidsluskiptingLana"] = []

	order = 1

	for lan in bestaGreidsluskiptingLanaResult:
		results["bestaGreidsluskiptingLana"].append({"nafn" : lan[0].nafn, "greidslur": lan[1], "rodun" : order, "vextir" : lan[0].vextir})
		order = order + 1

print json.dumps(results)