#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
#https://bangumi.bilibili.com/web_api/timeline_global
import json
import urllib2

def bilibililist():
    opener = urllib2.build_opener()
    f = opener.open('https://bangumi.bilibili.com/web_api/timeline_global')
    page = f.read()
    resluts = json.loads(page)
    return resluts

# bilibililist()
