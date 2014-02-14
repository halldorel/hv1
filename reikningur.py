class reikningur:
	#Bankareikningur 
	#Verdtryggt er True ef reikningur er verdtryggdur en annars False
	def __init__(self,nafn,vextir,verdtryggt,verdbolga):
		self.nafn = nafn
		self.vextir = vextir
		self.verdtryggt = verdtryggt
		self.raunvextir = vextir
		if verdtryggt == True:
			self.raunvextir = vextir + verdbolga
		else
			self.verdbolga = 0
		
#N: max_reikningur = maxReikningar(reikningar)
#F: reikningar er listi af reikningum
#E: max_reikningur er sa reikningur i listanum sem hefur haestu raunvexi
def maxReikningar(reikningar):
	max = -1.0
	max_reikningur = []
	for reikningur in reikningar:
		if reikningur.raunvextir > max:
			max_reikningur = reikningur
			max = reikningur.raunvextir

	return max_reikningur;

#N: sparn = sparnadurVaxtagrodi(greidslugeta,vextir,verdbolga)
#E: sparn = greidslugeta * (vextir + verdbolga)/12 - eda raunvextir af greidslugetu fyrir einn manud
def sparnadurVaxtagrodi(greidslugeta, vextir, verdbolga):
	raunvextir = vextir + verdbolga
	return greidslugeta * (raunvextir/12.0)

#N: sparn = sparnadurTimi(timi,greidslugeta,vextir,verdbolga)
#F: timi er fjoldi manada sem sparad er og greidslugeta er manadarlegur sparnadur
#E: sparn = timi * (greidslugeta * (vextir + verdbolga)/12) - eda heildar raunvextir af greidslugetu fyrir tima marga manudi
def sparnadurTimi(timi,greidslugeta,vextir,verdbolga):
	return  sparnadurVaxtagrodi(greidslugeta, vextir, verdbolga) * timi

#N: sparn = sparnadurTimiHeild(timi,greidslugeta,vextir,verdbolga)
#F: timi er fjoldi manada sem sparad er og greidslugeta er manadarlegur sparnadur og hofustoll er upphaed fyrir
#E: sparn = timi * (greidslugeta * (vextir + verdbolga)/12) + (timi * greidslugeta) - eda heildarupphaed i lok sparnadar 
def sparnadurTimiHeild(timi,greidslugeta,vextir,verdbolga,hofudstoll):
	return sparnadurTimi(timi,greidslugeta,vextir,verdbolga) + (timi * greidslugeta) + (sparnadurTimi(hofudstoll,vextir,verdbolga)) + hofudstoll

	
