__author__ = 'Frank'
# -*- coding: iso-8859-1 -*-

###Import other classes and other stuff
from player import Player
import locations
import os

###Declaration of global variables
rooms = list()
#currentRoom = locations.Room()
p = Player()

###The "main" function, not to be confused with anything to do with main above it###
def main():

	os.chdir('G:\\Programmieren\\TextRPG')

	#Load data
	rooms = locations.initialize_rooms()
	currentRoom = rooms[0]

	#Character generation
	#p.generate_character()

	#Start with first room
	print currentRoom.get_description()

	with open('test.json','w') as outfile:
		outfile.write(p.to_JSON())

if __name__ == '__main__':
	main()

###end main function###
