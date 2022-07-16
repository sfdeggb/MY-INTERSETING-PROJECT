#huaxiang_explore
## 目标在于描述比列和占比和比重，弄清楚是一个怎样的人

import plotly.express as px 
import pandas as pd
import collections

#加载数据
df = pd.read_csv(r"D:\用户画像\画像数据_finnal.csv")
#使用饼图进行探索
#如何进行每列数据的出现频率计数
# print(df.head(5))
# df=df["地理位置"]
# num_list = df.groupby("地理位置").count()
# print(num_list)
df.add
fig_pie = px.pie(data_frame=df, 
                 values="计数", 
                 names="地理位置",
                 title="用户地域分布",
                 hole=0.3,)

fig_pie.update_traces(textposition='inside',
                  textinfo='label+percent',
                  insidetextorientation="auto")

# print(fig_pie)
fig_pie.show()
# #线性图：用来描述趋势和走向的
