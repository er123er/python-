import copy
from pet.instrument.local_instrument import html_dict, html_re
import scrapy
from urllib.parse import urlencode
from pet.items import PetItem


class LocalSpider(scrapy.Spider):
    name = "local"
    allowed_domains = ["local.ch"]
    start_urls = ["https://www.local.ch/de/s/*/pet?rid=ca4a68"]

    def parse(self, response):
        html = html_re(text=response.text)
        if html is not None:
            url_demo = f'https://www.local.ch/_next/data/{html}/en/s/*/pet.json'
            for i in range(1, 56):
                params = {
                    "rid": "add134",
                    "search": "s",
                    "page": i,
                    "searchQuery": "pet"
                }
                url = url_demo + "?" + urlencode(params)
                yield scrapy.Request(url=url, callback=self.pet_one)
        else:
            pass

    def pet_one(self, response):
        html_list = html_dict(response=response)
        item = PetItem()
        for dic in html_list:
            json_dic = {
                'title': dic['title'],
                'url_id': dic['url_id'],
                'postcode': dic['postcode'],
                'city': dic['city'],
                'streetLine': dic['streetLine'],
                'source': dic['source'],
                'coordinates': dic['coordinates'],
                'en_neme': dic['en_neme'],
                'typename': dic['typename'],
                'platform': dic['platform'],
                'url': dic['url'],
            }
            item.update(json_dic)
            yield item
