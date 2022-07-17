import time
import requests
import parsel
import csv
import os
from concurrent.futures import ThreadPoolExecutor
from User_Agent import User_Agent

url_ = 'https://quanxiaoshuo.com'
headers = {
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'User-Agent': User_Agent()
}

requests.packages.urllib3.disable_warnings()  # 跳过认证

html_zhu = {}

html_url_li = []

def wanglo():
	wanglo_1 = requests.get(url=url, headers=headers)
	puanduan = wanglo_1.status_code
	if puanduan == 200:
		print('网址连接正常！')
	else:
		print('网址连接失败！请检查网络！')

def shouye():
	url = 'https://quanxiaoshuo.com'
	html = requests.get(url=url, headers=headers, verify=False)
	# print(html.text)
	html = parsel.Selector(html.text)
	html_li = html.xpath('/html/body/div[1]/div[1]/div[2]/ul/li/a').getall()
	for ii in html_li[1::]:
		i = parsel.Selector(text=ii)
		html_url = i.css('a::attr(href)').get()
		html_title = i.css('a::text').get()
		html_zhu[html_title] = 'https:' + html_url


def html_li(url):
	url__ = 'https://quanxiaoshuo.com'
	html = requests.get(url=url, headers=headers, verify=False)
	html = parsel.Selector(html.text)
	html_li = html.xpath('/html/body/div[3]/ul').getall()
	if not os.path.isdir('5200'):
		os.makedirs('5200')
	ff = open('5200//5200.csv', 'a', encoding='utf-8', newline='')
	f = csv.writer(ff)
	for ii in html_li[1::]:
		i = parsel.Selector(text=ii)
		html_url = i.css('li.cc2 > a::attr(href)').get()
		html_url_li.append(html_url)
		html_title = i.css('li.cc2 > a::text').get()
		html_zz = i.css('li.cc4 > a::text').get()
		#print(html_title, html_zz, url__ + html_url)
		f.writerows([[html_title, html_zz, url__ + html_url]])
		html_nei(url__ + html_url)

def html_nei(url):
	html = requests.get(url=url, headers=headers, verify=False)
	html = parsel.Selector(html.text)
	html_div = html.xpath('/html/body/div[9]/div').getall()
	html_tt = html.xpath('/html/body/div[2]/h1/a[1]/text()').get()
	print(f'开始：{html_tt}')
	if not os.path.isdir('5200//' + html_tt):
		os.makedirs('5200//' + html_tt)
	url__html = []
	for ii in html_div:
		i = parsel.Selector(text=ii)
		html_url = i.css('a::attr(href)').get()
		html_url = str(html_url)
		html_title = i.css('a::text').get()
		# html_title = ''.join(html_title).replace(' ', '_')
		# print(html_title)
		nj = url_ + html_url
		url__html.append(nj)
	# time.sleep(1)
	# nei_5200(nj)
	# print(nj)
	
	with ThreadPoolExecutor(2) as t:
		# t.map(nei_5200, url__html)
		for kl in url__html:
			time.sleep(1)
			t.submit(nei_5200, kl)


def nei_5200(urll):
	headers = {
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'User-Agent': User_Agent()
	}
	html = requests.get(url=urll, headers=headers, verify=False)
	html = parsel.Selector(html.text)
	html_title1 = html.xpath('/html/body/div[3]/h1/text()').get()
	html_title1 = str(html_title1)
	html_text = html.xpath('//*[@id="content"]/text()').getall()
	html_tt = html.xpath('//*[@id="home"]/text()').get()
	html_tt = str(html_tt)
	path = '5200//' + html_tt + '//' + html_title1 + '.txt'
	text_ = ''
	for kk in html_text:
		text_ += kk
	with open(path, 'a', encoding='utf-8') as f:
		f.write(text_.strip())


def mian_5200():
	print('5200开始采集>>>>')
	time_kai = time.time()
	shouye()
	try:
		for i_1 in html_zhu.values():
			html_li(i_1)
		
		
	except:
		print('错误！')
	
		
	time_jie = time.time()
	print('5200采集结束>>>>')
	print(f'5200总共:{time_jie - time_kai:.3f}')


if __name__ == '__main__':
	mian_5200()
