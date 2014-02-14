#!/usr/bin/python

import cgi
import cgitb
from lan import *
from reikningur import *
import json

cgitb.enable()

lanalisti = []

results = {}
jsonstring = ""
decoded = ""

verdbolga = 0.04

arguments = cgi.FieldStorage()

print "Content-Type: text/html;charset=utf-8;\n"

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

	for reikningur in decoded["reikn"]:
		nafn = reikningur["reikningur"]
		vextir = reikningur["vextir"]
		#sparnadurVaxtagrodiResult = sparnadurVaxtagrodi(greidslugeta, vextir, verdbolga)
		#results["sparnadurVaxtagrodi"].append({"nafn" : nafn, "vextir" : vextir, "sparnadur" : sparnadurVaxtagrodiResult})

	results["lanVenjulega"] = []
	results["lanAukalega"] = []

	for lanid in lanalisti:
		lanVenjulegaResult = lanVenjulega(lanid)
		lanAukalegaResult = lanAukalega(lanid, float(greidslugeta))

		results["lanVenjulega"].append({"nafn": lanid.nafn, "val": lanVenjulegaResult})
		results["lanAukalega"].append({"nafn": lanid.nafn, "val" : lanAukalegaResult})

print "Blessadur"
print json.dumps(results)