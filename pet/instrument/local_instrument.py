import json
import re


def html_re(text):
    html_re = re.compile('"buildId":"(.*?)","assetPrefix":', re.S)
    s = html_re.findall(text)
    if len(s) >= 1:
        return s[0]
    else:
        return None


def html_dict(response):
    list_dict = []
    html_json = response.json()["pageProps"]["data"]["search"]["entries"]
    for html in html_json:
        try:
            url_id = html.get('entry').get('id')  # id
            try:
                title = html.get('entry').get('title')  # 标题
            except:
                title = None
            try:
                postcode = html.get('entry').get('address').get('zipCode')  # 邮政编码
            except:
                postcode = None
            try:
                city = html.get('entry').get('address').get('city')  # 国家
            except:
                city = None
            try:
                streetLine = html.get('entry').get('address').get('streetLine')  # 地址
            except:
                streetLine = None
            try:
                source = html.get('entry').get('thumbnail').get('source')  # 头像地址
            except:
                source = None
            try:
                coordinates = html.get('entry').get('location').get('coordinates')  # 经纬度
            except:
                coordinates = {"latitude": '', "longitude": '', "__typename": "Coordinates"}
            # https://www.local.ch/en/d/sumiswald/3600/carpenter/a-schoeni-schrinerei-_FFDCcB6FkbRdhptuTQNBA

            en_neme = []  # 类别
            for i in html["entry"]["categories"]["all"]:
                en_neme.append(i.get('name').get('en'))
            typename = {}  # 联系方式
            for k in html["entry"]["contacts"]:
                __typename = k.get('__typename')
                if __typename == 'PhoneContact':
                    typename['PhoneContact'] = k.get('value')
                elif __typename == 'EmailContact':
                    typename['EmailContact'] = k.get('value')
                elif __typename == 'URLContact':
                    typename['URLContact'] = k.get('value')
            url_demo = f'https://www.local.ch/en/d/sumiswald/{postcode}/carpenter/a-schoeni-schrinerei-_{url_id}'
            json_dic = {
                'title': title,
                'url_id': url_id,
                'postcode': postcode,
                'city': city,
                'streetLine': streetLine,
                'source': source,
                'coordinates': json.dumps(coordinates),
                'en_neme': json.dumps(en_neme),
                'typename': json.dumps(typename),
                'platform': 'www.local.ch',
                'url': url_demo,
            }
            list_dict.append(json_dic)
        # [0]["entry"]["title"] 标题
        # [0]["entry"]["address"]["zipCode"]  邮政编码
        # [0]["entry"]["address"]["city"] 国家
        # [0]["entry"]["address"]["streetLine"] 地址
        # [0]["entry"]["thumbnail"]["source"] 头像地址
        # [0]["entry"]["location"]["coordinates"] 经纬度
        # [0]["entry"]["categories"]["all"][0]["name"]["en"] 类别
        # [0]["entry"]["contacts"] 邮箱 电话 网页  __typename：PhoneContact  ？ EmailContact ？ URLContact
        except:
            uuid = html.get('entry').get('id')  # id
            postcode = html.get('entry').get('address').get('zipCode')  # 邮政编码
            url_demo = f'https://www.local.ch/en/d/sumiswald/{postcode}/carpenter/a-schoeni-schrinerei-_{uuid}'
            pass
    return list_dict
