#画像app
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd 

app = Dash(__name__)


app.layout = html.Div([
    html.H4('用户画像分析'),
    dcc.Graph(id="graph"),
    html.P("Names:"),
    dcc.Dropdown(id='names',
        options=["答题时长","地理位置","专业年级","网站登录方式","教学满意度","专业满意度","导师安排","职业规划","学习方式","问题解决","规划","生活问题"],
        value='计数', clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(id='values',
        options=['计数'],
        value='计数', clearable=False
    ),
])


@app.callback(
    Output("graph", "figure"), #输出
    Input("names", "value"), #输入
    Input("values", "value"))#输入
def generate_chart(names, values):
    df = pd.read_csv(r"D:\用户画像\画像数据_finnal.csv")#数据集
    fig = px.pie(df, values=values, names=names, hole=.3)
    fig.update_traces(textposition='inside',
                  textinfo='label+percent',
                  insidetextorientation="auto")
    return fig


app.run_server(debug=True)