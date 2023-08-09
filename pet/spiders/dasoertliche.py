import json
from urllib.parse import urlencode

from pet.instrument.dasoertliche_instrument import one_html, two_html, json_list, html_one, html_two
from pet.items import PetItem
import scrapy


class DasoertlicheSpider(scrapy.Spider):
    name = "dasoertliche"
    allowed_domains = ["dasoertliche.de"]

    # start_urls = ["https://dasoertliche.de"]

    def start_requests(self):
        url_demo = 'https://www.dasoertliche.de/'
        # for i in range(1, 26, 25):
        for i in range(1, 226, 25):
            params = {
                'zvo_ok': '',
                'plz': '',
                'quarter': '',
                'district': '',
                'ciid': '',
                'kw': 'Haustier',
                'ci': '',
                'kgs': '',
                'buab': '',
                'zbuab': '',
                'form_name': 'search_nat',
                'recFrom': i,
            }
            url = url_demo + "?" + urlencode(params)
            yield scrapy.Request(url=url, callback=self.pet_one)

    def pet_one(self, response):
        li = one_html(text=response.text)  # 第一级的列表
        dic = two_html(text=response.text)  # 第一级的字典
        ok = html_one(itemData=li)  # 第二级的列表
        ko = html_two(kk=dic)  # 第二级的字典
        html_list = json_list(dic_kn=ko, list_li=ok)
        item = PetItem()
        for dic in html_list:
            item.update(dic)
            yield item
