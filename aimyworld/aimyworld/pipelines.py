# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time
import pprint
import json
import pymysql
import copy
class YoutubeDemoPipeline:
    def open_spider(self, spider):
        print("启动")
        self.open_time = time.time()

    def process_item(self, item, spider):
        # print('管道数据', dict(item))
        js = dict(item)
        with open('sj.txt', 'a', encoding='utf=8') as f:
            f.write(json.dumps(js, ensure_ascii=False) + '\n')
        return copy.deepcopy(item)

    def close_spider(self, spider):
        self.close_time = time.time()
        zong = self.close_time - self.open_time
        print("结束，用时%d" % zong)





class MySQLPipeline(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE')
        )

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        sql = """
            INSERT INTO mytable (vermicelli, title_img, banner_img, video_data, user, user_text, country, Number_of_views, Registration_time, name, platform, tags, video, depth, download_timeout, proxy, download_slot, download_latency)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            str(item['vermicelli']).encode('unicode_escape'),
            str(item['title_img']).encode('unicode_escape'),
            str(item['banner_img']).encode('unicode_escape'),
            str(item['video_data']).encode('unicode_escape'),
            str(item['user']).encode('unicode_escape'),
            str(item['user_text']).encode('unicode_escape'),
            str(item['country']).encode('unicode_escape'),
            str(item['Number_of_views']).encode('unicode_escape'),
            str(item['Registration_time']).encode('unicode_escape'),
            str(item['name']).encode('unicode_escape'),
            json.dumps(item['platform']),
            # str(item['platform']).encode('unicode_escape'),
            # item['platform'],
            str(item['tage']).encode('unicode_escape'),
            # str(item['video']).encode('unicode_escape'),
            # item['video'],
            json.dumps(item['video']),
            str(item['depth']).encode('unicode_escape'),
            str(item['download_timeout']).encode('unicode_escape'),
            str(item['proxy']).encode('unicode_escape'),
            str(item['download_slot']).encode('unicode_escape'),
            str(item['download_latency']).encode('unicode_escape'),
        )
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item
