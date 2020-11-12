#coding=utf-8
import ast
import json
import socket
import time
import subprocess as sb
import requests
# 获取IP的方法，返回的是一个IP池
def proxy():
    time.sleep(1)
    # ip = sb.getoutput('curl ifconfig.me').split('\n')[-1]
    # ip= 'http://webapi.jghttp.golangapi.com/index/index/save_white?neek=30156&appkey=3321c1fe77c5af9525526f3c3eb808e0&white=' + ip
    # print(ip)
    # # 调用芝麻添加白名单的链接，添加即可
    # requests.get(ip)
    url="http://d.jghttp.golangapi.com/getip?num=10&type=1&pro=&city=0&yys=0&port=1&pack=32367&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
    #请求地址
    content = requests.get(url)
    print(content)
    poxys = []
    poxy = {}
    try:
        for ip in content.text.split():
            poxy = {
                'http': ip,
                'https': ip,
            }
            poxys.append(poxy)
        print(poxys)
        return poxys
    except Exception as err:
        print('代理失败'+str(err))


