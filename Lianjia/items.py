# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    链接 = scrapy.Field()
    小区名称 = scrapy.Field()
    所在区域 = scrapy.Field()
    地铁站 = scrapy.Field()
    总价 = scrapy.Field()
    单价 = scrapy.Field()
    建筑时间 = scrapy.Field()
    # base info
    房屋户型 = scrapy.Field()
    所在楼层 = scrapy.Field()
    建筑面积 = scrapy.Field()
    户型结构 = scrapy.Field()
    套内面积 = scrapy.Field()
    建筑类型 = scrapy.Field()
    房屋朝向 = scrapy.Field()
    建筑结构 = scrapy.Field()
    装修情况 = scrapy.Field()
    梯户比例 = scrapy.Field()
    配备电梯 = scrapy.Field()
    产权年限 = scrapy.Field()
    # trade info
    挂牌时间 = scrapy.Field()
    交易权属 = scrapy.Field()
    上次交易 = scrapy.Field()
    房屋用途 = scrapy.Field()
    房屋年限 = scrapy.Field()
    产权所属 = scrapy.Field()
    抵押信息 = scrapy.Field()

    pass
