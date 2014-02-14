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
	for lanid in decoded["lan"]:
		this = lanid
		nafn = this["nafn"]
		vextir = this["vextir"]
		verdtr = this["verdtr"]
		lengd = this["lengd"]
		haus = this["haus"]
		lanid = lan(nafn, float(vextir), float(verdtr), int(lengd), float(haus), 0.04)
		lanalisti.append(lanid)

	results["lanVenjulega"] = []

	for lanid in lanalisti:
		lanVenjulegaResult = lanVenjulega(lanid)
		results["lanVenjulega"].append({"nafn": lanid.nafn, "val": lanVenjulegaResult})
		

print json.dumps(results)