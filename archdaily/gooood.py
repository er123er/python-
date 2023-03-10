import json
import time

from lxml import etree
from selenium import webdriver

all_json = {}


def sliding():
    # time.sleep(5)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    for y in range(30):
        js = 'window.scrollBy(0,800)'
        driver.execute_script(js)
        time.sleep(0.5)


driver = webdriver.Edge()

driver.get(r'https://www.gooood.cn/category/type/architecture')
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# sliding() # 开启滚动
pageSource = driver.page_source
# print(pageSource) 源码
tree = etree.HTML(pageSource)
html_div = tree.xpath('//*[@class="post-excerpt"]/a/@href')
# print(len(html_div))
theDomainName = 'https://www.gooood.cn'
sj = 0
for div_a in html_div[0:3]:
    # print(div_a)
    fen = {}
    driver.get(theDomainName + div_a)
    sliding()
    pageSource = driver.page_source
    tree = etree.HTML(pageSource)
    html_div_h1 = tree.xpath('//*[@class="single-content"]/h1/text()')
    html_div_h2 = tree.xpath('//*[@class="single-content"]/h2/text()')

    # print(html_div_h1, html_div_h2)
    #  projectLabel 项目标签
    projectLabel = tree.xpath('//*[@class="entry-spec"]/div')
    # print(projectLabel)
    projectLabel_dic = {}
    for projectLabel_html in projectLabel:
        projectLabel_label_text = ''.join(projectLabel_html.xpath('./div[1]/span[2]/text()'))
        projectLabel_blank = ''.join(projectLabel_html.xpath('.//*[@class="spec-data"]/a/text()')).strip()
        projectLabel_dic[projectLabel_label_text] = projectLabel_blank
    # time.sleep(30)
    # print(projectLabel_dic)
    html_text = tree.xpath('//*[@class="ss-twelvecol shortcolumn"]/p/text()')
    html_img = tree.xpath('//*[@class="colorbox_gallery"]/img/@src')
    print(html_img)
    fen['html_div_h1'] = html_div_h1
    fen['html_div_h2'] = html_div_h2
    fen['projectLabel_dic'] = projectLabel_dic
    fen['html_text'] = html_text
    fen['html_img'] = html_img
    all_json[sj] = fen
    sj+=1


with open('jjjjjj.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(all_json, ensure_ascii=False))


