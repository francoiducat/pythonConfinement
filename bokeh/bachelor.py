from bokeh.plotting import figure,output_file, show
import pandas

csv=pandas.read_csv("resources/bachelors.csv")

output_file("bachelors.html")
f=figure(plot_width=500,plot_height=400, tools='pan')

f.title.text="Cool Data"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Date"
f.yaxis.axis_label="Intensity"    

f.line(csv.Year,csv.Engineering)
show(f)