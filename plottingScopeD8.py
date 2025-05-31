import numpy as np
import matplotlib.pyplot as plt
import csv

data = []

#Henter data fra csvfil
with open(r'maalingerMotor/motorMaalingMedStoy2.csv') as csvfile:
    csvreader = csv.reader(csvfile)

    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
        
    time = [(p[0]) for p in data]
    ch1 = [(p[1]) for p in data]

    fig, (ax) = plt.subplots()  
    ax.plot(time, ch1, label='DC-Motor Spenning', color='orange')
    ax.set_xlabel('Tid [s]')
    ax.set_ylabel('Amplitude [V]')
    ax.legend(loc='upper right')
    ax.set_title('DC-Motor Spenning med Støy 2')
    ax.grid()
    # Lagrer figuren
    fig.savefig('motorMaalingMedStoy2.png', dpi=400)