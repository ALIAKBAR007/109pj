import csv 
import plotly.figure_factory as pf
import pandas as pd
import statistics as st

file = pd.read_csv("c109pj.csv")

Ll=file["reading score"].to_list()
Tl=file["writing score"].to_list()



mean = st.mean(Ll)
median = st.median(Ll)
mode = st.mode(Ll)

print("Mean of Ll is {}" .format(mean))
print("Median of Ll is {}" .format(median))
print("Mode of Ll is {}" .format(mode))

ST=st.stdev(Ll)
print("ST is {}" .format (ST))

min1= mean-3*ST
max1= mean+3*ST
firstSDList=[]
for o in Ll:
    if o>min1 and o<max1:
        firstSDList.append(o)

a=len(firstSDList)
total=len(Ll)

P=(a*100)/total

print("{}% 3rd of Tl" .format(P))
