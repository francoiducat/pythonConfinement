# basic bokeh line graph

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#raw data
#x=[1,2,3,4,5]
#y=[6,7,8,9,10]

# or data from pandas

csv=pandas.read_csv("resources/data.csv")

#prepare the output file
output_file("line.html")

#create figure object
f=figure()

#create line plot from raw data
#f.line(x,y)

#create line plot from csv
f.line(csv.x,csv.y)

show(f)
print(csv["x"])
print(csv.x)