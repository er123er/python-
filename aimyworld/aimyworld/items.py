# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubeDemoItem(scrapy.Item):
    video = scrapy.Field()
    platform = scrapy.Field()
    Registration_time = scrapy.Field()
    Number_of_views = scrapy.Field()
    country = scrapy.Field()
    user_text = scrapy.Field()
    user = scrapy.Field()
    banner_img = scrapy.Field()
    video_data = scrapy.Field()
    title_img = scrapy.Field()
    name = scrapy.Field()
    vermicelli = scrapy.Field()
    tage = scrapy.Field()
    download_slot = scrapy.Field()
    depth = scrapy.Field()
    download_timeout = scrapy.Field()
    proxy = scrapy.Field()
    download_latency = scrapy.Field()
    redirect_times = scrapy.Field()
