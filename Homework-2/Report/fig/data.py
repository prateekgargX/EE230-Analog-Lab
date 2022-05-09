import matplotlib.pyplot as plt
import numpy as np
import math

#_______________________________________________________________________________________________________________
filename     = "data.txt"              #filename : This is name of the file containing the x and y values
Plot_Title   =  "$log(I)$ vs $V $"
x_axis_label = "V"
y_axis_label = "$log(I)$"
#_______________________________________________________________________________________________________________

with open(filename) as f:
    lines = f.readlines()
x_readings = []
y_readings = []
for line in lines:
    val=line.rstrip().split()
    x_readings.append((float(val[0])))
    y_readings.append(float(val[1]))

x_readings=np.array(x_readings)
y_readings=np.log(np.array(y_readings))

plt.plot(x_readings , y_readings)
plt.title(Plot_Title)
plt.xlabel(x_axis_label)
plt.ylabel(y_axis_label)
#plt.yscale("log")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.grid(which='minor', color='#CCCCCC', linestyle=':')
plt.show()
