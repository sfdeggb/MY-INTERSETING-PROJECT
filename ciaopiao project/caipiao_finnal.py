"""所有库的文档可以在这个pypi网址上得到：https://pypi.org/"""

#urllib不能抓取这个网站，采用requests库，urllib库经常和re模块一起使用
#urllib库：https://www.cnblogs.com/sherlockChen/p/8064896.html
#正则表达式用来检索，替换，匹配某个模式的文本
#如何构建（re）正则表达式来匹配或者采用Xpath来匹配
#可以通过API可以获得网站提供的信息，但是API往往是有利于网站本身的
#为了爬虫不被网站封杀常有以下方法：1.设置user agent 2.防止IP被封，可以设置代理访问，属性为proxies
#re难用----》beautifulsoup库
#Beautiful Soup 4.4.0 文档 https://beautifulsoup.readthedocs.io/zh_CN/latest/
#requests库：https://docs.python-requests.org/zh_CN/latest/user/quickstart.html
#向服务器发送数据，提供参数
#对于动态网页，爬虫程序需自动获取网页中动态变化的数据。
#Ajax动态网页的基础是XMLHttpRequest（XHR）
#要用到json数据的话，要导入json模块
#beautiful库可以通过标签查找，可以通类名查找。也可以通过id查找
#模拟浏览器登录selnuine：https://selenium-python-zh.readthedocs.io/en/latest/navigating.html
#爬取工具fidder使用：https://www.cnblogs.com/conquerorren/p/8472285.html
#XPath是一种在XML和HTML文件中查找元素的语言，其属于lxml库
#获取xpath的两种方法：
#1.观察规律
#2.使用浏览器自动获取
#下次浏览器模拟:声明浏览器对象，访问页面，查找元素，元素交互，动作交互，执行js脚本，获取信息
#requests-html是对现有库的二次封装，使用更加简单。可以简单地获取超链接和通过css选择器find()\
#和XPATH语法来获取元素：https://www.jianshu.com/p/380974ba9540
#爬取数据的存储可以用，SQLite数据库（这个有驱动就可以进行）
#还可以是MYSQL数据库，要用PySQL驱动来操作MYSQL数据库。
#下次就到了scrapy爬虫框架

import requests
from bs4 import BeautifulSoup
import csv
import os
import json

def getHtmlCode(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'}
    response = requests.get(url, headers = headers)
    response.encoding="utf-8"
    page = response.text#获取字符串文本
    # page = str(page)
    # print(page)
    print("数据获取完毕！\n\n")
    return page#获取的是json文本

def jiexi(page):
    qihao=list()
    data=list()
    date=list()
    money=list()
    location=list()
    count=0
    
    zhuaihua = json.loads(page)#转化为python对象
    # print(type(zhuaihua))#转化成了字典
    search_res=zhuaihua['result']#找到查询结果
    
    for unit in search_res:
        #找到的是字符串
        chazhao1 = unit['red']
        chazhao2 = unit['blue']
        chazhao3= unit['code']
        chazhao4= unit['date']
        chazhao5= unit['content']
        chazhao6 = unit['poolmoney']
        
        chazhao = (str)(chazhao1)+","+str(chazhao2)
        data.append(chazhao)
        qihao.append(chazhao3)
        date.append(chazhao4)
        location.append(chazhao5)
        money.append(chazhao6)
        count+=1
    print("数据解析完毕！\n\n") 
       
    return qihao, data, date, location, money,count

#由于采取的页面是.sthml页面一般方法行不通，必须的采用seliunme的框架

#数据的储存
def download(qihao, data, date, location, money, count):
    localpath = "D:\\"#储存在D盘下
    
    if not os.path.exists(localpath):
        os.mkdir(localpath)#创建一个目录
    #每改变一个资源来源这里也要改
    f = open(localpath+"\caipiao_qlc.csv","w")
    #构建是csv写入对象
    csv_writer = csv.writer(f)   
    #构建表头
    csv_writer.writerow(["ID","data","date","location","money"]) 
    #写入内容
    for i in range(0, count):
        csv_writer.writerow([qihao[i], data[i], date[i], location[i], money[i]])
    
    
    print("数据写入完毕！请到指定位置查看！")        
            
#主函数执行                
if __name__== "__main__":
    root_url = "http://www.cwl.gov.cn"
    count_str = input("请输入你想要查询多少期：（最多为近100期）,没办法有限制")
    #几个参数：name：彩票种类；issueCount：请求期数；issueStart：
    # 第多少期开始；issueEnd：第多少期结束；dayStart=开始时间；dayEnd：结束时间
    json_url1 = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount="+count_str
    json_url2 = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=kl8&issueCount="+count_str
    json_url3 = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=3d&issueCount="+count_str
    json_url4 = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=qlc&issueCount="+count_str
    
    json_html = getHtmlCode(json_url4)
    qihao, data, date, location, money,count = jiexi(json_html)#redlist中的每个元素是一个长字符串
    download(qihao, data, date, location, money,count)
