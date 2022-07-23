#analisey

import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import sklearn.svm as svm
import numpy as np

### 进行数据分析了
##加载本地数据，16个城市
##第一组
shantou= pd.read_csv(filepath_or_buffer)
chaonan=pd.read_csv()
puning=pd.read_csv()
jiedong=pd.read_csv()
##第二组
zhaozhou=pd.read_csv()
fenshun=pd.read_csv()
beidou=pd.read_csv()
xiandong=pd.read_csv()
##第三组
wuhau=pd.read_csv()
meizhou=pd.read_csv()
zhangzhou=pd.read_csv()
longyan=pd.read_csv()
##第四组
heping=pd.read_csv()
dingnan=pd.read_csv()
shaoguan=pd.read_csv()
ganzhou=pd.read_csv()

#分析一天中气温的变化趋势
#选择第一个最近的城市
y1=shantou['main.temp']
x1=shantou['dt']
fig, ax=plt.subplot()
plt.xticks(rotation=70)
hours=mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatters(hours)
ax.plot(x1, y1, 'r')

#最高气温与沿海距离之间的关系
#选择第一组和第二组城市进行对比
y2_close=shantou['main.temp']
x2_close=shantou['dt']
y3_close=chaonan['main.temp']
x3_close=chaonan['dt']
y4_close=puning['main.temp']
x4_close=puning['dt']
y5_close=jiedong['main.temp']
x5_close=jiedong['dt']

y2_distance=heping['main.temp']
x2_distance=heping['dt']
y3_distance=dingnan['main.temp']
x3_distance=dingnan['dt']
y4_distance=shaoguan['main.temp']
x4_distance=shaoguan['dt']
y5_distance=ganzhou['main.temp']
x5_distance=ganzhou['dt']

fig, ax=plt.subplot()
plt.xticks(rotation=70)
hours=mdates.DateFormatter('%H:%M')
plt.plot(x2_close,y2_close,'r',x3_close,y3_close,'r', x4_close,y4_close,'r',x5_close,y5_close,'r')
plt.plot(x2_distance,y2_distance,'g',x3_distance,y3_distance,'g', x4_distance,y4_distance,'g',x5_distance,y5_distance,'g')

#最低气温与沿海距离之间的关系
#采用SVR算法找出临界点
dis=[
    shantou['dis'][0], chaonan['dis'][0], puning['dis'][0],jiedong['dis'][0],
     zhangzhou['dis'][0],fenshun['dis'][0],beidou['dis'][0],xiandong['dis'][0],
     wuhau['dis'][0],meizhou['dis'][0],zhangzhou['dis'][0],longyan['dis'][0],
     heping['dis'][0],dingnan['dis'][0],shaoguan['dis'][0],ganzhou['dis'][0]
    ]
temp_max=[
	shantou['main.temp'].max(), chaonan['main.temp'].max(), puning['main.temp'].max(),jiedong['main.temp'].max(),
     zhangzhou['main.temp'].max(),fenshun['main.temp'].max(),beidou['main.temp'].max(),xiandong['main.temp'].max(),
     wuhau['main.temp'].max(),meizhou['main.temp'].max(),zhangzhou['main.temp'].max(),longyan['main.temp'].max(),
     heping['main.temp'].max(),dingnan['main.temp'].max(),shaoguan['main.temp'].max(),ganzhou['main.temp'].max()
	]
temp_min=[
	shantou['main.temp'].min(), chaonan['main.temp'].min(), puning['main.temp'].min(),jiedong['main.temp'].min(),
     zhangzhou['main.temp'].min(),fenshun['main.temp'].min(),beidou['main.temp'].min(),xiandong['main.temp'].min(),
     wuhau['main.temp'].min(),meizhou['main.temp'].min(),zhangzhou['main.temp'].min(),longyan['main.temp'].min(),
     heping['main.temp'].min(),dingnan['main.temp'].min(),shaoguan['main.temp'].min(),ganzhou['main.temp'].min()
	]
#画图
plt.plot(dis,temp_max,'ro')
#SVR算法
svr_line1=svm.SVR(kernel='linear',C=1e3)
svr_line2=svm.SVR(kernel='linear',C=1e3)
svr_line1.fit(x2_close, y2_close)
svr_line2.fit(x3_close, y3_close)
xp1=np.arange(10,100,10).reshape(9,1)
xp2=np.arange(50,400,50).reshape(7,1)
yp1=svr_line1.predict(xp1)
yp2=svr_line2.predict(xp2)

plt.plot(xp1,yp1,c='b',label="Strong effect")
plt.plot(xp2,yp2, c='r', label="light effect")
plt.axis(0, 400, 27,32)
plt.scatter(x,y,c='k', label='data')

#分析湿度与距离之间的关系
y6_close=shantou['main.humidity']
x6_close=shantou['dt']
y7_close=chaonan['main.humidity']
x7_close=chaonan['dt']
y8_close=puning['main.humidity']
x8_close=puning['dt']
y9_close=jiedong['main.humidity']
x9_close=jiedong['dt']

# zhaozhou=pd.read_csv()
# fenshun=pd.read_csv()
# beidou=pd.read_csv()
# xiandong=pd.read_csv()
# ##第三组
# wuhau=pd.read_csv()
# meizhou=pd.read_csv()
# zhangzhou=pd.read_csv()
# longyan=pd.read_csv()
# ##第四组
# heping=pd.read_csv()
# dingnan=pd.read_csv()
# shaoguan=pd.read_csv()
# ganzhou=pd.read_csv()
y6_distance=heping['main.humidity']
x6_distance=heping['dt']
y7_distance=dingnan['main.humidity']
x7_distance=dingnan['dt']
y8_distance=shaoguan['main.humidity']
x8_distance=shaoguan['dt']
y9_distance=ganzhou['main.humidity']
x9_distance=ganzhou['dt']

fig, ax=plt.subplot()
plt.xticks(rotation=70)
hours=mdates.DateFormatter('%H:%M')
plt.plot(x6_close,y6_close,'r',x7_close,y7_close,'r', x8_close,y8_close,'r',x9_close,y9_close,'r')
plt.plot(x6_distance,y6_distance,'g',x7_distance,y7_distance,'g', x8_distance,y8_distance,'g',x9_distance,y9_distance,'g')

#湿度最小值
hum_min = [
	shantou['main.humidity'].min(), chaonan['main.humidity'].min(), puning['main.humidity'].min(),jiedong['main.humidity'].min(),
     zhangzhou['main.humidity'].min(),fenshun['main.humidity'].min(),beidou['main.humidity'].min(),xiandong['main.humidity'].min(),
     wuhau['main.humidity'].min(),meizhou['main.humidity'].min(),zhangzhou['main.humidity'].min(),longyan['main.humidity'].min(),
     heping['main.humidity'].min(),dingnan['main.humidity'].min(),shaoguan['main.humidity'].min(),ganzhou['main.humidity'].min()
]
#湿度最大值
hum_max = [
	shantou['main.humidity'].max(), chaonan['main.humidity'].max(), puning['main.humidity'].max(),jiedong['main.humidity'].max(),
     zhangzhou['main.humidity'].max(),fenshun['main.humidity'].max(),beidou['main.humidity'].max(),xiandong['main.humidity'].max(),
     wuhau['main.humidity'].max(),meizhou['main.humidity'].max(),zhangzhou['main.humidity'].max(),longyan['main.humidity'].max(),
     heping['main.humidity'].max(),dingnan['main.humidity'].max(),shaoguan['main.humidity'].max(),ganzhou['main.humidity'].max()
]
plt.plot(dis, hum_max, 'bo')

#分析风向和风速与距离之间的关系
#采用极区图,这里要画10个图
# new_df = df
hist, bins=np.histogram(shantou['wind.deg'],8,(0,360))

def show_wind_reg(values, names, max_value):
    NUM=8
    theta=np.arange(0,2*np.pi, 2*np.pi/NUM)
    raddi=np.array(values)
    plt.axes([0.025,0.025,0.95,0.95], polar=True)
    colors=[(1-x/max_value, 1-x/max_value, 0.75) for i in raddi]
    plt.bar(theta, raddi, bottom=0.0, width=(2*np.pi/NUM), colors=colors)
    plt.title(label)
def show_wind_speed(df_citys):
    degs=np.arange(45,361,45)
    tmp=[]
    for deg in degs:
        tmp.append(df_citys[(df_citys['wind.speed']>(deg-46)) & (df_citys['wind.speed']<deg)],
                   df_citys['wind.speed'].mean())  
    return np.array(tmp)

#调用函数
# show_wind(hist,"shantou",max(hist))
# show_wind(show_wind_speed,"shantou")
#end