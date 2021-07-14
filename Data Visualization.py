# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:24:48 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""

#Import Pckgs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import Clearances
clearances = pd.read_csv("ClearancesComb.txt", delimiter = "|", parse_dates = ["Clearance Date/Time", "Create Date/Time", "Update Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port Code" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})

#Import Entrances
data = "EntrancesComb.txt"
entrances = pd.read_csv(data, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port Code" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})

#Fix Datetime Stuff

#Assign variables to necessary columns
edt = entrances["Entrance Date/Time"]
adt = entrances["Arrival Date/Time"]
cdt = entrances["Create Date/Time"]
udt = entrances["Update Date/Time"]
df = entrances["Draft Feet"]
di = entrances["Draft Inches"]
yb = entrances["Year Built"]

#Modify datetimes
udt_t = pd.to_datetime(udt, format = "%m/%d/%Y %H:%M")
edt_t = pd.to_datetime(edt, format = "%m/%d/%Y %H:%M")
adt_t = pd.to_datetime(adt, format = "%m/%d/%Y %H:%M")
cdt_t = pd.to_datetime(cdt, format = "%m/%d/%Y %H:%M")

#Assign variables to necessary columns
cedt = clearances["Clearance Date/Time"]
ccdt = clearances["Create Date/Time"]
cudt = clearances["Update Date/Time"]

#Modify datetimes
cudt_t = pd.to_datetime(udt, format = "%m/%d/%Y %H:%M")
cedt_t = pd.to_datetime(edt, format = "%m/%d/%Y %H:%M")
ccdt_t = pd.to_datetime(cdt, format = "%m/%d/%Y %H:%M")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Data Visualization~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Find Top 25 popular entrance ports

#Create Series of only Arrival Port Codes
apc = entrances["Arrival Port Code"]

#Set up foundations of graph
fig, ax = plt.subplots()

#Get rid of all duplicate ports
ports = apc.unique()

#Assign number 25 to variable n
n = 25

#Use ".value_counts" to count how many are in each port -- 
#they come out in greatest to least so no need to rearrange
#"[:n]" slices for first 25 -- ".index.tolist()" makes the port codes into a list
ports25 = entrances['Arrival Port Code'].value_counts()[:n].index.tolist()   

#Make list into a numpy array -- a numpy array is just a list but put into a form...
#that's easier manipulated by packages like numpy and pandas -- it's an array
ports25 = np.array(ports25)

#This loop automates the values for each bar attached to x-axis -- you can copy and paste this
#What you should know: "port" is a variable to be used in loop -- "ports25" references..
#series I made above -- "yerr" creates an error bar with .std() or standard deviation
for port in ports25:
    port_df = entrances[entrances["Arrival Port Code"] == port]
    ax.bar(port, port_df["Net Tonnage"].mean(), yerr = port_df["Net Tonnage"].std())

#Name y label -- note there is no need to assign y values because this is a bar chart
ax.set_ylabel("Average Net Tonnage")

#Name x ticks and rotate to make readable
ax.set_xticklabels(ports25, rotation = 90)

#Make a title
ax.set_title("Avg Net Tonnage for Top 25 Entrance Ports")
plt.show()

#~~~~~~~~Do same exact thing with Clearances -- so I will not write notes

capc = clearances["Arrival Port Code"]
fig, ax = plt.subplots()

ports = capc.unique()

n = 25
ports25 = clearances['Arrival Port Code'].value_counts()[:n].index.tolist()    
ports25 = np.array(ports25)


for port in ports25:
    port_df = clearances[clearances["Arrival Port Code"] == port]
    ax.bar(port, port_df["Net Tonnage"].mean(), yerr = port_df["Net Tonnage"].std())

ax.set_ylabel("Average Net Tonnage")
ax.set_xticklabels(ports25, rotation = 90)
ax.set_title("Avg Net Tonnage for Top 25 Clearance Ports")
plt.show()

#~~~~~~~~~~~ Do same thing but with MARADTypes so I will not write notes

types = entrances["MARADType"].unique()

fig, ax = plt.subplots()

for MARADType in types:
    MARADType_df = entrances[entrances["MARADType"] == MARADType]
    ax.bar(MARADType, MARADType_df["Draft Size"].mean(), yerr = MARADType_df["Draft Size"].std())
    
ax.set_ylabel("Draft Size (in)")
ax.set_xticklabels(types, rotation = 90)
plt.show()


#~~~~~~~~~~~~~~~~~~~~~~~~~ Time Series Data Viz~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Function created to combine Draft Feet and Draft Inches from file "Writing Fucntions"
def measure(index):
    return df.loc[index] * 12 + di.loc[index]

#Measure Draft Size of all entrance rows
dm = measure(entrances.index)

#Turn Draft Size into its own DataFrame
df_dm = dm.to_frame()

#Name column "Draft Size"
df_dm.columns = ["Draft Size"]

#Turn "Year Built" column of entrances DataFrame into its own dataframe
df_yb = yb.to_frame()

#Identify values equal to 1900 -- as these are substitue values for missing values
nonyear = df_yb["Year Built"] != 1900

#Get rid of those values by creating reference series
nonyear = df_yb.loc[nonyear, "Year Built"]

#Make that series into a dataframe
df_yb = nonyear.to_frame()

#Concatenate "Year Built" and "Draft Size" dataframes -- as if you don't..
#it's easy to get errors such as "the size of x and y don't match"
df_t = pd.concat([df_yb, df_dm], axis = 1)

#Set up foundations for graph
fig, ax = plt.subplots()

#Set x as Year Built and y as Draft Size, color code by year, alpha of .5
ax.scatter(df_t["Year Built"], df_t["Draft Size"], c = df_t["Year Built"], alpha = .5)

#Name x-axis
ax.set_xlabel("Year Vessel Built")

#Name y-axis
ax.set_ylabel("Draft Size")

#Show plot
plt.show()


#~~~~~~~~~~

#Create a function to turn datetime objects into hour, minute, and second --
#then divide/multiply to make every value on a scale from 0-24 hours (think military time)
def excel_time(time):
    return time.hour + time.minute / 60 + time.second / (24 * 60)

#Create a blank list to hold what will become the x values
times = []

#Write loop that will append the calculated time (excel_time) into list "times"
for label, row in clearances.iterrows():
    x = excel_time(clearances["Clearance Date/Time"].loc[label])
    times.append(x)

#Set up foundations of graph
fig, ax = plt.subplots()

#Set times (list of excel_time's) as x and Draft Sizes as y
#alpha makes points partially invisible (scale of 0-1) to better see clusters
#c color codes data points by what's passed... 
#so most purple is near 00:00 and most yellow is near 24:00
ax.scatter(times, clearances["Draft Size"], c = times, alpha = .5)

#Name x-axis
ax.set_xlabel("Time of Day (0-24 hours)")

#Name y-axis
ax.set_ylabel("Draft Size")

#Make title
ax.set_title("Draft Size of Vessels by Time of the Day they Clear")

#Show Plot
plt.show()

#~~~~~~~~

#Merge clearance and entrance dataframes, I passed "Sequence" and "Vessel Name" for "on" because..
#I thought it would best match up data -- later on I figure out this is not the best..
#method, but it works just for this graph demonstration
vessels = clearances.merge(entrances, on = ["Sequence", "Vessel Name"])

#Create blank list for excel_time of Entrance dates
etimes = []

#Write loop to apppend Entrance excel_times to list "etimes"
for label, row in vessels.iterrows():
    x = excel_time(vessels["Entrance Date/Time"].loc[label])
    etimes.append(x)

#Write loop to apppend Clearance excel_times to list "ctimes"
ctimes = []
for label, row in vessels.iterrows():
    y = excel_time(vessels["Clearance Date/Time"].loc[label])
    ctimes.append(y)

#Set up foundations for graph
fig, ax = plt.subplots()

#etimes as x, ctimes as y, color code with etimes, alpha as .5
ax.scatter(etimes, ctimes, c = etimes, alpha = .5)

#Name x axis
ax.set_xlabel("Entrance Time of Day (0-24 hours)")

#Name y-axis
ax.set_ylabel("Clearance Time of Day")

#Make title
ax.set_title("Entrance vs Clearance Time of Day")

#Plot graph
plt.show()

#~~~~~~~~~~~~~~~~

#This function is not the most saavy but gets job done --
#It returns values like "6.5" which is equal to the middle of June
def day_time(time):
    return time.month + time.day/30.5

#Everything else is exactly the same, so I will not leave notes

detimes = []
for label, row in vessels.iterrows():
    x = day_time(vessels["Entrance Date/Time"].loc[label])
    detimes.append(x)

dctimes = []
for label, row in vessels.iterrows():
    y = day_time(vessels["Clearance Date/Time"].loc[label])
    dctimes.append(y)

fig, ax = plt.subplots()

ax.scatter(detimes, dctimes, c = detimes, alpha = .5)
ax.set_xlabel("Entrance Time by Date(month.day)")
ax.set_ylabel("Clearance Time by Date(month.day)")
ax.set_title("Entrance vs Clearance Date")
plt.show()


    