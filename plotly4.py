import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

df = px.data.tips()
fig = go.Figure(go.Sunburst(
    						labels=["Female", "Male", "Dinner", "Lunch", 'Dinner ', 'Lunch '],
    						parents=["", "", "Female", "Female", 'Male', 'Male'],
    						values=np.append(
        									df.groupby('sex').tip.mean().values,
        									df.groupby(['sex', 'time']).tip.mean().values),
    						marker=dict(colors=px.colors.sequential.Emrld)
    						),
                
                layout=go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)')
                )


fig.update_layout(margin=dict(t=0, l= 0, r = 0, b = 0),
                  title_text="Tiping Habbits Per Gender, Time and Day")
fig.show()