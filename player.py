__author__ = 'Frank'

from enum import Enum
from random import randint

charClasses = ['Fighter','Thief','Cleric','Wizard']
classHPperLevel = {'Fighter' : 4,
				  'Cleric': 3,
				  'Thief': 2,
				  'Wizard': 2}
classAttackBonusPerLevel = {'Fighter' : 1.0,
				  			'Cleric': 0.5,
				 			'Thief': 0.5,
							'Wizard': 1.0/3}
attributesList = ['STR','DEX','CON','INT','WIS','CHA']

class Player:

	def __init__(self):
		self.name = ""		#Name of the character
		self.charClass = charClasses[0]	#Class of the character
		self.HP = 0		#Hit points
		self.maxHP = 8	#Maximum hit points
		self.level = 1	#Level
		self.frayDice = 10	#Fray die to kill other monsters
		self.attributes = dict()

	def RollAttributes(self):
		bonus = 0
		while bonus <= 0:
			for attr in attributesList:
				self.attributes[attr] = randint(1,6) + randint(1,6) + randint(1,6)
				bonus += GetBonus(self.attributes[attr])

	def GenerateCharacter(self):
		print "\nCHARACTER GENERATION:"
		print "---------------------"
		print "Enter your name, adventurer!"
		self.name = raw_input("> ")
		#Roll attributes
		print "The gods gifted %s with these attributes:" % self.name
		self.RollAttributes()
		for key in self.attributes:
			print "%s : %s (%s)" % (key,DisplayAttribute(self.attributes[key]),DisplayBonus(self.attributes[key]))
		#Choose class
		out = ""
		selection = 0
		for index, item in enumerate(charClasses):
			if index > 0:
				out += ", "
			out += str(index+1) + ". " + item
		print "\nSelect your class: " + out
		while selection not in range(1,len(charClasses)+1):
			try:
				selection = int(raw_input("> "))
			except:
				print "Please enter a number between 1 and " + str(len(charClasses))
			else:
				if selection not in range(1,len(charClasses)+1):
					print "Please enter a number between 1 and " + str(len(charClasses))
		self.charClass = charClasses[selection-1]
		#Set things based on class info
		self.maxHP = classHPperLevel[self.charClass] * 2 + GetBonus(self.attributes['CON'])
		print "You have %s HP and an attack bonus of %s." % (self.maxHP,self.AttackBonus())
		print "Venture forth, %s the %s!" % (self.name, self.charClass)

	def AttackBonus(self):
		return round(self.level * classAttackBonusPerLevel[self.charClass],0)

def DisplayAttribute(attr):
	###Displays attribute score with trailing blank for scores <10
	res = ""
	if attr < 10: res = " "
	return res + str(attr)

def GetBonus(attr):
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

def DisplayBonus(attr):
	###Displays bonus of a given attribute, including trailing "+" in front
	bonus = GetBonus(attr)
	res = ""
	if bonus >= 0: res ="+"
	return res +  str(bonus)