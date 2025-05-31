# -*- coding: utf-8 -*-

"""
Created on Sat Apr 15 21:33:57 2023

@author: anyse
"""

import numpy as np
#Plotting
import matplotlib.pyplot as plt
#Lese CSV
import csv

data = []

#Henter data fra csvfil
with open(r'C:\MTELSYS\ESDA2\D8\scopeYtData.csv') as csvfile:
    csvreader = csv.reader(csvfile)


    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
        
    #Legger inn data fra hver kanal i hver sin liste
    time = [(p[0]) for p in data]
    ch1 = [(p[1]) for p in data]
    #ch2 = [(p[2]) for p in data]
    



    fig, (ax) = plt.subplots()
    

    
    
    ax.plot(time, ch1, label='$y(t)$', color='orange')
    # ax.plot(time, ch2, label='$V_0$')    
    ax.set_xlabel('Tid [s]')
    ax.set_ylabel('Amplitude [V]')
    ax.legend(loc='upper right')
    ax.axhline(y = 0, color = 'black')
    # ax.axvline(x = 0.00001, color = 'black')
    ax.set_title('Utgangssignal $y(t)$')
    ax.set_xlim(0.02,0.030)
    # ax.grid()
    
    # Lagrer figuren
    fig.savefig('C:\MTELSYS\ESDA2\D8\scopeYt.png', dpi=400)