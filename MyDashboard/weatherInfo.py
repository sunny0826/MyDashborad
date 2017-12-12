#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import json
import urllib2

# 上海天气
def weatherInfo():
    opener = urllib2.build_opener()
    f = opener.open('http://tj.nineton.cn/Heart/index/all?city=CHSH000000')
    page = f.read()
    resluts = json.loads(page)
    return resluts

# weatherInfo()