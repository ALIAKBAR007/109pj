import csv 
import plotly.figure_factory as pf
import pandas as pd
import statistics as st

file = pd.read_csv("c109pj.csv")

hl=file["reading score"].to_list()
Tl=file["writing score"].to_list()


mean = st.mean(Tl)
median = st.median(Tl)
mode = st.mode(Tl)

print("Mean of Tl is {}" .format(mean))
print("Median of Tl is {}" .format(median))
print("Mode of Tl is {}" .format(mode))

ST=st.stdev(Tl)
print("ST is {}" .format (ST))

min1= mean-3*ST
max1= mean+3*ST
firstSDList=[]
for o in Tl:
    if o>min1 and o<max1:
        firstSDList.append(o)

a=len(firstSDList)
total=len(Tl)

P=(a*100)/total

print("{}% 3rd of Tl" .format(P))
