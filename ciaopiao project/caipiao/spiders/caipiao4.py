import scrapy
from caipiao.items import CaipiaoItem

class caiSpider(scrapy.Spider):
    #爬虫的名字
    name ='caipiao4'
    #爬虫的开始点，可以有多个
    start_urls = ["http://www.cwl.gov.cn/ygkj/wqkjgg/"]
    
    def parse(self, response):
        #提取数据
        #通过xpath，或者通过css来选择页面的某一部分
		#爬取100期，最多也是100期
        for i in range(1,101):
            item = CaipiaoItem()
            xpath_ID ="/html/body/div[2]/div/div/div[2]/div/div/div[4]/table/tbody/tr[{0}]/td[1]".format(i)
            xpath_data = "/html/body/div[2]/div/div/div[2]/div/div/div[4]/table/tbody/tr[{0}]/td[3]/div".format(i)
            xpath_date = "/html/body/div[2]/div/div/div[2]/div/div/div[4]/table/tbody/tr[{0}]/td[2]".format(i)
             
            item['qihao']=response.xpath(xpath_ID)
            item['data']=response.xpath(xpath_data)
            item['date']=response.xpath(xpath_date)
            #返回信息
            yield item

        