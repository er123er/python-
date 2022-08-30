import json
import re
import execjs
import requests
import parsel
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, jsonify

app = Flask(__name__)


# 解析
def get_signature():  # 解密signature参数
    with open('3.js', encoding='utf-8') as f:
        jscode = f.read()
    signature = execjs.compile(jscode).call('get_signature')
    return signature


# 返回实时数据
def get_daily():
    sig = get_signature()

    url_wz = 'https://www.toutiao.com/hot-event/hot-board/?'
    url_sp = 'https://www.toutiao.com/api/pc/list/feed'
    he = {
        'referer': 'https://www.toutiao.com/?channel=tech&wid=1661828941061',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    }
    params = {
        'origin': 'toutiao_pc',
        '_signature': sig
    }
    html_wz = requests.get(url_wz, headers=he, params=params).json()
    pa = {
        'offset': '0',
        'channel_id': '94349549395',
        'max_behot_time': '0',
        'category': 'pc_profile_channel',
        'disable_raw_data': 'true',
        'aid': '24',
        'app_name': 'toutiao_web',
        '_signature': sig
    }
    html_sp = requests.get(url_sp, headers=he, params=pa).json()
    return html_wz, html_sp


#  生成cookies
def cook():
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    headers = {
        "User-Agent": ua,
    }
    s = requests.Session()
    url = 'https://www.toutiao.com/article/7137549095924744742/'
    resp = s.get(url, headers=headers)
    # print(resp.headers['set-cookie'].split(';')[0])
    msToken = resp.headers['set-cookie'].split(';')[0]
    url = 'https://i.snssdk.com/slardar/sdk_setting?bid=toutiao_web_pc'
    resp = s.get(url, headers=headers)
    # print(resp.headers['set-cookie'].split(';')[0])
    MONITOR_WEB_ID = resp.headers['set-cookie'].split(';')[0]
    pppp = '{"aid": 24, "service": "www.toutiao.com", "region": "cn", "union": true, "needFid": false}'
    hhh = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-length': '81',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.toutiao.com',
        'referer': 'https://www.toutiao.com/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    }
    resp = s.post(url='https://ttwid.bytedance.com/ttwid/union/register/', headers=hhh, data=pppp)
    # print(resp.headers['Set-Cookie'].split(';')[0])
    ttwid = resp.headers['set-cookie'].split(';')[0]
    cookie = msToken + ';' + MONITOR_WEB_ID + ';' + ttwid
    return cookie


z_cook = cook()


# 内容
def t(url=None):
    if url is not None:
        he = {
            'cookie': z_cook,
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
        }
        kk = requests.get(url=url, headers=he).text
        html = parsel.Selector(kk)
        title = html.xpath('//*[@class="article-content"]/h1/text()').get()
        nj = html.xpath('//*[@class="article-content"]/article')
        pppp = nj.xpath('string(.)').getall()
        print(title, pppp)
    else:
        print('空')


# 列表
def l_url(url):
    #     //*[@class='feed-card-wrapper feed-card-article-wrapper']/div/div[2]/a
    he = {
        'cookie': z_cook,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    }
    try:
        kk = requests.get(url=url, headers=he).text
        html = parsel.Selector(kk)
        href = html.xpath('//*[@class="feed-card-wrapper feed-card-article-wrapper"]/div/div[2]/a/@href').get()
        return href
    except:
        return None


def o():
    wz, sp = get_daily()
    l = 0
    # print(sp)
    with ThreadPoolExecutor(10) as ff:
        for i in wz['data']:
            Title = i['Title']
            ClusterIdStr = i['ClusterIdStr']
            l = l + 1
            url = f'https://www.toutiao.com/trending/{ClusterIdStr}/?rank={l}'
            print(Title, url, l)
            x = l_url(url)
            ff.submit(t, x)


# 搜索

def ss(keyword='夏普', page_num=1):
    he = {
        'Cookie': z_cook,
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    }

    url = 'https://so.toutiao.com/search?'
    f = {
        'dvpf': 'pc',
        'source': 'pagination',
        'keyword': keyword,  # 搜索关键字
        'page_num': page_num,  # 页数
        'pd': 'synthesis',
        'action_type': 'pagination',
        'search_id': '202208301727390101501320961EE8D639',  # 时间
        'from': 'search_tab',
        'cur_tab_title': 'search_tab',
    }
    kk = requests.get(url=url, headers=he, params=f).text
    html = parsel.Selector(kk)
    tiele = html.xpath('//*[@data-test-card-id="undefined-default"]/div').getall()
    x = re.compile("<div data-log-extra='(.*?)' data-log-view-stay=")
    for i in tiele:
        dic = ''.join(x.findall(i))
        user_dict = json.loads(dic)
        # pprint.pprint(user_dict)
        print('https://www.toutiao.com/article/' + user_dict['item_id'], user_dict['query'])
        t('https://www.toutiao.com/article/' + user_dict['item_id'])



@app.route('/daily', methods=['GET'])
def get_tasks():
    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]
    return jsonify({'tasks': tasks})


def zd():
    while True:
        print('1.自动获取每天更新50条\n2.指定搜索(只限今日头条)\n3.指定链接\n0.退出')
        id = input('输入:')
        if 1 == int(id):
            o()
        elif 2 == int(id):
            while True:
                print('默认：keyword=夏普, page_num=1')
                keyword = input('搜索名称:')
                pagenum = input('页数:')
                if keyword == '' and pagenum == '':
                    ss(keyword='夏普', page_num=1)
                else:
                    try:
                        ss(keyword=keyword, page_num=int(pagenum))
                    except:
                        print('参数错误！')
        elif 3 == int(3):
            ls = input('输入连接（如：https://www.toutiao.com/article/7137549095924744742/）')

            t(url=ls)
        elif 0 == int(id):
            break
        else:
            print('错误！')


def mian():
    print('1.终端\n2.网页api(点两次即可)\n0.退出')
    id = input('输入:')
    if 1 == int(id):
        zd()
    elif 2 == int(id):
        app.run(host='0.0.0.0', port=80, debug=True)
    else:
        print('错误！')


if __name__ == '__main__':
    mian()
