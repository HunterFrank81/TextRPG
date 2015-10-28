__author__ = 'Frank'

from csv import reader

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
#Just a list of common tags that are used
RoomTags = ['visited','unlit','dark']
ConnectionTags = ['closed','locked','hidden']

class Room:
	def __init__(self,id,name="",):
		self.id = id		#ID of the room
		self.name = name	#Name of the room
		self.connections = list()		#List of exits from this location
		self.descriptions = list()	#Description belonging to a room
		self.visited = False	#Flag if the room was visited or not
		self.tags = list()

	def get_description(self):
		"""
		Outputs the description text for this room.
		Will be extended later to things and creatures
		"""
		#Room descriptions
		out = ""
		for d in self.descriptions:
			if out != "":
				out += " "		#Add blank in between descriptions
			out = out + d.get_text(self.tags)
		description = out
		#Connections
		out = ""
		for c in self.connections:
			if out == "":
				out += "\n"		#Add line break with first connection
			out += c.get_description(self.tags)
		description += out
		#Return overall result
		return description

class Connection:
	def __init__(self,id,roomTo,name="",locked_DC=0,hidden_DC=0):
		self.id = id				#ID of the connection
		self.roomTo = roomTo	#Other room the connection links to
		self.name = name		#Name to be displayed in menu choices
		self.descriptions = list()	#Descriptions text to be displayed in room description
		self.locked_DC = locked_DC		#DC to open if locked - 0 means can be opened automatically
		self.hidden_DC = hidden_DC		#DC to find secret door - 0 means will be found automatically
		self.tags = list()			#Tags that describe the state of the connection

	def get_description(self,roomTags):
		"""
		Outputs all relevant descriptions of a connection
		"""
		out = ""
		for d in self.descriptions:
			if out != "":
				out += " "		#Add blank in between descriptions
			out += d.get_text(self.tags + roomTags)	#Add room tags for things like 'Dark','unlit', etc.
		return out

class Description:
	"""
	This class contains descriptions and criterias when to write it
	"""
	def __init__(self, text="",show=list(),omit=list()):
		self.text = text		#Text of the description
		self.show = show		#Show only if room has at least 1 of the tags or is completely emtpy
		self.omit = omit		#Don't show if room has at least 1 of the tags. Overrides 'show'

	def get_text(self,tags):
		"""
		Checks if description should be displayed and returns text if necessary
		"""
		out = ""
		#Check if should be excluded and included (if show is empty or has at least 1 tag in show
		print (not any(i in self.omit for i in tags))
		print any(i in self.show for i in tags)
		print (self.show[0] == '')
		if (not any(i in self.omit for i in tags)) and (self.show[0] == '' or any(i in self.show for i in tags)):
			out = self.text
		return out

def initialize_rooms():
	"""
	Reads in a list of rooms and connections and generates the proper object structure for it
	:return:
	Returns a list of rooms with all relevant things attached to it
	"""
	# Get room basics
	rooms = list()
	with open('data/rooms.csv','rb') as csvfile:
		data =  reader(csvfile, delimiter='|', quotechar='"')
		for row in data:
			rooms.append(Room(id=int(row[0]), name=row[1]))
			print row

	# Get room descriptions
	with open('data/roomDescriptions.csv','rb') as csvfile:
		data = reader(csvfile, delimiter='|', quotechar='"')
		for row in data:
			roomId = int(row[0])
			text =  row[1]
			show = row[2].replace(', ',',').split(',')
			omit = row[3].replace(', ',',').split(',')
			rooms[roomId].descriptions.append(Description(text, show, omit))

	# Get room Tags
	with open('data/roomTags.csv','rb') as csvfile:
		data = reader(csvfile, delimiter='|', quotechar='"')
		for row in data:
			id = int(row[0])
			rooms[id].tags.append(row[1])

	#Iniktialize connections and add to rooms
	roomId, connections = initialize_connections(rooms)
	for i in range(0,len(connections)):
		rooms[roomId[i]].connections.append(connections[i])

	return rooms

def initialize_connections(rooms):
	"""
	Initializes all connections between rooms
	:return:
	2 lists - one with the
	"""
	# Get connections
	roomIds = list()
	connections = list()
	with open('data/connections.csv','rb') as csvfile:
		data = reader(csvfile, delimiter='|', quotechar='"')
		for row in data:
			id = int(row[0])
			roomFromId = int(row[1])
			roomToId = int(row[2])
			name = row[3]
			locked_DC = int(row[4])
			hidden_DC = int(row[5])
			connections.append(Connection(id, rooms[roomToId], name=row[2], locked_DC=locked_DC, hidden_DC=hidden_DC))
			roomIds.append(roomFromId)

	# Get connection descriptions
	with open('data/connectionDescriptions.csv','rb') as csvfile:
		data = reader(csvfile, delimiter='|', quotechar='"')
		for row in data:
			id = int(row[0])
			text =  row[1]
			show = row[2].replace(', ',',').split(',')
			omit = row[3].replace(', ',',').split(',')
			connections[id].descriptions.append(Description(text, show, omit))

	# Get connection tags
	with open('data/connectionTags.csv','rb') as csvfile:
		data = reader(csvfile, delimiter='|', quotechar='"')
		for row in data:
			id = int(row[0])
			connections[id].tags.append(row[1])

	return roomIds, connections
