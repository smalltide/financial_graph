from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

start = datetime.datetime(2015, 11, 1)
end = datetime.datetime(2016, 3, 10)

df = data.DataReader(name = "GOOG", data_source="yahoo", start = start , end = end)

date_increase = df.index[df.Close > df.Open]
date_decrease = df.index[df.Close < df.Open]

df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close) / 2
df["Height"] = abs(df.Close - df.Open)
hours_12 = 12 * 60 * 60 * 1000

p = figure(x_axis_type = "datetime", width = 1000, height = 300, responsive = True)
p.title.text = "Candlestick Chart"
p.grid.grid_line_alpha = 0.3

p.segment(df.index, df.High, df.index, df.Low, color = "Black")

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
       hours_12, df.Height[df.Status == "Increase"], fill_color = "#CCFFFF", line_color = "black")

p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
       hours_12, df.Height[df.Status == "Decrease"], fill_color = "#FF3333", line_color = "black")

script1, div1 = components(p)
cdn_js = CDN.js_files
cdn_css = CDN.css_files

output_file("cs.html")
show(p)
