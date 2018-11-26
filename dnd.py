
import random
from dice import d4,d6,d8,d10,d12,d20
def main():
	#char = Character()
	player = Character()
	print(player.race,player.title)
	print(player.height)
	print(player.weight)
	print(player.family)
	

class Character(object):
	name =  ""
	race = ""
	age = 0
	height = ""
	weight = ""
	languages = []
	title = ""
	background = ""
	homeland=""
	family=""

	def __init__(self):
		self.name = ""
		self.age = random.randint(18,100)
		self.title = getTitle()
		#self.background = getBackground(title)
		self.race = getRace()
		size = getSize(self.race)
		ft = int(size[0]/12)
		inc = size[0]%12
		self.height = str(ft) + "'" + str(inc)+'"'
		self.weight = str(size[1]) + " lbs"
		self.family = getFamily()

	def show():
		print("Name: ", self.name)
		print("Age: ", self.age)
		print("Background: ", self.background)
		print("Name: ", name)
		print("Name: ", name)




def getRace():
	raceList = [
		'Dragonborn',
		'Dwarf',
		'Elf',
		'Gnome',
		'Half-Elf',
		'Half-Orc',
		'Halfling',
		'Human',
		'Tiefling'
	]
	return random.choice(raceList)

def getSize(race):
	if race == "Dragonborn":
		mod = d8(2)
		height = 66 + mod
		weight = 175 + mod*d6(2)
	if race == "Dwarf":
		mod = d4(2)
		height = 46 + mod
		weight = 120 + mod*d6(2)
	if race == "Elf":
		mod = d10(2)
		height = 54 + mod
		weight = 95 + mod*d4()
	if race == "Gnome":
		mod = d4(2)
		height = 35 + mod
		weight = 35 + mod
	if race == "Half-Elf":
		mod = d8(2)
		height = 57 + mod
		weight = 110 + mod*d4(2)
	if race == "Half-Orc":
		mod = d10(2)
		height = 58 + mod
		weight = 140 + mod*d6(2)
	if race == "Halfling":
		mod = d4(2)
		height = 31 + mod
		weight = 35 + mod
	if race == "Human":
		mod = d10(2)
		height = 56 + mod
		weight = 110 + mod*d4(2)
	if race == "Tiefling":
		mod = d8(2)
		height = 55 + mod
		weight = 110 + mod*d4(2)




	return (height,weight)




def background(title):
	title = title
	childhood_event=""
	parental_status= ""
	siblings=""
	adolescent_training= ""
	conflict=""
	conflict_subject=""
	coflict_goal=""
	deity=""
	romance=""




def getTitle():
	titleList=[
	'Soldier',
	'Spy',
	'Guild Artisan',
	'Guild Merchant',
	'Hermit',
	'Entertainer',
	'Folk Hero',
	'Gladiator',
	'Charlatan',
	'Acolyte',
	'Criminal',
	'Outlander',
	'Pirate',
	'Noble',
	'Knight',
	'Sage',
	'Urchin',
	'Sailor'
	]
	return random.choice(titleList)

def getFamily():


	momList = [
	"Your mother died in childbirth.",
	"Your mother was captured by slavers.",
	"Your mother is an alcoholic.",
	"You have a very loving mother.",
	"Your mother never loved you.",
	"You never knew your mother.",
	"Your mother is deceased.",
	"Your mother wants the best for you.",
	"You don't speak to your mother.",
	"Your mother owns a successful business in the city.",
	"Your mother is in prison.",
	"Your mother is very overprotective.",
	"Your mother mysteriously went missing one day.",
	"Your mother is a witch.",
	"Your mother is a famous warrior."
	]

	dadList = [
	"Your father is in prison", 
	"Your father just went out to get cigarettes, he'll be back soon.",
	"Your father is an alcoholic.",
	"Your father died in the war.",
	"Your father is abusive.",
	"Your father is a very kind and gentle-hearted man.",
	"Your father is deceased.",
	"You were never good enough for your father.",
	"Your father hates you.",
	"You don't know your father.",
	"Your father mysteriously disappeared one day.",
	"Your father is a famous general.",
	"Your father is the laughing-stock of the town.",
	"Your father is a hard-working man.",
	"Your father is a traveling merchant."
	]

	return random.choice(momList), random.choice(dadList)















if __name__ == '__main__':
	main()

