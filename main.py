__author__ = 'Frank'
# -*- coding: iso-8859-1 -*-

###Import other classes and other stuff
from player import Player
from helper import PickFromList, PickFromList_Room
import json
import locations
import os
import room
from config import DEBUG, FULL

###Declaration of global variables
rooms = list()
#currentRoom = locations.Room()
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
        #Game mode of ROOM
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
            if DEBUG:
                print(choice_options)
            action, action_type = PickFromList_Room(message, choice_options, GENERAL_OPTIONS)
            if DEBUG:
                print(action_type, '-', action)
            #Query the action from the character

            #Based on settings, change the game mode and do the action
            if action_type == 'General':
                game_mode = GENERAL_GAME_MODES[action]
            else:
                game_mode = action_type            
        #Game mode CONNECTIONS        
        if game_mode == 'Connections':
            #Select the chosen connection
            con = currentRoom.connections[action]
            
            #Check if the connection is locked
            if 'locked' in con.tags:
                #Tell the character that the door is closed
                message = "The '" + con.name + "' is closed. Do you want to open it?"
                reply = PickFromList(message, dct = {'Y' : '(Y)es', 'N' : '(N)o'})
                if reply == 'Y':
                    message = "The '" + con.name + "' seems to be locked. What do you want to do?"
                    reply = PickFromList(message, lst = ['Bash', 'Pick lock', 'Use magic', 'Leave'])
                    #TO DO - execute action
                    if con.OpenDoor(reply, p):
                        #If successful, move to the other room
                        currentRoom = con.room
                    
            #Check if the connection is closed
            elif 'closed' in con.tags:
                #Do a listening check before entering the next room
                #TO DO
                #Tell the character that the door is closed
                message = "The '" + con.name + "' is closed. Do you want to open it?"
                reply = PickFromList(message, dct = {'Y' : '(Y)es', 'N' : '(N)o'})
                if reply == 'Y':
                    #Change status from open to close
                    con.tags.remove('closed')
                    con.tags.append('open')
                    print("You open the '", con.name, "' and continue your journey.", sep = '')
                    #Move to the other room
                    currentRoom = con.room
            #Check if room is open
            elif 'open' in con.tags:
                #Move to other room
                currentRoom = con.room

            #Go back to game mode ROOM afterwards
            game_mode = 'Room'

                
        elif game_mode == 'Battle':
            #DO SOMETHING
            print('bla')
        else:
            if action == 'C':
                p.DisplayStats()
                game_mode = 'Room'
            if action == 'M':
                print("This was not a wise decision...", "Game mode =", game_mode)
                game_mode = 'Game over'
            else:
                print("In construction - do not enter!")
                game_mode = 'Room'
            
            
if __name__ == '__main__':
    main()

###end main function###
