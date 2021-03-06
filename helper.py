__author__ = 'Frank'

from random import randint
from config import DEBUG

def PickFromList_Room(message, room_options = {}, general_options = {}):
    """
    Creates a list of all possible options in a room. Returns
    - the value of the chosen action
    - the type of the chosen action
    """
    selection = ""
    values = []
    types = []
    
    #Generate message for output - first based on room options
    text = message
    next_index = 1
    if len(room_options) > 0:
        for key, lst in room_options.items():
            if len(lst) > 0:
                text += '\n' + key + ' - ' + StringFromList(lst, next_index)
                next_index += len(lst)
                #Add key value to list of types
                values += lst
                types += [key] * len(lst)
    #Now add general options
    if len(general_options) > 0:
        text += '\n' + StringFromDict(general_options)
    print(text)
    
    out_value = ""
    out_type = ""
    while out_value == "":
        selection = input("> ")
        
        #Check if input is an "integer" for the list
        if IsInteger(selection):
            if int(selection) not in range(1,len(values)+1):
                print("Please enter a number between 1 and " + str(len(values)))
            else:
                out_value = values[int(selection)-1]
                out_type = types[int(selection)-1]
        else:
            #Check if value entered appears in keys list of dictionary
            if selection.capitalize() in general_options:
                out_value = selection.capitalize()
                out_type = 'General'
            else:
                print("This is not a valid option!")
    
    return out_value, out_type

###PickFromList takes the task to pick from a list of features
def PickFromList(message, lst = [], dct = {}):
    """
    Manages the task to select from a list and dictionary of options
    """
    selection = ""
    
    #Generate message for output
    text = message
    if len(lst) > 0:
        text += '\n' + StringFromList(lst, start_index = 1)
    if len(dct) > 0:
        text += '\n' + StringFromDict(dct)
    print(text)
    
    out = ""
    while out == "":
        selection = input("> ")
        
        #Check if input is an "integer" for the list
        if IsInteger(selection):
            if int(selection) not in range(1,len(lst)+1):
                print("Please enter a number between 1 and " + str(len(lst)))
            else:
                out = lst[int(selection)-1]
        else:
            #Check if value entered appears in keys list of dictionary
            if selection.capitalize() in dct:
                out = selection.capitalize()
            else:
                print("This is not a valid option!")
    
    return out

def IsInteger(sel):
    """
    Checks if an input is an integer
    """
    try:
        int(sel)
        return True
    except ValueError:
        pass

    return False

###StringFromList concatenates all entries from a list, separated by a comma. Optionally adds numbering
def StringFromList(lst, start_index = 0):
	out = ""
	for index, item in enumerate(lst):
		if index > 0:
			out += ", "
		if start_index > 0:
			out += "(" + str(index + start_index) + ") "
		out += item
	return out
 
def StringFromDict(dct):
    """
    Combines all values from a dictionary into a string
    """
    out = ""
    for key, value in dct.items():
        if len(out) > 0:
            out += ", "
        out += value
    return out
    
###Adds new text to a string and inputs a blank or a line break in between
def AddText(old,new,newLine=False):
    if len(old) > 0 and old[len(old)-1] != "\n":
        if newLine:
            old += "\n"
        else:
            old += " "
    return old + new
    
###Creates a header for a text output
def CreateHeader(text):
    length = len(text)
    text = "\n" + "-" * length + "\n" + text
    text += "\n"
    text += "-" * length
    text += "\n" * 2
    return text

def GetBonus(attr):
    ###Returns attribute bonus based on attribute
    if attr == 3:
        return -3
    elif attr <= 5:
        return -2
    elif attr <= 8:
        return -1
    elif attr <= 12:
        return 0
    elif attr <= 15:
        return 1
    elif attr <= 17:
        return 2
    elif attr == 18:
        return 3
    else:
        return 0

def DoTest(attr_score, DC = 10, advantage = False, disadvantage = False):
    """
    Executes a test with a D20 against a DC
    """
    #Determine number of tries
    result = 0
    if advantage == True and disadvantage == False:
        result = max([D(20), D(20)])
    elif advantage == False and disadvantage == True:
        result = min([D(20), D(20)])
    else:
        result = D(20)
    
    result += GetBonus(attr_score)
    
    if DEBUG:
        print("attr_score:", attr_score, type(attr_score))
        print("DC:", DC, type(DC))
        print("Advantage:", advantage, type(advantage))
        print("Disadvantage:", disadvantage, type(disadvantage))
        print("Result:", result)        
    
    return result >= DC
    
def D(size):
    """
    Rolls a die with a given size
    """
    return randint(1, size)