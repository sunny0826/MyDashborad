#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import json
import urllib
import urllib2


def ticketsInfo():
    url = 'https://search.damai.cn/searchajax.html'
    textmod = {'keyword': '陈奕迅周杰伦五月天', 'cty': '上海','ctl':'','tn':'','sctl':'','singleChar':'','order':''}
    textmod = urllib.urlencode(textmod)     #将参数格式化
    req = urllib2.Request(url=url, data=textmod)
    res = urllib2.urlopen(req)
    res = res.read()
    info = json.loads(res)
    return  info
    # info = info.get('pageData').get('resultData')
    # leninfo = len(info)
    # for port in info:
    #     name = port.get('nameNoHtml')
    #     price = port.get('pricestr')
    #     venue = port.get('venue')
    #     # star = port.get('actors')
    #     stars = ''
    #     for starname in port.get('starname'):
    #         # stars.append(starname.decode('utf8'))
    #         stars += starname+' '
    #     print '名称：%s' % name
    #     print '价格：%s' % price
    #     print '场馆：%s' % venue
    #     # print star
    #     print '艺人：%s' % stars
    #     print '-----------------------'
    # print info
