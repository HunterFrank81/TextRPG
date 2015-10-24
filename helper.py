__author__ = 'Frank'

###PickFromList takes the task to pick from a list of features
def PickFromList(message, lst):
	selection = 0
	print message + StringFromList(lst,numbering=True)
	while selection not in range(1,len(lst)+1):
		try:
			selection = int(raw_input("> "))
		except:
			print "Please enter a number between 1 and " + str(len(lst))
		else:
			if selection not in range(1,len(lst)+1):
				print "Please enter a number between 1 and " + str(len(lst))
	return lst[selection-1]

###StringFromList concatenates all entries from a list, separated by a comma. Optionally adds numbering
def StringFromList(lst, numbering = False):
	out = ""
	for index, item in enumerate(lst):
		if index > 0:
			out += ", "
		if numbering:
			out += str(index+1) + ". "
		out += item
	return out