# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:05:20 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""
#Import package
import pandas as pd

#Import data
ec2021 = pd.read_csv("ec2021.txt", delimiter = "|", dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "IMO" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date/Time" : str, "Update Date/Time" : str, "Entrance Date/Time" : str, "Arrival Date/Time" : str}, parse_dates = ["Update Date/Time", "Create Date/Time", "Clearance Date/Time", "Entrance Date/Time", "Arrival Date/Time"])

#Drop duplicate values
ec2021.drop_duplicates()

#First make DataFrame out of  column you want to convert
on = ec2021[["Owner Name"]]

#Make it so every value only appears once
on.drop_duplicates()

#Create an empty dictionary for it
az = {}

#Assign each value to a number (its index number is the same as the label)
for label, row in enumerate(on.iterrows()):
	az[on["Owner Name"][label]] = label

#Assign number values to it with loop
for label, row in enumerate(ec2021.iterrows()):
	ec2021.loc[label, ["Owner Name Numbered"]] = az[ec2021["Owner Name"][label]]

#Make sure to save this as a new text file (.txt) or your choice so you don’t have to do this again
ec2021.to_csv = (header = True, index = False, path_or_buf = “C:/Users/TreeP/Desktop/Python/ec2021numbered.txt”)

