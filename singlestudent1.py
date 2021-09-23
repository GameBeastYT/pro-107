import csv
import plotly.graph_objects as pg
import pandas as pd

df = pd.read_csv("studentid.csv")

studentdf = df.loc[df["student_id"]=="TRL_mda"]

mean = studentdf.groupby("level")["attempt"].mean()

print(mean)

fig = pg.Figure(pg.Bar(y = mean, x = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = "v"))

fig.show()