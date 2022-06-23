# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
 
# fig = make_subplots(rows=1, cols=2)

# fig.add_trace(go.Scatter(y=[4,2,1], mode="lines"), row=1, col=1)
# fig.add_trace(go.Bar(y=[2,1,3]), row= 1, col=2)

# fig.show()

# from plotly.subplots import make_subplots

# fig = make_subplots(rows=1, cols=2)#返回一个plotly.graph_objs类的实例对象

# #这个实例对象有可以添加子图的简便方法
# fig.add_scatter(y=[4, 2, 1], mode="lines", row=1, col=1)
# fig.add_bar(y=[2, 1, 3], row=1, col=2)

# fig.show()


# import plotly.graph_objects as go
# import plotly.express as px 

# fig = go.Figure(
#     data=[go.Scatter(y=[1, 3, 2], line_color="crimson")],
#     # layout=dict(title=dict(text="A Graph Objects Figure Without Magic Underscore Notation"))
#     layout_title_text="A Graph Objects Figure With Magic Underscore Notation"#这可叫做魔法注解，用多个带下划线的属性来引用
# )

# fig.show()

# import plotly.graph_objects as go
# import plotly.express as px 
 
# df = px.data.iris()

# #一个散点图对象
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
#                  title="Using The add_trace() method With A Plotly Express Figure")
# fig.add_trace(
#     go.Scatter(#这是一个顶级api
#         x= [2,4],
#         y=[4,8],
#         mode = 'lines',
#         line=go.scatter.Line(color="gray"),
#         showlegend=False
#     )
# )

# fig.show()

# import plotly.graph_objects as go 

# fig = go.Scatter(#这是一个顶级api
#         x= [2,4],
#         y=[4,8],
#         mode = 'lines',
#         line=go.scatter.Line(color="gray"),
#         showlegend=False
# )

# fig.show()

