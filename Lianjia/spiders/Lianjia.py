import re
import scrapy
from scrapy.http import Request
from Lianjia.items import LianjiaItem

class MySpider(scrapy.Spider):
    name = 'Lianjia'
    base_url = 'https://sz.lianjia.com'
    start_url = 'https://sz.lianjia.com/ershoufang/'
    # 爬取二手房首页
    def start_requests(self):
        yield Request(self.start_url, self.get_district)

    # 获取当前城市（深圳）所有城区
    def get_district(self, response):
        # /ershoufang/luohuqu/
        district = response.xpath('//div[@data-role="ershoufang"]//a//@href').extract()
        for url in district:
            district_url = self.base_url + url
            # print("=============", district_url)
            yield Request(district_url, self.get_pages)

    # 获取当前城区所有页码页面
    def get_pages(self, response):
        max_page = int(response.xpath('//div[@class="page-box fr"]/div/@page-data').extract()[0].split(',')[0].split(':')[-1])
        for i in range(1, max_page+1):
            url_temp = response.url + 'pg' + str(i)
            yield Request(url_temp, self.get_urls)

    # 获取每个城区，每个页码页面
    def get_urls(self, response):
        # print("*********************")
        urls = response.xpath('//ul[@class="sellListContent"]//li//div[@class="title"]//a//@href').extract()
        for url in urls:
            yield Request(url, self.get_info)

    def get_info(self, response):
        # print("++++++++++++++++", item)
        item = LianjiaItem()
        # print("++++++++++++++++", item.keys)
        item['链接'] = response.url
        item['小区名称'] = response.xpath('//div[@class="communityName"]//text()').extract()[1]
        item['所在区域'] = response.xpath('//div[@class="areaName"]//span[@class="info"]//a//text()').extract()
        item['地铁站'] = response.xpath('//div[@class="areaName"]/a[@class="supplement"]//text()').extract()
        item['总价'] = response.xpath('//span[@class="total"]//text()').extract()
        item['单价'] = response.xpath('//span[@class="unitPriceValue"]//text()').extract()[0]
        item['建筑时间'] = response.xpath('//div[@class="area"]//div[@class="subInfo"]//text()').extract()[0].split('/')[0]

        base_infos_keys = response.xpath('//div[@class="base"]//li/span/text()').extract()
        base_infos = response.xpath('//div[@class="base"]//li/text()').extract()
        for key in base_infos_keys:
            try:
                item[key] = base_infos[base_infos_keys.index(key)]
            except:
                pass

        transactions_infos_keys = response.xpath('//div[@class="transaction"]//li/span[@class="label"]//text()').extract()
        transactions_infos = response.xpath('//div[@class="transaction"]//li//span[2]//text()').extract()
        for key in transactions_infos_keys:
            try:
                item[key] = transactions_infos[transactions_infos_keys.index(key)]
            except:
                pass

        yield item
        pass







