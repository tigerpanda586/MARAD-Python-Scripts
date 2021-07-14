# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 22:36:41 2021

@author: Jessica Brown
@email: TreePerson586@yahoo.com
"""
#Import Pckges
import pandas as pd

#Import text file -- clarification: using pandas imports as dataframe
data = "Entrances06062021.txt"
entrances = pd.read_csv(data, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})

#Import new/additional text file
data2 = "Entrances06132021.txt"
entrances2 = pd.read_csv(data2, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})

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

#Print new dataframe's columns' datatypes for inspection
print(entrances2.dtypes)

#Print new dataframe for inspection
print(entrances2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Concatenate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Concatenate -- axis = 1 concatenates on columns -- axis = 0 concatenates on indices
#When columns are the same, you want to concatenate on indices (0)
#When indicies are the same in both datasets, you want to concatenate on columns (1)
#ignore_index renames indices, w/o this you will not have 0-some number, w/o it may give repeat or odd indices
entrances_1_2 = pd.concat([entrances, entrances2], axis = 0, ignore_index = True)

#Remove duplicates -- .drop.duplicates() drops duplicates only when every column has the same exact value..
#Unless you pass argument "subset = " -- this will allow you to only delete duplicates in certain columns
entrances_1_2 = entrances_1_2.drop_duplicates()

#Resets indices (after dropping duplicates) -- does the same as "ignore_index = True" argument in pd.concat above
#inplace = True drops duplicates, no copies, makes for cleaner dataframe
entrances_1_2.reset_index(drop = True, inplace = True)
