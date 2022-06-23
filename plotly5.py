import plotly.graph_objects as go 

fig = go.Figure(
	go.Indicator(
		domain = {'x':[0,1], 'y':[0,1]},#设置域的范围
		value = 4.3,
		mode = "gauge+number+delta",
		title = {'text':'Suncess Metric'},
		delta={'reference':3.9},#三角洲
		gauge={'bar':{'color':"lightgreen"},#设置规矩
				'axis':{'range':[None, 5]},
				'steps':[
					{'range':[0,2.5], 'color':'lightgray'},
					{'range':[2.5, 4], 'color':'lightblue'},
				],
         }
	)
)

fig.show()