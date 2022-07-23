# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CaipiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    qihao= scrapy.Field()#爬取的期号
    data = scrapy.Field()#爬取的数据
    date = scrapy.Field()#爬取的日期
