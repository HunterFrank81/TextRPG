__author__ = 'Frank'
# -*- coding: iso-8859-1 -*-

###Import other classes and other stuff
from player import Player
from helper import PickFromList, PickFromList_Room
import json
import os
import room

### Helper stuff
FULL = False

###Declaration of global variables
rooms = list()
p = Player()
GENERAL_OPTIONS = {'M' : '(M)enu', 'C' : '(C)haracter overview', 'I' : '(I)nventory', 'R' : '(R)est', 'S' : '(S)pell', 'U' : '(U)se item'}
GAME_MODES = ['Room', 'Connections', 'Item', 'Creature', 'Battle', 'Game over']
GENERAL_GAME_MODES = {'M': 'Menu', 'C': 'Character overview', 'I': 'Inventory', 'R': 'Rest', 'S': 'Spell', 'U': 'Use item'}

###The "main" function, not to be confused with anything to do with main above it###
def main():
    """Main function. Check if a savegame exists, and if so, load it. Otherwise
    initialize the game state with defaults. Finally, start the game.
    """
    if FULL:
        p.GenerateCharacter()
        p.DisplayStats()
    else:
        p.name = 'Horst'
        
    #Initialize rooms
    rooms = room.CreateRooms()
    
    #Initialize game state variables
    currentRoom = rooms[0]
    game_mode = 'Room'
    
    #Main game loop
    while not game_mode == 'Game over':
        if game_mode == 'Room':    
            #Get information of the current room
            currentRoom.Describe()
            exits = currentRoom.ListExits()
            items = currentRoom.ListItems()
            creatures = currentRoom.ListCreatures()
            
            #Build the list of options we need
            choice_options = {'Connections': exits, 'Item' : items, 'Creature': creatures}
            #Now we need to constuct our list, but from a dictionary of 
            message = "\n" + p.name + ", what do you want to do next?"
            print(choice_options)
            action, action_type = PickFromList_Room(message, choice_options, GENERAL_OPTIONS)
            print(action_type, '-', action)
            #Query the action from the character

            #Based on settings, change the game mode and do the action
            if action_type == 'General':
                game_mode = GENERAL_GAME_MODES[action]
            else:
                game_mode = action_type            
        if game_mode == 'Connections':
            #Check if the chosen connection is open. If yes, go to the next room
            print('bla')
            game_mode = 'Game over'
        elif game_mode == 'Battle':
            #DO SOMETHING
            print('bla')
        else:
            print("This was not a wise decision...", "Game mode =", game_mode)
            game_mode = 'Game over'
            
if __name__ == '__main__':
    main()

###end main function###
