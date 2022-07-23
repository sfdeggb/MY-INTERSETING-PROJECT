""" SQLite访问需要python标准模块SQLite3来操作
	request-html库的使用
	爬取彩票数据7乐彩"""
 
#- * -  encoding UTF-8  - * -
#author MISS ZHU
#这个还是需要得到每一个shtml页面的url
#整个requests_html最重要的一个属性就是r.html，他代表一个HTML对象

import requests_html
from requests_html import HTMLSession
import sqlite3
import json
import re

def getUrlList(page):
    url_list = []
    url_meige = []
    chazhao_kuai=""
    root_url="http://www.cwl.gov.cn/"
    page = json.loads(page)#转化为python对象
    #是一个字典
    search_res=page["result"]
    
    for unit in search_res:
        chazhao_kuai = unit['detailsLink']#找到的是字符串
        url_list.append(chazhao_kuai)

    for item in url_list:
        wanzheng = root_url + item
        url_meige.append(wanzheng)
        
    return url_meige

def store_data(data):
    #建立链接，创建一个数据库
    con= sqlite3.connect("D:7cailei.db")
    #建立一个数据库中的表
    con.execute("create table qi_lei_cai(ID primary key, date, data)")
    #建立一个游标
    cur = con.cursor()
    #向数据库添加数据
    for item in data:
        # insert_sql_table = 
        cur.execute("insert into qi_lei_cai (ID, date, data) values(?, ?, ?)",(item[0], item[1], item[2]))#执行语句
        cur.commit()#提交
    #最后关闭数据库
    con.close()

def main():    
	root_url="http://www.cwl.gov.cn/"
	json_url="http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=qlc&issueCount=100&issueStart=&issueEnd=&dayStart=&dayEnd="
	#这里采用多重列表
	temp_store = list()
	item_list = list()
	data_list = list()
 
	session = HTMLSession()#创建一个类的对象
	hearders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"}
	r_page = session.get(json_url, headers=hearders)
	# print(r_page.cookies)
	url_list = getUrlList(r_page.html.html)#r.html是HTNL对象
	
	# print(url_list)
	#这里的xpath是通用的
	#无xpath_ID = ""，需要从json文件中找出来
	xpath_id = "/html/body/div[4]/div[1]/div[1]"#这个文本内容还要提取里面的数字
	xpath_date = "/html/body/div[4]/div[1]/div[2]/div/div[2]"#日期
	# xpath_data = "/html/body/div[4]/div[1]/div[2]/div/div[4]"#数据
	
	#无xpath_address = ""
	for url in url_list:
	
		session2 = HTMLSession()
		r=session2.get(url, headers= hearders)
  
  		#通过xpath要查找元素
		cai_id = r.html.xpath(xpath_id)
		date = r.html.xpath(xpath_date)
		pattern = re.compile(r'(?<=第)\d+\.?\d*')#这是一个正则表达式的对象
		#会返回一个列表
		mm = pattern.findall(str(cai_id[0].text))

		for i in range(1, 9):
			xpath_data= "/html/body/div[4]/div[1]/div[2]/div/div[4]/div[{0}]".format(i)
			data=r.html.xpath(xpath_data)
			print(data[0].html)
			data= data[0].text
			data_list.append(data)
   
		print(mm)#期号（列表）
		print(date[0].text)#日期（字符串）
		print(data_list)#数据
  
		item_list.append(mm)
		item_list.append(date)
		item_list.append(data)
  
		temp_store.append(item_list)#列表中写入一个列表
		break
  
	#这个主函数最重要返回的是一个列表，列表的每个元素就是要插入的4个值
	return temp_store


 
data = main()
# print(data)
# store_data(data)
     

