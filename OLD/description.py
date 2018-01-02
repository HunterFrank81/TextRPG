# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:59:36 2016

@author: Frank Jaeger

Class description
Displays
"""

import os
import csv

class Description:
    def __init__(self):
        self.text = ""  #Text to be displayed
        self.showTags = list() #List of tags when item should be displayed
        self.hideTags = list() #List of tags when description should not be displayed; overrides showTags
        
    #Returns the description based on a given set of tags
    def Tell(self, tags):
        tell = False        
        for t in tags:
            if t in self.hideTags:
                return ""
            elif t in self.showTags:
                tell = True
        if tell:
            return self.text
        else:
            return ""
    
#Creates a list containing a tuple of (objectID,description)
def CreateDescriptions(descType):
    descriptions = list()    
    with open(os.curdir + '/data/' + descType + 'Descriptions.csv','r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            dat = str.split(row[0], sep='|')
            desc = Description()
            desc.text = dat[1]
            desc.showTags = str.split(dat[2], sep=',')
            if len(dat) == 4:
                desc.hideTags = str.split(dat[3], sep=',')
            descriptions.append((int(dat[0]),desc))
    return descriptions