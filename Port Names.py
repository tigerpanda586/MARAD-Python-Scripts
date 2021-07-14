# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 18:56:07 2021

@author: Jessica Brown
@email: TreePerson586@yahoo.com
"""

#Import Pckges
import pandas as pd

#Import txt file
data = "Entrances06062021.txt"
entrances = pd.read_csv(data, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})

#Import new txt fil
data2 = "Entrances06132021.txt"
entrances2 = pd.read_csv(data2, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Concatenate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Concatenate 06062021 and 06132021
entrances = pd.concat([entrances, entrances2], axis = 0, ignore_index = True)


#Remove duplicates
entrances = entrances.drop_duplicates()
entrances.reset_index(drop = True, inplace = True)

#~~~~~~~~~~~~~~~~~~~~~~~~~Variables and Organization~~~~~~~~~~~~~~~~~~~~~~~~~#

#Assign variables to each column
fp = entrances["Filing Port"]
fy = entrances["Fiscal Year"]
s = entrances["Sequence"]
edt = entrances["Entrance Date/Time"]
ap = entrances["Arrival Port"]
adt = entrances["Arrival Date/Time"]
cdt = entrances["Create Date/Time"]
udt = entrances["Update Date/Time"]
an = entrances["Agent Name"]
ctc = entrances["Cargo Type Code"]
df = entrances["Draft Feet"]
di = entrances["Draft Inches"]
ldp = entrances["Last Domestic Port"]
lfp = entrances["Last Foreign Port"]
vp = entrances["Via Port"]
tc = entrances["Total Crew"]
tp = entrances["Total Passengers"]
dp = entrances["Disembarking Passengers"]
vr = entrances["Vessel Repair"]
vn = entrances["Vessel Name"]
imo = entrances["IMO"]
csn = entrances["Call Sign Number"]
orn = entrances["Official Registration Number"]
bcc = entrances["Built Country Code"]
yb = entrances["Year Built"]
vt = entrances["Vessel Type"]
uscs = entrances["USCS Code"]
own = entrances["Owner Name"]
opn = entrances["Operator Name"]
occ = entrances["Operator Country Code"]
rcc = entrances["Registration Country Code"]
gt = entrances["Gross Tonnage"]
nt = entrances["Net Tonnage"]

#Modify datetimes
pd.to_datetime(udt, format = "%m/%d/%Y %H:%M")
pd.to_datetime(edt, format = "%m/%d/%Y %H:%M")
pd.to_datetime(adt, format = "%m/%d/%Y %H:%M")
pd.to_datetime(cdt, format = "%m/%d/%Y %H:%M")

#Print dataframe and columns' datatypes
(entrances2.dtypes)
(entrances)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~Add Port Name Column~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Import new text file for Port Names
data3 = "Portnames.txt"

#Import new txt file as dataframe
portname = pd.read_csv(data3, dtype = str, delimiter = "|")

#Rename columns
portname.columns = ["Port Name", "Arrival Port Code", "District/Port"]

#Rename column of entrances dataframe to match column names in portname dataframe
entrances.rename(columns = {"Arrival Port" : "Arrival Port Code"}, inplace = True)

#Make portname dataframe with Port Name and Arrival Port Code columns only
del portname["District/Port"]

#Merge portname dataframe with entrances
#"on" argument merges dataframe by matching values in specified column
#"how" argument ensures all data in "left" dataframe in this instance is retained, and the only "right" data that eill appear is thr "right" data that matches "left" data
#left is the dataframe before ".merge", and right dataframe is one inside () 
#validate = many_to_one here says that many values from "left" dataframe correspond to one value from "right" dataframe
entrances = entrances.merge(portname, on = "Arrival Port Code", how = "left", validate = "many_to_one")

#Make Variable/Series for new columns
apc = entrances["Arrival Port Code"]
pn = entrances["Port Name"]

#Print dataframe
print(entrances)