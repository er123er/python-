import copy
import json
import re

import scrapy

cookies = {
    'ig_did': 'D40217CE-3A13-48C6-894B-B1CAC28571A5',
    'ig_nrcb': '1',
    'mid': 'ZIbO9gALAAH75R3ki8wX2DVrY9Rc',
    'datr': '786GZO8-mQuVCcR7mx7RhNEi',
    'csrftoken': '5waQe3lNyhJo1dxKxDFqjkS3xbuL7SSx',
    'ds_user_id': '59703935504',
    'sessionid': '59703935504%3A4UQ0Vo9HwrqvYg%3A9%3AAYfMFDfgYgVi2UVpEsISv3OlTxl6jnalcUzOuYvjbA',
    'rur': '"NCG\\05459703935504\\0541718092471:01f7aadd3e1834743e283f88719d7d2c180e97108f48cc0dc6a2b8af6a0353f8cf7cd9c0"',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'ig_did=D40217CE-3A13-48C6-894B-B1CAC28571A5; ig_nrcb=1; mid=ZIbO9gALAAH75R3ki8wX2DVrY9Rc; datr=786GZO8-mQuVCcR7mx7RhNEi; csrftoken=5waQe3lNyhJo1dxKxDFqjkS3xbuL7SSx; ds_user_id=59703935504; sessionid=59703935504%3A4UQ0Vo9HwrqvYg%3A9%3AAYfMFDfgYgVi2UVpEsISv3OlTxl6jnalcUzOuYvjbA; rur="NCG\\05459703935504\\0541718092471:01f7aadd3e1834743e283f88719d7d2c180e97108f48cc0dc6a2b8af6a0353f8cf7cd9c0"',
    'referer': 'https://www.instagram.com/you_r_love/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Microsoft Edge";v="114.0.1823.43"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
    'x-asbd-id': '129477',
    'x-csrftoken': '5waQe3lNyhJo1dxKxDFqjkS3xbuL7SSx',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3-YhZCVXTXQjAI6n7drW1hh9jqLAzIvVtDzqRquUTCFS-X',
    'x-requested-with': 'XMLHttpRequest',
}


class InsSpider(scrapy.Spider):
    name = "ins"
    allowed_domains = ["www.instagram.com"]
    start_urls = ["https://www.instagram.com/explore/"]

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        status_text = re.compile('"result":\{"response":(.*?),"status_code":200}')
        text = status_text.findall(response.text)[0]
        sectional_items = json.loads(text)
        try:
            for i in json.loads(sectional_items)['fit_sections']:
                name = i["l1"]["name"]
                if name is None:
                    continue
                subtopic = i['subtopic']
                try:
                    for x in subtopic:
                        x_name = x['name']
                        medias = x['medias']
                        if x_name is None:
                            continue
                        if not medias:
                            continue
                        # print(medias)
                        # username = [lll["user"]["username"] for lll in x['medias'][0]["usertags"]["in"]]
                        url_name = x["medias"][0]["user"]["username"]
                        url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={url_name}'
                        params = {
                            'tags_1': name,
                            'tags_2': x_name,
                        }
                        # print(url)
                        # print(params)

                        yield scrapy.Request(url=url, headers=headers, cookies=cookies, callback=self.html_about,
                                             meta=copy.deepcopy(params))
                        # print(x_name, x["medias"][0]["user"]["username"])

                        # print(username)   [0]["caption"]["user"]["username"]
                        # ["fit_sections"][0]["subtopic"][1]["medias"][0]["user"]["username"]
                        # ["fit_sections"][0]["subtopic"][1]["medias"][0]["usertags"]["in"][0]["user"]["username"]
                except:
                    # print('subtopic'
                    pass
                break
        except:
            pass
            # print('sectional_items')

    def html_about(self, response):
        print(response.url)
        print(response.headers)
        print('*' * 60)
        # print(response.text)
        # print(response.json())
        # print(response.json()["data"]["user"]["biography"])
        # print(response.json()["data"]["user"]["edge_owner_to_timeline_media"]["count"])
        # print(response.json()["data"]["user"]["edge_followed_by"]["count"])
        # print(response.json()["data"]["user"]["profile_pic_url"])
        # print(response.json()["data"]["user"]["username"])
        # print(response.json()["data"]["user"]["biography"])
        # print(response.json()["data"]["user"]["category_name"])
