import re
import scrapy
from scrapy.http import Request
from Lianjia.items import LianjiaItem

class MySpider(scrapy.Spider):
    name = 'Lianjia'
    base_url = 'https://sz.lianjia.com'
    start_url = 'https://sz.lianjia.com/ershoufang/'

    def start_requests(self):
        response = Request(self.start_url)
        # /ershoufang/luohuqu/
        district = response.xpath('//div[@data-role="ershoufang"]//a//@href').extract()
        for url in district:
            district_url = self.base_url + url
            yield Request(district_url, self.parse)






