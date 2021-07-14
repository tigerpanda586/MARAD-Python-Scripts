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

#Assign variables to each column -- made for ease of coding, to easily call variables
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

#Modify datetimes -- this is necesarry for "parse_dates" when dates are not in standard form
#W/o this, data will not be classified as "datetime"
#%m is month like "01" -- %d is day like "27" -- %Y is year like "2002"
#%H is hour like "15" (military time) -- %M is minute like "32"
pd.to_datetime(udt, format = "%m/%d/%Y %H:%M")
pd.to_datetime(edt, format = "%m/%d/%Y %H:%M")
pd.to_datetime(adt, format = "%m/%d/%Y %H:%M")
pd.to_datetime(cdt, format = "%m/%d/%Y %H:%M")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Basic Data Wrangling~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Count entries of data per column
entrances_count = entrances.count()

#Count blank entries per column
entrances_blank = entrances.isnull().sum()

#Sum of Total Passengers
sum_tp = tp.sum()

#Mean, Median, Mode of Gross Tonnage
mean_gt = gt.mean()
med_gt = gt.median()
mod_gt = gt.mode()

#Minimum and Maximum of Net Tonnage
min_nt = nt.min()
max_nt = nt.max()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Basic Data Filtering~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Import Package
import numpy as np

#Store Entrance/Date Time as own dataFrame
df_edt = entrances[["Entrance Date/Time"]]

#Store Date Columns as DataFrame
df_dates = entrances[["Entrance Date/Time", "Arrival Date/Time", "Create Date/Time", "Update Date/Time"]]

#Select all number columns
numeric_inputs = entrances.select_dtypes(include = np.number)

#This command when printed will list column info
numeric_inputs.columns

#Select row by row number
s_1321 = entrances.loc[1321]
df_1321 = entrances.loc[[1321]]

#Select multiple rows -- ":" slices indicies to get what's before ":" to what's after ":" but not including that index
#Putting a comma "," allows you to pass more than one command at a time -- so printing "df_multiple" will give 2 results
df_multiple = entrances.loc[1321:1341], entrances.loc[1520:1540]

#Select Multiple Columns and Rows -- gives rows (indicies) of specified columns -- ex: "Cargo Type Code"
df_multiple_rc = entrances.loc[1321:1341, ["Cargo Type Code", "Draft Feet", "Draft Inches"]]



