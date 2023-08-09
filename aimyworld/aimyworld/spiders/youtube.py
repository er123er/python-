import scrapy
import re
import json
import copy
from aimyworld.instrument import instrument
from aimyworld.items import YoutubeDemoItem


class YoutubeSpider(scrapy.Spider):
    name = "youtube"
    allowed_domains = ["youtube.com"]
    start_urls = ["https://www.youtube.com/feed/guide_builder"]

    def parse(self, response):
        re_html = re.compile('"content":(.*),"tabIdentifier":', re.S)
        o = re_html.findall(response.text)[0]
        dic_dic = json.loads(o)
        li = dic_dic['sectionListRenderer']['contents']
        for li_demo in li[1::]:
            title = li_demo['itemSectionRenderer']['contents'][0]['shelfRenderer']['title']['runs'][0]['text']
            html_li = \
            li_demo['itemSectionRenderer']['contents'][0]['shelfRenderer']['content']['horizontalListRenderer'][
                'items']
            # html_li = ['/@Brookemonk','/@SaffronBarker','/@Jazzybumblee','/@JavierLunaOfc','/@FidiasPanayiotou','/@MatthewandRyanUK',
            #            '/@sophielouisebeauty','/@UC5NT5DADrZ4LWBkr-5XVAaA','/@muchelleb','/@FarnsworthFarms','/@TravelBeans',
            #            '/@EliseBuch','/@UCVv-y0k91qAA-uI_K46UBvg','/@DemiDonnelly','/@Tulasendlesssummer','/@RobbieKnox','/@TopFlightFamily',
            #            '/@PeytonCharles','/@LinneaAkelaVanLife','/@JAMIEANDSARAH','/@UCBrvl0Mx8jmPXcr1Wz45_gQ','/@UCZYXO1yZnSAT6sK79bZV_Hg',
            #            '/@ThoseHappyDays','/@UCJJu15z_0OLSQW-oJQ8wvSA','/@GoTimeTravels']
            for i in html_li:
                url_one = i['gridChannelRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
                # url_one = i
                print(url_one)
                url_1 = 'https://www.youtube.com' + url_one + '/about'
                print(url_1)
                url_2 = 'https://www.youtube.com' + url_one + '/channels'
                params = copy.deepcopy({
                    'title': title,
                    'url_one': url_one
                })
                # li_li.append(scrapy.Request(url=url_1, callback=self.html_about, meta=copy.deepcopy(params)))
                yield scrapy.Request(url=url_1, callback=self.html_about, meta=copy.deepcopy(params))
                # yield scrapy.Request(url=url_2, callback=self.html_channels)
            break

    def html_channels(self, response):
        html_json = instrument.go_re(response=response)
        li_li = []
        try:
            for i in html_json["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][-3]["tabRenderer"]["content"][
                "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["gridRenderer"]["items"]:
                if i.get('continuationItemRenderer') is None:
                    url_one = i["gridChannelRenderer"]["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"][
                        "url"]
                    # print(
                    # i["gridChannelRenderer"]["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"],
                    # i["gridChannelRenderer"]["title"]["simpleText"])
                    params = copy.deepcopy({
                        'title': i["gridChannelRenderer"]["title"]["simpleText"],
                        'url_one': url_one
                    })
                    url = 'https://www.youtube.com' + url_one + '/about'
                    url_2 = 'https://www.youtube.com' + url_one + '/channels'
                    # yield scrapy.Request(url=url, callback=self.html_about, meta=copy.deepcopy(params))
                    li_li.append(scrapy.Request(url=url, callback=self.html_about, meta=copy.deepcopy(params)))
                    li_li.append(scrapy.Request(url=url_2, callback=self.html_channels))
            for on in li_li:
                yield on

        except KeyError as e:
            print('此人没有频道', str(e))

    def html_about(self, response):
        html_json = instrument.go_re(response=response)
        dic_json = instrument.go(html_json)
        dic_json['tage'] = response.meta['title']
        params = copy.deepcopy(dic_json)
        url = 'https://www.youtube.com' + response.meta['url_one'] + '/videos'
        yield scrapy.Request(url=url, callback=self.html_videos, meta=copy.deepcopy(params))

    def html_videos(self, response):
        html_json = instrument.go_re(response=response)
        dic_json = instrument.go_html_two(html_json=html_json)
        dic_json.update(response.meta)
        item = YoutubeDemoItem()
        itme = copy.deepcopy(item.update(dic_json))
        yield itme
