__author__ = 'Frank'
# -*- coding: iso-8859-1 -*-

###Import other classes and other stuff
from player import Player
import locations
import os

###Declaration of global variables
rooms = list()
currentRoom = locations.Room(1)
p = Player()

###The "main" function, not to be confused with anything to do with main above it###
def main():

	#Character generation
	p.GenerateCharacter()
	os.chdir('G:\\Programmieren\\TextRPG')
	with open('test.json','w') as outfile:
		outfile.write(p.to_JSON())

if __name__ == '__main__':
	main()

###end main function###
