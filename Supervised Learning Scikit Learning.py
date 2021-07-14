# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 10:34:47 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""

#Import basic pckgs
import pandas as pd

#Import entrances and clearances for 2021
ec2021 = pd.read_csv(filepath_or_buffer = "ec2021.txt", delimiter = "|", dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "IMO" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date/Time" : str, "Update Date/Time" : str, "Entrance Date/Time" : str, "Arrival Date/Time" : str}, parse_dates = ["Update Date/Time", "Create Date/Time", "Clearance Date/Time", "Entrance Date/Time", "Arrival Date/Time"])

#Import pckgs fpr data analyzation
import matplotlib.pyplot as plt

#Make Chart Prettier -- "ggplot" is a style of graph
plt.style.use("ggplot")

#This is for Exploratory Data Analysis (EDA) -- it is supposed to help you better..
#understand your data, but its usefulness will depend on the situation
pd.plotting.scatter_matrix(ec2021, figsize = [9,9], alpha = .5)

#Show plot of EDA
plt.figure()

#Get rid of duplicates(3000+)
ec2021 = ec2021.drop_duplicates(ignore_index = True)

#Replace strange value of "DON'T" in dataframe to rightful IMO
ec2021["IMO"][ec2021["IMO"] == "DON'T"] = 7611913

#Where IMO is NaN, replace with a 0 -- Note: When using sklearn, you cannot..
#have NaN values -- gives errors
ec2021["IMO"][ec2021["IMO"].isnull()] = 0

#Set IMOs as floats as they were originally imported as strings
ec2021["IMO"] = ec2021["IMO"].astype(float)

#Only get columns I'm interested in for matching
ec2021 = ec2021[["Vessel Name", "IMO", "Gross Tonnage", "Net Tonnage", "Year Built", "Vessel Type"]]

#Make Exploratory Data Analysis (EDA) for these "more important" columns
pd.plotting.scatter_matrix(ec2021, figsize = [9,9], alpha = .5)

#Show plot of EDA
plt.figure()

#Copy ec2021 dataframe to manipulate separately
vnn = ec2021.drop_duplicates(subset = "Vessel Name", ignore_index = True)
        
#Set y as one column that will become target values
y = vnn["Vessel Name"]

#Set X as all values that target values will be fit by called Features -- recognize..
#sklearn only takes number, no strings
X = vnn.drop(["Vessel Name"], axis = 1).values

#Create empty dictionary for Vessel Name matching -- the reason I do this is
#because I like it -- it is actually completely unnecessary -- you can compare
#vessel names instead of numbers, but I like having numbers that correspond to..
#the vessel names
z = {}

#Write loop so that dictionary receives key (number) and value pair (vessel name)
for label, row in enumerate(vnn.iterrows()):
    z[label] = vnn["Vessel Name"].loc[label]
    
#Create empty dictionary for same reason
zz = {}

#This time the loop makes the key the vessel name and value pair the number --
#this is for versatility/if you get ideas that require one way or another
for label, row in enumerate(vnn.iterrows()):
    zz[vnn["Vessel Name"].loc[label]] = label

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Copy same dataframe again this time for test values -- what will make predictions off of
ec2021_test = pd.read_csv(filepath_or_buffer = "ec2021.txt", delimiter = "|", dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date/Time" : str, "Update Date/Time" : str, "Entrance Date/Time" : str, "Arrival Date/Time" : str, "Gross Tonnage" : int, "Net Tonnage" : int}, parse_dates = ["Update Date/Time", "Create Date/Time", "Clearance Date/Time", "Entrance Date/Time", "Arrival Date/Time"])

#These do the same as above -- replace missing values and etc
ec2021_test["IMO"][ec2021_test["IMO"] == "DON'T"] = 7611913
ec2021_test["IMO"][ec2021_test["IMO"].isnull()] = 0
ec2021_test["IMO"] = ec2021_test["IMO"].astype(float)

#Drop duplicates
ec2021_test.drop_duplicates(ignore_index = True)

#Separate all needed features from this new copy of dataframe for prediction –-
#it must have the same values that were passed in “X”
test = ec2021_test[["IMO", "Gross Tonnage", "Net Tonnage", "Year Built", "Vessel Type"]]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#All of these messages are to encourage you while waiting for the result
print("Started Neighbors")

#Import pckg
from sklearn.neighbors import KNeighborsClassifier

#Call KNeighborsClassifier -- here n_neighbors = 1 is best because some y values only have..
#one corresponding row (in X) -- other datasets will see different things --
#weights = "distance" works better here -- the alternative is "uniform" which weighs..
#all features equally to fit/assign prediction
knn = KNeighborsClassifier(n_neighbors = 1, weights = "distance")

#Fits sample values I picked for future prediction
knn.fit(X, y)

print("Started Prediction")

#This is the prediction
prediction = knn.predict(test)

print("Ended Prediction")

#This puts predictions into a dataframe so I can organize results
ta = pd.DataFrame(prediction, columns = ["Target Answer"])

#Create empty list for number corresponding to Target Answers
c = []

#Write loop to append corresponding numbers to list "c"
for label, row in enumerate(ta.iterrows()):
    c.append(zz[ta["Target Answer"].loc[label]])
    
#These are the correct Vessel Names, so I make a dataframe of this
ta3 = ec2021_test[["Vessel Name"]]

#This is a list, I was having problems appending to this empty list, so I..
#resorted to making a list of values then replacing them
d = [2] * len(ec2021)

#Turn list "c" into dataframe
ta2 = pd.DataFrame(c)

#Turn list "d" into dataframe
ta4 = pd.DataFrame(d)

print("Getting Close -- One Loop Done")

#Write loop to change values of dataframe "ta4" -- this returns correct numbers of vessels for..
#correct vessels 
for label, row in enumerate(ta3.iterrows()):
    ta4.loc[label] = zz[ta3["Vessel Name"].loc[label]]

#Concatenate all of these dataframes into one
ta = pd.concat([ta, ta2, ta3, ta4], axis = 1, ignore_index = True)

#Name columns of dataframe
ta.columns = ["Target Answer", "Corresponding Target Number", "Actual Vessel", "Actual Corresponding Number"]

print("Almost There -- Second Loop Done")

#Create empty dataframe to calculate accuracy
e = []

#This loop calculates accuracy -- Note: there are ways sklearn has to compute accuracy such..
#as "train_test_split" and ".score" -- However, you cannot use those with this data set..
#as there are some y values with only one corresponing  row (x value) -- more than one..
#is required to use train_test_split and .score
#Simple logic of loop -- if prediction number equals actual number: 1, if not: 0
for label, row in enumerate(ta.iterrows()):
    if ta["Corresponding Target Number"].loc[label] == ta["Actual Corresponding Number"].loc[label]:
        e.append(1)
    else:
        e.append(0)

#Make list "e" into its own dataframe
ta5 = pd.DataFrame(e)

#Concatenate ta5 to other dataframe
ta = pd.concat([ta, ta5, test], axis = 1, ignore_index = True)

#Rename columns so column from ta5 has a label
ta.columns = ["Target Answer", "Corresponding Target Number", "Actual Vessel", "Actual Corresponding Number", "Binary", "IMO", "Gross Tonnage", "Net Tonnage", "Year Built", "Vessel Type"]

#Save dataframe to computer as an excel file
ta.to_excel(header = True, index = False, excel_writer = "C:/Users/TreeP/Desktop/Python/ta_success.xlsx")
      
#Self-explanatory -- this calculates the accuracy  
print("Percentage: " + str((sum(e))/len(e) * 100) + "%")

print("Done.")