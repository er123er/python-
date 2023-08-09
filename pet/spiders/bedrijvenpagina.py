import json

import scrapy
from scrapy import Selector
from urllib.parse import urljoin
from pet.items import PetItem


class BedrijvenpaginaSpider(scrapy.Spider):
    name = "bedrijvenpagina"
    allowed_domains = ["bedrijvenpagina.nl"]

    # start_urls = ["https://bedrijvenpagina.nl"]
    url_one = 'https://bedrijvenpagina.nl'

    def start_requests(self):
        for i in range(1077):
            url_demo = f'https://www.bedrijvenpagina.nl/zoek/pet/?p={i}'
            # ?p = 2
            yield scrapy.Request(url=url_demo, callback=self.pet_one)

    def pet_one(self, response):
        selector = Selector(text=response.body)

        s = [selector_data.extract() for selector_data in selector.xpath('//*[@class="fn org"]/a/@href')]
        for i in s:
            url = urljoin(self.url_one, i)
            yield scrapy.Request(url=url, callback=self.pet_two)

    def pet_two(self, response):
        typename = {
            "URLContact": '',
            "EmailContact": None,
            "PhoneContact": '',
        }
        selector = Selector(text=response.body)
        title = ''.join(selector.xpath('//*[@class = "box-title"]//text()').extract())
        streetLine = [selector_data.extract() for selector_data in selector.xpath('//*[@class ="adr"] // text()')]
        streetLine = ''.join(''.join(streetLine).strip().split())  # 位置

        EmailContact = [selector_data.extract() for selector_data in selector.xpath('//*[@class ="mail"] // text()')]
        PhoneContact = [selector_data.extract() for selector_data in
                        selector.xpath('//*[@class ="tel phone"] // text()')]
        URLContact = [selector_data.extract() for selector_data in selector.xpath('//*[@class ="url"] // text()')]
        postcode = [selector_data.extract() for selector_data in selector.xpath('//*[@class ="kvk"]/div[1]/a/text()')]
        typename.update({'EmailContact': EmailContact})
        typename.update({'PhoneContact': PhoneContact})
        typename.update({'URLContact': URLContact})
        # print(typename)

        item = PetItem()
        json_dic = {
            'title': title,
            'url_id': None,
            'postcode': json.dumps(postcode),
            'city': '荷兰',
            'streetLine': streetLine,
            'source': None,
            'coordinates': None,
            'en_neme': 'pet',
            'typename': json.dumps(typename),
            'platform': 'https://bedrijvenpagina.nl',
            'url': response.url,
        }
        item.update(json_dic)
        yield item
        # //*[@class ="adr"] // text()   位置
        # //*[@class ="mail"] // text()   邮件
        # //*[@class ="tel mobile"] // text()   电话
        # //*[@class ="url"] // text()   url
        # //*[@class ="kvk"]/div[1]/a/text()   postcode
