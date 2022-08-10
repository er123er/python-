import json
import pprint
import random
import subprocess
import time
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import requests
import execjs

with open('1.js', 'r', encoding='utf-8') as f:
    js = f.read()


header = {
    'Host': 'jzsc.mohurd.gov.cn',
    'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
    'timeout': '30000',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47',
}

html = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list'
for i in range(1,5):
    params = {
        'pg': i,
        'pgsz': '15',
        'total': '0'
    }
    html__ = requests.get(url=html, headers=header, params=params).text
    ctx = execjs.compile(js).call('h', html__)
    json1 = json.loads(ctx)
    pprint.pprint(json1)
    time.sleep(random.randint(3,5))