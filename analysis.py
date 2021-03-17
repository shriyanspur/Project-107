import pandas as p
import csv
import plotly.graph_objects as pg

data = p.read_csv('data.csv')

student_data = data.loc[data['student_id'] == "TRL_987"]

print(student_data.groupby("level")["attempt"].mean())

chart = pg.Figure(pg.Bar(
            x = student_data.groupby("level")["attempt"].mean(),
            y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            orientation = 'h'))

chart.show()