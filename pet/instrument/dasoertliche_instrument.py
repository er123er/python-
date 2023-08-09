import ast
import json
import re

import pymysql
from pet.settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

conn = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, port=MYSQL_PORT, db=MYSQL_DATABASE)
cur = conn.cursor()


def html_one(itemData):
    """
    传入清洗过的列表，返回列表
    :param itemData:
    :return: list
    """
    list_li = []
    for i in itemData:
        dic = {
            'email': None,  # 7
            'telephone_1': None,  # 1
            'telephone_2': None,  # 10
            'name': None,  # 15
            'url_1': None,  # 3
            'url_2': None,  # 17
            'postalCode': None,  # 2
        }
        for x, l in enumerate(i):
            if x == 7 or x == 10 or x == 1 or x == 15 or x == 17 or x == 3 or x == 2:
                # print(x, l)
                pass
            if x == 7:
                dic.update({'email': l})
            if x == 1:
                dic.update({'telephone_1': l})
                # print(l)
            if x == 10:
                # print(l)
                dic.update({'telephone_2': l})
            if x == 15:
                # print(x,l)
                dic.update({'name': l})
            if x == 3:
                dic.update({'url_1': l})
            if x == 17:
                dic.update({'url_2': l})
            if x == 2:
                dic.update({'postalCode': l})
            # 1   10  手机    15 name      17 3 url        2邮编
        # print(dic)
        list_li.append(dic)
    return list_li


def json_list(dic_kn,list_li):
    # op = html_one(list_li)
    # html_two(list_li)
    """
    传入html_one清洗过的，自动匹配数据库中的字段返回itme列表
    :param list_li:
    :return: list
    """
    list_l = []
    # sql = 'SELECT * FROM `web`.`schema`;'
    # cur.execute(sql)
    for i in dic_kn:
    # for i in cur.fetchall():
        for x in list_li:
            if i['name'] == x['name']:
                # print(i)
                # print(x)
                json_dic = {
                    'title': x['name'],
                    'url_id': None,
                    'postcode': x['postalCode'],
                    'city': json.loads(i['address']).get('addressLocality'),
                    'streetLine': json.loads(i['address']).get('streetAddress'),
                    'source': None,
                    'coordinates': json.dumps(i['geo']),
                    'en_neme': 'pet',
                    'typename': json.dumps({
                        'telephone_1': x['telephone_1'],
                        'telephone_2': x['telephone_2'],
                        'url_1': x['telephone_2'],
                        'url_2': x['telephone_2'],
                    }),
                    'platform': 'www.dasoertliche.de',
                    'url': i['url'],
                }
                # print(json_dic)
                list_l.append(json_dic)
                break
    # unique_list = list(set(list_l))
    return list_l


def html_two(kk):
    """
    html初步解析的数据，洗过传入sql里面等待json_list使用
    :param kk:
    :return:
    """
    ml = []
    # sql = "INSERT INTO `web`.`schema` (`name`, `url`, `address`, `geo`, `telephone`) VALUES (%s, %s, %s, %s, %s)"
    for itme in kk['@graph']:
        values = {
            'name': None,
            'url': None,
            'address': None,
            'geo': None,
            'telephone': None,

        }
        for k, v in itme.items():
            if k == 'name':
                # print(k, v)
                values.update({'name': v})
            if k == 'url':
                # print(k, v)
                values.update({'url': v})
            if k == 'address':  # 地址
                # print(k, v)
                values.update({'address': json.dumps(v)})
            if k == 'geo':  # 经纬度
                # print(k, v)
                values.update({'geo': json.dumps(v)})
            if k == 'telephone':  # 手机
                # print(k, v)
                values.update({'telephone': json.dumps(v)})
            ml.append(values)
    return ml
        # values = (values['name'], values['url'], values['address'], values['geo'], values['telephone'])
        # cur.execute(sql, values)
        # conn.commit()


def one_html(text):
    """
    传入response.text 做数据清洗
    :param text:
    :return: json
    """
    mk = re.compile('var itemData = \[\[(.*?)\]\];', re.S)
    # print(mk.findall(response.text)[0])
    # print(response.text)
    s = '[[' + mk.findall(text)[0] + ']]'
    # print(type(json.loads(json.dumps(s))))
    li = ast.literal_eval(s)
    return li


def two_html(text):
    """
    传入response.text 做数据清洗
    :param text:
    :return: 字典
    """
    pattern = r'<script type="application/ld\+json">([\s\S]*?)</script>'
    match = re.search(pattern, text)
    if match:
        json_data = match.group(1)
        return json.loads(json_data.strip())
    else:
        return None
