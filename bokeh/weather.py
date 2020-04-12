from bokeh.plotting import figure,output_file, show
import pandas

xsls=pandas.read_excel("resources/verlegenhuken.xlsx")

output_file("verlegenhuken.html")
f=figure(plot_width=500,plot_height=400, tools='pan')

f.title.text="Temperature and Air Pressure"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Temperature (°C)"
f.yaxis.axis_label="Pressure (hPa)"    

f.circle(xsls.Temperature/10,xsls.Pressure/10,size=0.5)
show(f)
