import requests
import ddddocr
#  米瓜博客
request = requests.get('https://www.miigua.com/commons/captcha')
ocr = ddddocr.DdddOcr()
req_cookies = request.cookies
with open('p.jpg', 'wb') as f:
	f.write(request.content)
with open('p.jpg', 'rb') as ff:
	img_bytes = ff.read()

rr = ocr.classification(img_bytes).upper()
dit = {
	'articleId': '347',  # 博客地址编号
	'render': 'default',
	'pid': '',
	'nickname': 'asdasdasdseqweqweqwa',  # 用户名
	'email': 'weqeqweqweqweasdasd',  # 邮箱
	'content': 'asdasdasdasdasdasdasdasdasdasdas',  # 评论内容
	'captcha': rr  # 验证码
}
url = 'https://www.miigua.com/article/postComment'
h = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
	'Connection': 'keep-alive',
	'Content-Length': '134',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Host': 'www.miigua.com',
	'Origin': 'https://www.miigua.com',
	'Referer': 'https://www.miigua.com/',
	'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
	'X-Requested-With': 'XMLHttpRequest',
}
fg = requests.post(url=url, headers=h, data=dit, cookies=req_cookies)
print(fg.json())
