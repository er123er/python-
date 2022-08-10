import random
import re
import time
import csv
import requests
from prettytable import PrettyTable
header = {
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47',
}
html = 'https://www.taoguba.com.cn/bbs/'

table = PrettyTable(['标题', 'url'])
f = open('path.csv', 'w', encoding='utf-8', newline='')
ff = csv.writer(f)
ff.writerow(['标题', 'url'])
u = 'https://www.taoguba.com.cn'
html__ = requests.get(url=html, headers=header)
r = re.compile(
    '<div class=".*?" style="background:#f0f0f0">[\s\S]*?.*?<a href="(.*?)" .*?[\s\S]target="_blank">[\s\S].*?(.*?)[\s\S]</a>',
    re.S)
ys = re.compile('<span>共<b style="color:#ff0000;">[\s\S].*?[\s\S]</b>/(.*?)页</span></div>')
y = ys.search(html__.text).group(1)
for x in range(int(y)):
    for i in r.findall(html__.text):
        ff.writerows([[i[1].strip(), u + i[0]]])
        table.add_row([i[0], i[1].strip()])
    print(f'第{x+1}页')
    print(table)
    time.sleep(random.randint(2, 6))
