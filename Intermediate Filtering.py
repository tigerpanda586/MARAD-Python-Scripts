# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 22:36:41 2021

@author: Jessica Brown
@email: TreePerson586@yahoo.com
"""
#Import Pckgs
import pandas as pd
import numpy as np

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

#~~~~~~~~~~~~~~~~~~~~~~~~~Intermediate Filtering~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Select where Arrival Port is 5201
ap_5201 = entrances[ap == "5201"]
print(ap_5201)

#Rows where arrival date/time is before June 4
adt_b0604 = entrances[adt < "06/04/2021 00:00"]
print(adt_b0604)

#Rows where arrival date/time is after June 4
adt_a0604 = entrances[adt >= "06/05/2021 00:00"]
print(adt_a0604)

#Rows where arrival date/time is June 4
adt_0604 = entrances[np.logical_and(adt >= "06/04/2021 00:00", adt < "06/05/2021 00:00")]
print(adt_0604)

#Select where passengers > 0
tp_not_0 = entrances[tp > 0]
print(tp_not_0)

#Select where rows registration country code is "US"
rcc_us = entrances[rcc == "US"]
print(rcc_us)

#Select Vessel Name column for rows with US registration country code
rcc_us_vn = rcc_us["Vessel Name"]
print(rcc_us_vn)

#Select Owner Name and Operator Name for rows where Owner Name == Operator name
own_opn_bool = entrances["Owner Name"] == entrances["Operator Name"]
own_opn_bool_true = (entrances[own_opn_bool == True])
own_opn_bool_true = own_opn_bool_true.merge(entrances, how = "left")
own_opn_same = own_opn_bool_true[["Owner Name", "Operator Name"]]
print(own_opn_same)

#Select rows where Arrival Port is not 5201
ap_not_5201 = entrances[ap != "5201"]
print(ap_not_5201)

#Select Vessel Name where rows registration country code is not "US"
rcc_not_us = entrances[rcc != "US"]
rcc_not_us_vn = rcc_not_us["Vessel Name"]
print(rcc_not_us_vn)

#Select rows where arrival port is 5201 and registration country code is "US"
ap_5201_rcc_us = entrances[np.logical_and(ap == "5201", rcc == "US")]
print(ap_5201_rcc_us)

#Select all rows where arrival port is 5201 or registration code is "US"
ap_5201_or_rcc_us = entrances[np.logical_or(ap == "5201", rcc == "US")]
print(ap_5201_or_rcc_us)                     