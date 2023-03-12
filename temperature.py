import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the spreadsheet into a Pandas DataFrame
data = pd.read_excel('data.xlsx')

x_axis = data['X']
y_axis = data['Y']
y_axis2 = data['Y2']

# make the y values less than 0 the color blue and greater than 0 the color red
plt.bar(x_axis, y_axis, width=5, color=['blue' if y < 0 else 'red' for y in y_axis])
# plot the y2 values as a line
plt.plot(x_axis, y_axis2, color='black')

# add a legend for Y1 that includes the colors for the both bars and the Y2 line
plt.legend(['Lowess 5', 'No smoothing', 'Y1', 'Y2'])

# add a caption on the figure below the plot
plt.figtext(.5, .0001, "Source: https://climate.nasa.gov/vital-signs/global-temperature/", horizontalalignment='center', fontsize=8)

# plot the data
plt.title("Global Land-Ocean Temperature Index")
plt.xlabel("Temperature")
plt.ylabel("Years")
plt.show()

