# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pprint
import time
import json
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

inTotal = {}


class ArchdailyPipeline:
    def open_spider(self, spider):
        print("启动")
        self.open_time = time.time()

    def process_item(self, item, spider):
        # print('管道数据', dict(item))
        sz = len(inTotal)
        inTotal[sz + 1] = item['branch']
        with open('sj.txt','w',encoding='utf=8') as f:
            f.write(json.dumps(inTotal,ensure_ascii=False))
        return item


    def close_spider(self, spider):
        pprint.pprint(inTotal)

        self.close_time = time.time()
        zong = self.close_time - self.open_time
        print("结束，用时%d" % zong)
