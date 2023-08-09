import re
import json


def go(html_json):
    """
            vermicelli = html_json['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText'] # 粉丝
            title_img = html_json['header']['c4TabbedHeaderRenderer']['avatar']['thumbnails'][-1]['url']  # 头像url
            banner_img = html_json['header']['c4TabbedHeaderRenderer']['tvBanner']['thumbnails'][-1]['url']  # 背景url
            video_data = html_json['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text']  # 视频数
            user_img = html_json['header']['c4TabbedHeaderRenderer']['channelHandleText']['runs'][-1]['text']  # 用户id
            user_text = html_json['metadata']['channelMetadataRenderer']['description']  # 简介
            country = html_json["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][7]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["channelAboutFullMetadataRenderer"]["country"] # 国家
            Number_of_views = html_json['contents']['twoColumnBrowseResultsRenderer']['tabs'][7]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['viewCountText']['simpleText'] # 观看次数
            Registration_time = html_json['contents']['twoColumnBrowseResultsRenderer']['tabs'][7]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['joinedDateText']['runs'][0]['text'] # 注册时间
            ping = html_json['contents']['twoColumnBrowseResultsRenderer']['tabs'][7]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['primaryLinks']
            """
    try:
        vermicelli = html_json['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText'].replace('subscribers','').strip()    # 粉丝
        if vermicelli[-1] == 'M':
            vermicelli = int(float(vermicelli.replace('M', '').strip()) * 1000000)
        elif vermicelli[-1] == 'K':
            vermicelli = int(float(vermicelli.replace('K', '').strip()) * 1000)
    except:
        vermicelli = 0

    try:
        title_img = html_json['header']['c4TabbedHeaderRenderer']['avatar']['thumbnails'][-1]['url']  # 头像url
    except:
        title_img = None

    try:
        banner_img = html_json['header']['c4TabbedHeaderRenderer']['tvBanner']['thumbnails'][-1]['url']  # 背景url
    except:
        banner_img = None

    try:
        video_data = html_json['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text']  # 视频数
    except:
        video_data = None

    try:
        user = html_json['header']['c4TabbedHeaderRenderer']['channelHandleText']['runs'][-1]['text']  # 用户id
    except:
        user = None

    try:
        user_text = html_json['metadata']['channelMetadataRenderer']['description']  # 简介
    except :
        user_text = None

    try:
        country = html_json["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][-2]["tabRenderer"]["content"][
            "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0][
            "channelAboutFullMetadataRenderer"]["country"]["simpleText"]  # 国家

    except:
        country = None

    try:
        Number_of_views = html_json['contents']['twoColumnBrowseResultsRenderer']['tabs'][-2]['tabRenderer']['content'][
            'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0][
            'channelAboutFullMetadataRenderer']['viewCountText']['simpleText'].replace('views','')  # 观看次数
    except:
        Number_of_views = None

    try:
        Registration_time = html_json['contents']['twoColumnBrowseResultsRenderer']['tabs'][-2]['tabRenderer']['content'][
                'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0][
                'channelAboutFullMetadataRenderer']['joinedDateText']['runs'][0]['text']  # 注册时间
    except:
        Registration_time = None

    try:
        ping = html_json['contents']['twoColumnBrowseResultsRenderer']['tabs'][-2]['tabRenderer']['content'][
            'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0][
            'channelAboutFullMetadataRenderer']['primaryLinks']
    except:
        ping = None
    try:
        name = html_json["header"]["c4TabbedHeaderRenderer"]["title"] # 名字
    except:
        name = None
    if ping:
        platform = {}  # 平台
        for k in ping:
            title = k['title']['simpleText']
            title_url = k['navigationEndpoint']['urlEndpoint']['url']
            pattern = r"(?<=q=)[^&]+"
            match = re.search(pattern, title_url)
            if match:
                result = match.group(0)
                result = result.replace("%3A", ":").replace("%2F", "/")
                platform[title] = result
            else:
                pass
    else:
        platform = {}  # 平台
    dic = {
        'platform': platform,
        'Registration_time': Registration_time,
        'Number_of_views': Number_of_views,
        'country': country,
        'user_text': user_text,
        'user': user,
        'banner_img': banner_img,
        'video_data': video_data,
        'title_img': title_img,
        'name': name,
        'vermicelli': vermicelli,
    }

    return dic


def go_re(response):
    re_html = re.compile('{"responseContext":.*?}}};</script>', re.S)
    html = re_html.findall(response.text)
    html_json = json.loads(html[0].replace(';</script>', ''))
    return html_json

def go_html_two(html_json):
    li_demo = []
    json_di = {}
    try:
        li = html_json["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][1]["tabRenderer"]["content"]["richGridRenderer"]["contents"]
        # print(i["richItemRenderer"]["content"]["videoRenderer"]["shortViewCountText"]["simpleText"])  # 播放次数
        # print(i["richItemRenderer"]["content"]["videoRenderer"]["thumbnail"]["thumbnails"][-1]["url"])  # 图片背景
        # print(i["richItemRenderer"]["content"]["videoRenderer"]["navigationEndpoint"]["commandMetadata"][
        #           "webCommandMetadata"]["url"])  # 视频url
        # print(i["richItemRenderer"]["content"]["videoRenderer"]["lengthText"]["simpleText"])  # 视频时常
        # print(i["richItemRenderer"]["content"]["videoRenderer"]["title"]["runs"][-1]["text"])  # 视频标题
        for i in li[:-1]:
            try:
                times_of_play = i["richItemRenderer"]["content"]["videoRenderer"]["shortViewCountText"]["simpleText"].replace('views','')
            except:
                times_of_play = "View count not available"  # 播放次数
            try:
                thumbnail_url = i["richItemRenderer"]["content"]["videoRenderer"]["thumbnail"]["thumbnails"][-1]["url"]
            except:
                thumbnail_url = "Thumbnail not available"    # 图片背景
            try:
                video_url = i["richItemRenderer"]["content"]["videoRenderer"]["navigationEndpoint"]["commandMetadata"][
                    "webCommandMetadata"]["url"]
            except:
                video_url = "Video url not available"    # 视频url
            try:
                video_length = i["richItemRenderer"]["content"]["videoRenderer"]["lengthText"]["simpleText"] # 视频时常
            except:
                video_length = "Video length not available"
            try:
                video_title = i["richItemRenderer"]["content"]["videoRenderer"]["title"]["runs"][-1]["text"]
            except:
                video_title = "Video title not available"  # 视频标题

            json_dic = {
                'times_of_play':times_of_play,
                'thumbnail_url':thumbnail_url,
                'video_url':video_url,
                'video_length':video_length,
                'video_title':video_title,
            }
            li_demo.append(json_dic)
        json_di['video'] = li_demo
        return json_di
    except:
        json_dic = {
            'times_of_play': '',
            'thumbnail_url': '',
            'video_url': '',
            'video_length': '',
            'video_title': '',
        }
        return json_dic




def str_2_bin(str):
    """
    字符串转换为二进制
    """
    return ' '.join([bin(ord(c)).replace('0b', '') for c in str])


def bin_2_str(bin):
    """
    二进制转换为字符串
    """
    return ''.join([chr(i) for i in [int(b, 2) for b in bin.split(' ')]])
