#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong

# 数据库操作
from django.http import HttpResponse

from dashboard.models import Test, sinaRank

#数据库操作测试
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

#新浪热搜榜查询（mysql数据库查询）
def sinaRankDB(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    #总条数
    count = sinaRank.objects.all().count()
    #总页面
    sumpage = count/50
    #传入的参数
    try:
        numlist = int(request.GET.get('num'))
    except ValueError as e:
        print '请输入数字!',e
        raise SystemExit
    for i in range(numlist-1, numlist):
        start = i*50
        end = i*50+50
        list =sinaRank.objects.all().order_by("-id")[start:end]
        result = []
        for var in list:
            name = var.name
            rank = var.rank
            rankNum = int(var.rankNum)
            url = var.url
            time = var.time
            response = {'name':name,'rank':rank,'rankNum':rankNum,'url':url,'time':str(time),'sumpage':sumpage}
            result.append(response)
    return result
