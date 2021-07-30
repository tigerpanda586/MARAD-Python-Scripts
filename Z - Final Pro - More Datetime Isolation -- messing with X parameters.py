# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:05:20 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""

#~~~~~~~~~~I would like to say that I found that doing this excessively does
#not help. I would recommend separating year and then "monthdayhourminute" as
#it would make no difference in your results if you separate into additional
#month, day, hour, minute, etc~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Also these manipulate a Date/Time that's already numbered which I do in the
#code file Datetime to Integer. So look at that one first if you haven't
#already


#Import basic pckgs
#Import basic pckgs
import pandas as pd
import numpy as np
import datetime as dt

test = pd.read_csv("testnumbered4.txt", delimiter = ",", dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "IMO" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date/Time" : str, "Update Date/Time" : str, "Entrance Date/Time" : str, "Arrival Date/Time" : str})

#Get rid of duplicates(3000+)
test = test.drop_duplicates(ignore_index = True)

#Isolates Month in Create Date/Time
for label, row in enumerate(test.iterrows()):
   if test["Create Date/Time Numbered"][label] != None:
       test.loc[label, ["Create Date/Time Month"]] = str(test["Create Date/Time Numbered"][label])[0:2]
     
#Isolates day in Create Date/Time
for label, row in enumerate(test.iterrows()):
   if test["Create Date/Time Numbered"][label] != None:
       test.loc[label, ["Create Date/Time Day"]] = str(test["Create Date/Time Numbered"][label])[2:4]
 
#Isolates hour in Create Date/Time
for label, row in enumerate(test.iterrows()):
   if test["Create Date/Time Numbered"][label] != None:
       test.loc[label, ["Create Date/Time Hour"]] = str(test["Create Date/Time Numbered"][label])[4:6]

#Isolates minute in Create Date/Time
for label, row in enumerate(test.iterrows()):
   if test["Create Date/Time Numbered"][label] != None:
       test.loc[label, ["Create Date/Time Minute"]] = str(test["Create Date/Time Numbered"][label])[6:8]
      
        
#Save to text file
test.to_csv(header = True, index = False, path_or_buf = "C:/Users/TreeP/Desktop/Python/testnumbered4.txt")