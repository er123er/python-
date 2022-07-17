import time

import requests
import User_Agent
from concurrent.futures import ThreadPoolExecutor


def x(i):
	header = {
		'Connection': 'keep-alive',
		'Host': 's2.monidai.com',
		'Origin': 'https://www.xumin.cc',
		'Referer': ' https://www.xumin.cc/',
		'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
		'sec-ch-ua-mobile': '?0',
		'Sec-Fetch-Dest': 'empty',
		'User-Agent': User_Agent.User_Agent()
		
	}
	url = f'https://s2.monidai.com/20220709/0q18vBCg/1000kb/hls/MEwmrR7l3277{str(i).zfill(3)}.ts'
	# https://s2.monidai.com/20220709/0q18vBCg/1000kb/hls/MEwmrR7l3277931.ts
	# https://s2.monidai.com/20220709/0q18vBCg/1000kb/hls/MEwmrR7l3277001.ts
	s = requests.get(url=url)
	s.raise_for_status()
	print(i, s.status_code)
	path = url[-6:-3]
	# print(url)
	# print(path)
	with open('Spide/' + path + '.mp4', 'wb') as f:
		f.write(s.content)
	print('成功:', path)


def oo(k):
	time.sleep(1)
	print('d', k)


if __name__ == '__main__':
	# 932
	with ThreadPoolExecutor(100) as t:
		for p in range(1, 932):
			t.submit(x, p)
