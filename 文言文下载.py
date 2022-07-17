import random
import parsel
import requests
import pymysql
import time
import User_Agent
from concurrent.futures import ThreadPoolExecutor


def sql(t_1=None, t_2=None, t_3=None, t_4=None):
	db = pymysql.connect(host='localhost', user='root', port=3306, password='123456789', db='op', charset='utf8')
	cur = db.cursor()
	sql = f'''INSERT INTO `sc` (`sc_mc`, `sc_zz`, `sc_nd`, `sc_nr`) VALUES ('{t_1}', '{t_2}', '{t_3}', '{t_4}');'''
	cur.execute(sql)
	db.commit()


def sql_query_login():
	db = pymysql.connect(host='localhost', user='root', port=3306, password='123456789', db='op', charset='utf8')
	cur = db.cursor()
	sql = """SELECT * from sc WHERE id=2;"""
	cur.execute(sql)
	db.commit()
	return cur.fetchall()[0]


def sc():
	for ii in range(1, 4039):
		print(f'第{ii}页.')
		url = f'https://www.gushimi.org/wenyanwen/index_{ii}.html'
		headers = {
			'User-Agent': User_Agent.User_Agent()
		}
		fff = requests.get(url=url, headers=headers)
		fff.encoding = fff.apparent_encoding
		ff = parsel.Selector(fff.text)
		url_ = ff.xpath('/html/body/div[7]/div[1]/div/div/div[2]/a/@href').getall()
		pa = 'https://www.gushimi.org/'
		sj = random.randint(1, 3)
		time.sleep(sj)
		with ThreadPoolExecutor(20) as t:
			for i in url_:
				url_url = pa + i
				t.submit(ti_, url_url)


def ti_(url):
	headers = {
		'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
	}
	fff = requests.get(url=url, headers=headers)
	fff.encoding = fff.apparent_encoding
	ff = parsel.Selector(fff.text)
	wz_mc = ff.xpath('//*[@id="layer-photos-demo"]/div[5]/div[1]/h2/text()').get()
	wz_cd = ff.xpath('//*[@id="layer-photos-demo"]/div[5]/div[2]/div[1]/a[1]/text()').get()
	wz_zz = ff.xpath('//*[@id="layer-photos-demo"]/div[5]/div[2]/div[1]/a[2]/text()').get()
	wz_nr = ff.xpath('//*[@id="layer-photos-demo"]/div[5]/div[2]/div[2]/text()').getall()
	wz = ''.join(wz_nr)
	sql(wz_mc, wz_zz, wz_cd, wz)
	print('完成：', wz_mc)


def tt(f):
	time.sleep(2)
	print('现在:', f)


if __name__ == '__main__':
	sc()
