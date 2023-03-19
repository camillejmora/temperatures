import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
# import sqlalchemy
import sqlite3

# Connect to the database (create it if it doesn't exist)
conn = sqlite3.connect('database.db')

# Read the data from the spreadsheet into a Pandas DataFrame
data = pd.read_excel('data.xlsx')

# Write the DataFrame to the database table 'data'
data.to_sql('data', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

# Open a new connection to the database
conn = sqlite3.connect('database.db')

# Add new data to the database
new_data = pd.DataFrame({'X': [2024], 'Y': [0.8], 'Y2': [1.2]})
new_data.to_sql('data', conn, if_exists='append', index=False)

# Query the database for the updated data
# database = pd.read_sql('SELECT * FROM data', conn)

# Save the updated data to the Excel file
updated_data = pd.read_sql('SELECT * FROM data', conn)
updated_data.to_excel('data.xlsx', index=False)

# Close the database connection
conn.close()

# Read the data from the spreadsheet into a Pandas DataFrame
data = pd.read_excel('data.xlsx')

x_axis = data['X']
y_axis = data['Y']
y_axis2 = data['Y2']

# make the y values less than 0 the color blue and greater than 0 the color red
bars = plt.bar(x_axis, y_axis, width=5, color=['blue' if y < 0 else 'red' for y in y_axis])

# plot the y2 values as a line
line, = plt.plot(x_axis, y_axis2, color='black')

# add a legend for Y1 that includes the colors for the both bars and the Y2 line
plt.legend(handles=[bars[0], bars[-1], line], labels=['No Smoothing - negative', 'No Smoothing - positive', 'Smoothed'])

# add a caption on the figure below the plot
plt.figtext(.5, .0001, "Source: https://climate.nasa.gov/vital-signs/global-temperature/", horizontalalignment='left', fontsize=8)

# Adjust the spacing between the subplots
plt.subplots_adjust(bottom=0.2)

# set figure size to make room for the legend
fig = plt.gcf()
fig.set_size_inches(10, 6)

# plot the data
plt.title("Global Land-Ocean Temperature Index")
plt.xlabel("Temperature")
plt.ylabel("Years")
plt.show()

# save the plot as a png file
plt.savefig('temperature.png')
