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

f = open('json/verdbolga.json', 'r')
verdbolga = f.read()
f.close()

verdbolga = json.loads(verdbolga)
verdbolga = float(verdbolga["nuverandi"])

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

# Lesum oll gildi ut ur JSON strengnum
	for lanid in decoded["lan"]:
		nafn = lanid["nafn"]
		vextir = lanid["vextir"]
		verdtr = lanid["verdtr"]# == "1" ? True : False
		lengd = lanid["lengd"]
		haus = lanid["haus"]
		lanid = lan(nafn, float(vextir), verdtr, int(lengd), float(haus), verdbolga)
		lanalisti.append(lanid)

# greidslugeta	Hversu mikid haegt er ad greida a manudi
# hvenaer		Hversu lengi skal sparad
# eign			Hversu mikid er a bankareikning nuna

	greidslugeta = decoded["spar"]["greidslugeta"]
	hvenaer = decoded["spar"]["hvenaer"]
	eign = decoded["spar"]["eign"]
	upphaed = decoded["spar"]["upphaed"]

# sparnadurVaxtagrodi
# timiAdTakmarki

	results["sparnadurVaxtagrodi"] = []
	results["timiAdTakmarki"] = []

	for reikningurinn in decoded["reikn"]:
		nafn = reikningurinn["reikningur"]
		vextir = reikningurinn["vextir"]
		reikningar.append(reikningur(nafn, float(vextir), verdtryggt, float(verdbolga))
		sparnadurVaxtagrodiResult = sparnadurTimi(int(hvenaer),float(greidslugeta), float(vextir), float(verdbolga))
		timiAdTakmarkiResult = timiAdTakmarki(float(eign),float(greidslugeta), float(vextir), float(verdbolga), float(upphaed))
		results["sparnadurVaxtagrodi"].append({"nafn" : nafn,
			"vextir" : round(float(vextir), 2),
			"sparnadur" : round(sparnadurVaxtagrodiResult, 2)})
		results["timiAdTakmarki"].append({"nafn" : nafn,
			"vextir": round(float(vextir), 2),
			"timi" : int(timiAdTakmarkiResult)})

# lanVenjulega
# lanAukalega

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
	bestaGreidsluskiptingLanaResult = bestaGreidsluskiptingLana(lanalisti, float(greidslugeta), int(hvenaer))

	results["maxReikningar"] = { "nafn": maxReikningarResult.nafn, "vextir" : maxReikningarResult.vextir}
	results["maxLan"] = maxLanResult[0].nafn
	results["maxAllt"] = maxAlltResult.nafn
	results["bestaGreidsluskiptingLana"] = []
	results["verdbolga"] = round(float(verdbolga) * 100, 2)
	results["haestaMogulegtLan"] = round(haestaMogulegtLan(float(eign)), 2)

	order = 1

	#if len(bestaGreidsluskiptingLanaResult) > 1:
	for lan in bestaGreidsluskiptingLanaResult:
		results["bestaGreidsluskiptingLana"].append({"nafn" : lan[0].nafn,
			"greidslur": lan[1],
			"rodun" : order,
			"vextir" : round(lan[0].vextir, 2)})
		order = order + 1
	#else:
	#	lan = bestaGreidsluskiptingLanaResult
	#	results["bestaGreidsluskiptingLana"].append({"nafn" : lan[0].nafn,
	#		"greidslur": lan[1],
	#		"rodun" : order,
	#		"vextir" : lan[0].vextir})

print json.dumps(results)