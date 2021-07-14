# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:32:31 2021

@author: Jessica Brown
@position: Economics Intern at MARAD 06/2021 - 07/2021
@personal email: TreePerson586@yahoo.com
@school email: Jessica.Marie.Brown@live.mercer.edu
"""

#Import Pckgs
import pandas as pd
import datetime as dt

#Assign a variable to all Entrance files
a = "Entrances01032021.dat"
b = "Entrances01102021.dat"
c = "Entrances01172021.dat"
d = "Entrances01242021.dat"
e = "Entrances01312021.dat"
f = "Entrances02072021.dat"
g = "Entrances02142021.dat"
h = "Entrances02212021.dat"
i = "Entrances02282021.dat"
j = "Entrances03072021.dat"
k = "Entrances03142021.dat"
l = "Entrances03212021.dat"
m = "Entrances03282021.dat"
n = "Entrances04042021.dat"
o = "Entrances04112021.dat"
p = "Entrances04182021.dat"
q = "Entrances04252021.dat"
r = "Entrances05022021.dat"
s = "Entrances05092021.dat"
t = "Entrances05162021.dat"
u = "Entrances05232021.dat"
v = "Entrances05302021.dat"
w = "Entrances06062021.dat"
x = "Entrances06132021.dat"
y = "Entrances06202021.dat"
z = "Entrances06272021.dat"

#Assign variable to all Clearance files
aa = "Clearances01032021.dat"
bb = "Clearances01102021.dat"
cc = "Clearances01172021.dat"
dd = "Clearances01242021.dat"
ee = "Clearances01312021.dat"
ff = "Clearances02072021.dat"
gg = "Clearances02142021.dat"
hh = "Clearances02212021.dat"
ii = "Clearances02282021.dat"
jj = "Clearances03072021.dat"
kk = "Clearances03142021.dat"
ll = "Clearances03212021.dat"
mm = "Clearances03282021.dat"
nn = "Clearances04042021.dat"
oo = "Clearances04112021.dat"
pp = "Clearances04182021.dat"
qq = "Clearances04252021.dat"
rr = "Clearances05022021.dat"
ss = "Clearances05092021.dat"
tt = "Clearances05162021.dat"
uu = "Clearances05232021.dat"
vv = "Clearances05302021.dat"
ww = "Clearances06062021.dat"
xx = "Clearances06132021.dat"
yy = "Clearances06202021.dat"
zz = "Clearances06272021.dat"

#Create a list holding each variable for Entrance files
eucea = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

#Create a list holding each variable for Clearance files
cucc = [aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz]

#Create Parser that will be inserted into pd.read with lambda
parser = lambda date: dt.datetime.strptime(date, "%m/%d/%Y %H:%M")

#Create blank list for Entrances
n = []

#Using loop, read every Entrance file in eucea then append each dataframe to list "n"
for thing in eucea:
    x = pd.read_csv(thing, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Entrance Date/Time", "Arrival Date/Time"], date_parser = parser, dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str})
    n.append(x)

#Concatenate every Entrance dataframe in list "n" into one big dataframe
entrances = pd.concat(n, ignore_index = True)

#Create blank list for Clearances
m = []

#Using loop, read every Clearance file in cucc then append each dataframe to list "m"
for thing in cucc:
    y = pd.read_csv(thing, delimiter = "|", parse_dates = ["Update Date/Time", "Create Date/Time", "Clearance Date/Time"], date_parser = parser, dtype = {"Filing Port" : str, "Sequence" : str, "Arrival Port" : str, "Agent Name" : str, "Cargo Type Code" : str, "Last Domestic Port" : str, "Last Foreign Port" : str, "Via Port" : str, "Vessel Repair" : str, "Vessel Name" : str, "IMO" : str, "Call Sign Number" : str, "Official Registration Number" : str, "Built Country Code" : str, "Vessel Type" : str, "USCS Code" : str, "Owner Name" : str, "Operator Name" : str, "Operator Country Code" : str, "Registration Country Code" : str, "Clearance Date/Time" : str, "Create Date Time" : str, "Update Date/Time" : str})
    m.append(y)

#Concatenate every Clearance dataframe in list "m" into one big dataframe
clearances = pd.concat(m, ignore_index = True)

#Creating a column in each bigger dataframe called "Movement" to denote which rows are --
#entrances and which are clearances so this data can be told apart in their combined dataframe
entrances["Movement"] = "Entrance"
clearances["Movement"] = "Clearance"

#Concatenate entrance and cleaance dataframe into a single dataframe
ec = pd.concat([clearances, entrances], ignore_index = True)

#Print dataframe to verify hardwork
print(ec)

#Save dataframe to computer as a text file 
ec.to_csv(index = False, sep = "|", header = True, path_or_buf = "C:/Users/TreeP/Downloads/Okay/ec2021.txt")






