# #使用plotly Express模块构建图形对象是最高级也是最常用的数据展现形式
# import plotly.express as px 
# #iris数据库是关于花朵相关数据的数据库
# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y= "sepal_length", color="species", title="散点图")#sepal:花萼
# fig.show()


import numpy as np
import plotly.figure_factory as ff 

x1, y1 = np.meshgrid(np.arange(0,2,.2), np.arange(0,2,.2))#从坐标向量中返回坐标矩阵
print(x1)
print("n\n\n\n\\n")
print(y1)

u1 = np.cos(x1)*y1
v1 = np.sin(x1)*y1

# data1 = np.arange(1, 3, 0.2)#产生一个随机数列表，指定star， stop ， 包左不包右
# print(data1)

fig = ff.create_quiver(x1, y1, u1, v1)

#fig.show()