import sys
from lan import *
from reikningur import *

print "Sladu inn verdbolgu til ad mida vid (t.d 0.04)"
vb = raw_input()
verdbolga = float(vb)

reikningar = []

#reikningar sem vid bjodum upp
reikningar.append(reikningur("kjorbok",0.0180,False,verdbolga))
reikningar.append(reikningur("sparireikningur",0.0445,False,verdbolga))
reikningar.append(reikningur("vaxtareikningur",0.0425,False,verdbolga))
reikningar.append(reikningur("landsbok",0.0190,False,verdbolga))

#listi af lanum notanda		
lanalisti = []

print "Sladu inn greidslugetu a manudi"
greidslugeta = int(raw_input())
print "Sladu inn fjolda manada"
timi = int(raw_input())
print "Sladu inn heildargreidslugeta til utborgunar"
heildargreidslugeta = int(raw_input())
print "Sladu inn upphaed til ad setja a bankareikning i byrjun"
hofudstollbanki = int(raw_input())

#Notandi slaer inn allar upplysingar um lanin sin
while True:
	inp = [] #Holdum utan um lanaupplysingar til ad faera inn i lanalistann
	print "Sladu inn nafn lans" 
	inp.append(raw_input())
	print "Sladu inn vexti lans a forminu 0.03 - vaeri 3% "
	vext = raw_input()
	inp.append(float(vext))
	print "Sladu True fyrir verdtryggingu "
	if raw_input() == "True":
		inp.append(True)
	else:
		inp.append(False)
	print "Sladu inn tima lans i manudum"
	inp.append(int(raw_input()))
	print "Sladu inn hofudstols lans i kr."
	hof = raw_input()
	inp.append(float(hof))
	
	lanalisti.append(lan(inp[0],inp[1],inp[2],inp[3],inp[4],verdbolga))
	
	print "Sladu inn 1 til ad sla inn fleiri lan "
	cont = raw_input()
	if not cont or cont != '1':
		break

# Upplysingar um hvad se hagkvaemast midad vid greidslubyrdi og lan notanda
print "Hagkvaemast er ad greida inn a lanid: "
max_lan = maxLan(lanalisti)[0]
print(max_lan.nafn)
print "Midad vid greidslugetu thina er avinningur a manudi: "
print(sparnadurVaxtagrodi(greidslugeta,max_lan.vextir,max_lan.verdbolga))
print "I heildina sparast "
print(sparnadurTimi(timi,greidslugeta,max_lan.vextir,max_lan.verdbolga))

print "Listi yfir mogulega reikninga og vexti theirra er "
for reikningur in reikningar:
	print(reikningur.nafn)
	print(reikningur.vextir)

max_reikningur = maxReikningar(reikningar)
print "Ef peningurinn yrdi settur a hagkvaemasta bankareikning yrdi avinningur a manudi: "
print(sparnadurTimi(timi,greidslugeta,max_reikningur.vextir,max_reikningur.verdbolga))
print "Ef upphaflegri greidsla yrdi sett a hagkvaemasta bankareikning i byrjun myndum vid enda med: "
print(sparnadurTimiHeild(timi,greidslugeta,max_reikningur.vextir,max_reikningur.verdbolga,hofudstollbanki))
print "Hagkvaemara er ad nota peninginn i "
print(maxAllt(max_lan,max_reikningur).nafn)
	
skipting_lana = bestaGreidsluskiptingLana(lanalisti,greidslugeta,timi)
print "Besta greidsluskipting lana er: "
for lan in skipting_lana:
	print("Greitt af eftirfarandi lani i tiltekinn fjolda manuda ")
	print(lan[0].nafn)
	print(lan[1])

print "Midad vid heildargreidslugetu til utborgunar er haesta mogulegt husnaedislan: "
print haestaMogulegtLan(heildargreidslugeta)
