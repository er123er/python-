import pprint
import random
import time
from User_Agent import User_Agent
import requests
from lxml import etree
import json

archdaily = {}


def zhu(one, two):
    headers = {
        'authority': 'www.archdaily.cn',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        # 'cookie': '_ga=GA1.2.1035883960.1678353606; _gid=GA1.2.1667145406.1678353606; __io_d=1_3719803979; __io_lv=1678353606663; __io=cd24a7e8f.9dffb56eb_1678353606664; __io_session_id=188b3a90a.afe45a552_1678353606666; __io_unique_25768=9; __io_uh=1; __io_visit_25768=1; __io_unique_34359=9; __io_visit_34359=1; __asc=27c2491d186c5aba898e05dc133; __auc=27c2491d186c5aba898e05dc133; __gads=ID=e51fd7eefb028b5e:T=1678353607:S=ALNI_MbyLIg4NK32DikwwWRI40-WI7lf2A; __gpi=UID=00000bd4dcf854be:T=1678353607:RT=1678353607:S=ALNI_Mb-F1X73InAU_TZroJal9l7HutPqA; _hjFirstSeen=1; _hjIncludedInSessionSample_270045=0; _hjSession_270045=eyJpZCI6IjNjYTcxYTgzLTdlZDMtNGY3My1hYWE5LTkxMGExZDI2ODg1MyIsImNyZWF0ZWQiOjE2NzgzNTM2MTUzMzgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; __io_nav_state25768=%7B%22current%22%3A%22%2F%22%2C%22currentDomain%22%3A%22www.archdaily.cn%22%2C%22previous%22%3A%22%2F%22%2C%22previousDomain%22%3A%22www.archdaily.cn%22%7D; _hjSessionUser_270045=eyJpZCI6IjU2ODU0OWM3LWYzOTAtNWY3MC04MWY0LTE2Zjk3OTY4MDAxNCIsImNyZWF0ZWQiOjE2NzgzNTM2MTUzMzAsImV4aXN0aW5nIjp0cnVlfQ==',
        'pragma': 'no-cache',
        'referer': 'https://www.archdaily.cn/search/cn/projects?ad_source=jv-header&ad_name=main-menu',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': User_Agent(),
    }

    response = requests.get('https://www.archdaily.cn/search/api/v1/cn/projects', headers=headers)

    json = response.json()['results']
    for i in json[one:two]:
        print(i['url'])
        print(i['title'])
        er(title_t=i['title'], url=i['url'])
        time.sleep(random.randint(2, 3))
        '''
        https://www.archdaily.cn/cn/996756/ao-kan-bo-zhu-zhai-estudio-morton-51st?ad_source=search&ad_medium=projects_tab
        单间即独栋，奥坎波住宅 / Estudio Morton 51st
        '''


# 图片
def img_href_code(url):
    href = 'https://www.archdaily.cn' + url
    headers = {
        'authority': 'www.archdaily.cn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.archdaily.cn/search/cn/projects',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': User_Agent(),
    }
    response = requests.get(href, headers=headers)
    tree = etree.HTML(response.text)
    img_href = tree.xpath('/html/head/meta[16]/@content')

    # https://images.adsttc.com.qtlcn.com/media/images/6407/2190/3dfe/8201/6f73/1a3c/large_jpg/not-ready-cabin-house-miss-maos-home-jin-qiuye-studio_5.jpg?1678188998
    img_title = ''.join(img_href).split('?')[1]

    response = requests.get(img_href[0], headers=headers)
    with open(img_title + ".jpg", "wb") as f:  # wb是写二进制
        f.write(response.content)


def er(title_t, url):
    headers = {
        'authority': 'www.archdaily.cn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        # 'cookie': '_ga=GA1.2.1035883960.1678353606; _gid=GA1.2.1667145406.1678353606; __io_lv=1678353606663; __io=cd24a7e8f.9dffb56eb_1678353606664; __io_session_id=188b3a90a.afe45a552_1678353606666; __io_unique_25768=9; __io_uh=1; __io_unique_34359=9; __asc=27c2491d186c5aba898e05dc133; __auc=27c2491d186c5aba898e05dc133; __gads=ID=e51fd7eefb028b5e:T=1678353607:S=ALNI_MbyLIg4NK32DikwwWRI40-WI7lf2A; __gpi=UID=00000bd4dcf854be:T=1678353607:RT=1678353607:S=ALNI_Mb-F1X73InAU_TZroJal9l7HutPqA; _hjFirstSeen=1; _hjIncludedInSessionSample_270045=0; _hjSession_270045=eyJpZCI6IjNjYTcxYTgzLTdlZDMtNGY3My1hYWE5LTkxMGExZDI2ODg1MyIsImNyZWF0ZWQiOjE2NzgzNTM2MTUzMzgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _hjSessionUser_270045=eyJpZCI6IjU2ODU0OWM3LWYzOTAtNWY3MC04MWY0LTE2Zjk3OTY4MDAxNCIsImNyZWF0ZWQiOjE2NzgzNTM2MTUzMzAsImV4aXN0aW5nIjp0cnVlfQ==; __io_nav_state34359=%7B%22current%22%3A%22%2Fcn%2F997521%2Fcang-zhai-mao-nu-shi-jia-jin-qiu-ye-jian-zhu-gong-zuo-shi%22%2C%22currentDomain%22%3A%22www.archdaily.cn%22%2C%22previousDomain%22%3A%22%22%7D; ad-consented_at=2023-03-09T09%3A35%3A19.048Z; __io_d=6_2918589664; _gat=1; __io_nav_state25768=%7B%22current%22%3A%22%2Fcn%2F997521%2Fcang-zhai-mao-nu-shi-jia-jin-qiu-ye-jian-zhu-gong-zuo-shi%22%2C%22currentDomain%22%3A%22www.archdaily.cn%22%2C%22previous%22%3A%22%2Fcn%2F997368%2Fshuang-ting-yuan-shang-hai-su-kai-tai-jiu-dian-hu-wai-kong-jian-gai-zao-zhi-zuo-shi%22%2C%22previousDomain%22%3A%22www.archdaily.cn%22%7D; __io_visit_25768=1; __io_visit_34359=1',
        'pragma': 'no-cache',
        'referer': 'https://www.archdaily.cn/search/cn/projects',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': User_Agent(),
    }
    title = {}
    response = requests.get(url, headers=headers)

    tree = etree.HTML(response.text)
    html_div1_a = tree.xpath('//*[@id="single-content"]/div[2]/div/div[1]/a/text()')  # 主要第一部分 标识
    html_div2_div = ''.join(tree.xpath('//*[@id="single-content"]/div[2]/div/div[2]/text()'))  # 主要第一部分 地区
    html_div2_a = ''.join(tree.xpath('//*[@id="single-content"]/div[2]/div/div[2]/a/text()'))  # 主要第一部分 地区2
    html_div2_zong = html_div2_div + html_div2_a
    html_div_ul_li = tree.xpath('//*[@id="single-content"]/div[2]/ul/li')
    html1 = {}
    for html_div_li in html_div_ul_li:  # html[1]
        html_div_key = ''.join(html_div_li.xpath('.//*[@class="afd-specs__key"]/text()')).strip()
        html_div_value = ''.join(html_div_li.xpath('.//*[@class="afd-specs__value"]/a/text()')).strip()
        # print(html_div_key, html_div_value)
        html1[html_div_key] = html_div_value
    html2_div_ul = tree.xpath('//*[@id="single-content"]/div[3]/ul/li')
    # print(len(html2_div_ul))
    html2 = {}
    for html_div_li2 in html2_div_ul:  # html[2]
        html_div2_key = ''.join(html_div_li2.xpath('.//*[@class="afd-specs__key"]/text()')).strip()
        html_div2_value = ''.join(html_div_li2.xpath('.//*[@class="afd-specs__value"]/text()')).strip()
        # print(html_div2_key, html_div2_value)
        html2[html_div2_key] = html_div2_value
    img_href = tree.xpath('//*[@id="gallery-thumbs"]/li')  # 图片
    h1_title = tree.xpath('//*[@id="content"]/div/div[2]/header[2]/h1/text()')  # 标题
    p_title = tree.xpath('//*[@id="single-content"]/p')

    str_text = ''  # 文本内容
    for p in p_title:
        detail = p.xpath('./text()')
        str_text += ''.join(detail)
    # print(str_text)  # 文本
    title['html1'] = html1
    title['html2'] = html2
    title['str_text'] = str_text

    print(title)
    # 图片下载
    # for img in img_href:
    #     img_detail = img.xpath('./a/@href')
    #     herf_code = ''.join(img_detail)
    #     img_href_code(url=herf_code)
    #     time.sleep(2)
    archdaily[title_t] = title


if __name__ == '__main__':
    o = time.time()
    zhu(one=0, two=3)
    # pprint.pprint(archdaily)
    with open('json2.txt', "w+", encoding='utf-8') as dump_f:
        dump_f.write(json.dumps(archdaily, ensure_ascii=False))
    p = time.time()
    pp = p - o
    print('勇士%s' % pp)