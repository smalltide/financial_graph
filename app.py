from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 10)

df = data.DataReader(name = "GOOG", data_source="yahoo", start = start , end = end)

date_increase = df.index[df.Close > df.Open]
date_decrease = df.index[df.Close < df.Open]

df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close) / 2
df["Height"] = abs(df.Close - df.Open)

p = figure(x_axis_type = "datetime", width = 1000, height = 300)
p.title.text = "Candlestick Chart"
hours_12 = 12 * 60 * 60 * 1000

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
       hours_12, df.Height[df.Status == "Increase"], fill_color = "green", line_color = "black")

p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
       hours_12, df.Height[df.Status == "Increase"], fill_color = "red", line_color = "black")


output_file("cs.html")
show(p)
