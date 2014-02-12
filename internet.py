#!/usr/bin/python

import cgi
import cgitb
from lan import *
from reikningur import *
import json

cgitb.enable()

results = {}


arguments = cgi.FieldStorage()
jsonstring = arguments['jsonstring'].value
decoded = json.loads(jsonstring)

print "Content-Type: text/html;charset=utf-8;\n"
print decoded["bless"]


