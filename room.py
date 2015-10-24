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

RoomLighting = ['lit','unlit','dark']
LockedStatus = ['open','closed','locked']

class Room:
	def __init__(self):
		self.id = 0		#ID of the room
		self.name = ""	#Name of the room
		self.connections = None		#List of exits from this location
		self.lighting = RoomLighting[0]
		self.descriptions = ""	#Description belonging to a room

class Connection:
	def __init__(self):
		self.room = None	#Other room the connection links to
		self.name = ""		#Name to be displayed in menu choices
		self.description = ""	#Description text to be displayed in room description
		self.locked = LockedStatus[0]	#Flag if connection is open, closed, or locked
		self.locked_DC = 0		#DC to open if locked - 0 means can be opened automatically
		self.hidden = False		#Flag if connection is
		self.hidden_DC = 0		#DC to find secret door - 0 means will be found automatically
