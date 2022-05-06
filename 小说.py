import time
import requests
import parsel
import os
import array

from parsel import Selector

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Mobile Safari/537.36 Edg/100.0.1185.44 '
}
url = 'https://www.mianfeixiaoshuoyueduwang.com/'
surl = 'https://www.mianfeixiaoshuoyueduwang.com/index.php?c=book&a=search&keywords='
zhuye_lj = []
zhuye_lj_er = []
zhuye_lj_san = []
zhuye_zidian = {}


def wanglo():
    wanglo_1 = requests.get(url=url, headers=headers)
    puanduan = wanglo_1.status_code
    if puanduan == 200:
        print('网址连接正常！')
    else:
        print('网址连接失败！请检查网络！')










def tu_xing():
    zhu_ye()
    while True:
        print("操作内容".center(30, "*"))  # .center 居中
        for i in zhuye_zidian:
            print(i.center(30))
        print('下载(复制查询出来的链接)'.center(30))

        print("操作内容".center(30, "*"))
        x = input('需要操作的指令:')
        if x == '奇幻玄幻':
            leibie_libiao_zhu(zhuye_zidian['奇幻玄幻'])
        elif x == '武侠仙侠':
            leibie_libiao_zhu(zhuye_zidian['武侠仙侠'])
        elif x == '历史军事':
            leibie_libiao_zhu(zhuye_zidian['历史军事'])
        elif x == '都市娱乐':
            leibie_libiao_zhu(zhuye_zidian['都市娱乐'])
        elif x == '竞技同人':
            leibie_libiao_zhu(zhuye_zidian['竞技同人'])
        elif x == '科幻游戏':
            leibie_libiao_zhu(zhuye_zidian['科幻游戏'])
        elif x == '悬疑灵异':
            leibie_libiao_zhu(zhuye_zidian['悬疑灵异'])
        elif x == '古代言情':
            leibie_libiao_zhu(zhuye_zidian['古代言情'])
        elif x == '都市言情':
            leibie_libiao_zhu(zhuye_zidian['都市言情'])
        elif x == '幻想时空':
            leibie_libiao_zhu(zhuye_zidian['幻想时空'])
        elif x == '下载' or '下载(复制查询出来的链接)':
            chaxunlianjie = input('复制查询的链接:')
            chaxunlianjie_ol = chaxunlianjie.startswith(url)
            try:
                if chaxunlianjie_ol != 'True':
                    wenzhang_liebiao(chaxunlianjie)
                else:
                    pass
            except:
                print('指令错误')
        else:
            print('指令错误，重新选择')
            print('\n')








def zhu_ye():
    zhuye_libiao1 = requests.get(url=url, headers=headers)
    zhuye_libiao1.encoding = zhuye_libiao1.apparent_encoding  # 万能编码
    zhuye_libiao = zhuye_libiao1.text  # 转换text
    zy_zh = parsel.Selector(zhuye_libiao)  # 转化可以使用样式提取
    zhuye_qishi = zy_zh.css('body > div.nav > ul >li').getall()  # 提取 样式 起始
    for i in zhuye_qishi:  # for 遍历出来
        i = Selector(text=i)  # 一定要用selector 转换一下 不然无法使用
        zhuye_tou = ' '.join(i.css('a > span::text').getall())
        # zhuye_lj = ' '.join(i.css('a::attr(href)').getall()
        zhuye_lj1 = ' '.join(i.css('a::attr(href)').getall())
        # zhuye_lj.append(url + zhuye_lj1)
        # zhuye_lj_er.append(zhuye_tou)
        zhuye_lj = url + zhuye_lj1
        zhuye_zidian[zhuye_tou] = zhuye_lj


def leibie_libiao_zhu(oooo):
    leinei_libiao = requests.get(url=oooo, headers=headers)
    leinei_libiao.encoding = leinei_libiao.apparent_encoding
    leibiao_zhuanhuan_texe = leinei_libiao.text
    leinei_libiao_yangshitiqu = parsel.Selector(leibiao_zhuanhuan_texe)
    # div 分类页函数获取内容如   标题 作者 简介 链接  遍历全部链接
    leinei_libiao_div = leinei_libiao_yangshitiqu.css('.w33 .box .pic_txt_list').getall()
    # print(leinei_libiao_div)
    for lis in leinei_libiao_div:
        # print('\n',lis)
        lis = Selector(text=lis)  # 需要转换一下不要报错
        lis_tite = lis.css('h3 a span::text').getall()
        lis_lianjie1 = lis.css('h3 a::attr(href)').getall()
        lis_zuozhe1 = lis.css('.info::text').getall()
        lis_zz0 = lis.css('.info span::text').getall()
        lis_jianjie0 = lis.css('.description::text').getall()
        # ['作者: ', ' (完结)']
        # str = ''.join(tup1)
        # lis_zuozhe =''.join(str(lis_zuozhe1).replace(" ', ' (完结)",""))
        lis_zuozhe2 = ' '.join(lis_zuozhe1)
        lis_zuozhe = lis_zuozhe2.replace('   (完结)', '')
        lis_zz = ' '.join(lis_zz0)
        # print(lis_zz1)
        # print(lis_zuozhe)
        lis_jianjie = ' '.join(lis_jianjie0)
        # lis_zuozhe = str(lis_zuozhe2).replace("       ( 完 结 )"," ")
        # lis_zuozhe = str(lis_zuozhe1).replace("', ' (完结)"," ") # str 才有replace方法其他没有 需要转换
        # print(' '.join(lis_zuozhe) + ' '.join(lis_zz))
        lis_lianjie = url + ' '.join(lis_lianjie1)
        # print(lis_zz,lis_lianjie)
        zhuye_lj_san.append(lis_lianjie)
        print(lis_tite, lis_zuozhe, lis_zz + '   链接：' + lis_lianjie, lis_jianjie)
        # print(lis_tite)


    try:
        xiayizhang = url + leinei_libiao_yangshitiqu.css('#page_next > a::attr(href)').get()

        pppp = xiayizhang.startswith(url + '/category')

        if pppp != 'True':
            leibie_libiao_zhu(xiayizhang)

        else:
            print('没有了')
    except:
        pass


def wenzhang_liebiao(mk):
    global wz_zonglianjie
    wenzhang_liebiao_url = requests.get(url=mk, headers=headers)
    wenzhang_liebiao_url.encoding = wenzhang_liebiao_url.apparent_encoding
    wenzhang_libiao_txt = wenzhang_liebiao_url.text
    wz_li = parsel.Selector(wenzhang_libiao_txt)
    wz_li_sm = wz_li.css('.pic_txt_list h3 span::text').get()  # 获取书名
    wz_li_zz = wz_li.css('html>body>div.wrapper>div.box>div.pic_txt_list>p.info>span::text').get()  # 获取作者
    wz_li_lb = wz_li.css('body > div.wrapper > div:nth-child(2) > div > p:nth-child(4) > span::text').get()
    wz_li_zt = wz_li.css('body > div.wrapper > div:nth-child(2) > div > p:nth-child(5) > span::text').get()
    # print('书名:'+ wz_li_sm + '\n作者:' + wz_li_zz+'\n类型:'+wz_li_lb+'\n状态:'+wz_li_zt)
    wz_mu = wz_li.css('html>body>.wrapper>.box>ul>li').getall()
    # time.sleep(1)
    for io in wz_mu:
        io = Selector(text=io)
        io_mu_lj = ' '.join(io.css('a::attr(href)').getall())
        wz_zonglianjie = url + io_mu_lj
        # io_name = io.css('a>span::text').getall()
        io_name = ' '.join(io.css('a>span::text').getall())

        # print(wz_zonglianjie,io_name)
        def nei(qqqq):
            yemian = requests.get(url=qqqq, headers=headers)
            yemian.encoding = yemian.apparent_encoding
            yemian_txt = yemian.text
            # 样式提取
            sele = parsel.Selector(yemian_txt)
            neirong_tou1 = sele.css('body > div.wrapper > div.content > h1::text').get()
            neirong_tou = str(neirong_tou1)
            neirong_zhengwen = sele.css('#content > p ::text').getall()
            neirong_zhengwen_text1 = ' '.join(neirong_zhengwen)
            neirong_zhengwen_text = str(neirong_zhengwen_text1)
            hh = '\n'
            chchch = "{0}{1}{2}{3}".format(neirong_tou, hh, neirong_zhengwen_text, hh)
            # chchch = str(chchch)
            file = open(wz_li_sm + '.txt', mode='a+', encoding='utf-8')
            file.write(chchch)
            file.close()
            shifou = os.path.exists(neirong_tou + '.txt')
            # print(shifou)
            if not shifou:
                print(wz_li_sm, neirong_tou + '  成功')
            else:
                print(wz_li_sm, neirong_tou + '  失败')

        nei(wz_zonglianjie)


if __name__ == '__main__':
    wanglo()
    tu_xing()
