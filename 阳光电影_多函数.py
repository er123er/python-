import time
import requests
import re
import csv
import threading

zhuyu = 'https://www.ygdy8.com'
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}


def duoxiancheng(lj):
	dx = []
	for hj in lj:
		zong = zhuyu + hj
		t1 = threading.Thread(target=xiazai, args=(zong,))
		t1.start()
		dx.append(t1)
	for xh in dx:
		xh.join()


def xiazai(url):
	html_xiazia = requests.get(url=url, headers=headers)
	html_xiazia.encoding = html_xiazia.apparent_encoding
	tiqu_url = re.compile(r'<a target="_blank" href="(.*?)"><strong>', re.S)
	tiqu_pm = re.compile(r'<div class="title_all"><h1>.*?《(.*?)》.*?</h1></div>', re.S)
	tiqu_url = tiqu_url.findall(html_xiazia.text)
	tiqu_pm = tiqu_pm.findall(html_xiazia.text)
	
	with open('磁力链接.csv', 'a', encoding='utf-8', newline='') as ff:
		f = csv.writer(ff)
		dit = [tiqu_pm,tiqu_url]
		f.writerow(dit)

def new_movies():
	url = 'https://www.ygdy8.com/html/gndy/dyzz/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/gndy/dyzz/list_23_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('最新影片.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def domestic_movies():
	url = 'https://www.ygdy8.com/html/gndy/china/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/gndy/china/list_4_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('国内影片.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
		
	
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def oumei():
	url = 'https://www.ygdy8.com/html/gndy/oumei/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/gndy/oumei/list_7_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('欧美影片.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
		
	
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def Chinese_TV_series():
	url = 'https://www.ygdy8.com/html/tv/hytv/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/tv/hytv/list_71_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('华语电视.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
		
	
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def rihantv():
	url = 'https://www.ygdy8.com/html/tv/rihantv/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/tv/rihantv/list_8_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('日韩电视.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
	
	
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def oumeitv():
	url = 'https://www.ygdy8.com/html/tv/oumeitv/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/tv/oumeitv/list_9_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('欧美电视.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
	
	
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def zongyi2013():
	url = 'https://www.ygdy8.com/html/zongyi2013/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/zongyi2013/list_99_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('最新综艺.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
		
	
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def zongyi2009():
	url = 'https://www.ygdy8.com/html/2009zongyi/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/2009zongyi/list_89_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('旧版综艺.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
		
	
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def dongman():
	url = 'https://www.ygdy8.com/html/dongman/index.html'
	
	kaishi = time.time()
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	obj = re.compile(r'<td height="25" align="center" bgcolor="#F4FAE2"> 共(.*?)页.*?记录', re.S)
	yeshu = obj.findall(html.text)
	yeshu = yeshu[0]
	for i in range(1, int(yeshu) + 1):
		print(f'正在下载第{i}页,资源信息')
		urll = f'https://www.ygdy8.com/html/dongman/list_16_{i}.html'
		urll = requests.get(url=urll, headers=headers)
		urll.encoding = urll.apparent_encoding
		obj1 = re.compile('<a href=".*?" class="ulink">(.*?)</a>', re.S)
		obj2 = re.compile('<td style="padding-left:3px">.*?日期：(.*?)点击.*?</td>', re.S)
		obj3 = re.compile('<td height="26">.*?href="(.*?)" class="ulink">.*?</b>', re.S)
		obj4 = re.compile('<td colspan="2" style="padding-left:3px">(.*?)</td>', re.S)
		zm = obj1.findall(urll.text)
		ri = obj2.findall(urll.text)
		lj = obj3.findall(urll.text)
		jj = obj4.findall(urll.text)
		duoxiancheng(lj)
		ff = open('动漫资源.csv', 'a+', encoding='utf-8', newline='')
		f = csv.DictWriter(ff, fieldnames={
			'电影名称',
			'电影时间',
			'URL',
			'介绍',
		})
		f.writeheader()
		for zm, ri, lj, jj in zip(zm, ri, lj, jj):
			dit = {
				'电影名称': zm,
				'电影时间': ri,
				'URL': zhuyu + lj,
				'介绍': jj,
			}
			f.writerow(dit)
			xiazai(zhuyu + lj)
		time.sleep(1)
		
	
	jiesu = time.time()
	sj = jiesu - kaishi
	print(f'共用时间:{sj:.3f}秒')


def main():
	while True:
		print('', '指令'.center(20, '*'), '')
		print('|', '1.最新影片'.center(20), '|')
		print('|', '2.动漫资源'.center(20), '|')
		print('|', '3.国内影片'.center(20), '|')
		print('|', '4.欧美影片'.center(20), '|')
		print('|', '5.华语电视'.center(20), '|')
		print('|', '6.日韩电视'.center(20), '|')
		print('|', '7.欧美电视'.center(20), '|')
		print('|', '8.最新综艺'.center(20), '|')
		print('|', '9.旧版综艺'.center(20), '|')
		print('|', '0.结束运行'.center(20), '|')
		print('', '*'.center(20, '*'), '')
		zl = input('指令序号：')
		if zl == '1':
			new_movies()
		elif zl == '2':
			dongman()
		elif zl == '3':
			domestic_movies()
		elif zl == '4':
			oumei()
		elif zl == '5':
			Chinese_TV_series()
		elif zl == '6':
			rihantv()
		elif zl == '7':
			oumeitv()
		elif zl == '8':
			zongyi2013()
		elif zl == '9':
			zongyi2009()
		elif zl == '0':
			break
		else:
			print('错误！')


main()
