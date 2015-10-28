__author__ = 'Frank'

from random import randint
from helper import pick_from_list, string_from_list
import json

charClasses = ['Fighter','Thief','Cleric','Wizard']
classHPperLevel = {'Fighter' : 4,
				  'Cleric': 3,
				  'Thief': 2,
				  'Wizard': 2}
classattack_bonusPerLevel = {'Fighter' : 1.0,
				  			'Cleric': 0.5,
				 			'Thief': 0.5,
							'Wizard': 1.0/3}
classfray_dice = {'Fighter' : 8,
				 'Cleric': 6,
				 'Thief': 6,
				 'Wizard': 4}
classNumberOfSkills = {'Fighter' : 2,
				 'Cleric': 2,
				 'Thief': 4,
				 'Wizard': 2}
attributesList = ['STR','DEX','CON','INT','WIS','CHA']
skillsList = ['Acrobatics','Arcana','Athletics','Intimidation','Knowledge',
			  'Locks and Traps','Medicine','Perception','Persuation','Stealth']

class Player:

	def __init__(self):
		self.name = ""		#Name of the character
		self.charClass = charClasses[0]	#Class of the character
		self.currentHP = 0		#Hit points
		self.maxHP = 8	#Maximum hit points
		self.level = 1	#Level
		self.attributes = dict()	#Dictionary of the 6 attributes
		self.skills =  list()		#List of skills a character is trained in


	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

	def roll_attributes(self):
		bonus = 0
		while bonus <= 0:
			for attr in attributesList:
				self.attributes[attr] = randint(1,6) + randint(1,6) + randint(1,6)
				bonus += get_bonus(self.attributes[attr])

	def generate_character(self):
		"""
		Character generation and all that belongs to it.
		:return:
		"""

		print "\nCHARACTER GENERATION:"
		print "---------------------"
		print "Enter your name, adventurer!"
		self.name = raw_input("> ")

		# Roll attributes
		print "The gods gifted %s with these attributes:" % self.name
		self.roll_attributes()
		for key in self.attributes:
			print "%s : %s (%s)" % (key,display_attribute(self.attributes[key]),display_bonus(self.attributes[key]))

		# Choose class
		self.charClass = pick_from_list("\nChoose your profession: ",charClasses)

		# Set things based on class info
		self.maxHP = classHPperLevel[self.charClass] * 2 + self.attr_bonus('CON')
		self.currentHP = self.maxHP

		#Select skills
		numSkills = max(classNumberOfSkills[self.charClass] + self.attr_bonus('INT'), 1)
		print "%s, select %s skills you excel in!" % (self.name,numSkills)
		for i in range(numSkills, 0, -1):
			self.skills.append(pick_from_list(str(i) + " remaining: ", [x for x in skillsList if x not in self.skills]))

		#Give final overview
		print "You have %s HP and an attack bonus of %s." % (self.maxHP, self.attack_bonus())
		print "Your skills are: " + string_from_list(self.skills)
		print "Venture forth, %s the %s!" % (self.name, self.charClass)

	def attack_bonus(self):
		return round(self.level * classattack_bonusPerLevel[self.charClass], 0)

	def fray_dice(self):
		return classfray_dice[self.charClass]

	def attr_bonus(self,attr):
		return get_bonus(self.attributes[attr])

def display_attribute(attr):
	###Displays attribute score with trailing blank for scores <10
	res = ""
	if attr < 10: res = " "
	return res + str(attr)

def get_bonus(attr):
	###Returns attribute bonus based on attribute
	if attr == 3:
		return -3
	elif attr <= 5:
		return -2
	elif attr <= 8:
		return -1
	elif attr <= 12:
		return 0
	elif attr <= 15:
		return 1
	elif attr <= 17:
		return 2
	elif attr == 18:
		return 3
	else:
		return 0

def display_bonus(attr):
	###Displays bonus of a given attribute, including trailing "+" in front
	bonus = get_bonus(attr)
	res = ""
	if bonus >= 0: res ="+"
	return res +  str(bonus)