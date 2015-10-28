__author__ = 'Frank'

###pick_from_list takes the task to pick from a list of features
def pick_from_list(message, lst):
	selection = 0
	print message + string_from_list(lst,numbering=True)
	while selection not in range(1,len(lst)+1):
		try:
			selection = int(raw_input("> "))
		except:
			print "Please enter a number between 1 and " + str(len(lst))
		else:
			if selection not in range(1,len(lst)+1):
				print "Please enter a number between 1 and " + str(len(lst))
	return lst[selection-1]

###string_from_list concatenates all entries from a list, separated by a comma. Optionally adds numbering
def string_from_list(lst, numbering = False):
	out = ""
	for index, item in enumerate(lst):
		if index > 0:
			out += ", "
		if numbering:
			out += str(index+1) + ". "
		out += item
	return out