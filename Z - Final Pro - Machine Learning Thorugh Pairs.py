# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:07:08 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""
#Import packages
import pandas as pd
import numpy as np

#Import data
ec2021 = pd.read_csv("testnumbered4.txt", delimiter = ",", dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "IMO" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date/Time" : str, "Update Date/Time" : str, "Entrance Date/Time" : str, "Arrival Date/Time" : str}, parse_dates = ["Update Date/Time", "Create Date/Time", "Clearance Date/Time", "Entrance Date/Time", "Arrival Date/Time"])

#Get rid of duplicates(3000+)
ec2021 = ec2021.drop_duplicates(ignore_index = True)

#Fix incorrect data
ec2021["IMO"][ec2021["IMO"] == "DON'T"] = 7611913
ec2021["IMO"][ec2021["IMO"].isnull()] = 0
ec2021["IMO"] = ec2021["IMO"].astype(float)

#Only get columns I'm interested in for matching
test = ec2021[["Vessel Name", "Net Tonnage", "Gross Tonnage", "Vessel Type", "Year Built", "Operator Country Code Numbered", "Owner Name Numbered", "Registration Country Code Numbered", "Built Country Code Numbered"]]

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
ta = pd.DataFrame(prediction, columns = ["Vessel Name Prediction"])

ec2021 = pd.concat([ta, ec2021], axis = 1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Assign a new variable so we can manipulate the same imported DataFrame
mvt = ec2021

#It never hurts to reset index just in case – honestly do not remember what this is for
mvt = mvt.reset_index()
 
#Make a series to call “Movement” column of DataFrame
mvtmvt = mvt["Movement"]

#Call the entrances only as this will be our training set
emvt = mvt[mvtmvt == "Entrance"]

#The y is the index numbers because that’s the only unique thing for each entrance
y2 = emvt.index

#Set X parameters to what I deem fit
X2 = emvt[["Arrival Port", "Filing Port", "Create Date/Time Numbered", "Create Date/Time Year", "Gross Tonnage", "Net Tonnage", "Vessel Type", "Owner Name Numbered", "Year Built", "Operator Country Code Numbered", "Owner Name Numbered", "Registration Country Code Numbered", "Built Country Code Numbered"]]

print("Started Neighbors")

#Import KNeighbors
from sklearn.neighbors import KNeighborsClassifier

#Give Kneighbors a variable and assign parameters
clf = KNeighborsClassifier(n_neighbors = 1, algorithm = "brute", metric = "hamming", weights = "distance")

#Fit training set
clf.fit(X2, y2)

print("Started Prediction2")

#Set test set
mvt = mvt[["Arrival Port", "Filing Port", "Create Date/Time Numbered", "Create Date/Time Year", "Gross Tonnage", "Net Tonnage", "Vessel Type", "Owner Name Numbered", "Year Built", "Operator Country Code Numbered", "Owner Name Numbered", "Registration Country Code Numbered", "Built Country Code Numbered"]]

#Predict test set
prediction2 = clf.predict(mvt)

print("Ended Prediction2")

print("Fixing DataFrames for sorting2")

#Make prediction into its own DataFrame
ta2 = pd.DataFrame(prediction2, columns = ["Pair's Index Number"])

#Concatnate predictions and original ec2021 DataFrame
ec2021 = pd.concat([ta2, ec2021], axis = 1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Sort by what I deem fit
ec2021 = ec2021.sort_values(by = ["Filing Port", "Pair's Index Number", "Create Date/Time", "Entrance Date/Time"], ignore_index = True)

#Assign variables and make list z
x = 0
y = 1
z = []

print("Started Loop for Sorting Accurracy")

#Drop duplicates for ec2021
ec2021 = ec2021.drop_duplicates(ignore_index = True)

#Use same way to calculate accuracy – note that you can use “Vessel Name Prediction” here or “Vessel Name” –- you will have to run two Supervised Learning training and tests sets to use “Vessel Name Prediction unless you saved it in the text file previously – note: you will not have a big difference in results with “Vessel Name Prediction” vs “Vessel Name” anyways
for label, row in enumerate(ec2021.iterrows()):
        if label != len(ec2021) - 1:
           if ec2021["Vessel Name Prediction"].loc[label] != ec2021["Vessel Name Prediction"].loc[label + 1]:
                z.append(x)
           elif ec2021["Arrival Port"].loc[label] != ec2021["Arrival Port"].loc[label + 1]:
                z.append(x)
           elif ec2021["Movement"].loc[label] != "Entrance":
              	 	z.append(x)
           elif np.logical_and(ec2021["Movement"].loc[label + 1] == "Clearance", ec2021["Entrance Date/Time"].loc[label] <= ec2021["Clearance Date/Time"].loc[label + 1]):
                    z.append(y)
           else:
               		z.append(x)

#To account for skipped value in loop
z.append(0)

print("Calculating Accuracy")
        
#Calculate percentage
print("Percentage = " + str((sum(z)/(len(z)/2)) * 100) + "%")

#Add 1, 0 results onto DataFrame
ec2021["Binary"] = z

#Save as files if you so wish
ec2021.to_excel(index = False, header = True, excel_writer = "C:/Users/TreeP/Desktop/Python/Please2.xlsx") 
ec2021.to_csv(index = False, header = True, path_or_buf = "C:/Users/TreeP/Desktop/Python/Please.txt")


