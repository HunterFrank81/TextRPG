__author__ = 'Frank'
# -*- coding: iso-8859-1 -*-

###Import other classes and other stuff
from player import Player
import player
import room

###Declaration of global variables
rooms = list()
p = Player()

###The "main" function, not to be confused with anything to do with main above it###
def main():
	"""Main function. Check if a savegame exists, and if so, load it. Otherwise
	initialize the game state with defaults. Finally, start the game.
	"""
	p.GenerateCharacter()

if __name__ == '__main__':
	main()

###end main function###
