class lan:
	#Lan med jofnum afborgunum
	#F: verdtryggt er True ef lan er verdtryggt annars False.
	def __init__(self,nafn,vextir,verdtryggt,timi,hofudstoll,verdbolga):
		self.nafn = nafn
		self.vextir = vextir
		self.verdtryggt = verdtryggt
		self.timi = timi
		self.hofudstoll = hofudstoll
		self.raunvextir = vextir
		if verdtryggt == True:
			self.raunvextir = vextir + verdbolga
			
#N: [vaxtagreidslur, heildargreidslur] = lanVenjulega(lan)
#E: vaxtagreidslur er listi af manadarlegum upphaedum sem borgadar eru i vexti af lani 
#	og heildargreidslur er listi af heildargreidslum a manudi.
def lanVenjulega(lan):
	afborgun = lan.hofudstoll/lan.timi
	heildargreidslur = []
	vaxtagreidslur = []
	hofudstoll = lan.hofudstoll
	for i in range(0,lan.timi):
		vaxtagreidslur.append((hofudstoll - (i * hofudstoll / lan.timi)) * lan.raunvextir)
		heildargreidslur.append(vaxtagreidslur[i] + afborgun)
	return {"vaxtagreidslur" : vaxtagreidslur, "heildargreidslur" : heildargreidslur}

#N: #N: [vaxtagreidslur, heildargreidslur] = lanVenjulega(lan,greidslugeta)
#E: vaxtagreidslur er listi af manadarlegum upphaedum sem borgadar eru vexti af lani 
#	og heildargreidslur er listi af heildargreidslum a manudi. Baedi midad vid aukaframlag a manudi
# 	sem nemur greidslugetunni.
def lanAukalega(lan, greidslugeta):
	afborgun = lan.hofudstoll / lan.timi 
	heildargreidslur = []
	vaxtagreidslur = []
	hofudstoll = lan.hofudstoll
	for i in range(0,lan.timi):
		vaxtagreidslur.append((hofudstoll - (i * (hofudstoll/lan.timi))) * lan.raunvextir)
		heildargreidslur.append(vaxtagreidslur[i] + afborgun)
		hofudstoll = hofudstoll - greidslugeta
		afborgun = hofudstoll/lan.timi
		
		if hofudstoll <= 0:
			break
			
	return {"vaxtagreidslur" : vaxtagreidslur, "heildargreidslur" : heildargreidslur}

#N: [max_lan, lanastadur] = maxLan(lanalisti)
#F: lanalisti er listi af lanum
#E: max_lan er tad lan i lanalista med haestu raunvexti og lanastadur er stadsetning thess i listanum.
def maxLan(lanalisti):
	max = -1.0
	max_lan = []
	i = 0
	lanastadur = 0
	for lan in lanalisti:
		if lan.raunvextir > max:
			max_lan = lan
			lanastadur = i
		i = i + 1

	return [max_lan,lanastadur];

#N: max = maxAllt(maxreikningr,maxlan)
#E: max er annadhvort maxreikningur eda maxlan - eftir tvi hvort hefur haerri raunvexti
def maxAllt(maxreikningur, maxlan):
	
	if maxlan.raunvextir > maxreikningur.raunvextir:
		return maxlan
	else:
		return maxreikningur

#N: [[bestalan,timi_greidslu]] = bestaGreidsluskiptingLana(lanalisti,greidslugeta,timi)
#F: lanalisti er listi af lanum, greidslugeta er manadarleg upphaed og timi er fjoldi manadarlegra upphaeda
#E: bestalan er hagkvaemasta lan til ad greida og timi_greidslu er hversu oft greitt var af bestalan. 
#	Ytri listinn er radadur fra hagkvaemasta lani til ad greida af til thess ohagkvaemasta
def bestaGreidsluskiptingLana(lanalisti,greidslugeta,timi):
	lan_sorted = [] #holdum utan um laninn i rod eftir greidsluhagkvaemni 
	new_lanalisti = list(lanalisti) 
	timi_greidslu = timi #Manudir sem vid eigum eftir af heildartima
	for i in range(0,len(lanalisti)):
		besta = maxLan(new_lanalisti)[0] #Hagkvaemast ad greida besta 
		stadsetning = maxLan(new_lanalisti)[1] #
		greidslur = lanAukalega(besta,greidslugeta)
		if len(greidslur["vaxtagreidslur"]) < timi_greidslu: #Enn timi eftir fyrir fleiri lan
			new_lanalisti.pop(stadsetning) #Eydum besta ur listanum og finnum naest besta af teim stokum sem eru eftir
			timi_greidslu = timi_greidslu - len(greidslur["vaxtagreidslur"])
			lan_sorted.append([besta,len(greidslur["vaxtagreidslur"])])
		else: #Ekki timi fyrir fleiri lan
			lan_sorted.append([besta,timi_greidslu])  
			break
<<<<<<< HEAD
	return lan_sorted
	

#N: lan = haestaMogulegtLan(heildargreidslugeta)
#F: heildargreidslugeta er heildarupphaed sem er laus til að greida i husnaedi
#E: lan er haesta mogulegt lan sem haegt er taka midad vid greidslugetu
def haestaMogulegtLan(heildargreidslugeta):
	return heildargreidslugeta/0.15 - heildargreidslugeta

	
	
	
	
=======
	return lan_sorted
>>>>>>> a6511bfb557a82b7abc6e3b79d70752167ba7965
