# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:24:48 2021

@author: Jessica Brown
@email: TreePerson586@yahoo.com
"""

#Import Pckg
import pandas as pd

#Import new text file for Port Names
data3 = "PLBN.txt"

#Read as Fixed Width File
#This file included unnecessary "|", so they were named "Filler"s and deleted below
portname = pd.read_fwf(data3, widths = [54, 1, 9, 1, 14], names = ["Port Name", "Filler 1", "Arrival Port Code", "Filler 2", "District/Port"], dtype = str)

#Make portname dataframe with Port Name and Arrival Port Code columns only -- delete unnecessary
del portname["District/Port"]
del portname["Filler 1"]
del portname["Filler 2"]

#Print dataframe
print(portname)



