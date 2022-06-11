import time
import ddddocr
import requests
import random
import linecache
import pprint
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
}
ocr = ddddocr.DdddOcr()


def sj(n=6):
    return ''.join(random.sample('qweasdzxcrtyfghvcb', n))


def sjsz(o=11):
    return linecache.getline('1.js', o)


f = open('注册信息.csv', 'a+', encoding='utf-8', newline='')
csv_we = csv.DictWriter(f, fieldnames=[
    '注册信息',
    'kk账号',
    'uid账号',
    '账号',
    '密码',

])
csv_we.writeheader()

for i in range(130, 150):  # 这是设置多少个身份证 具体了解看range用法，130行到150行 1.JS放置身份证号码
    urll = 'http://zc.7k7k.com/authcode?width=100&height=42&k=reg&t='
    shijian_ = str(int(time.time() * 1000))
    urll = urll + shijian_
    print(urll)
    html = requests.get(urll, headers)
    html_cookies = html.cookies
    with open('o.jpg', 'wb') as g:
        g.write(html.content)
    with open('o.jpg', 'rb') as f:
        image_bytes = f.read()
    res = ocr.classification(image_bytes).upper()
    print(res)
    try:
        mz = sjsz(i)[0:3].replace('-', '')
        zj = sjsz(i)[-19:-1]

        data = {
            'authcode': res,
            'identity': sj(),
            'realname': mz,
            'card': zj,
            'mode': 'identity',
            'codekey': 'reg',
            'password': '123456',
            'reg_type': 'web7k'
        }
        print(sj())
        html_url = 'http://zc.7k7k.com/post_reg'
        op = requests.post(url=html_url, headers=headers, data=data, cookies=html_cookies).json()
        pprint.pprint(op)

        dit = {
            '注册信息': op['data'],
            'kk账号': op['user']['kk'],
            'uid账号': op['user']['uid'],
            '账号': op['user']['username'],
            '密码': '123456',
        }

        csv_we.writerow(dit)
    except:
        print('验证错误！')
