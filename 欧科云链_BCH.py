import random
import time
import base64
import requests
from prettytable import *

def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


class OuYun:

    def __init__(self, limit=20, offset=0):
        self.limit = limit  # 显示数量
        self.offset = offset # 从第一页等于0，第二页等于=100

    def u():
        def sjs(t):
            c1 = random.randint(0, 10)
            c2 = random.randint(0, 10)
            c3 = random.randint(0, 10)
            t += 1111111111111
            t = str(t)
            sj = t[0:-3] + str(c1) + str(c2) + str(c3)
            return sj

        t = int(time.time() * 1000)
        e = '-b31e-4547-9299-b6d07b7631aba2c903cc'
        c1 = random.randint(0, 10)
        c2 = random.randint(0, 10)
        c3 = random.randint(0, 10)
        t += 1111111111111
        t = str(t)
        sj = t[0:-3] + str(c1) + str(c2) + str(c3)
        sj = sjs(int(sj))
        zui1 = e + '|' + sj
        # print(sj,e)
        zui = str(base64.b64encode(zui1.encode()))
        zm = zui.replace('b', '').replace('\'', '')
        # print(zm)
        return zm

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
        'x-apiKey': u(),
        'x-cdn': 'https://static.oklink.com',
        'x-utc': '8',
    }

    # BCH 交易
    def bch_trade(self):
        params = {
            't': int(time.time() * 1000),
            'limit': self.limit,
            'offset': self.offset,
        }
        url = 'https://www.oklink.com/api/explorer/v1/bch/transactionsNoRestrict'
        html = requests.get(url, headers=OuYun.headers, params=params).json()
        # pprint.pprint(html)

        print(f'共计{html["data"]["total"]}交易')
        table = PrettyTable(['交易哈希', '	所在区块', '时间', '输入', '输出', '数量(BCH)', '手续费(BCH)'])
        for o in html['data']['hits']:
            table.add_row([o['hash'], o['blockHeight'],
                           timestamp_to_date(o['blocktime']), o['inputsCount'],
                           o['outputsCount'], str(o['realTransferValue']),
                           o['realTransferValueSat']])
        print(table)

    # BCH 大额交易
    def bch_big_trade(self):
        params = {
            't': int(time.time() * 1000),
            'limit': self.limit,  # 显示页数
            'offset': self.offset,  # 从第一页等于0，第二页等于=100
            'type': 'large',
            'upperBound': '1000'
        }
        url = 'https://www.oklink.com/api/explorer/v1/bch/transactions'
        html = requests.get(url, headers=OuYun.headers, params=params).json()
        # pprint.pprint(html)

        print(f'共计{html["data"]["total"]}交易')
        table = PrettyTable(['交易哈希', '	所在区块', '时间', '输入', '输出', '数量(BCH)', '手续费(BCH)'])
        for o in html['data']['hits']:
            table.add_row([o['hash'], o['blockHeight'],
                           timestamp_to_date(o['blocktime']), o['inputsCount'],
                           o['outputsCount'], str(o['realTransferValue']),
                           o['realTransferValueSat']])

        print(table)

    # BCH 没有交易
    def bch_no_trade(self):
        params = {
            't': int(time.time() * 1000),
            'limit': self.limit,  # 显示页数
            'offset': self.offset,  # 从第一页等于0，第二页等于=100
            'type': 'pending',
        }
        url = 'https://www.oklink.com/api/explorer/v1/bch/transactions'
        html = requests.get(url, headers=OuYun.headers, params=params).json()
        # pprint.pprint(html)

        print(f'共计{html["data"]["total"]}交易')
        table = PrettyTable(['交易哈希', '最后收录', '输入', '输出', '数量(BCH)', '手续费(BCH)'])
        for o in html['data']['hits']:
            table.add_row([o['hash'],
                           timestamp_to_date(o['blocktime']), o['inputsCount'],
                           o['outputsCount'], str(o['realTransferValue']),
                           o['realTransferValueSat']])

        print(table)


if __name__ == '__main__':
    while True:
        print('1.BCH 交易\n2.BCH 大额交易\n3.BCH 没有交易\n0.退出\n')
        k = input('请输入:')
        l = OuYun()
        if k == '1' or k == 1:
            x = input('当前默认显示20条！可以选择10，20，50，100-------y默认n自选(y/n)')
            if x =='y':
                l.bch_trade()
            elif x =='n':
                limi = input('需要显示页数:')
                nx = OuYun(limit=int(limi))
                nx.bch_trade()
            else:
                print('错误！')
        elif k == '2' or k == 2:
            x = input('当前默认显示20条！可以选择10，20，50，100-------y默认n自选(y/n):')
            if x == 'y':
                l.bch_big_trade()
            elif x == 'n':
                limi= input('需要显示页数:')
                nx = OuYun(limit=int(limi))
                nx.bch_big_trade()
            else:
                print('错误！')

        elif k == '3' or k == 3:
            x = input('当前默认显示20条！可以选择10，20，50，100-------y默认n自选(y/n)')
            if x == 'y':
                l.bch_no_trade()
            elif x == 'n':
                limi = input('需要显示页数:')
                nx = OuYun(limit=int(limi))
                nx.bch_no_trade()
            else:
                print('错误！')
        elif k == '0' and 0:
            break
        else:
            print('错误！')
