# import pandas as pd
# import requests as rq


# # url = "http://api.openweathermap.org/data/2.5/forecast?lat=35&lon=139&appid=59d046440aa1e8adb751bb944ab422d4"
# # rs =rq.get(url)
# # rs = rs.json()
# # df = pd.DataFrame(rs)
# # print(df.head(5))

# # dict= {1:"niam", 2:"caoni"}
# # li= [dict]
# # print(li)

# data_list = [{"cod":"200","message":0,"cnt":40,"list":[{"dt":1658232000,"main":{"temp":297.84,"feels_like":298.79,"temp_min":297.84,"temp_max":297.97,"pressure":1000,"sea_level":1000,"grnd_level":976,"humidity":93,"temp_kf":-0.13},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":100},"wind":{"speed":6.92,"deg":244,"gust":14.32},"visibility":3486,"pop":0.64,"rain":{"3h":0.38},"sys":{"pod":"n"},"dt_txt":"2022-07-19 12:00:00"},{"dt":1658242800,"main":{"temp":297.96,"feels_like":298.82,"temp_min":297.96,"temp_max":298.06,"pressure":1000,"sea_level":1000,"grnd_level":975,"humidity":89,"temp_kf":-0.1},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":99},"wind":{"speed":7.6,"deg":250,"gust":14.21},"visibility":10000,"pop":0.28,"rain":{"3h":0.13},"sys":{"pod":"n"},"dt_txt":"2022-07-19 15:00:00"},{"dt":1658253600,"main":{"temp":296.58,"feels_like":297.51,"temp_min":296.58,"temp_max":296.58,"pressure":1002,"sea_level":1002,"grnd_level":975,"humidity":97,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":94},"wind":{"speed":2.5,"deg":270,"gust":3.9},"visibility":10000,"pop":0.24,"sys":{"pod":"n"},"dt_txt":"2022-07-19 18:00:00"},{"dt":1658264400,"main":{"temp":297.04,"feels_like":297.94,"temp_min":297.04,"temp_max":297.04,"pressure":1003,"sea_level":1003,"grnd_level":976,"humidity":94,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":100},"wind":{"speed":1.19,"deg":249,"gust":1.61},"visibility":10000,"pop":0,"sys":{"pod":"d"},"dt_txt":"2022-07-19 21:00:00"},{"dt":1658275200,"main":{"temp":301.09,"feels_like":304.24,"temp_min":301.09,"temp_max":301.09,"pressure":1004,"sea_level":1004,"grnd_level":977,"humidity":74,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":100},"wind":{"speed":0.89,"deg":64,"gust":1.2},"visibility":10000,"pop":0,"sys":{"pod":"d"},"dt_txt":"2022-07-20 00:00:00"},{"dt":1658286000,"main":{"temp":302.94,"feels_like":306.38,"temp_min":302.94,"temp_max":302.94,"pressure":1004,"sea_level":1004,"grnd_level":977,"humidity":64,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":100},"wind":{"speed":1.93,"deg":98,"gust":2.11},"visibility":10000,"pop":0.04,"sys":{"pod":"d"},"dt_txt":"2022-07-20 03:00:00"},{"dt":1658296800,"main":{"temp":303.38,"feels_like":308.01,"temp_min":303.38,"temp_max":303.38,"pressure":1003,"sea_level":1003,"grnd_level":977,"humidity":67,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":87},"wind":{"speed":0.81,"deg":123,"gust":1.5},"visibility":10000,"pop":0.36,"rain":{"3h":0.25},"sys":{"pod":"d"},"dt_txt":"2022-07-20 06:00:00"},{"dt":1658307600,"main":{"temp":300.48,"feels_like":303.75,"temp_min":300.48,"temp_max":300.48,"pressure":1004,"sea_level":1004,"grnd_level":977,"humidity":81,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":75},"wind":{"speed":1.63,"deg":167,"gust":1.82},"visibility":10000,"pop":0.4,"rain":{"3h":1.13},"sys":{"pod":"d"},"dt_txt":"2022-07-20 09:00:00"},{"dt":1658318400,"main":{"temp":297.99,"feels_like":298.72,"temp_min":297.99,"temp_max":297.99,"pressure":1006,"sea_level":1006,"grnd_level":979,"humidity":84,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":87},"wind":{"speed":0.63,"deg":49,"gust":0.76},"visibility":10000,"pop":0.36,"rain":{"3h":0.13},"sys":{"pod":"n"},"dt_txt":"2022-07-20 12:00:00"},{"dt":1658329200,"main":{"temp":296.64,"feels_like":297.5,"temp_min":296.64,"temp_max":296.64,"pressure":1005,"sea_level":1005,"grnd_level":978,"humidity":94,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":92},"wind":{"speed":1.88,"deg":55,"gust":2.82},"visibility":10000,"pop":0.16,"sys":{"pod":"n"},"dt_txt":"2022-07-20 15:00:00"},{"dt":1658340000,"main":{"temp":296.54,"feels_like":297.42,"temp_min":296.54,"temp_max":296.54,"pressure":1005,"sea_level":1005,"grnd_level":978,"humidity":95,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":96},"wind":{"speed":1.84,"deg":48,"gust":3.6},"visibility":10000,"pop":0.2,"sys":{"pod":"n"},"dt_txt":"2022-07-20 18:00:00"},{"dt":1658350800,"main":{"temp":296.61,"feels_like":297.49,"temp_min":296.61,"temp_max":296.61,"pressure":1007,"sea_level":1007,"grnd_level":979,"humidity":95,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":96},"wind":{"speed":2.16,"deg":57,"gust":4.93},"visibility":10000,"pop":0.08,"sys":{"pod":"d"},"dt_txt":"2022-07-20 21:00:00"},{"dt":1658361600,"main":{"temp":298.6,"feels_like":299.39,"temp_min":298.6,"temp_max":298.6,"pressure":1007,"sea_level":1007,"grnd_level":980,"humidity":84,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":98},"wind":{"speed":2.95,"deg":60,"gust":4.6},"visibility":10000,"pop":0.32,"rain":{"3h":0.13},"sys":{"pod":"d"},"dt_txt":"2022-07-21 00:00:00"},{"dt":1658372400,"main":{"temp":300.63,"feels_like":303.17,"temp_min":300.63,"temp_max":300.63,"pressure":1006,"sea_level":1006,"grnd_level":979,"humidity":73,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":91},"wind":{"speed":3.27,"deg":82,"gust":3.14},"visibility":10000,"pop":0.4,"rain":{"3h":0.19},"sys":{"pod":"d"},"dt_txt":"2022-07-21 03:00:00"},{"dt":1658383200,"main":{"temp":299.75,"feels_like":299.75,"temp_min":299.75,"temp_max":299.75,"pressure":1006,"sea_level":1006,"grnd_level":979,"humidity":74,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":95},"wind":{"speed":1.11,"deg":72,"gust":0.71},"visibility":10000,"pop":0.24,"rain":{"3h":0.13},"sys":{"pod":"d"},"dt_txt":"2022-07-21 06:00:00"},{"dt":1658394000,"main":{"temp":297.77,"feels_like":298.51,"temp_min":297.77,"temp_max":297.77,"pressure":1006,"sea_level":1006,"grnd_level":979,"humidity":85,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":100},"wind":{"speed":1.28,"deg":60,"gust":1.53},"visibility":10000,"pop":0.4,"rain":{"3h":0.25},"sys":{"pod":"d"},"dt_txt":"2022-07-21 09:00:00"},{"dt":1658404800,"main":{"temp":296.89,"feels_like":297.62,"temp_min":296.89,"temp_max":296.89,"pressure":1006,"sea_level":1006,"grnd_level":979,"humidity":88,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":100},"wind":{"speed":0.34,"deg":291,"gust":0.41},"visibility":10000,"pop":0.4,"sys":{"pod":"n"},"dt_txt":"2022-07-21 12:00:00"},{"dt":1658415600,"main":{"temp":296.64,"feels_like":297.45,"temp_min":296.64,"temp_max":296.64,"pressure":1005,"sea_level":1005,"grnd_level":978,"humidity":92,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":100},"wind":{"speed":0.76,"deg":246,"gust":0.8},"visibility":10000,"pop":0.28,"rain":{"3h":0.13},"sys":{"pod":"n"},"dt_txt":"2022-07-21 15:00:00"},{"dt":1658426400,"main":{"temp":296.39,"feels_like":297.17,"temp_min":296.39,"temp_max":296.39,"pressure":1004,"sea_level":1004,"grnd_level":977,"humidity":92,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":91},"wind":{"speed":1.56,"deg":261,"gust":1.8},"visibility":10000,"pop":0.32,"rain":{"3h":0.19},"sys":{"pod":"n"},"dt_txt":"2022-07-21 18:00:00"},{"dt":1658437200,"main":{"temp":296.71,"feels_like":297.42,"temp_min":296.71,"temp_max":296.71,"pressure":1003,"sea_level":1003,"grnd_level":976,"humidity":88,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":63},"wind":{"speed":1.07,"deg":272,"gust":1.61},"visibility":10000,"pop":0.12,"sys":{"pod":"d"},"dt_txt":"2022-07-21 21:00:00"},{"dt":1658448000,"main":{"temp":300.39,"feels_like":302.51,"temp_min":300.39,"temp_max":300.39,"pressure":1003,"sea_level":1003,"grnd_level":976,"humidity":71,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":62},"wind":{"speed":2.98,"deg":262,"gust":6.62},"visibility":10000,"pop":0.08,"sys":{"pod":"d"},"dt_txt":"2022-07-22 00:00:00"},{"dt":1658458800,"main":{"temp":302.39,"feels_like":304.93,"temp_min":302.39,"temp_max":302.39,"pressure":1001,"sea_level":1001,"grnd_level":975,"humidity":62,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":73},"wind":{"speed":2.7,"deg":290,"gust":6.2},"visibility":10000,"pop":0,"sys":{"pod":"d"},"dt_txt":"2022-07-22 03:00:00"},{"dt":1658469600,"main":{"temp":303.35,"feels_like":306.79,"temp_min":303.35,"temp_max":303.35,"pressure":1001,"sea_level":1001,"grnd_level":974,"humidity":62,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":44},"wind":{"speed":0.81,"deg":266,"gust":3.81},"visibility":10000,"pop":0.04,"sys":{"pod":"d"},"dt_txt":"2022-07-22 06:00:00"},{"dt":1658480400,"main":{"temp":300.07,"feels_like":302.71,"temp_min":300.07,"temp_max":300.07,"pressure":1001,"sea_level":1001,"grnd_level":974,"humidity":80,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":45},"wind":{"speed":1.17,"deg":287,"gust":2.3},"visibility":10000,"pop":0.32,"sys":{"pod":"d"},"dt_txt":"2022-07-22 09:00:00"},{"dt":1658491200,"main":{"temp":297.24,"feels_like":298.03,"temp_min":297.24,"temp_max":297.24,"pressure":1002,"sea_level":1002,"grnd_level":975,"humidity":89,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":50},"wind":{"speed":1.2,"deg":259,"gust":1.33},"visibility":10000,"pop":0.4,"rain":{"3h":0.19},"sys":{"pod":"n"},"dt_txt":"2022-07-22 12:00:00"},{"dt":1658502000,"main":{"temp":296.63,"feels_like":297.41,"temp_min":296.63,"temp_max":296.63,"pressure":1002,"sea_level":1002,"grnd_level":974,"humidity":91,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":4},"wind":{"speed":0.6,"deg":66,"gust":0.8},"visibility":10000,"pop":0.28,"rain":{"3h":0.13},"sys":{"pod":"n"},"dt_txt":"2022-07-22 15:00:00"},{"dt":1658512800,"main":{"temp":296.69,"feels_like":297.55,"temp_min":296.69,"temp_max":296.69,"pressure":1001,"sea_level":1001,"grnd_level":974,"humidity":94,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":26},"wind":{"speed":2.05,"deg":73,"gust":3.31},"visibility":10000,"pop":0.24,"rain":{"3h":0.13},"sys":{"pod":"n"},"dt_txt":"2022-07-22 18:00:00"},{"dt":1658523600,"main":{"temp":296.6,"feels_like":297.48,"temp_min":296.6,"temp_max":296.6,"pressure":1003,"sea_level":1003,"grnd_level":976,"humidity":95,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":97},"wind":{"speed":2.19,"deg":73,"gust":4.1},"visibility":10000,"pop":0.4,"rain":{"3h":0.19},"sys":{"pod":"d"},"dt_txt":"2022-07-22 21:00:00"},{"dt":1658534400,"main":{"temp":298.22,"feels_like":299.05,"temp_min":298.22,"temp_max":298.22,"pressure":1003,"sea_level":1003,"grnd_level":976,"humidity":87,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":97},"wind":{"speed":2.4,"deg":74,"gust":3.21},"visibility":10000,"pop":0.24,"rain":{"3h":0.19},"sys":{"pod":"d"},"dt_txt":"2022-07-23 00:00:00"},{"dt":1658545200,"main":{"temp":299.98,"feels_like":302.27,"temp_min":299.98,"temp_max":299.98,"pressure":1004,"sea_level":1004,"grnd_level":977,"humidity":77,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":74},"wind":{"speed":2.25,"deg":69,"gust":2.21},"visibility":10000,"pop":0.52,"rain":{"3h":0.44},"sys":{"pod":"d"},"dt_txt":"2022-07-23 03:00:00"},{"dt":1658556000,"main":{"temp":300.11,"feels_like":302.53,"temp_min":300.11,"temp_max":300.11,"pressure":1004,"sea_level":1004,"grnd_level":977,"humidity":77,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":82},"wind":{"speed":1.11,"deg":50,"gust":1.21},"visibility":10000,"pop":0.56,"rain":{"3h":0.69},"sys":{"pod":"d"},"dt_txt":"2022-07-23 06:00:00"},{"dt":1658566800,"main":{"temp":298.66,"feels_like":299.49,"temp_min":298.66,"temp_max":298.66,"pressure":1005,"sea_level":1005,"grnd_level":978,"humidity":85,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":97},"wind":{"speed":1.1,"deg":25,"gust":1.6},"visibility":10000,"pop":0.4,"rain":{"3h":0.19},"sys":{"pod":"d"},"dt_txt":"2022-07-23 09:00:00"},{"dt":1658577600,"main":{"temp":297.02,"feels_like":297.86,"temp_min":297.02,"temp_max":297.02,"pressure":1007,"sea_level":1007,"grnd_level":979,"humidity":92,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":87},"wind":{"speed":0.67,"deg":10,"gust":0.72},"visibility":10000,"pop":0.44,"sys":{"pod":"n"},"dt_txt":"2022-07-23 12:00:00"},{"dt":1658588400,"main":{"temp":296.04,"feels_like":296.89,"temp_min":296.04,"temp_max":296.04,"pressure":1007,"sea_level":1007,"grnd_level":979,"humidity":96,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":100},"wind":{"speed":0.27,"deg":24,"gust":0.34},"visibility":10000,"pop":0.32,"rain":{"3h":0.13},"sys":{"pod":"n"},"dt_txt":"2022-07-23 15:00:00"},{"dt":1658599200,"main":{"temp":295.42,"feels_like":296.24,"temp_min":295.42,"temp_max":295.42,"pressure":1007,"sea_level":1007,"grnd_level":979,"humidity":97,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":84},"wind":{"speed":0.58,"deg":82,"gust":0.71},"visibility":10000,"pop":0.32,"rain":{"3h":0.19},"sys":{"pod":"n"},"dt_txt":"2022-07-23 18:00:00"},{"dt":1658610000,"main":{"temp":296.29,"feels_like":297.11,"temp_min":296.29,"temp_max":296.29,"pressure":1008,"sea_level":1008,"grnd_level":981,"humidity":94,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":100},"wind":{"speed":0.47,"deg":125,"gust":0.71},"visibility":10000,"pop":0.24,"rain":{"3h":0.25},"sys":{"pod":"d"},"dt_txt":"2022-07-23 21:00:00"},{"dt":1658620800,"main":{"temp":300.07,"feels_like":302.36,"temp_min":300.07,"temp_max":300.07,"pressure":1008,"sea_level":1008,"grnd_level":981,"humidity":76,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":97},"wind":{"speed":0.65,"deg":67,"gust":1.2},"visibility":10000,"pop":0.4,"rain":{"3h":0.38},"sys":{"pod":"d"},"dt_txt":"2022-07-24 00:00:00"},{"dt":1658631600,"main":{"temp":300.72,"feels_like":303.46,"temp_min":300.72,"temp_max":300.72,"pressure":1008,"sea_level":1008,"grnd_level":981,"humidity":74,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":98},"wind":{"speed":0.74,"deg":51,"gust":1.41},"visibility":10000,"pop":0.36,"rain":{"3h":0.75},"sys":{"pod":"d"},"dt_txt":"2022-07-24 03:00:00"},{"dt":1658642400,"main":{"temp":300.37,"feels_like":302.97,"temp_min":300.37,"temp_max":300.37,"pressure":1008,"sea_level":1008,"grnd_level":981,"humidity":76,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":98},"wind":{"speed":0.95,"deg":358,"gust":1.72},"visibility":10000,"pop":0.28,"rain":{"3h":0.38},"sys":{"pod":"d"},"dt_txt":"2022-07-24 06:00:00"},{"dt":1658653200,"main":{"temp":298.96,"feels_like":299.74,"temp_min":298.96,"temp_max":298.96,"pressure":1009,"sea_level":1009,"grnd_level":982,"humidity":82,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":100},"wind":{"speed":1.89,"deg":299,"gust":2.82},"visibility":10000,"pop":0.04,"sys":{"pod":"d"},"dt_txt":"2022-07-24 09:00:00"}],"city":{"id":1851632,"name":"Shuzenji","coord":{"lat":35,"lon":139},"country":"JP","population":0,"timezone":32400,"sunrise":1658173405,"sunset":1658224602}}
# ]

# agr1=[]
# agr2=[]

# for key,value in data_list[0].items():
#     if isinstance(value, list):
#         agr1.append(key)
#     elif isinstance(value, dict):
#         for j in data_list[0][key].keys():
#             l=[]
#             l.append(key)
#             l.append(j)
#             agr2.append(l)
#     else:
#         agr2.append(key)
# import pandas as pd

# df = pd.json_normalize(data_list, agr1, agr2)
# # print(df.head(5))
# # with open("D:\\测试.xlsx", 'r') as f:
# df.to_excel("D:\\测试.xlsx")
# print(df.head(5))
# # print(df.columns)
# df["main.temp"] = df["main.temp"]-273.15
# df['dt'] = df['dt'].apply(datetime.datetime.fromtimestamp)
# print(df["main.temp"])
# print(df['dt'])
##有个问题我得好好了解一下dataframe

# import pandas as pd
# import datetime

# df = pd.read_excel(r"C:\Users\HP\Desktop\海洋系统分析\测试数据.xlsx")
# col_name= ['dt','city.name','city.name','weather','main.temp','main.pressure','main.humidity','wind.speed','wind.deg']
# df2=df[col_name]
# #进行每一列数据的修改，apply函数， dt列, 添加距离列
# df2["main.temp"] = df2["main.temp"]-273.15
# df2['dt'] = df2['dt'].apply(datetime.datetime.fromtimestamp)
# df2["dis"]=12
# # df2["weather"]=list(df2["weather"][0])['icon']
# # df_list.append(df2)
# print("数据形状如下！！！")
# print(df2.shape)
# #将文件保存到本地
# #这里需要知道city_names,和距离列
# df2.to_csv("ninnin.csv")
# # str = "[{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}]"
# # li = list[str]
# # print(type(li))
# import time
# time.sleep(secs)
# for i in range(16):
#     print(i)

# for i in range(10):
#     print("曹尼玛"+str(i))

# companys=["上海公司","四川公司","重庆公司","深圳公司"]
# print(enumerate(companys))

import json
import pandas as pd

with open(r"D:\100 of 100\jsonji\梅州.json") as fp:
	py_obj = json.load(fp)
	# print([py_obj])
	# print(pyobj[0])
	data=[py_obj]
	agr1=[]
	agr2=[]
	for key,value in data[0].items():
		if isinstance(value, list):
			agr1.append(key)
		elif isinstance(value, dict):
			for j in data[0][key].keys():
				l=[]
				l.append(key)
				l.append(j)
				agr2.append(l)
			else:
				agr2.append(key)
	df = pd.json_normalize(data, agr1,agr2)
