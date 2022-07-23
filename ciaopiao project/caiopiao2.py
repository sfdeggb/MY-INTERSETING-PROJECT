"""采用模拟浏览器来爬取快乐8的中奖信息"""

#元素的交互(主要是输入和单击)和交互动作, 执行脚本这里不需要。就不在演示
#福彩的这个页面不是一个html页面。
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import requests

def getJson(json_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'}
    response = requests.get(json_url, headers = headers)
    response.encoding="utf-8"
    page = response.text#获取字符串文本
    # page = str(page)
    # print(page)
    return page#获取的是json文本

def getUrlList(page):
    url_list = []
    chazhao_kuai=""
    page = json.loads(page)#转化为python对象
    #是一个字典
    search_res=page["result"]
    
    for unit in search_res:
        chazhao_kuai = unit['detailsLink']#找到的是字符串
        url_list.append(chazhao_kuai)
    return url_list

if __name__ == "__main__":
    root_url = "http://www.cwl.gov.cn"
    jsonurl= "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=kl8&issueCount=100&issueStart=&issueEnd=&dayStart=&dayEnd="
    url_meige = []
    result = []
    page = getJson(jsonurl)
    list = getUrlList(page)
    #拼接每一个url
    for item in list:
        wanzheng = root_url + item
        url_meige.append(wanzheng)
    #检查一下
    # print(url_meige)
    ######接下来就用selnium来模拟访问.shtml页面
    
  	#申明对象
    broswer = webdriver.Edge()
    ##访问页面
    for yuan in url_meige:
        broswer.get(yuan)
        # content = broswer.page_source
        # print(content)
        # elems = broswer.find_elements_by_css_selector("#qiu")#查找类名为qiu的多个元素
        #elems = broswer.find_element(By.CSS_SELECTOR,"money")
        # elem = broswer.find_element_by_tag_name("div")
        #每个页面中的xpath是通用的
        xpath = "/html/body/div[4]/div[1]/div[2]/div/div[4]"
        elems = broswer.find_element_by_xpath(xpath)
        
        broswer.implicitly_wait(5)#模仿人进行一定的等待（隐式的）
        result.append(elems.text)
    print("爬取完毕")
       
    #将数据写入文件
    print("正在写入数据......")
    with open("D:\\caipiao_kuia.txt", "w") as f:
        for res in result:
            f.write(res)#text返回的是一个字符串
            f.write("\n")#每个数据之间换行  
    print("数据写入完毕！")
    broswer.close()

