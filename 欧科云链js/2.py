
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen,encoding = 'utf-8')
import requests

from prettytable import *
import time
import execjs

def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


with open('1.js','r',encoding='utf-8') as f:
    js = f.read()

ctx = execjs.compile(js).call('getApiKey')


url = 'https://www.oklink.com/api/explorer/v1/bch/transactionsNoRestrict'
headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN',
    'App-Type': 'web',
    'Connection': 'keep-alive',
    'devId': '11f59f7a-69de-47ef-98bb-d654c3ddb9b0',
    'Host': 'www.oklink.com',
    'Referer': 'https://www.oklink.com/zh-cn/bch/tx-list?limit=20&pageNum=4',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47',
    'x-apiKey': ctx,
    'x-cdn': 'https://static.oklink.com',
    'x-utc': '8',
}
params = {
    't': int(time.time()*1000),
    'limit': '20',
    'offset': '0',
}
html = requests.get(url, headers=headers,params=params).json()
table = PrettyTable(['交易哈希','	所在区块','时间','输入','输出','数量(BCH)','手续费(BCH)'])
print(f'共计{html["data"]["total"]}交易')
for o in html['data']['hits']:
    table.add_row([o['hash'], o['blockHeight'],
                   timestamp_to_date(o['blocktime']), o['inputsCount'],
                   o['outputsCount'], str(o['realTransferValue']),
                   o['realTransferValueSat']])
table.set_style(RANDOM)
print(table)