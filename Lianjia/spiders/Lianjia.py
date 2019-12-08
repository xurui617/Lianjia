import re
import scrapy
from scrapy.http import Request
from Lianjia.items import LianjiaItem

class MySpider(scrapy.Spider):
    name = 'Lianjia'
    base_url = 'https://sz.lianjia.com'
    start_url = 'https://sz.lianjia.com/ershoufang/'

    def start_requests(self):
        yield Request(self.start_url, self.get_district)

    def get_district(self, response):
        # /ershoufang/luohuqu/
        district = response.xpath('//div[@data-role="ershoufang"]//a//@href').extract()
        for url in district:
            district_url = self.base_url + url
            print("=============", district_url)
            yield Request(district_url, self.get_urls)

    def get_urls(self, response):
        print("*********************")
        urls = response.xpath('//ul[@class="sellListContent"]//li//div[@class="title"]//a//@href').extract()
        for url in urls:
            yield Request(url, self.get_info)

    def get_info(self, response):
        print("++++++++++++++++")

        pass







