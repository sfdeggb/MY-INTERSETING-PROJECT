import plotly.express as px
from vega_datasets import data
import pandas as pd

#df = data.disasters()
df = pd.read_csv(u"D:\disasters.csv")#加载数据
df = df[df.Year >1990]#删选数据

fig = px.bar(df, 
             y= "Entity",
             x= "Deaths",
             animation_frame="Year",
             orientation = "h",
             range_x = [0, df.Deaths.max()],
             color = "Entity")
fig.update_layout(width= 1000,
                  height = 800,
                  xaxis_showgrid = True,
                  yaxis_showgrid = True,
                  paper_bgcolor="rgba(51,0,0,0)",
                  plot_bgcolor="rgba(51,0,0,0)",
                  title_text = "Evolution of Natural Disasters",
                  showlegend=True)
fig.update_xaxes(title_text="Number of Deaths")
fig.update_yaxes(title_text="灾难类型")
fig.show()
#print(df.url)
print(data.disasters.url)
                 
