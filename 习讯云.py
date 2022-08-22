# -*- coding: utf-8 -*-

import requests
import pprint
import random
import datetime  # 导入日期时间模块


root = '' # 账号
paw = '' # 密码


# 实习工作具体情况及实习任务完成情况
def internshiptasks():
    title = [
        '公司力图以最有限的人力完成最繁重的任务，把每个人都推向所能承受的极限，以此来争取高效率和高 利润。实习期间我对这一点感受很深刻。每个人都很忙碌，压力巨大，没有人有时间教你什么。他们在安排给你任务时已经预先假定：你到蜈支洲岛来干活，你就是蜈支洲岛的员工，那么你应该天生就明白一切做法和规则。',
        '时间总是在不经意间流逝，感觉自己做了不少，但是还有很多也没做……\n工作虽然很枯燥，挺麻烦的，但总是能学到不少东西，呵呵!',
        '在上班时间总感觉自己的时间利用率不够，特别是在晚上，都不知道干什么所以对自己的要求还应再紧些……',
        '这两天事好多，好象连喘息的机会都没有，一件事做完接着做另一件事。开始感觉到自己睡眠不足，恩!看来得好好保养自己了...',
        '又是晴天，真好。昨天接到朋友们的短信，祝我中秋节快乐。其实一直以来，是我应该感谢他们，给我那么多的关心、信任和感动，让我总能乐观的生活着。而现在，有着温暖阳光的清晨，我用微笑迎接新的一天!',
        '留一刻不泯的童心给自己! 祝我们这些表面风光，内心彷徨;容颜未老，心已沧桑;似乎有才，实为江郎;成就难有，郁闷经常;比鸡起的早，比狗睡的晚;比驴干的多，比猪吃的差;比岳飞忠良，比赖昌星紧张的小青年。',
        '很早就到公司了，但人事部要到八点钟才上班，无聊的我转了一遍。看到挥汗如雨的工人，才意识到自己是那么的幸运，一名还未走出校门的大学生，可以和那些资历深厚的前辈们坐在同一个办公室，真的是莫大的幸运。所以，我一定要好好工作，努力学好知识。',
        '我的同事，我觉得他们都很好，经理也很好，很愉快的一个工作环境。不好的是我自己，也不知道怎么了，每每到一个新的环境我总需要一个很漫长的时间来让自己学会说“地方话”。在学会方言之前我总是保持沉默，这种沉默让别人会感觉很压抑，我自己也是。亲爱的，慢慢来，别紧张!你会适应新生活的',
        '我基本了解了公司的工作程序和工作要领，也通过了公司的一些考核，并且我于今天开始承接培训任务。又找到了以前的相关文章进行了细致研究。由于是第一次接受任务，我不敢掉以轻心，所以拿出公司提供给我们的资料仔细的看，边看边做。我所能做的就是怎么样把公司提供给我们的这些资料合理的去综合，并提出具体措施。',
        '开始的时候很不满足整天在这里朝六晚八的生活，在办公室一座就是一整天，觉得生活特别的没希望，特别是没有活的时候，就更加感到很无聊。我现在的是：好好学习，天天向上，希望每一天的我都能够学到一点新的东西。',
        '今天早早来到公司上班，到办公室后主动打扫室内卫生，等其他同事们来到时我已经忙完了，看到大家高兴的神情，我的心情无比高兴。由于我学会了使用复印机和传真机，所以只要有复印和传真的活就主动去做，使我对这项工作越来越熟悉了，做起事来也不手忙脚乱了。对于复印机除了简单的复印又学会了扫描复印、双页复印、双面复印等，基本了解了A3、A4、B4、B5等纸张规格，并且学会了自己更换复印机纸盒和打印机粉墨等操作。',
    ]
    return title[random.randint(0, len(title) - 1)]


# 主要收获及工作成绩
def Achievements():
    title_1 = [
        '在工作中，冲突与矛盾总是难免的。有的时候会发生争吵、争执、争斗乃至斗争，其实也难免。但是不管以前发生过怎样的事，只要是我的同事，他主动表现出来和解或和好的意愿，我愿意和解。',
        '若是你视工作为一种乐趣，人生就是天堂；若是你视工作为一种义务，人生就是地狱。检视一下你的工作态度，那会让我们都感觉愉快',
        '做事，应适当考虑。比如，为何做，值不值得做，是否必须做，不做不可？这样，你一旦开始做的时候，就会全身心投入，而不再为一些鸡毛蒜皮的事情，一次次打断工作，也不会出现徒有忙碌而无进展的情况了。',
        '工作之余，必须要抽出时刻多认识一些人，多进入一些社交圈，这对你的发展会有极大的好处。',
        '生命中终将会错过一些人，我们应该感谢那一些错过的人，他们让我们明白了幸福的珍贵。不要相信该是自己的终该是自己的，不去争取不去掌握的话，永远都不会有机会。缘分是什么，缘分就是给了你一次遇到的机会，幸福全靠去争取。',
        '时代造就英雄 时代造就人才，我们现在这个时代很好，这个时代给你提供了很好的平台，你能不能成为人才，关键在于自己。一定要在这个时代中练就成大才。这次我们招聘，精挑细选，从全国知名高校选拔，目的就是让大家成为栋梁之才。',
        '机关工作的情况类似于制造业，工作的成果不是以制造者个人的成果面貌呈现，而是以工厂之成果的面貌呈现。',
        '在人生的道路上，即使一切都失去了，只要一息尚存，你就没有丝毫理由绝望。因为失去的一切，又可能在新的层次上复得。',
        '对于工作，你要弄明白哪些是你必须要做的、能产生绩效的工作，哪些是别人有意无意给你但不该你做的活，先做前者，如果有时间再做后者，如果没有时间，请直接婉言谢绝。',
        '善于倾听别人，要善于倾听别人的想法，找到大家的共鸣点，找到共同点，这并不是说让你去迎合别人。要和别人打交道、沟通，要学会善于合作。',
        '人生的磨难是很多的，所以我们不可对于每一件轻微的伤害都过于敏感。在生活磨难面前，精神上的坚强和无动于衷是我们抵抗罪恶和人生意外的最好武器。',
        '那一瞬，我飞升成仙，不为长生，只为找一份工作。',
        '我的努力求学没有得到别的好处，只不过是愈来愈发觉自己的无知。',
        '相信生活是美好的，相信人生是充满希望的，懂得人比钱重要，能用钱解决的问题都不是问题。',
    ]
    return title_1[random.randint(0, len(title_1) - 1)]


s = requests.Session()
today = datetime.date.today()  # 获得今天的日期
# print(today)

url = 'https://api.xixunyun.com/login/admin'
he = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-length': '58',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://www.xixunyun.com',
    'referer': 'https://www.xixunyun.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36 Edg/104.0.1293.63',
}

data = {
    'school_id': '842',  # 学院
    'j_data': f'{root};{paw};1',  # 账户密码
    'type': 'web',
}

html = s.post(url, headers=he, data=data)

token = html.json()['data']['token']
# cook = html.cookies.get_dict()['PHPSESSID']

urll = f'https://api.xixunyun.com/Reports/StudentOperator?token={token}'
# print(urll)
h = {
    'content-length': '1978',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.xixunyun.com',
    'referer': 'https://www.xixunyun.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
}
tomorrow = today + datetime.timedelta(days=1)
# print(tomorrow)
da = {
    'business_type': 'day',
    'start_date': str(tomorrow).replace('-', '/'),
    'end_date': str(tomorrow).replace('-', '/'),
    'content': f'[{{"title":"实习工作具体情况及实习任务完成情况","content":"{internshiptasks()}","require":"1","sort":"1"}},{{"title":"主要收获及工作成绩","content":"{Achievements()}","require":"0","sort":"2"}},{{"title":"工作中的问题及需要老师的指导帮助","content":"","require":"0","sort":"3"}}]',
    'attachment': '',
}
pprint.pprint(da)
biaodan = s.post(urll, headers=h, data=da, cookies=html.cookies)

print(biaodan.json())
