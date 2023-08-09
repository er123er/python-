import pandas as pd
import re
import pymongo
import pymysql


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


conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='web')
cursor = conn.cursor()
#
list_sun = []
sql = 'SELECT * FROM `web`.`mytable_copy2`;'
cursor.execute(sql)
for i in cursor.fetchall():
    # print(i[6])
    dic_list = {}
    decoded_str = ddd(kmk=i[6])
    valid_emails = extract_emails(decoded_str)
    if valid_emails:
        # print(i[0], i[5],ddd(kmk=i[12]), valid_emails)
        dic_list = {
            'id': i[0],
            'name': i[5],
            'tage': ddd(kmk=i[12]),
            'email': valid_emails,
        }
        print(dic_list)
        list_sun.append(dic_list)
df = pd.DataFrame(list_sun)

# 将数据框写入新的 Excel 文件
# df.to_excel('output.xlsx', index=False)
# SELECT * FROM `web`.`pet_2`

# client = pymongo.MongoClient("mongodb://localhost:27017/")

# # 选择数据库
# db = client["mydatabase"]
# # 选择集合
# collection = db["mycollection"]
#
# sql = '''SELECT * FROM `web`.`pa`'''
# # sql = '''SELECT * FROM `web`.`pet_2`'''
#
# cursor.execute(sql)
# list_sum = []
# for i in cursor.fetchall():
#     ss = extract_emails(i[10])  # 9
#     if ss:
#         dic_list = {
#             'name': i[2],
#             'city': i[5],  # 国家
#             'typename': i[9],  # 类别
#             'platform': i[10],  # 联系方式
#             'url': i[-1],  # url
#         }
#         print(dic_list)
#         list_sum.append(dic_list)
# df = pd.DataFrame(list_sum)
# df.to_excel('output.xlsx', index=False)
# ll = list(ss)
# if len(ll) > 1:
#     for x in ll:
#         list_sum.append(x)
# if len(ll) == 1:
#     list_sum.append(ll[0])

# print(len(list_sum))
# print(list_sum)
# print(len(set(list_sum)))
# # DELETE FROM `web`.`pa` WHERE `id` = 2360
# # SELECT * FROM `web`.`pa` ORDER BY `title`
#
# # 定义要插入的数据
# mydict = {"name": "John", "address": "Highway 37" }
# for h in list_sum:
#
#     # # 插入数据
#     x = collection.insert_one(h)
#     #
#     # # 打印插入的数据的ID
#     print(x.inserted_id)

#
# df = pd.read_excel('宠物.xlsx')
# for  j in df:
#     print(j)