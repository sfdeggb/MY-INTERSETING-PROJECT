#weather data

"""
请求api：api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
参数：lat，lon， apikey
转码器：http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
参数：cityname, apikey
mykey: 59d046440aa1e8adb751bb944ab422d4
免费版只能几个小时的数据吧!
api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
"""

import xlwings as xw
import requests as rq
import json
import pandas as pd
import datetime
import time

key= "59d046440aa1e8adb751bb944ab422d4"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
cookis={'_ga':'GA1GA1.2.9773019.1658116467',
            '__gads':'ID=2eb39f16fe5cb9b4-2247a72e3ad500cb:', 
            'signed_in':'jjgjg',
            '_gid':'GA1.2.732247642.1658463160' 
}
# 读取excel文
def get_city_names():
	file= r"C:\Users\HP\Desktop\海洋系统分析\距海城市.xlsx"
	wbook=xw.Book(file)
	wsheet=wbook.sheets["城市选择"]
	ran_citys=wsheet.range("A2:A17")
	ran_dis=wsheet.range("B2:B17")
	citys=[]
	dis=[]
	for num in range(0,16):
		name = ran_citys[num, 0].value
		distance=ran_dis[num,0].value
		citys.append(name)
		dis.append(distance)
	print("城市加载成功！！")
	return citys,dis

#获取经纬度
def get_con_alt(names):
    loc = list()
    print("正在获取经纬度信息.......")
    for name in names:
        url="http://api.openweathermap.org/geo/1.0/direct?q="+name+"&appid="+key
        response = rq.get(url, headers=headers)
        if(response.status_code!=200):
            print("请求出现错误， 请检查")
        content = response.json()#这里直接进行了反序列化
        # print(type(content))
        #处理json文件
        # content = json.load(response)
        # print(content)
        lat=content[0]["lat"]
        lon=content[0]["lon"]
        temp =[lat, lon]
        loc.append(temp)
        # break
    print("位置经纬度，获取成功！")
    return loc

# names = get_city_names()
# loc = get_con_alt(names)  
# print(loc)

#请求数据
def get_data(loc):
	lenght = len(loc)
	data_list=[]
	mykey= "59d046440aa1e8adb751bb944ab422d4"
	for i in range(lenght):
		url = "http://api.openweathermap.org/data/2.5/forecast?lat="+str(loc[i][0])+"&lon="+str(loc[i][1])+"&appid="+mykey
		#要在这里形成dataframe
		print("正在加载城市"+str(i+1))
		print(url)
		rs =rq.get(url, headers=headers)
		time.sleep(0.5)
		#直接进行了发序列化,这里rs的类型为字典
		rs = rs.json()
		#形成列表
		rs=[rs]
		#形成函数参数
		agr1=[]
		agr2=[]
		for key,value in rs[0].items():
			if isinstance(value, list):
				agr1.append(key)
			elif isinstance(value, dict):
				for j in rs[0][key].keys():
					l=[]
					l.append(key)
					l.append(j)
					agr2.append(l)
			else:
				agr2.append(key)
		df = pd.json_normalize(rs, agr1,agr2)
		data_list.append(df)
		print("城市"+str(i+1)+"加载成功!")
	return data_list

def deco_data(datas, distances):
	df_list=[]
	i =0
	for data in datas:
        #data is  a dataframe
		col_name= ['dt','city.name','weather','main.temp','main.pressure','main.humidity','wind.speed','wind.deg']
		df2=pd.DataFrame(data=data, columns=col_name)
		#进行每一列数据的修改，apply函数， dt列, 添加距离列
		df2["main.temp"] = df2["main.temp"]-273.15
		df2['dt'] = df2['dt'].apply(datetime.datetime.fromtimestamp)
		df2["dis"]=distances[i]
		i=i+1
		df_list.append(df2)
	return df_list

def save_to_local(dfs, city_names):
	i= 0
	print("正在写入数据!")
	for df in dfs:
		#查看数据形状
		print("数据形状如下！！！")
		print(df.shape)
		#将文件保存到本地
		#这里需要知道city_names,和距离列
		df.to_csv(city_names[i]+".csv")
		i=i+1
	print("数据已经全部加载到了本地，下面开始分析吧！！")

if __name__ == "__main__":
	city_names, dis =get_city_names()
	loc = get_con_alt(city_names)
	data_list = get_data(loc)
	# dfs = deco_data(data_list, distances=dis)
	# save_to_local(dfs,city_names)
