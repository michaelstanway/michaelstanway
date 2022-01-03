# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:10:06 2021

@author: micha
"""

import pandalab_base as pd
import numpy as np
import mathplotlib as plt

#opens the data file and displays it
myfile = open("detector_data.txt")
print(myfile.read())

#converts the data file to usable data
data = pd.read_csv("detector_data.txt")
print(data)

#puts it into a table
np.shape(data)

#same thing but creates a gap between columns
data = pd.read_csv("detector_data.txt", sep = ' ')
print(data)

#ensures that none of the rows are classed as headers
data = pd.read_csv("detector_data.txt", sep = ' ', header = None)
print(data)

#creates headers for the columns
data = pd.read_csv("detector_data.txt", sep = ' ', header = None, names = ['Date', 'Time', 'Hit', 'Ard Time', 'Amp', 'Ard Amp', 'Dead Time'])
print(data)

#prints certain columns
print(data.iloc[2, 4])

#prints certain rows
print(data.iloc[82:83])

#plots as a graph
data.iloc[0:10].plot()

subset = data[["Hit"]]
print(subset)

subset.iloc[0:100].plot()

subset = data[["Amp"]]
subset.iloc[0:100].plot()

data.plot.scatter('Time', 'Amp')

#this is all used to plot a variety of different graphs

subdata = data[0:10]
subdata.plot.scatter('Hit', 'Amp')

data.plot.scatter('Hit', 'Amp', c = 'Amp', colormap='viridis')

data2 = pd.read.csv("detector_data_2.txt", sep = ' ', header = None, names = ['Date', 'Time', 'Hit', 'Ard Time', 'Amp', 'Ard Amp', 'Dead Time'])
ax1 = data.plot('Hit', 'Amp', c = 'r')
ax2 = data2.plot('Hit', 'Amp', c = 'g', ax = ax1)
ax1.legend(['1.5Hz', '1.7Hz'])

ax1 = data.plot('Hit', 'Amp', kind = 'bar')
ax2 = data2.plot('Hit', 'Amp', kind = 'bar', ax = ax1)
ax1.legend(['1.5Hz', '1.7Hz'])

ax1 = data.plot('Hit', 'Amp', kind = 'barh')
ax2 = data2.plot('Hit', 'Amp', kind = 'barh', ax = ax1)
ax1.legend(['1.5Hz', '1.7Hz'])

ax1 = data.plot('Hit', 'Amp', kind = 'hist')
ax2 = data2.plot('Hit', 'Amp', kind = 'hist', ax = ax1)
ax1.legend(['1.5Hz', '1.7Hz'])

ax1 = data.plot('Hit', 'Amp', kind = 'kde')
ax2 = data2.plot('Hit', 'Amp', kind = 'kde', ax = ax1)
ax1.legend(['1.5Hz', '1.7Hz'])

ax1 = data.plot('Hit', 'Amp', kind = 'pie')
ax2 = data2.plot('Hit', 'Amp', kind = 'pie', ax = ax1)
ax1.legend(['1.5Hz', '1.7Hz'])

