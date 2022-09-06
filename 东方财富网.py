# -*- coding:utf-8 -*-
import pprint
import random
import re
import time
import json
from User_Agent import User_Agent
import requests
import csv


def new_string(original_string, cd):
    # cd = 'datatable4562789' + '('
    new_strin = re.sub('' + cd + '[()]', "", original_string)
    new_string = re.sub('[)$]', "", new_strin)
    # print(json.loads(new_string))
    return json.loads(new_string)['data']


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Host': 'data.eastmoney.com',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': User_Agent(),

}
csvfile = open("test.csv", "w", encoding='utf-8', newline='')

tou = {
    "信息代码",
    "报告名称",
    "股票代码",
    "股票名称",
    "东财评级",
    "机构",
    "公司名称",
    "研究员",
    "行业",
    "2022盈利预测-收益",
    "2022盈利预测-市盈率",
    "2023盈利预测-收益",
    "2023盈利预测-市盈率",
    "近一个月个股研报数",
    "查询日期"
}
f = csv.DictWriter(csvfile, fieldnames=tou)
f.writeheader()
url = 'http://reportapi.eastmoney.com/report/list?'
# url = 'http://reportapi.eastmoney.com/report/list?'
for page in range(1, 100):
    # page = 1
    cd = 'datatable' + ''.join(random.sample('123456789', 7))
    params = {
        'cb': cd,
        'industryCode': '*',
        'pageSize': '50',
        'industry': '*',
        'rating': '',
        'ratingChange': '',
        'beginTime': '2020-09-06',
        'endTime': time.strftime("%Y-%m-%d", time.localtime()),
        'pageNo': page,
        'fields': '',
        'qType': '0',
        'orgCode': '',
        'code': '*',
        'rcode': '',
        'p': page,
        'pageNum': page,
        'pageNumber': page,
        '_': int(time.time() * 1000),
    }
    html_ = requests.get(url=url, headers=headers, params=params).text
    # pprint.pprint(new_string(html_, cd))
    for i in new_string(html_, cd):
        # pprint.pprint(i)

        indvInduName = i['indvInduName']  # 行业
        researcher = i['researcher']  # 研究员
        publishDate = i['publishDate']  # 查询日期
        orgName = i['orgName']  # 公司名称
        orgSName = i['orgSName']  # 机构
        emRatingName = i['emRatingName']  # 东财评级
        stockName = i['stockName']  # 股票名称
        stockCode = i['stockCode']  # 股票代码
        title = i['title']  # 报告名称
        count = i['count']  # 近一个月个股研报数
        predictThisYearEps = i['predictThisYearEps']  # 2022盈利预测-收益
        predictThisYearPe = i['predictThisYearPe']  # 2022盈利预测-市盈率
        predictNextYearEps = i['predictNextYearEps']  # 2023盈利预测-收益
        predictNextYearPe = i['predictNextYearPe']  # 2023盈利预测-市盈率
        infoCode = i['infoCode']  # 信息代码
        print(infoCode,title,stockCode,stockName,emRatingName,orgSName,orgName,researcher,indvInduName,predictThisYearEps,predictThisYearPe,predictNextYearEps,predictNextYearPe,count,publishDate)
        dic = {'信息代码': infoCode,
               '报告名称': title,
               '股票代码': stockCode,
               '股票名称': stockName,
               "东财评级": emRatingName,
               "机构": orgSName,
               "公司名称": orgName,
               "研究员": researcher,
               "行业": indvInduName,
               "2022盈利预测-收益": predictThisYearEps,
               "2022盈利预测-市盈率": predictThisYearPe,
               "2023盈利预测-收益": predictNextYearEps,
               "2023盈利预测-市盈率": predictNextYearPe,
               "近一个月个股研报数": count,
               "查询日期": publishDate
               }
        f.writerow(dic)

    time.sleep(random.randint(2,5))
