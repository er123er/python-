import requests
import parsel
from parsel import Selector
import csv
import threading
import time

q_url = 'https://www.pearvideo.com/'
zong_dit = {}


def download(url):
	url = url
	j = url.split("_")[1]
	url2 = f'https://www.pearvideo.com/videoStatus.jsp?contId={j}&mrd=0.5354881134233345'
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
		'Host': 'www.pearvideo.com',
		'Referer': url
	}
	request = requests.get(url=url2, headers=headers)
	dit = request.json()
	dit1 = dit['videoInfo']['videos']['srcUrl']
	dit2 = dit['systemTime']
	lj = dit1.replace(dit2, 'cont-' + j)
	viod_ID = j + '.mp4'
	with open(viod_ID, 'wb', ) as f:
		f.write(requests.get(lj).content)


def pai_hang(url):
	url = url
	html = requests.get(url)
	html_1 = parsel.Selector(html.text)
	a_1 = html_1.xpath('/html/body/div[2]/div/ul/li/div[2]').getall()
	path = '美食.csv'
	f = open(path, 'w', encoding='utf-8', newline='')
	ff = csv.writer(f)
	ff.writerow(['标题', '介绍', 'url'])
	url_list = []
	for ii in a_1:
		i = Selector(text=ii)
		viod_url = i.css('a::attr(href)').get()
		viod_bt = i.css('a>h2::text').get()
		viod_jj = i.css('a>p::text').get()
		url_list.append(q_url + viod_url)
		viod_url.strip()
		viod_bt.strip()
		viod_jj.strip('\n')
		ff.writerows([[viod_bt, viod_jj, q_url + viod_url]])
	f.close()
	thread = []
	for i in url_list:
		t = threading.Thread(target=download, args=(i,))
		t.start()
		thread.append(t)
	for kk in thread:
		kk.join()


def zong_html():
	url = 'https://www.pearvideo.com/popular'
	request = requests.get(url).text
	html_html = parsel.Selector(request)
	html_html_url = html_html.xpath('/html/body/div[2]/div/div[1]/ul/li/a/@href').getall()
	html_html_mz = html_html.xpath('/html/body/div[2]/div/div[1]/ul/li/a/text()').getall()
	for html_html_url, html_html_mz in zip(html_html_url, html_html_mz):
		zong_dit[html_html_mz] = q_url + html_html_url


def main():
	kaishi = time.time()
	zong_html()
	for hj in zong_dit.values():
		pai_hang(hj)
	jieshi = time.time()
	time_ = jieshi - kaishi
	print(f'总共用时{time_:%3f}')


if __name__ == '__main__':
	main()
