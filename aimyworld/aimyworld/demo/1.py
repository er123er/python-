# -*- coding: utf-8 -*-
import json
import re
import pymysql
import requests

from validate_email import validate_email

proxies = {
    'http': '127.0.0.1:10809',
    'https': '127.0.0.1:10809',
}
cookies = {
    'ig_did': 'D6D21DC6-BFB4-4BB4-B4D4-4405580DBA3E',
    'datr': '7eNZZBSzPMe3fCxBuxWyaaEO',
    'mid': 'ZFnj7wALAAEd8K4vlMHzTUW8j2hi',
    'ig_nrcb': '1',
    'shbid': '"2027\\05454002339669\\0541718073276:01f7cdebd798d2968d565772e644184b80bfd59e27cf7e3c560e9c48a78a39f3a6fc6fdd"',
    'shbts': '"1686537276\\05454002339669\\0541718073276:01f77d0fd7400e83fb6719a024fa3e18886ed0b0b50062f117f6105af96cf1e724fc2f8e"',
    'sessionid': '59703935504%3AIMNv8PHdGhGnsJ%3A7%3AAYd2sP5y2irmdMqYi66pQuUy8gW-r3zF24QpG0_fHA',
    'ds_user_id': '59703935504',
    'csrftoken': 'Cmrk1nwxQbeuL9bE5Z8cW7BAPuPsRGjH',
    'rur': '"NAO\\05459703935504\\0541718172445:01f7f096ec7cf5c475283a16a1d8649e079a1ad0ec6b879211249d19cd0569c776207e9b"',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'X-CSRFToken': 'Cmrk1nwxQbeuL9bE5Z8cW7BAPuPsRGjH',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '129477',
    'X-IG-WWW-Claim': 'hmac.AR3-YhZCVXTXQjAI6n7drW1hh9jqLAzIvVtDzqRquUTCFcb6',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/minasluxebeauty/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',

}


def demo_1():
    url = "https://www.instagram.com/explore/"
    response = requests.get(url, headers=headers, cookies=cookies, proxies=proxies)
    status_text = re.compile('"result":\{"response":(.*?),"status_code":200}')
    text = status_text.findall(response.text)[0]
    sectional_items = json.loads(text)
    # print(list(find_username(json.loads(sectional_items))))
    # print(set(list(find_username(json.loads(sectional_items)))))
    # print(len(set(list(find_username(json.loads(sectional_items))))))
    li = list(set(list(find_username(json.loads(sectional_items)))))
    # li = []
    # for username_1 in json.loads(sectional_items)['sectional_items']:
    #     li.append(list(find_username(username_1)))
    return li


def demo_2(name):
    url = "https://www.instagram.com/api/v1/users/web_profile_info/"
    params = {
        "username": name
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params, proxies=proxies)
    print(name, response.status_code)
    # print(response.text)
    # ["data"]["user"]["biography"] # 简历
    # ["data"]["user"]["edge_owner_to_timeline_media"]["count"] # 视频数
    # ["data"]["user"]["edge_followed_by"]["count"] # 粉丝数
    # ["data"]["user"]["profile_pic_url"] # 头像url
    # ["data"]["user"]["username"] # 用户id
    # ["data"]["user"]["biography"] # 名字
    # ["data"]["user"]["category_name"] # 类型
    # ["data"]["user"]["edge_owner_to_timeline_media"]["edges"] # 视频
    # ["node"]["video_view_count"]  视频观看次数
    # ["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]  视频标题
    # ["node"]["shortcode"]  视频url
    # ["node"]["thumbnail_resources"][-1]["src"]  视频封面

    vermicelli = response.json()["data"]["user"]["edge_owner_to_timeline_media"]["count"]  # 粉丝数
    title_img = response.json()["data"]["user"]["profile_pic_url"]  # 头像url
    banner_img = 'None'  # 背景url
    video_data = response.json()["data"]["user"]["edge_followed_by"]["count"]  # 视频数
    user = response.json()["data"]["user"]["username"]  # 名字
    user_text = response.json()["data"]["user"]["biography"]  # 简历
    country = 'None'  # 国家
    Number_of_views = 'None'  # 观看次数
    registration_time = 'None'  # 注册时间
    proxy = 'https://127.0.0.1:7890'
    download_latency = ''
    name = response.json()["data"]["user"]["biography"]  # 名字
    platform = {}
    tags = response.json()["data"]["user"]["category_name"]  # 类型
    download_slot = 'www.instagram.com'
    video = []
    for i in response.json()["data"]["user"]["edge_owner_to_timeline_media"]["edges"]:
        # times_of_play = i["node"]["video_view_count"]  # 视频观看次数
        try:
            thumbnail_url = i["node"]["thumbnail_resources"][-1]["src"]  # 视频封面
        except:
            thumbnail_url = 'None'
        try:
            video_title = i["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]  # 视频标题
        except:
            video_title = 'None'
        try:
            video_url = i["node"]["shortcode"]  # 视频url
        except:
            video_url = 'None'
        video.append({
            'times_of_play': 'None',
            'video_title': video_title,
            'thumbnail_url': thumbnail_url,
            'video_url': video_url,
        })
    download_timeout = 'None'
    # (vermicelli, title_img, banner_img, video_data, user, user_text, country, Number_of_views, Registration_time, name, platform, tags, video, depth, download_timeout, proxy, download_slot, download_latency)
    depth = 'None'
    data_tuple = (
        vermicelli,
        str(title_img).encode('unicode_escape'),
        str(banner_img).encode('unicode_escape'),
        str(video_data).encode('unicode_escape'),
        str(user).encode('unicode_escape'),
        str(user_text).encode('unicode_escape'),
        str(country).encode('unicode_escape'),
        Number_of_views,
        registration_time,
        str(name).encode('unicode_escape'),
        str(platform).encode('unicode_escape'),
        str(tags).encode('unicode_escape'),
        str(json.dumps(video)).encode('unicode_escape'),
        depth,
        download_latency,
        str(proxy).encode('unicode_escape'),
        download_slot,
        download_timeout
    )

    return data_tuple


def find_username(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (str, int, float)):
                continue
            elif isinstance(value, dict):
                if 'username' in value:
                    yield value['username']
                else:
                    yield from find_username(value)
            elif isinstance(value, list):
                for item in value:
                    yield from find_username(item)
            else:
                continue
    elif isinstance(data, list):
        for item in data:
            yield from find_username(item)
    else:
        return


def validate_emails(text):
    emails = text.split()
    valid_emails = []
    for email in emails:
        if validate_email(email):
            valid_emails.append(email)
    return valid_emails


def ddd(kmk):
    encoded_str = str(kmk).encode('unicode_escape')
    decoded_str = bytes(encoded_str).decode('unicode_escape')
    decoded_str = bytes(decoded_str, 'utf-8').decode('unicode_escape')
    return decoded_str


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Email pattern to match
    return bool(re.match(pattern, email))


def extract_emails(text):
    pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    emails = re.findall(pattern, text)
    valid_emails = {email for email in emails if validate_email(email)}
    return valid_emails

    return valid_emails


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='web')
    cursor = conn.cursor()

    for kin in range(5000):
        try:
            ty_li = demo_1()
            sql = """
                INSERT INTO mytable_copy2 (vermicelli, title_img, banner_img, video_data, user, user_text, country, Number_of_views, Registration_time, name, platform, tags, video, depth, download_timeout, proxy, download_slot, download_latency)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            for k in ty_li:
                tttt = demo_2(name=k)
                cursor.execute(sql, tttt)
                conn.commit()
            print(kin, '成功')
        except:
            print(kin, '错误')

    # list_sun = []
    # sql = 'SELECT * FROM `web`.`mytable_copy2`;'
    # cursor.execute(sql)
    # for i in cursor.fetchall():
    #     # print(i[6])
    #     dic_list = {}
    #     decoded_str = ddd(kmk=i[6])
    #     valid_emails = extract_emails(decoded_str)
    #     if valid_emails:
    #         # print(i[0], i[5],ddd(kmk=i[12]), valid_emails)
    #         dic_list = {
    #             'id': i[0],
    #             'name': i[5],
    #             'tage': ddd(kmk=i[12]),
    #             'email': valid_emails,
    #         }
    #         print(dic_list)
    #         list_sun.append(dic_list)
    # df = pd.DataFrame(list_sun)
    #
    # # 将数据框写入新的 Excel 文件
    # df.to_excel('output.xlsx', index=False)
