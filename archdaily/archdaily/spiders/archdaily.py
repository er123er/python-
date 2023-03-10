import scrapy
from lxml import etree
import json
import random
import time
import copy
from archdaily.items import ArchdailyItem


class ExampleSpider(scrapy.Spider):
    name = "archdaily"
    allowed_domains = ["archdaily.cn"]  # 允许域名

    def start_requests(self):
        url = 'https://www.archdaily.cn/search/api/v1/cn/projects'
        yield scrapy.Request(url, callback=self.parse_one)

    def parse_one(self, response):
        json = response.json()['results']
        for i in json[0:3]:
            # print(i['url'])
            # print(i['title'])
            title_t = i['title']
            url = i['url']
            time.sleep(random.randint(2, 3))
            yield scrapy.Request(url=url, callback=self.parse_two, meta={'title_t': title_t})

    def parse_two(self, response):
        title_t = {}
        tree = etree.HTML(response.text)
        html_div1_a = tree.xpath('//*[@id="single-content"]/div[2]/div/div[1]/a/text()')  # 主要第一部分 标识
        html_div2_div = ''.join(tree.xpath('//*[@id="single-content"]/div[2]/div/div[2]/text()'))  # 主要第一部分 地区
        html_div2_a = ''.join(tree.xpath('//*[@id="single-content"]/div[2]/div/div[2]/a/text()'))  # 主要第一部分 地区2
        html_div2_zong = html_div2_div + html_div2_a
        # print(html_div1_a,html_div2_zong)
        html_div_ul_li = tree.xpath('//*[@id="single-content"]/div[2]/ul/li')
        html1 = {}
        for html_div_li in html_div_ul_li:  # html[1]
            html_div_key = ''.join(html_div_li.xpath('.//*[@class="afd-specs__key"]/text()')).strip()
            html_div_value = ''.join(html_div_li.xpath('.//*[@class="afd-specs__value"]/a/text()')).strip()
            # print(html_div_key, html_div_value)
            html1[html_div_key] = html_div_value
        html2_div_ul = tree.xpath('//*[@id="single-content"]/div[3]/ul/li')
        html2 = {}
        for html_div_li2 in html2_div_ul:  # html[2]
            html_div2_key = ''.join(html_div_li2.xpath('.//*[@class="afd-specs__key"]/text()')).strip()
            html_div2_value = ''.join(html_div_li2.xpath('.//*[@class="afd-specs__value"]/text()')).strip()
            # print(html_div2_key, html_div2_value)
            html2[html_div2_key] = html_div2_value

        img_href = tree.xpath('//*[@id="gallery-thumbs"]/li')  # 图片
        h1_title = tree.xpath('//*[@id="content"]/div/div[2]/header[2]/h1/text()')  # 标题
        p_title = tree.xpath('//*[@id="single-content"]/p')
        # print(img_href,h1_title)
        str_text = ''  # 文本内容
        for p in p_title:
            detail = p.xpath('./text()')
            str_text += ''.join(detail)
        # print(str_text)  # 文本
        title_t['html1'] = html1
        title_t['html2'] = html2
        title_t['str_text'] = str_text
        # response.meta['title_t']
        branch = {response.meta['title_t']: title_t}
        item = ArchdailyItem()
        item['branch'] = branch
        item['title'] = response.meta['title_t']
        # print(item)
        yield item
