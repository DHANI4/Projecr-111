from operator import mod
from typing import Counter
import pandas as pd
from pandas.core.algorithms import mode
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df=pd.read_csv("population.csv")
data=df["population"].to_list()

def randomSetofMean(counter):
    dataSet=[]
    for i in range(0,counter):
        rand_index=random.randint(0,len(data)-1)
        value=data[rand_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

ml=[]
for i in range(0,1000):
      r=randomSetofMean(100)
      ml.append(r)

sd=statistics.stdev(ml)
mean=statistics.mean(ml)

