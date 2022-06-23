"""使用字典来进行图形组装"""
# fig = dict(
# 	{
# 		'data':[
# 			{
#        		'type':'bar',
#     		'x':[1,2,3],
# 			'y':[1,3,2],
#       		}
# 		],
# 		"layout":{"title":{"text":"a figure of by python dectionary"}}
# 		#"layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
# 	}
# )

# import plotly.io as ptio 

# ptio.show(fig) 

"""使用graphy_objects来进行图像组装"""
# import plotly.graph_objects as go 

# fig = go.Figure(
# 	data = [go.Bar(x=[1,2,3], y= [1,3,2])],
# 	layout=go.Layout(
# 		title = go.layout.Title(text="a figure of Graphy object")
# 	)
# )

# fig.show()

# import plotly.graph_objects as go

# dict_of_fig = dict({
#     "data": [
#         {
#         "type": "bar",
#         "x": [1, 2, 3],
#         "y": [1, 3, 2]
#         }
#         ],
#      "layout": {"title": {"text": "A Figure Specified By A Graph Object With A Dictionary"}}
# })

# fig = go.Figure(dict_of_fig)
# fig.show()

"""将图像对象转化为字典或json对象"""

import plotly.graph_objects as go

fig = go.Figure(
	data=[go.Bar(
		x=[1,2,3],
		y = [3,2,1]
	)],
	layout=go.Layout(height=600, width=800)
)
print(fig.to_dict())
print("\n\n")
print(fig.to_json())


