import time
import requests
import parsel
import csv
import os
from concurrent.futures import ThreadPoolExecutor
from User_Agent import User_Agent

html_yeshu = []


def tidy(ok):
	return ok.strip('笔趣阁 www.bqg.org，最快更新').replace('    ', '')


def wanglo():
	if not os.path.isdir('笔趣阁'):
		os.makedirs('笔趣阁')
	url = 'https://www.bqg.org/top/allvisit/'
	headers = {
		'User-Agent': User_Agent()
	}
	wanglo_1 = requests.get(url=url, headers=headers)
	puanduan = wanglo_1.status_code
	if puanduan == 200:
		print('网址连接正常！')
	else:
		print('网址连接失败！请检查网络！')


def shouye():
	url = 'https://www.bqg.org/top/allvisit/'
	headers = {
		'User-Agent': User_Agent()
	}
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	html = parsel.Selector(html.text)
	html_yeshu_ = html.xpath('/html/body/div[2]/div[2]/div[1]/div/div/a[14]/text()').get()
	html_yeshu.append(html_yeshu_)


def html_zonglei():
	path = '笔趣阁\\' + '笔趣阁.csv'
	f = open(path, 'a', encoding='utf-8', newline='')
	ff = csv.writer(f)
	for iiii in range(1, int(html_yeshu[0])):
		url = f'https://www.bqg.org/top/allvisit/{iiii}.html'
		print(f'正在获取第{iiii}页')
		headers = {
			'User-Agent': User_Agent()
		}
		html = requests.get(url=url, headers=headers)
		html.encoding = html.apparent_encoding
		html = parsel.Selector(html.text)
		html_url = html.xpath('//*[@id="main"]/div[1]/li/span[2]/a/@href').getall()
		html_title = html.xpath('//*[@id="main"]/div[1]/li/span[2]/a/text()').getall()
		# for i, l in zip(html_title, html_url):
		for l in html_url:
			html__url(l)
			print(l)
			break
		# ff.writerow([i, l])
		print(f'获取第{iiii}页成功！')


def html__url(url):
	urll = url
	headers = {
		'User-Agent': User_Agent()
	}
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	html = parsel.Selector(html.text)
	html_url = html.xpath('//*[@id="list"]/dl/dd').getall()
	for i in html_url[12:]:
		ii = parsel.Selector(text=i)
		html_href = ii.css('a::attr(href)').get()
		# print(type(html_href))
		# print(type(urll))
		# print(urll + html_href)
		# print(type(urll + html_href))
		try:
			with ThreadPoolExecutor(3) as t:
				t.submit(html__nei, urll + html_href)
		except:
			pass


def html__nei(url):
	headers = {
		'User-Agent': User_Agent()
	}
	html = requests.get(url=url, headers=headers)
	html.encoding = html.apparent_encoding
	# print(html.text)
	html = parsel.Selector(html.text)
	html_text = html.xpath('//*[@id="content"]/text()').getall()
	html_titel = html.xpath('/html/body/div[1]/div[2]/div/div[2]/h1/text()').get()
	html_title = html.xpath('//*[@id="box_con"]/div[1]/a[2]/text()').get()
	print(f'正在下载:{html_title, html_titel}')
	path = '笔趣阁//' + html_title
	if not os.path.isdir(path):
		os.makedirs(path)
	ok = ''
	for i in html_text:
		ok += i
	with open('笔趣阁//' + html_title + '//' + html_titel + '.txt', 'w', encoding='utf-8') as f:
		f.write(tidy(ok))



def main__bqg():
	wanglo()
	print('笔趣阁开始采集>>>>')
	time_kai = time.time()
	shouye()
	html_zonglei()
	time_jie = time.time()
	print('笔趣阁采集结束>>>>')
	print(f'笔趣阁总共:{time_jie - time_kai:.3f}')
	
	
if __name__ == '__main__':
	main__bqg()