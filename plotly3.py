import plotly.express as px

df = px.data.gapminder()
df2= px.data.tips()
fig = px.scatter(df, 
                 x="gdpPercap",
                 y="lifeExp",
                 animation_frame="year",
                 size="pop",
                 color="continent",
                 hover_name="country",
                 log_x=True,
                 log_y=True,
                 size_max=55,
                 range_x=[100, 100000],
                 range_y=[25,90])

fig.update_layout(width = 1000,
                  height=800,
                  xaxis_showgrid=False,
                  yaxis_showgrid=False,
                  paper_bgcolor="rgba(0,0,0,0)",
                  plot_bgcolor="rgba(0,0,0,0)")

fig.show()
