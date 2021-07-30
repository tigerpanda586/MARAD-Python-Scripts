# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:01:40 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""

#Import basic packages
import pandas as pd

#Import data as DataFrame
test = pd.read_csv("testnumbered3.txt", delimiter = "|", dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "IMO" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date/Time" : str, "Update Date/Time" : str, "Entrance Date/Time" : str, "Arrival Date/Time" : str})

#Get rid of duplicates(3000+)
test = test.drop_duplicates(ignore_index = True)

#CHANGE VESSEL NAME

vn = test.drop_duplicates(subset = "Vessel Name", ignore_index = True)
    
zz = {}
for label, row in enumerate(vn.iterrows()):
    zz[vn["Vessel Name"].loc[label]] = label 
    
for label, row in enumerate(test.iterrows()):
    test.loc[label, ["Vessel Name Numbered"]] = zz[test["Vessel Name"].loc[label]]

#CHANGE CREATE, ENTRANCE, CLEARANCE, UPDATE DATE TIMES

#It was giving me errors even though there is no blank data -- this not necessary, for my peace of mind
for label, row in enumerate(test.iterrows()):
    if test["Entrance Date/Time"][label] == None:
        test["Entrance Date/Time"][label] = 0
        
#This loop removes all spaces, colons, and dashes to make one consistent number – example: 200201271205 would be 2002/01/27 12:05 with this dataset’s datetime data
for label, row in enumerate(test.iterrows()):
    if test["Entrance Date/Time"][label] != None:
        test.loc[label, ["Entrance Date/Time Numbered"]] = str(test["Entrance Date/Time"][label]).replace(" ", "").replace("-", "").replace(":", "")

#All these loops are exactly the same....
for label, row in enumerate(test.iterrows()):
    if test["Create Date/Time"][label] == None:
        test["Create Date/Time"][label] = 0

for label, row in enumerate(test.iterrows()):
    if test["Create Date/Time"][label] != None:
        test.loc[label, ["Create Date/Time Numbered"]] =  str(test["Create Date/Time"][label]).replace(" ", "").replace("-", "").replace(":", "")
        
for label, row in enumerate(test.iterrows()):
    if test["Clearance Date/Time"][label] == None:
       test["Clearance Date/Time"][label] = 0
        
for label, row in enumerate(test.iterrows()):
    if test["Clearance Date/Time"][label] != None:
        test.loc[label, ["Clearance Date/Time Numbered"]] =  str(test["Clearance Date/Time"][label]).replace(" ", "").replace("-", "").replace(":", "")

for label, row in enumerate(test.iterrows()):
    if test["Update Date/Time"][label] == None:
        test["Update Date/Time"][label] = 0

for label, row in enumerate(test.iterrows()):
    if test["Update Date/Time"][label] != None:
        test.loc[label, ["Update Date/Time Numbered"]] =  str(test["Update Date/Time"][label]).replace(" ", "").replace("-", "").replace(":", "")

#Save as txt file
test.to_csv(header = True, index = False, path_or_buf = "C:/Users/TreeP/Desktop/Python/testnumbered4.txt")


    