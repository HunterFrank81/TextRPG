__author__ = 'Frank'

"""
Class room
Contains information belonging to rooms
- ID - the ID of the room
- Name - the name of the room
- Connections - List of conneection objects with info whether they are visible or closed
- lighting - Light status of the room
- descriptions - list of descriptions with certain criterias when to display
- objects - List of objects within the room
"""

import os
import csv
import description
from helper import AddText, CreateHeader, DoTest
from config import DEBUG

RoomLighting = ['lit','unlit','dark']
LockedStatus = ['open','closed','locked', 'hidden']

class Room:
    def __init__(self):
        self.id = 0        #ID of the room
        self.name = ""    #Name of the room
        self.connections = dict()        #Dictionary of exits from this location
        self.lighting = RoomLighting[0]
        self.descriptions = list()    #Dictionary belonging to a room
        self.tags = list()  #List of tags that are used for displaying a room
    
    #Write description of a room based on a list of tags
    def Describe(self):
        text = CreateHeader(self.name)        
        #General description of room       
        for desc in self.descriptions:
            text = AddText(text,desc.Tell(self.tags))
    
        #Desccribe connections to other rooms
        text = AddText(text,"",newLine=True)        
        for key, con in self.connections.items(): 
            text = AddText(text, con.Describe(self.tags), newLine=True)
            
        #Describe items within room
    
        #Describe creatures within room
    
        #Output to console
        print(text)
    
    def ListExits(self):
        """
        Returns a list of names of all visible connections
        """
        out = []
        for key, con in self.connections.items():
            if not 'hidden' in con.tags:
                out.append(con.name)
        return out
    
    def ListItems(self):
        return []

    def ListCreatures(self):
        return []

class Connection:
    def __init__(self):
        self.room = None    #Other room the connection links to
        self.name = ""        #Name to be displayed in menu choices
        self.descriptions = list()    #List of descriptions text to be displayed in room description
        self.state = "open"     #State of the connection        
        self.locked_DC = 15        #DC to open if locked - 0 means can be opened automatically
        self.hidden_DC = 10        #DC to find secret door - 0 means will be found automatically
        self.bash_DC = 10        #DC to bash open a locked door
        self.tags = list()      #List of tags that are used for classifying a connection
    
    #Outputs the description of a connection
    def Describe(self, room_tags):
        text = ""
        for desc in self.descriptions:
            text = AddText(text, desc.Tell(self.tags + room_tags))
        
        return text
    
    def OpenDoor(self, action, p):
        """
        Contains the game logic for bashing a door, picking a lock or using a magic spell to open the door
        """
        res = False
        if action == 'Bash':
            res = DoTest(p.attributes['STR'], self.bash_DC)
            if res:
                print('You successfully bashed open the', self.name, ' and boldly continue your journey.')
            else:
                print('You try hard but do not manage the open the ', self.name, '. Weakling.', sep = '')
        elif action == 'Pick lock':
            #TO DO: add disadvantage if no lockpicking equipment is included in inventory
            if DEBUG:
                print('locked_DC is of type', type(self.locked_DC))
            res = DoTest(p.attributes['DEX'], self.locked_DC, advantage = ('Locks and traps' in p.skills))
            if res:
                print('You successfully picked the lock of the', self.name, 'and boldly continue your journey.')
            else:
                print('You try hard but do not manage to open the ', self.name, '. Disappointing.', sep='')
        if res:
            #Change status of door
            self.tags.remove('locked')
            self.tags.append('open')
        #Return result of test
        return res

#Returns a list of all room objects to be read in
def CreateRooms():
    rooms = list()
    
    #Create list of rooms
    with open(os.curdir + '/data/rooms.csv','r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            dat = str.split(row[0],sep='|')
            room = Room()
            room.id = int(dat[0])
            room.name = dat[1]
            rooms.append(room)
    
    #Create list of room descriptions
    for tup in description.CreateDescriptions('room'):
        rooms[tup[0]].descriptions.append(tup[1])
    
    #Read in list of roomTags    
    with open(os.curdir + '/data/roomTags.csv','r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            dat = str.split(row[0],sep='|')            
            rooms[int(dat[0])].tags.append(dat[1])
    
    #Create list of connections
    for tup in CreateConnections(rooms):
        con = tup[1]
        rooms[tup[0]].connections[con.name] = con
    
    return rooms
    
#Returns a list containing tuples of (roomID, connection)
def CreateConnections(rooms):
    connections = list()
    with open(os.curdir + '/data/connections.csv','r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            dat = str.split(row[0],sep='|')
            con = Connection()
            con.room = rooms[int(dat[2])]
            con.name = dat[3]
            con.locked_DC = int(dat[4])
            con.hidden_DC = int(dat[5])
            connections.append((int(dat[1]),con))
    
    #Read in list of connection descriptions
    for tup in description.CreateDescriptions('connection'): 
        connections[tup[0]][1].descriptions.append(tup[1])

    #Read in list of connection tags
    with open(os.curdir + '/data/connectionTags.csv','r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            dat = str.split(row[0],sep='|')
            connections[int(dat[0])][1].tags.append(dat[1])
            
    return connections