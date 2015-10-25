__author__ = 'Frank'

import odbc

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

RoomLighting = ['lit','unlit','dark']
LockedStatus = ['open','closed','locked']

class Room:
	def __init__(self,id,name="",lighting=RoomLighting[0]):
		self.id = id		#ID of the room
		self.name = name	#Name of the room
		self.connections = None		#List of exits from this location
		self.lighting = lighting
		self.descriptions = None	#Description belonging to a room

class Connection:
	def __init__(self,roomTo,name="",description="",locked=LockedStatus[0],locked_DC=0,hidden=False,hidden_DC=0):
		self.room = roomTo	#Other room the connection links to
		self.name = name		#Name to be displayed in menu choices
		self.description = description	#Description text to be displayed in room description
		self.locked =locked	#Flag if connection is open, closed, or locked
		self.locked_DC = locked_DC		#DC to open if locked - 0 means can be opened automatically
		self.hidden = hidden		#Flag if connection is
		self.hidden_DC = hidden_DC		#DC to find secret door - 0 means will be found automatically

def InitializeRooms():
	"""
	Reads in a list of rooms and connections and generates the proper object structure for it
	:return:
	Returns a list of rooms with all relevant things attached to it
	"""
	#Read database
	print "This is still work in progres..."
