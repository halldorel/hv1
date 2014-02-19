import unittest
from reikningur import *
from lan import *

verdbolga = 0.04
hofudstoll = 10000000
greidslugeta = 10000
heildargreidslugeta = 10000000
		
lanalistiAnVerd = []
lanalistiAnVerd.append(lan("versta",0.0180,False,12,hofudstoll,verdbolga))
lanalistiAnVerd.append(lan("besta",0.0445,False,12,hofudstoll,verdbolga))
lanalistiAnVerd.append(lan("naestbesta",0.0425,False,12,400000,verdbolga))
lanalistiAnVerd.append(lan("naestversta",0.0190,False,12,hofudstoll,verdbolga))
		
lanalistiMedVerd = []
lanalistiMedVerd.append(lan("besta",0.0180,True,12,hofudstoll,verdbolga))
lanalistiMedVerd.append(lan("naestbesta",0.0445,False,12,hofudstoll,verdbolga))
lanalistiMedVerd.append(lan("naestversta",0.0425,False,12,hofudstoll,verdbolga))
lanalistiMedVerd.append(lan("versta",0.0190,False,12,hofudstoll,verdbolga))

reikAnVerd = []
reikAnVerd.append(reikningur("naestversti",0.0180,False,verdbolga))
reikAnVerd.append(reikningur("besti",0.0445,False,verdbolga))
reikAnVerd.append(reikningur("naestbesti",0.0425,False,verdbolga))
reikAnVerd.append(reikningur("versti",0.0190,False,verdbolga))
		
reikMedVerd = []
reikMedVerd.append(reikningur("besti",0.0180,True,verdbolga))
reikMedVerd.append(reikningur("naestbesti",0.0445,False,verdbolga))
reikMedVerd.append(reikningur("naestversti",0.0425,False,verdbolga))
reikMedVerd.append(reikningur("versti",0.0190,False,verdbolga))

class testLan(unittest.TestCase):
		
	def test_bestaGreidsluskiptingLana(self):
		self.assertEqual(bestaGreidsluskiptingLana(lanalistiAnVerd,10000,20)[0][0].nafn, "besta")
		self.assertEqual(bestaGreidsluskiptingLana(lanalistiMedVerd,10000,20)[0][0].nafn, "besta")
		
	def test_maxAllt(self):
		self.assertEqual(maxAllt(lanalistiAnVerd[1],reikAnVerd[0]).nafn,"besta")

	def test_maxLan(self):
		self.assertEqual(maxLan(lanalistiAnVerd)[0].nafn,"besta")
		self.assertEqual(maxLan(lanalistiAnVerd)[1],1)
	
	def test_lanAukalega(self):
		lanAukalega(lanalistiAnVerd[0],10000)
		self.assertEqual(int(sum(lanAukalega(lanalistiAnVerd[0],10000)['heildargreidslur'])-sum(lanAukalega(lanalistiAnVerd[0],10000)['vaxtagreidslur'])),10000000)
		self.assertEqual(int(sum(lanAukalega(lanalistiAnVerd[2],10000)['heildargreidslur'])-sum(lanAukalega(lanalistiAnVerd[2],10000)['vaxtagreidslur'])),400000)
	
	#Athugar hvort munurinn a heildargreidslum og vaxtargreidslum se ekki orugglega jafn hofudstolnum
	def test_lanVenjulega(self):
		lanVenjulega(lanalistiAnVerd[0])
		self.assertEqual(int(sum(lanVenjulega(lanalistiAnVerd[0])['heildargreidslur'])-sum(lanVenjulega(lanalistiAnVerd[0])['vaxtagreidslur'])),9999996)
		self.assertEqual(int(sum(lanVenjulega(lanalistiAnVerd[2])['heildargreidslur'])-sum(lanVenjulega(lanalistiAnVerd[2])['vaxtagreidslur'])),399996)
		
	def test_haestaMogulegtLan(self):
		self.assertEqual(int(haestaMogulegtLan(heildargreidslugeta)),56666666)
		
	def test_validLan(self):
		self.assertEqual(validLan("Krummi",2.0,True,19,12324234.0,9.4),True)
		self.assertEqual(validLan("Krummi",2.0,30,19,12324234.0,9.4),False)
		self.assertEqual(validLan(1,2.0,True,19,12324234.0,9.4),False)
		self.assertEqual(validLan("Krummi",2.0,True,"krummi",12324234.0,9.4),False)
		self.assertEqual(validLan("Krummi",2.0,True,19,12324234,9.4),False)
		self.assertEqual(validLan("Krummi",2.0,True,19,12324234,9),False)
		
class testReikningur(unittest.TestCase):
		
	def test_maxReikningar(self):
		self.assertEqual(maxReikningar(reikAnVerd).nafn,reikAnVerd[1].nafn)
		self.assertEqual(maxReikningar(reikMedVerd).nafn,reikMedVerd[0].nafn)

	def test_sparnadurVaxtagrodi(self):
		self.assertEqual(sparnadurVaxtagrodi(10000,0.05,verdbolga),75.0)
		self.assertEqual(sparnadurVaxtagrodi(10000,0.05,-0.02),25.0)

	def test_sparnadurTimi(self):
		self.assertEqual(sparnadurTimi(10,10000,0.05,verdbolga),750)
		self.assertEqual(sparnadurTimi(10,10000,0.05,-0.02),250)
	
	def test_sparnadurTimiHeild(self):
		self.assertEqual(int(sparnadurTimiHeild(10,10000,0.05,0,10000000)),10517083)
		
if __name__ == '__main__':
	unittest.main()
