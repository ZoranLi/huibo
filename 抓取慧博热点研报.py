import requests
import json
from datetime import datetime
from urllib.parse import quote

from wechat_ftqq import sendWechat

# -*- coding: utf-8 -*-
__author__ = "zoranlee"


def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典对象
    {
        "Host": "mp.weixin.qq.com",
        "Connection": "keep-alive",
        "Cache-Control":"max-age="
    }
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


# 提取数据内容
def extract_data(html_content):
    """
       从html页面中提取历史文章数据
       :param html_content 页面源代码
       :return: 历史文章列表
       """
    import re
    import html
    import json
    # rex = "data = '({.*?})'"
    rex = "data=({.*?\n)"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        # 按换行符
        data = data[:-2]
        data = json.loads(data)
        articles = data.get("appmsg_list")
        for item in articles:
            print(item)
        return articles


def detail(range, id):
    url = "http://mp.hibor.com.cn/MobilePhone/DocDetailHandler.ashx?systype=android&btype=2&username=yTmUqTfY3XmV6XhWrQnMmN&id={}&ver=341".format(
        id)
    headers = """
accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
cookie:devicetype=iOS13.6.1; lang=zh_CN; pass_ticket=Gd7oyTKM6dlbkNgUH3qtICelGKGOz2qQ8S56kql/hvSnK5zySYhIP2UsniJPiTox; version=17001127; wap_sid2=CMnySxKKAXlfSExGa0RyaWE2N1YwX1J6dVM3RzFyWlgxNTJOSDNNYmN5Vk5OYXlxeE1CQU1TQ0UwdlJYeDhveWp4WXdQaUdxcW93VGl0ZnlxRElCcVVEaWllcTBxQS1OZVRGWjNhYWNiT3hIaWRPUzQ4cmpjaV9xamFyQW4tb2RodEFoZ29Tc0dxeGtTQUFBfjD0z7n8BTgMQJRO; wxuin=1243465; pgv_pvid=8943368020; sd_cookie_crttime=1602647434777; sd_userid=11881602647434777
x-wechat-key:b810338f9a1f3ac1a0660c632747bb59746731efabb4ce0b806447887cbc7756b34ea5bcac9ec4d6997d126e2ca9699ed47833ccef620744268bf4ae77cfa7dddc2c2fb6742daa52023a41e43cf9040f68ca2f9b8da9a27eb543d706845b38fe7f9f7a46390c3d4c3728feef6a681d853512747c1269612a7acf634dd17351bb
x-wechat-uin:MTI0MzQ2NQ%3D%3D
user-agent:Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001127) NetType/WIFI Language/zh_CN
accept-language:zh-cn
accept-encoding:gzip, deflate, br
"""

    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    json_str = json.loads(response.text)
    print(json_str['data']['codenamestr'])
    # 将抓取到的数据写成网页
    currentDate = datetime.today().strftime('%Y-%m-%d')

    if (range == "day"):
        range = "天"
    elif (range == "week"):
        range = "周"
    elif (range == "month"):
        range = "月"

    with open("time/{}热点研报{}.txt".format(currentDate, range), "a", encoding="utf-8") as f:
        f.write(json_str['data']['id'] + ' ')
        f.write(json_str['data']['title'])
        f.write('\n')
        f.write(json_str['data']['codenamestr'])
        f.write('\n')
        f.write('\n')


def detailSort(range, id):
    url = "http://mp.hibor.com.cn/MobilePhone/DocDetailHandler.ashx?systype=android&btype=2&username=yTmUqTfY3XmV6XhWrQnMmN&id={}&ver=341".format(
        id)
    headers = """
accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
cookie:devicetype=iOS13.6.1; lang=zh_CN; pass_ticket=Gd7oyTKM6dlbkNgUH3qtICelGKGOz2qQ8S56kql/hvSnK5zySYhIP2UsniJPiTox; version=17001127; wap_sid2=CMnySxKKAXlfSExGa0RyaWE2N1YwX1J6dVM3RzFyWlgxNTJOSDNNYmN5Vk5OYXlxeE1CQU1TQ0UwdlJYeDhveWp4WXdQaUdxcW93VGl0ZnlxRElCcVVEaWllcTBxQS1OZVRGWjNhYWNiT3hIaWRPUzQ4cmpjaV9xamFyQW4tb2RodEFoZ29Tc0dxeGtTQUFBfjD0z7n8BTgMQJRO; wxuin=1243465; pgv_pvid=8943368020; sd_cookie_crttime=1602647434777; sd_userid=11881602647434777
x-wechat-key:b810338f9a1f3ac1a0660c632747bb59746731efabb4ce0b806447887cbc7756b34ea5bcac9ec4d6997d126e2ca9699ed47833ccef620744268bf4ae77cfa7dddc2c2fb6742daa52023a41e43cf9040f68ca2f9b8da9a27eb543d706845b38fe7f9f7a46390c3d4c3728feef6a681d853512747c1269612a7acf634dd17351bb
x-wechat-uin:MTI0MzQ2NQ%3D%3D
user-agent:Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001127) NetType/WIFI Language/zh_CN
accept-language:zh-cn
accept-encoding:gzip, deflate, br
"""

    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    json_str = json.loads(response.text)
    print(json_str['data']['codenamestr'])
    # 将抓取到的数据写成网页
    currentDate = datetime.today().strftime('%Y-%m-%d')

    if (range == "day"):
        range = "天"
    elif (range == "week"):
        range = "周"
    elif (range == "month"):
        range = "月"

    with open("score/80-100评分研报股票{}.txt".format(range), "a", encoding="utf-8") as f:
        f.write(json_str['data']['id'] + ' ')
        f.write(json_str['data']['title'])
        f.write('\n')
        f.write(json_str['data']['codenamestr'])
        f.write('\n')
        f.write('\n')



# 抓取评80-100分研报 count 是抓取的条数 20、60、100 time 1是周 2是月
def crawlSort(count,time):
    url = "http://mp.hibor.com.cn/MobilePhone/GetJsonHandler.ashx?btype=33&systype=android&count={}&page=1&stype=0&time={}&argfen=80-100&username=yTmUqTfY3XmV6XhWrQnMmN".format(
        count,time)
    headers = """
accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
cookie:devicetype=iOS13.6.1; lang=zh_CN; pass_ticket=Gd7oyTKM6dlbkNgUH3qtICelGKGOz2qQ8S56kql/hvSnK5zySYhIP2UsniJPiTox; version=17001127; wap_sid2=CMnySxKKAXlfSExGa0RyaWE2N1YwX1J6dVM3RzFyWlgxNTJOSDNNYmN5Vk5OYXlxeE1CQU1TQ0UwdlJYeDhveWp4WXdQaUdxcW93VGl0ZnlxRElCcVVEaWllcTBxQS1OZVRGWjNhYWNiT3hIaWRPUzQ4cmpjaV9xamFyQW4tb2RodEFoZ29Tc0dxeGtTQUFBfjD0z7n8BTgMQJRO; wxuin=1243465; pgv_pvid=8943368020; sd_cookie_crttime=1602647434777; sd_userid=11881602647434777
x-wechat-key:b810338f9a1f3ac1a0660c632747bb59746731efabb4ce0b806447887cbc7756b34ea5bcac9ec4d6997d126e2ca9699ed47833ccef620744268bf4ae77cfa7dddc2c2fb6742daa52023a41e43cf9040f68ca2f9b8da9a27eb543d706845b38fe7f9f7a46390c3d4c3728feef6a681d853512747c1269612a7acf634dd17351bb
x-wechat-uin:MTI0MzQ2NQ%3D%3D
user-agent:Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001127) NetType/WIFI Language/zh_CN
accept-language:zh-cn
accept-encoding:gzip, deflate, br
"""

    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    # print(response.text)
    # 将抓取到的数据写成网页

    json_str = json.loads(response.text)
    list = json_str['data']['list']
    length = len(list)
    for item in list:
        # detail(range=range, id=item['id'])
        print(item['id'])
        print(item['DocTitle'])
        print(item['DocUploadTime'])
        print(item['grade'])
        if time is 1:
            category = '周'
        if time is 2:
            category = '月'

        with open("score/80-100评分研报【{}】.txt".format(category), "a", encoding="utf-8") as f:
            f.write(item['DocUploadTime'] + ' ')
            f.write(item['DocTitle'] + ' ')
            f.write(item['grade'] + ' ')
            f.write('\n')
        detailSort(range='day', id=item['id'])
    # sendWechat(sc_key='SCU120489T53a231e65dfeb970d00b789861acf7bc5f9640f1456d9', text='一周热点研报', desp='dddd')





def crawl(range):
    url = "http://mp.hibor.com.cn/MobilePhone/GetJsonHandler.ashx?systype=android&btype=2&count=50&time=2999-01-01%2000%3A00%3A00&stype=0&uord=up&username=yTmUqTfY3XmV6XhWrQnMmN&range={}".format(
        range)
    headers = """
accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
cookie:devicetype=iOS13.6.1; lang=zh_CN; pass_ticket=Gd7oyTKM6dlbkNgUH3qtICelGKGOz2qQ8S56kql/hvSnK5zySYhIP2UsniJPiTox; version=17001127; wap_sid2=CMnySxKKAXlfSExGa0RyaWE2N1YwX1J6dVM3RzFyWlgxNTJOSDNNYmN5Vk5OYXlxeE1CQU1TQ0UwdlJYeDhveWp4WXdQaUdxcW93VGl0ZnlxRElCcVVEaWllcTBxQS1OZVRGWjNhYWNiT3hIaWRPUzQ4cmpjaV9xamFyQW4tb2RodEFoZ29Tc0dxeGtTQUFBfjD0z7n8BTgMQJRO; wxuin=1243465; pgv_pvid=8943368020; sd_cookie_crttime=1602647434777; sd_userid=11881602647434777
x-wechat-key:b810338f9a1f3ac1a0660c632747bb59746731efabb4ce0b806447887cbc7756b34ea5bcac9ec4d6997d126e2ca9699ed47833ccef620744268bf4ae77cfa7dddc2c2fb6742daa52023a41e43cf9040f68ca2f9b8da9a27eb543d706845b38fe7f9f7a46390c3d4c3728feef6a681d853512747c1269612a7acf634dd17351bb
x-wechat-uin:MTI0MzQ2NQ%3D%3D
user-agent:Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001127) NetType/WIFI Language/zh_CN
accept-language:zh-cn
accept-encoding:gzip, deflate, br
"""

    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    # print(response.text)
    # 将抓取到的数据写成网页

    json_str = json.loads(response.text)
    list = json_str['data']['list']
    length = len(list)
    for item in list:
        detail(range=range, id=item['id'])
        # print(item['id'])
        # print(item['title'])

    # sendWechat(sc_key='SCU120489T53a231e65dfeb970d00b789861acf7bc5f9640f1456d9', text='一周热点研报', desp='dddd')


# 根据关键字查询
# http://mp.hibor.com.cn/MobilePhone/SelectJsonHandler.ashx?systype=android&x=1&btype=1&stype=0&count=20&page=1&reportrange=1&keyword=%E6%96%B0&timerange=5&username=yTmUqTfY3XmV6XhWrQnMmN
def crawlKeywords(words):
    originWords = words
    words = quote(words, 'utf-8')
    url = "http://mp.hibor.com.cn/MobilePhone/SelectJsonHandler.ashx?systype=android&x=1&btype=1&stype=0&count=20&page=1&reportrange=1&keyword={}&timerange=5&username=yTmUqTfY3XmV6XhWrQnMmN".format(
        words)
    headers = """
accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
cookie:devicetype=iOS13.6.1; lang=zh_CN; pass_ticket=Gd7oyTKM6dlbkNgUH3qtICelGKGOz2qQ8S56kql/hvSnK5zySYhIP2UsniJPiTox; version=17001127; wap_sid2=CMnySxKKAXlfSExGa0RyaWE2N1YwX1J6dVM3RzFyWlgxNTJOSDNNYmN5Vk5OYXlxeE1CQU1TQ0UwdlJYeDhveWp4WXdQaUdxcW93VGl0ZnlxRElCcVVEaWllcTBxQS1OZVRGWjNhYWNiT3hIaWRPUzQ4cmpjaV9xamFyQW4tb2RodEFoZ29Tc0dxeGtTQUFBfjD0z7n8BTgMQJRO; wxuin=1243465; pgv_pvid=8943368020; sd_cookie_crttime=1602647434777; sd_userid=11881602647434777
x-wechat-key:b810338f9a1f3ac1a0660c632747bb59746731efabb4ce0b806447887cbc7756b34ea5bcac9ec4d6997d126e2ca9699ed47833ccef620744268bf4ae77cfa7dddc2c2fb6742daa52023a41e43cf9040f68ca2f9b8da9a27eb543d706845b38fe7f9f7a46390c3d4c3728feef6a681d853512747c1269612a7acf634dd17351bb
x-wechat-uin:MTI0MzQ2NQ%3D%3D
user-agent:Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001127) NetType/WIFI Language/zh_CN
accept-language:zh-cn
accept-encoding:gzip, deflate, br
"""

    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    # print(response.text)
    # 将抓取到的数据写成网页

    json_str = json.loads(response.text)
    list = json_str['data']['list']
    print(list)
    for item in list:
        with open("keywords/【{}】.txt".format(originWords), "a", encoding="utf-8") as f:
            f.write(item['grade'] + ' ')
            f.write(item['time'] + ' ')
            f.write(item['title'] + ' ')
            f.write(item['type'] + ' ')
            f.write(item['id'] + ' ')
            f.write('\n')
    print('写入完毕')


if __name__ == '__main__':
    # 天
    # crawl(range='day')
    # 周
    # crawl(range='week')
    # 月
    # crawl(range='month')

    # detail(id=3071561);
    # crawlKeywords("合盛硅业")

    crawlSort(120,1)
