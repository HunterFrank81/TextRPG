# -*- coding: utf-8 -*-
__author__ = "Frank"

"""
Created on Wed Dec 27 21:25:27 2017

Items class

Contains classes and sub-classes around items


@author: Frank Jaeger
"""

# state variables for items


# Item class
class item:
    """
    **Item** is the master class for all item-related things. It has the following properties
    * id - the ID of the item
    * name - the name of the item
    * descriptions - a list of possible descriptions to be displayed
    * tags - a list of tags that can be associated to an item
    """
    def __init__(self):
        self.id = 0
        self.name = ""
        self.descriptions = list()
        self.tags = list()
        
# Create items
def CreateItems():
    items = list()
    
    #Create list of items
    