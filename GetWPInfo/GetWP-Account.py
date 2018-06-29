#!/usr/bin/env python
# encoding: utf-8
# wp_get_auth.py
# author: persuit

import requests
import sys
import os
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive'
}


def getAuthor():
    # url = 'http://60.251.255.145/'
    url = 'http://www.yebaochen.com/'
    for i in range(1, 50):

        geturl = url + "?author={}".format(i)
        print (geturl)

        try:
            global res
            res = requests.get(geturl, headers=headers, verify=False, timeout=10).content
        except Exception as e:
            print (str(e))

        p = re.compile(r'<body class="archive author author-(.+?) author-')
        matchs = []
        try:
            matchs = p.findall(res.decode())
        except UnicodeDecodeError:
            matchs = p.findall(res)

        for auth in matchs:
            fp = open('auth.txt', 'a')
            fp.write(auth + '\n')
            fp.close()


if __name__ == '__main__':
    getAuthor()