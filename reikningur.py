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
#F: greidslugeta => 0, vextir => 0
#E: sparn = greidslugeta * (vextir + verdbolga)/12 - eda raunvextir af greidslugetu fyrir einn manud
def sparnadurVaxtagrodi(greidslugeta, vextir, verdbolga):
	raunvextir = vextir + verdbolga
	return greidslugeta * (raunvextir/12.0)

#N: sparn = sparnadurTimi(timi,greidslugeta,vextir,verdbolga)
#F: greidslugeta => 0, vextir => 0, timi => 0
#E: sparn = timi * (greidslugeta * (vextir + verdbolga)/12) - eda heildar raunvextir af greidslugetu fyrir tima marga manudi
def sparnadurTimi(timi,greidslugeta,vextir,verdbolga):
	return  sparnadurVaxtagrodi(greidslugeta, vextir, verdbolga) * timi