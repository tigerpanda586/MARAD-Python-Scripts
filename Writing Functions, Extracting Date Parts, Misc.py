# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:24:48 2021

@author: Jessica Brown
@email: TreePerson586@yahoo.com
"""

#Import Pckges
import pandas as pd

#Import txt file
data = "Entrances06062021.txt"
entrances = pd.read_csv(data, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})

#Import new txt file
data2 = "Entrances06132021.txt"
entrances2 = pd.read_csv(data2, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Concatenate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Concatenate 06062021 and 06132021
entrances = pd.concat([entrances, entrances2], axis = 0, ignore_index = True)


#Remove duplicates
entrances = entrances.drop_duplicates()
entrances.reset_index(drop = True, inplace = True)


#~~~~~~~~~~~~~~~~~~~~~~~Variables and Organization 1~~~~~~~~~~~~~~~~~~~~~~~~~#

#Assign variables to necessary columns
imo = entrances["IMO"]
edt = entrances["Entrance Date/Time"]
adt = entrances["Arrival Date/Time"]
cdt = entrances["Create Date/Time"]
udt = entrances["Update Date/Time"]

#Modify datetimes
udt_t = pd.to_datetime(udt, format = "%m/%d/%Y %H:%M")
edt_t = pd.to_datetime(edt, format = "%m/%d/%Y %H:%M")
adt_t = pd.to_datetime(adt, format = "%m/%d/%Y %H:%M")
cdt_t = pd.to_datetime(cdt, format = "%m/%d/%Y %H:%M")


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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Function basics --
#"def" starts function
#here "measure" is function name
#here "index" is what is passed in the function, any word/variable can be used --
#you can also pass more than one variable -- just use all variables in how function is executed
#I used "return" as the function's purpose is to return certain values

#Combine draft feet and draft inches of a certain vessel into sum in inches
def measure(index):
    return int(df.loc[index] * 12) + int(di.loc[index])


#Tells type or category of a vessel -- this is a loop
def category(index):
    if int(entrances.loc[index, ["Vessel Type"]]) < 110:
        return "Other"
    elif int(entrances.loc[index, ["Vessel Type"]]) <= 139:
        return "Tanker"
    elif int(entrances.loc[index, ["Vessel Type"]]) <= 149:
        return "Barge"
    elif int(entrances.loc[index, ["Vessel Type"]]) <= 199:
        return "Tanker"
    elif int(entrances.loc[index, ["Vessel Type"]]) <= 299:
        return "Dry Bulk"
    elif int(entrances.loc[index, ["Vessel Type"]]) == 310:
        return "Container"
    elif int(entrances.loc[index, ["Vessel Type"]]) <= 331:
        return "General Cargo"
    elif int(entrances.loc[index, ["Vessel Type"]]) <= 339:
        return "Ro-Ro"
    elif int(entrances.loc[index, ["Vessel Type"]]) <= 349:
        return "Barge"
    elif int(entrances.loc[index, ["Vessel Type"]]) == "Passenger":
        return "Passenger"
    elif int(entrances.loc[index, ["Vessel Type"]]) == "600":
        return "Dry Bulk"
    else:
        return "Other"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Extracting Dates~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Import pckg
import datetime as dt

#Extract iso year and make year column
entrances["Year"] = adt.dt.isocalendar().year

#Extract month and make year column -- note: isocalendar returns a week number, week day, and year -- no month, so I use the normal month
entrances["Month"] = adt.dt.month

#Extract iso week and make week column
entrances["Week"] = adt.dt.isocalendar().week

#New Variables
y = entrances["Year"]
m = entrances["Month"]
w = entrances["Week"]

#Print series (isolated columns from dataframe) to check
print(y)
print(m)
print(w)


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

