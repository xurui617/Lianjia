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
            # print("=============", district_url)
            yield Request(district_url, self.get_urls)

    def get_urls(self, response):
        # print("*********************")
        urls = response.xpath('//ul[@class="sellListContent"]//li//div[@class="title"]//a//@href').extract()
        for url in urls:
            yield Request(url, self.get_info)

    def get_info(self, response):
        # print("++++++++++++++++")
        item = LianjiaItem()

        item.链接 = response.url
        item.小区名称 = response.xpath('//div[@class="communityName"]//text()').extract()[1]
        item.所在区域 = scrapy.Field()
        item.地铁站 = scrapy.Field()
        item.总价 = response.xpath('//span[@class="total"]//text()').extract()
        item.单价 = response.xpath('//span[@class="unitPriceValue"]//text()').extract()[0]
        item.建筑时间 = response.xpath('//div[@class="area"]//div[@class="subInfo"]//text()').extract()[0].split('/')[0]



        pass







