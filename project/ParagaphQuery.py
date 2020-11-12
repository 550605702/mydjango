import random
import time
import urllib
from bs4 import BeautifulSoup  # 处理抓到的页面
import sys
import requests
import re
import importlib
import uuid
importlib.reload(sys)  # 编码转换，python3默认utf-8,一般不用加

# 伪造请求cookis
def get_uuid():
    return str(uuid.uuid4())
cookie = "JSESSIONID=" + get_uuid() + ";" \
                                      "user_trace_token=" + get_uuid() + "; LGUID=" + get_uuid() + "; index_location_city=%E6%88%90%E9%83%BD; " \
                                                                                                   "SEARCH_ID=" + get_uuid() + '; _gid=GA1.2.717841549.1514043316; ' \
                                                                                                                               '_ga=GA1.2.952298646.1514043316; ' \
                                                                                                                               'LGSID=' + get_uuid() + "; "                                                                                                                                                      "LGRID=" + get_uuid() + "; "
# 伪造请求头
headers = {
    # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'cache-control': 'max-age=0',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400",
    "Cookie": cookie
}

def query(wd,proxy):
    proxys = proxy
    key = {"wd": wd}
    data = urllib.parse.urlencode(key)  # 对关键字进行url编码
    base_url = "https://www.baidu.com/s?"  # 搜索网页的默认url
    url = base_url + data  # 拼接得到真实的url
    urls = base_url + "wd="+wd
    requests.urllib3.disable_warnings()
    try:
        content = requests.get(url, headers=headers, proxies=random.choice(proxys), verify=False)

        if content.status_code == 200:
            pass
    except Exception as err:
        try:
            content = requests.get(url, headers=headers, proxies=random.choice(proxys), verify=False)
        except Exception as err:
            print("代理失败" + str(err))
            content = requests.get(url, headers=headers, verify=False)


    content.encoding = 'utf-8'#解决中文乱码
    if content.status_code==200:
        data={}
        bsobj = BeautifulSoup(content.text, features="html.parser")
        # 获取搜索结果队列s
        tel =bsobj.find_all("title")[0].next
        data['dl'] = wd
        data['lj'] = urls
        print(tel)
        if tel =="百度安全验证": #如果遇到验证判断
            print("百度验证")
            data['cfd'] = "查重失败"
            return data

        search_results = bsobj.find_all('div', {'class': 'result c-container new-pmd'})
        redtext = ""
        sum = 0
        # 对于每一个搜索结果
        for item in search_results:
            # 获取每个搜索结果的标题的所有文本
            text = item.h3.a.get_text(strip=True)
            # 获取每个搜索结果的摘要内容中的标红关键字
            keywords = item.div.find_all('em')
            sumred =len(keywords)
            if(sumred>sum):
                sum= sumred
                redtext = ""
                for em in keywords:
                    redtext = redtext+em.next

        cfd = "%.2f%%" % (len(redtext) / len(wd) * 100)
        # print(cfd)
        data['cfd'] = cfd
        return data
    else:
        print("获取失败")