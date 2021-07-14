# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:32:31 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""

#Import Pckgs
import pandas as pd
import numpy as np

#WE ARE TRYING TO MATCH ENTRANCES AND CLEARANCES

#Read file
ec2021 = pd.read_csv(filepath_or_buffer = "ec2021.txt", delimiter = "|", dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date/Time" : str, "Update Date/Time" : str, "Entrance Date/Time" : str, "Arrival Date/Time" : str}, parse_dates = ["Update Date/Time", "Create Date/Time", "Clearance Date/Time", "Entrance Date/Time", "Arrival Date/Time"])

#Sort values first by "Vessel Name" then "Arrival Port" then "Create Date/Time" then "Entrance Date/Time"
ec2021 = ec2021.sort_values(by = ["Vessel Name", "Arrival Port", "Create Date/Time", "Entrance Date/Time"], ignore_index = True)

#Set x equal to 0
x = 0

#Set y equal to 1
y = 1

#Create list to append results (0 and 1's) to
z = []

#Drop all duplicate values in dataset -- because these datasets may have overlapping dates --
#there are often repeat entries
ec2021 = ec2021.drop_duplicates(ignore_index = True)

#Print to make sure dataframe is okay
print(ec2021)

#This loop will assign either a 0 (not a match) or a 1 (a match)
# I will go through logic of each line:
#First if -- takes away last row as we are comparing a row to the row ahead of it..
#including this row will cause an error
#Second if -- Vessel Name must be equal to Vessel Name ahead of it
#First elif -- Arrival Port must be equal to Arrival Port ahead of it
#Second elif -- Row specified must be an Entrance
#Third elif -- Row after row specified must be a Clearance (therefore a pair)..
#AND Entrance time has to come before Clearance Time -- this clarifies the pairs are..
#matched correctly, think of it as the final hurdle/quintuple checking

for label, row in enumerate(ec2021.iterrows()):
        if label != len(ec2021) - 1:
           if ec2021["Vessel Name"].loc[label] != ec2021["Vessel Name"].loc[label + 1]:
                z.append(x)
           elif ec2021["Arrival Port"].loc[label] != ec2021["Arrival Port"].loc[label + 1]:
                z.append(x)
           elif ec2021["Movement"].loc[label] != "Entrance":
                z.append(x)
           elif np.logical_and(ec2021["Movement"].loc[label + 1] == "Clearance", ec2021["Entrance Date/Time"].loc[label] <= ec2021["Clearance Date/Time"].loc[label + 1]):
                    z.append(y)
           else:
               z.append(x)

#I appended this extra 0 as it corresponds to the index I took out in the loop..
#However, adding or not adding will not change the data much, it may change it by .001..
#but the point is for the most accurate calculating
z.append(0)
        
#This prints the percentage of matches -- we aim for 100%
#You must divide sum of 0's and 1's by total number of values in list "z"..
#divided by 2 because each pair only yields one "1" -- a matching pair will
#yield one "1" and one "0" even though there are 2 values -- 
#Then we multiply by 100 and add % sign to make it easier to look at
print("percentage = " + str((sum(z)/(len(z)/2)) * 100) + "%")

#This adds the column "Binary" to the dataframe, the point is so I can export this..
#data into excel and analyze it by looking at it, sorting it etc..
#this quickly allows me to see which pairs matched by looking for "1, 0" pair
ec2021["Binary"] = z

#Save dataframe to computer as an excel file
ec2021.to_excel(index = False, header = True, excel_writer = "C:/Users/TreeP/Downloads/Okay/Sortedec202111.xlsx")


