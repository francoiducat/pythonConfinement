from bokeh.plotting import figure, output_file, show
import pandas

csv=pandas.read_csv("resources/timeseries.csv",parse_dates=["Date"])


p = figure(plot_width=500, plot_height=400, tools = 'pan, reset',x_axis_type="datetime",sizing_mode="scale_both")


p.line(csv.Date, csv.Close, color="orange", alpha=0.5)

output_file("timeseries.html")
show(p)