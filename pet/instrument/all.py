import datetime
import os
import re
import pandas as pd


def time_strftime(mytable='mytable_'):
    """生成今天日期

    :param mytable : 自定义名称 (默认值: mytable_)
    :return: mytable_2023_06_07
    """
    today = datetime.date.today()
    today_str = today.strftime('%Y-%m-%d')
    table_name = str(mytable) + today_str.replace('-', '_')
    return table_name


def find_text(data, username='username'):
    """递归查找字典或列表中的所有 'username' 值

    :param data :字典或者列表
    :param username: 查找的字典键 (默认值: username)
    :return: 返回所有 ’username‘
    """

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (str, int, float)):
                continue
            elif isinstance(value, dict):
                if username in value:
                    yield value[username]
                else:
                    yield from find_text(value)
            elif isinstance(value, list):
                for item in value:
                    yield from find_text(item)
            else:
                continue
    elif isinstance(data, list):
        for item in data:
            yield from find_text(item)
    else:
        return


def text_encode_unicode_escape(text):
    """unicode_escape 转utf-8

    :param text :文本
    :return: 文本
    """
    encoded_str = str(text).encode('unicode_escape')
    decoded_str = bytes(encoded_str).decode('unicode_escape')
    decoded_str = bytes(decoded_str, 'utf-8').decode('unicode_escape')
    return decoded_str


def emails_extract(text):
    """传入文本，洗出邮箱

    :param text :文本
    :return: set
    """

    def validate_email(email):
        demo_1 = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # 匹配电子邮件的正则表达式模式
        return bool(re.match(demo_1, email))

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    emails = re.findall(pattern, text)
    valid_emails = {email for email in emails if validate_email(email)}
    return valid_emails


def excel_open(excel_demo):
    """传入excel，列表套字典
       :param excel_demo :excel路径
       :return: 返回列表字典 [{},{}]
       """
    df = pd.read_excel(excel_demo)
    data = df.to_dict(orient='records')
    return data


def excel_close(excel_demo):
    """传列表字典
    :param excel_demo :数据  [{},{}]
    :return:
    """
    df = pd.DataFrame(excel_demo)
    # 将数据框写入新的 Excel 文件
    df.to_excel('output.xlsx', index=False)


def os_mkdir(folder_name='demo'):
    """创建文件夹
    :param folder_name :文件夹名字
    :return:
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        # print(f'Folder "{folder_name}" created successfully.')
    else:
        # print(f'Folder "{folder_name}" already exists.')
        pass


if __name__ == '__main__':
    a = 874
    print(int(a/40))
