# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PetItem(scrapy.Item):
    # 商家名称
    title = scrapy.Field()
    # 商家唯一标识符
    url_id = scrapy.Field()
    # 邮政编码
    postcode = scrapy.Field()
    # 城市名称
    city = scrapy.Field()
    # 商家地址
    streetLine = scrapy.Field()
    # 商家信息来源
    source = scrapy.Field()
    # 商家地理坐标
    coordinates = scrapy.Field()
    # 商家英文名称
    en_neme = scrapy.Field()
    # 商家类型名称
    typename = scrapy.Field()
    # 商家所在平台
    platform = scrapy.Field()
    # 商家网址
    url = scrapy.Field()
