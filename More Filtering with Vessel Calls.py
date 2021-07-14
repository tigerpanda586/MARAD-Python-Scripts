# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 22:36:41 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""
#Import Pckg
import pandas as pd

#Import txt file
data = "Entrances06062021.txt"
entrances = pd.read_csv(data, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Vessel Calls ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#How Many vessel calls into port 5201? -- filter for 5201
ap_5201 = entrances[ap == "5201"]

#Count the number of vessels that come into port 5201
vc_5201 = ap_5201.count()[0]

#How many vessel calls for vessel imo 9837080? -- filter for 9837080
ap_imo_9837080 = entrances[imo == "9837080"]

#Count number of vessel calls for imo 9837080
vc_imo_9837080 = ap_imo_9837080.count()[0]

#Make list with unique arrival ports
ap_drop = entrances.drop_duplicates(subset = "Arrival Port")

#Take out all non-arrival port columns (turn into a series)
ap_drop_unique = ap_drop["Arrival Port"]

#Turn into dataframe
df_adu = ap_drop_unique.to_frame()

#Fix indicies (list them 0-98)
df_adu.reset_index(drop = True, inplace = True)

#Count how many vessel calls in each port
vc = entrances["Arrival Port"].value_counts()

#Turn into dataframe
df_vc = vc.to_frame()

#Rename Column
df_vc.columns = ["Vessel Calls"]

#Fix indicies (list them 0-98)
df_vc.reset_index(drop = True, inplace = True)

#Concatenate vessel calls and arrival ports into one dataframe --
#showing how many vessel calls there are per arrival port
df_c = pd.concat([df_adu, df_vc], axis = 1)

#Print result
print(df_c)


    

    




