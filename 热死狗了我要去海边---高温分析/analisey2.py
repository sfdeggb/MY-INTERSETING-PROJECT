#analissey2.py

import os, json
import time
import datetime
import pandas as pd
import xlwings as xw

path="D:\\100 of 100\\jsonji"
coll=list()
lenght=0
data_list=[]

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

def load_1():
	for file_name in os.listdir(path):
		ident = file_name.split(".")[0]
		coll.append(ident)
		global lenght
		lenght=lenght+1
	#load josn
	for i in range(lenght):
		with open(path+"\\"+ident+".json") as fp:
			py_obj = json.load(fp)
			# print(py_obj)
			#[{}]==data
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
			data_list.append(df)
	return data_list, coll

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
 
if __name__=="__main__":
    datas, names =load_1()
    city_names, dis = get_city_names()
    dfs = deco_data(datas=datas, distances=dis)
    save_to_local(dfs, names)
