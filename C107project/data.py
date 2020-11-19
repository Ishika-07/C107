import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv")
df.groupby("level", as_index=False)["attempt","student_id"].mean()
fig = px.scatter(df, x="student_id", y="level",color ="attempt")
fig.show()