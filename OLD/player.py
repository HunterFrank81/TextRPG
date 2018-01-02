__author__ = 'Frank'

from random import randint
from helper import PickFromList, StringFromList, CreateHeader
import json

charClasses = ['Fighter','Thief','Cleric','Wizard']
classHPperLevel = {'Fighter' : 4,
                  'Cleric': 3,
                  'Thief': 2,
                  'Wizard': 2}
classAttackBonusPerLevel = {'Fighter' : 1.0,
                              'Cleric': 0.5,
                             'Thief': 0.5,
                            'Wizard': 1.0/3}
classFrayDice = {'Fighter' : 8,
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
clericSpellList = [['Cure light wounds', 'Bless', 'Destroy undead'],
                   ['Might', 'Cure level drain', 'Cure poison']]
wizardSpellList = [['Magic missile', 'Mage armor', 'Shield'],
                   ['Mirror image', 'Invisibility', 'Scorching ray']]

xpPerLevel = 100

class Player:

    def __init__(self):
        self.name = ""        #Name of the character
        self.charClass = charClasses[0]    #Class of the character
        self.currentHP = 0        #Hit points
        self.maxHP = 8    #Maximum hit points
        self.level = 1    #Level
        self.attributes = dict()    #Dictionary of the 6 attributes
        self.skills =  list()        #List of skills a character is trained in
        self.XP = 0     #Number of experience points

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def RollAttributes(self):
        bonus = 0
        while bonus <= 0:
            for attr in attributesList:
                self.attributes[attr] = randint(1,6) + randint(1,6) + randint(1,6)
                bonus += GetBonus(self.attributes[attr])

    def GenerateCharacter(self):
        print(CreateHeader("Character Generation"))
        print("Enter your name, adventurer!")
        self.name = input("> ")
        
        #Roll attributes
        print("The gods gifted %s with these attributes:" % self.name)
        self.RollAttributes()
        for key in self.attributes:
            print("%s : %s (%s)" % (key,DisplayAttribute(self.attributes[key]),DisplayBonus(self.attributes[key])))

        #Choose class
        self.charClass = PickFromList("\nChoose your profession: ",charClasses)

        #Set things based on class info
        self.maxHP = classHPperLevel[self.charClass] * 2 + GetBonus(self.attributes['CON'])
        self.currentHP = self.maxHP

        #Select skills
        numSkills = classNumberOfSkills[self.charClass]
        print("%s, select %s skills you excel in!" % (self.name,numSkills))
        for i in range(numSkills,0,-1):
            self.skills.append(PickFromList(str(i) + " remaining: ",[x for x in skillsList if x not in self.skills]))
            
        #Select spells

    def AttackBonus(self):
        return int(round(self.level * classAttackBonusPerLevel[self.charClass],0))

    def FrayDice(self):
        return classFrayDice[self.charClass]

    def DisplayStats(self):
        print("You are %s, the %s." % (self.name, self.charClass))
        print("You have %s/%s HP, an attack bonus of %s, and a D%s fray dice." % (self.currentHP, self.maxHP, self.AttackBonus(), self.FrayDice()))
        print("Your attributes are: " + DisplayAttributes(self.attributes))
        print("Your are skilled in: " + StringFromList(self.skills) + ".")
        print("You are on level %s with %s XP. You need %s additional XP to reach the next level." % (self.level, self.XP, self.xpToLevelUp()))
        print("\nPress Enter to continue adventuring...")
        #TO DO - add additional information
        
    def xpToLevelUp(self):
        return (self.level * (self.level + 1)) / 2 * xpPerLevel - self.XP

def DisplayAttributes(attributes):
    res = ""
    for key in attributes:
        if res != "":
            res += ", "
        res += key + " " + DisplayAttribute(attributes[key]) + " (" + DisplayBonus(attributes[key]) + ")"
    return res

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