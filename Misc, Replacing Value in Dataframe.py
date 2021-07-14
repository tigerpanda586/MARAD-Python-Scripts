# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:24:48 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~Replace Value of Row~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Create filter for identity of ONE MINATO
filt = entrances["IMO"] == "9805477"

#Replace Official Registration Number of ONE MINATO with 143272
entrances.loc[filt, ["Official Registration Number"]] = ["143272"]

#This is row location of where one ONE MINATO vessel is located, double checking
print(entrances.loc[1529])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Misc ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Calculate average Gross and Net Tonnage then round to nearest tenth
nt_tenth = round(nt.mean(), 1)
gt_tenth = round(gt.mean(), 1)


#Round to nearest whole number
nt_whole = round(nt.mean())
gt_whole = round(gt.mean())


#To the nearest ten
nt_ten = round(nt.mean(), -1)
gt_ten = round(gt.mean(), -1)


#Find distinct list of Vessel Codes
vc = entrances["Vessel Type"].drop_duplicates()

#Print to see how many distinct vessel codes there are
print(vc.count())



