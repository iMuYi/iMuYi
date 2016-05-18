#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LoveNight
# @Date:   2015-11-16 20:45:59
# @Last Modified by:   LoveNight
# @Last Modified time: 2015-11-18 18:07:19
import os
import sys
import json
from bs4 import BeautifulSoup as BS
import requests
import msvcrt

"""

"""


url = 'http://data.zz.baidu.com/urls?site=imuyi.me&token=5cx7rmr2CPXmAFmJ'
baidu_sitemap = os.path.join(sys.path[0], 'public', 'baidusitemap.xml')
google_sitemap = os.path.join(sys.path[0], 'public', 'sitemap.xml')
sitemap = [baidu_sitemap, google_sitemap]

print (os.path.exists(baidu_sitemap) or os.path.exists(
    google_sitemap))



def getUrls():
    urls = []
    for _ in sitemap:
        if os.path.exists(_):
            with open(_, "r") as f:
                xml = f.read()
            soup = BS(xml, "xml")
            tags = soup.find_all("loc")
            urls += [x.string for x in tags]
            if _ == baidu_sitemap:
                tags = soup.find_all("breadCrumb", url=True)
                urls += [x["url"] for x in tags]
    return urls


def postUrls(urls):
    urls = set(urls)  
    print("there are %s urls" % len(urls))
    data = "\n".join(urls)
    return requests.post(url, data=data).text


if __name__ == '__main__':

    urls = getUrls()
    result = postUrls(urls)
    print("results：")
    print(result)
    msvcrt.getch()
