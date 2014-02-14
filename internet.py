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
	for i in decoded["lan"]:
		this = decoded["lan"][i]
		nafn = this["nafn"]
		vextir = this["vextir"]
		verdtr = this["verdtr"]
		lengd = this["lengd"]
		haus = this["haus"]
		lanid = lan(nafn, vextir, verdtr, lengd, haus, 0.04)
		lanalisti.append(lanid)

	for j in lanalisti:
		print lanVenjulega(j)