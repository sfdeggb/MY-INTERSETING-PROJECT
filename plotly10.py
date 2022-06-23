try:
    
	import pandas as pd 
	import plotly.express as px
except Exception():
    print("the third moudle is not found, please check in!")
    
# #导入数据
# path =u"D:/us.us.csv"
# df = pd.read_csv(path,parse_dates=['date'], index_col=0)#将数据集中date列解析为日期，并以其为索引列
# #将数据复制一份
# df_all = df.copy()
#df_all = data.copy()
# 将时间格式转为字符串格式的日期，以 YYYY-mm-dd 的形式保存
# df_all['dates'] = df_all['date'].apply(lambda x:x.strftime('%Y-%m-%d'))
# # 添加现存确诊列
# df_all['current'] = df_all['confirmed'] - df_all['cured'] - df_all['dead']
# df_all.fillna('', inplace=True)
# print(df_all.info())
# df_all
# # 国内总计数量
# df_cn = df_all.query("country=='中国' and province==''") #按照bool表达式来查询一列数据
# df_cn = df_cn.sort_values('date',ascending=False)#按列名排序数据

# # 国外，按国家统计
# df_oversea = df_all.query("country!='中国'") 
# df_oversea = df_oversea.fillna(value="")
# df_oversea = df_oversea.sort_values('date',ascending=False)

# df_global =  df_cn.append(df_oversea)
# df_global = df_global.sort_values(['country','date'])
# df_global
#pandas按列名存取数据
#['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']#size几号桌给的，total——biil：上一天的数据+当天小费
"""这里直接使用小费数据集吧"""
df = px.data.tips()
#打印前几行看一下
# print(df.head(5))

###线形图
def px_line():
    fig = px.line(df, x=df.index, y="tip", title="做个尝试")#这里的y也可以是多变量的列表[ , , ]，就可以话出多条线
    return fig

# fig1 = px_line()
# fig1.show()
def px_line_facet():
    fig = px.line(
        data_frame=df,
		x=df.index,
    	y="total_bill",
		facet_col = "time",#按照时间来分列显示
		#facet_row ="time",
		#line_group='time',
		#log_y = True
	)
    #fig.update_traces(mode='markers+lines')
    return fig

# fig2 = px_line_facet()
# fig2.show()
### 面积图
def px_area():
    fig = px.area(data_frame=df,
                  x="tip",
                  y="total_bill",
                  color= "sex",
                  #line_group="time"
                  )
    return fig

# fig3 = px_area()
# fig3.show()

def plot_scatter():
    fig = px.scatter(data_frame=df, 
                     x="tip", 
                     y="total_bill", 
                     title="没啥意义",
                     color = "sex", 
                     size="tip")#size 参数设置按照什么来显示大小
    return fig;

# fig4 = plot_scatter()
# fig4.show()
### @这里换一数据集合
df2= px.data.election()
# print(df2.head(5))

# def plot_pie():
#     fig=px.pie(data_frame=df2, 
#                names="winner", 
#                 values=[[[df2["winner"].<limiang> == "Joly"? A:B ?,]]]#这里如果可以做个多重判断也是可以的。
#                 #color="winner"#添加hole参数可以变成环
#                 )
#     return fig

# fig5= plot_pie()
# fig5.show()


###@柱状图（不同的东西站有多大量）
#fig = px.bar(df,x='country',y='confirmed',color='country')
#oretation = "h", 可以进行水平画图
#log_x=True， 熟知太大可以采用对数
#barmode="group" ， 默认堆叠，这里可以改成分组
# pattern_shape="country", #要改那个参数
# pattern_shape_sequence=[".", "x", "+",'/','\\'],#要改成什么


###@小提琴图
# box=True；显示分位数等
# points='all' ，可以在小提琴图旁边展示数据的密度分布情况

###@密度图
#绘制数据密度分布情况
# px.strip()，来绘制数据密度分布，

# ###@甘特图
# def plot_timeline():
#     df = pd.DataFrame([
#         dict(Task="项目1",Start='2021-02-01', Finish='2021-03-20', Manager='Lemon', Completion=90),
#         dict(Task="项目2",Start='2021-03-11', Finish='2021-04-01', Manager='Mark', Completion=80),
#         dict(Task="项目3",Start='2021-02-12', Finish='2021-04-25', Manager='Lemon', Completion=70),
#         dict(Task="项目4",Start='2021-05-11', Finish='2021-06-15', Manager='Join', Completion=90),
#     ])
#     fig = px.timeline(data_frame=df, x_start='Start', x_end="Finish",y="Task")
#     fig.update_yaxes(autorange="reversed")
#     return fig

# fig6 = plot_timeline()
# fig6.show()


### @地图
## 使用另一个数据集合
df3 =px.data.gapminder()
# print(df3.head(5))
new_df3 = df3.query("year == 2007")
print(new_df3.head(5))

def plot_map():
    fig=px.scatter_geo(data_frame=new_df3, locations="iso_alpha",#在什么地方显示位置
                       size='pop',
                       )
    return fig

# fig7 = plot_map()
# fig7.show()
