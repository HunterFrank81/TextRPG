# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:59:36 2016

@author: Frank Jaeger

Class description
Displays
"""

import os
import csv
from config import DEBUG

class Description:
    def __init__(self):
        self.text = ""  #Text to be displayed
        self.showTags = list() #List of tags when item should be displayed
        self.hideTags = list() #List of tags when description should not be displayed; overrides showTags
        
    #Returns the description based on a given set of tags
    def Tell(self, tags):
        #DEBUG output
        if DEBUG:
            print("Description:", self.text)
            print("Tags input:", tags)
            print("Show tags:", self.showTags)
            print("Hide tags:", self.hideTags)
            
        #If no "show" tags exist, display description by default
        print("Length of showTags:", len(self.showTags))
        if len(self.showTags) == 0:
            tell = True
        else:
            tell = False
        for t in tags:
            #don't show if one of the tags is in the "hidden" list
            if t in self.hideTags:
                if DEBUG:
                    print("RESULT: has hidden tag", t)
                    print("---")
                return ""
            #show if at least one tag is included in "show" list or tag list is empty
            elif t in self.showTags:
                tell = True
        if DEBUG:
            print("Result of check:", tell)
            print("---")
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
            #Add description text
            desc.text = dat[1]
            #Add show tags - only if it actually has content
            if len(dat[2]) > 0:
                desc.showTags = str.split(dat[2], sep=',')
            if len(dat) == 4:
                desc.hideTags = str.split(dat[3], sep=',')
            descriptions.append((int(dat[0]),desc))
    return descriptions