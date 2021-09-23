import plotly.graph_objects as pg
import csv
import pandas as pd

df = pd.read_csv("studentid.csv")

mean = df.groupby("level")["attempt"].mean()

fig = pg.Figure(pg.Bar(x = mean, y = ["Level 1","Level 2", "Level 3", "Level 4"], orientation = "h"))

fig.show()