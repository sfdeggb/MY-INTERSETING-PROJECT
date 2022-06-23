import plotly.express as px 
from vega_datasets import data
import pandas as pd 

df= data.movies()
df = df.dropna()#将有nan值的行从dataframe删除掉
df['Genre_id'] = df.Major_Genre.factorize()[0]#datafarme对象的操作
#桑基图，来进行流量的分配
fig = px.parallel_categories(
	df,
	dimensions=['MPAA_Rating','Creative_Type','Major_Genre'],
 color="Genre_id",
 color_continuous_scale=px.colors.sequential.Emrld,
)

fig.show()
