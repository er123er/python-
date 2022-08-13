import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
import requests
import time




with open('kugou.js', 'r', encoding='utf-8') as f:
    js = f.read()

mz = input('名字:')

ti = int(time.time()*1000)
text = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtcallback=callback123clienttime={str(ti)}clientver=2000dfid=-iscorrection=1keyword={mz}mid={str(ti)}page=1pagesize=30platform=WebFilterprivilege_filter=0srcappid=2919userid=0uuid={str(ti)}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'

ctx = execjs.compile(js).call('faultylabs.MD5', text)

params = {
    'callback':'callback123',
    'keyword':mz,
    'page':'1', # 页数
    'pagesize':'30', # 显示数量
    'userid':'0',
    'clientver':'2000',
    'platform':'WebFilter',
    'iscorrection':'1',
    'privilege_filter':'0',
    'srcappid':'2919',
    'clienttime':ti,
    'mid':ti,
    'uuid':ti,
    'dfid':'-',
    'signature':ctx,
}
url = 'https://complexsearch.kugou.com/v1/search/mv'


he = {
    'Referer':'https://www.kugou.com/',
    'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Dest':'script',
    'Sec-Fetch-Mode':'no-cors',
    'Sec-Fetch-Site':'same-site',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
}
html = requests.get(url, headers=he, params=params)
print(html.text)
