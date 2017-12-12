# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.cache import cache_page

import testdb, BiliBili, weatherInfo
from EDAS import searchedas, nodelist, nodeinfo, edasinfo
from dos import openfile1
from ticketsInfo import ticketsInfo

# @cache_page(60 * 15)
def index(request):
    return render(request,"index.html")

#api接口
@cache_page(60 * 15)
def searchApi(request):
    if request.method == 'GET':
        modules = request.GET.get("modules")
        deployName = request.GET.get("deployName")
        infos = json.dumps(searchedas(modules,deployName))
    return HttpResponse(infos, content_type='application/json; charset=utf-8')

#时间列表查询
# @cache_page(60 * 15)
def timeListApi(request):
    if request.method == 'GET':
        modules = request.GET.get("modules")
        appId = request.GET.get("appId")
        timelist = json.dumps(nodelist(modules,appId))
    return HttpResponse(timelist, content_type='application/json; charset=utf-8')

#自动化发布部署信息查询
@cache_page(60 * 15)
def deployListApi(request):
    if request.method == 'GET':
        modules = request.GET.get("modules")
        appId = request.GET.get("appId")
        deploylist = json.dumps(nodeinfo(modules,appId))
    return HttpResponse(deploylist, content_type='application/json; charset=utf-8')

#检查信息查询
def checkUrlApi(request):
    if request.method == 'GET':
        modules = request.GET.get("modules")
        appId = request.GET.get("appId")
        checkurl = json.dumps(edasinfo(modules,appId))
    return HttpResponse(checkurl, content_type='application/json; charset=utf-8')

#自动化发布部署（未完成）
def DeployApi(request):
    if request.method == 'GET':
        modules = request.GET.get("modules").encode('utf8')
        evn = request.GET.get("evn").encode('utf8')
        openfile1()
        deploy = []
    return HttpResponse(deploy, content_type='application/json; charset=utf-8')

#演唱会门票查询（爬虫）
@cache_page(60 * 60 * 24)
def ticketsInfoApi(request):
    if request.method == 'GET':
        info = ticketsInfo()
        info = json.dumps(info.get('pageData').get('resultData'))
    return HttpResponse(info, content_type='application/json; charset=utf-8')

#新浪实时热搜榜查询（MySQL查询）
@cache_page(60 * 120)
def sinaRankApi(request):
    if request.method == 'GET':
        sinaRank=testdb.sinaRankDB(request)
        sinaRank = json.dumps(sinaRank)
    return HttpResponse(sinaRank, content_type='application/json; charset=utf-8')

#b站新番时间表
@cache_page(60 * 60 * 24)
def bilibiliListApi(request):
    if request.method == 'GET':
        bilibiliList = BiliBili.bilibililist().get('result')
        bilibiliList = json.dumps(bilibiliList)
    return HttpResponse(bilibiliList, content_type='application/json; charset=utf-8')

#天气信息
@cache_page(60 * 15)
def weatherInfoApi(request):
    if request.method == 'GET':
        weatherinfo = weatherInfo.weatherInfo()
        weatherinfo = json.dumps(weatherinfo)
    return HttpResponse(weatherinfo, content_type='application/json; charset=utf-8')