# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:01:40 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""
#Import package
import pandas as pd

#Import data
test = pd.read_csv("testnumbered3.txt", delimiter = "|", dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "IMO" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date/Time" : str, "Update Date/Time" : str, "Entrance Date/Time" : str, "Arrival Date/Time" : str}, parse_dates = ["Update Date/Time", "Create Date/Time", "Clearance Date/Time", "Entrance Date/Time", "Arrival Date/Time"])

#Get rid of duplicates(3000+)
test = test.drop_duplicates(ignore_index = True)

#Fix incorrect data
test["IMO"][test["IMO"] == "DON'T"] = 7611913
test["IMO"][test["IMO"].isnull()] = 0
test["IMO"] = test["IMO"].astype(float)

#Only get columns I'm interested in for matching
test = test[["Vessel Name", "Net Tonnage", "Gross Tonnage", "Vessel Type", "Year Built", "Operator Country Code Numbered", "Owner Name Numbered", "Registration Country Code Numbered", "Built Country Code Numbered"]]

#Take out Vessel Name for testing set
test2 = test.drop(["Vessel Name"], axis = 1).values

#Get first occurrence of every Vessel Name
vnn = test.drop_duplicates(subset = "Vessel Name", ignore_index = True)
    
#Write a loop to assign each vessel name to a unique number – used during scoring
zz = {}
for label, row in enumerate(vnn.iterrows()):
    zz[vnn["Vessel Name"].loc[label]] = label  

#Make y and X
y = vnn["Vessel Name"]
X = vnn.drop(["Vessel Name"], axis = 1).values

print("We've Made It -- data was able to be read")

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print("Started Neighbors")
#Import KNeighbors
from sklearn.neighbors import KNeighborsClassifier

#Assign parameters to KNeighbors
clf = KNeighborsClassifier(n_neighbors = 1, algorithm = "brute", metric = "hamming", weights = "distance")

#Fit training set
clf.fit(X, y)

print("Started Prediction")

#Predict y values (Vessel Names) for test set
prediction = clf.predict(test2)

print("Ended Prediction")

#This is for scoring – make predictions into new dataframe
ta = pd.DataFrame(prediction, columns = ["Target Answer"])

#Make empty list
c = []

#Append corresponding Vessel Name Number of Vessel Name Target Answer to empty DataFrame
for label, row in enumerate(ta.iterrows()):
    c.append(zz[ta["Target Answer"].loc[label]])

#Make DataFrame of correct Vessel Names
ta3 = test[["Vessel Name"]]

#Make another list – this is just a complicated way to make a list I will append values to like with c
d = [2] * len(test)

#Turn list c into DataFrame
ta2 = pd.DataFrame(c)

#Make list d a DataFrame
ta4 = pd.DataFrame(d)

print("Getting Close -- One Loop Done")

#This gets the corresponsing Vessel Name number for the actual Vessel Name
for label, row in enumerate(ta3.iterrows()):
    ta4.loc[label] = zz[ta3["Vessel Name"].loc[label]]

#Concatenate all DataFrames together for scoring
ta = pd.concat([ta, ta2, ta3, ta4], axis = 1, ignore_index = True)

#Name the columns so I can call them properly
ta.columns = ["Target Answer", "Corresponding Target Number", "Actual Vessel", "Actual Corresponding Number"]

print("Almost There -- Second Loop Done")

#If prediction = actual vessel name it gives 1, if not a 0 and append it to list e
e = []
for label, row in enumerate(ta.iterrows()):
    if ta["Corresponding Target Number"].loc[label] == ta["Actual Corresponding Number"].loc[label]:
        e.append(1)
    else:
        e.append(0)
        
#This calculates the percentage or accuracy
print("Percentage: " + str((sum(e))/len(e) * 100) + "%")

#Make e into DataFrame
e = pd.DataFrame(e)

#Concatenate e with ta DataFrame
ta = pd.concat([ta, e], axis = 1, ignore_index = True)

#Rename Columns
ta.columns = ["Target Answer", "Corresponding Target Number", "Actual Vessel", "Actual Corresponding Number", "Binary"]

#Export to excel file to engage with results
ta.to_excel(excel_writer = "C:/Users/TreeP/Desktop/Python/Proof.xlsx", header = True, index = False)
