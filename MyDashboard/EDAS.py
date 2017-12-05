#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import json
import urllib2
from selenium import webdriver
import time

import sys

uat_cookie = ''
dev_cookie = ''

def searchedas(modules,deployName):
    # 判定环境
    if modules == 'dev':
        cookie = dev_cookie
    elif modules == 'uat':
        cookie = uat_cookie
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie',cookie))
    f = opener.open('http://edas.console.shgtuat.com/json/queryAppList.json?action=AppAction&eventSubmitDoQuery=1&__preventCache=1508230422685'
                    '&appname=%s&currentPage=1&pageSize=10' % deployName)
    page = f.read()
    resluts = json.loads(page)
    reslut = resluts.get('data').get('result')
    nodeinfo = []
    for node in reslut:
        print node
        # print node.get('appId')
        # nodeinfo = {'appname':node.get('appname'),'appId':node.get('appId')}
        nodeinfo.append({'appname':node.get('appname').encode('utf8'),'appId':node.get('appId').encode('utf8'),'owner':node.get('owner').encode('utf8')})
    return nodeinfo

def edasinfo(modules,appid):
    # 判定环境
    if modules == 'dev':
        cookie = dev_cookie
    elif modules == 'test':
        cookie = uat_cookie
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie',cookie))
    f = opener.open('http://edas.console.shgtuat.com/json/app/queryAppStatusJson.htm?__preventCache1508230422685=&appId=%s&cid=0' % appid)
    page = f.read()
    resluts = json.loads(page)
    reslut = resluts.get('data')
    StatusList = reslut.get('ecuStatusList')
    status = []
    for index, list in enumerate(StatusList):
        name = reslut.get('warName').encode('utf-8').split('/')[-1].split('.')[0]
        state = list.get('state').encode('utf-8')
        status.append({'num':index+1,'name':name,'state':state})
        if state == 'DEPLOYING' :
            print '部署中'
        elif state == 'RUNNING':
            print '运行中'
        elif state == 'STOPPED':
            print '容器退出'
        elif state == 'APP_OFF':
            print '应用异常'
        elif state == 'STARTING':
            print '应用启动中'
        else:
            print '其他'
    return status

def nodeinfo(modules,appid):
    # 判定环境
    if modules == 'dev':
        cookie = dev_cookie
    elif modules == 'test':
        cookie = uat_cookie
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie',cookie))
    f = opener.open('http://edas.console.shgtuat.com/json/app/queryAppInfoJson.htm?__preventCache=1508287785414&appId=%s' % appid)
    page = f.read()
    resluts = json.loads(page)
    reslut = resluts.get('data')
    info = []
    info.append({'name':reslut.get('name'),'sum':reslut.get('instances'),'running':reslut.get('runnings')})
    status = []
    for state in reslut.get('ecus'):
        cpu = state.get('cpu')
        mem = state.get('mem')
        name = state.get('name')
        ip = state.get('ipAddr')
        states = state.get('state')
        running = state.get('running')
        status.append({'cpu':cpu,'mem':mem,'name':name,'ip':ip,'states':states,'running':running})
    return status

def nodelist(modules,appid):
    # 判定环境
    if modules == 'dev':
        cookie = dev_cookie
    elif modules == 'test':
        cookie = uat_cookie
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie',cookie))
    f = opener.open('http://edas.console.shgtuat.com/json/app/QueryAppDeployWarJson.htm?__preventCache=1510536258095&appId=%s' % appid)
    page = f.read()
    resluts = json.loads(page)
    reslut = resluts.get('data')
    timeList = []
    for index,reslut in enumerate(resluts.get('data')):
        creatTime = reslut.get('createTime')
        timeArray = time.localtime(float(creatTime/1000))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        timeList.append(otherStyleTime)
        print '发布时间为:' ,otherStyleTime
    return timeList

def Deploy(modules,deployName):
    if modules == 'dev':
        module = '10.70.64.48'
    elif modules == 'test':
        module = '10.70.95.102'
    url = 'http://'+module+':8080/xservices-deploy/standardRelease/toStandardRelease'
    #浏览器模拟点击发布
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element_by_id('username').send_keys('user')
    browser.find_element_by_id('password').send_keys('user')
    browser.find_element_by_id('submit').click()

    # deployName = 'yjyg-yjyg-ng'
    time.sleep(2)
    browser.find_elements_by_xpath('//*[@id="grid-pager"]/div[1]/div/table/thead/tr/th[2]/a[1]/span')[0].click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[3]/form/div[1]/input[1]').clear()
    browser.find_element_by_xpath('/html/body/div[3]/form/div[1]/input[1]').send_keys(deployName)
    browser.find_element_by_xpath('/html/body/div[3]/form/div[1]/div[2]/button[1]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="grid-pager"]/div[2]/table/tbody/tr').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="main-container"]/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="main-container"]/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    browser.close()     #关闭浏览器
    print '环境名：%s 模块名：%s 发布开始时间记录：'.decode('utf-8'),modules,deployName
    return 1

# info = searchedas('uat','seller')
# # print info
# id = info[0].get('appId')
# information = edasinfo('uat','fb8c23d6-0872-45f3-9a99-645e453c30ae')
# print information
# info = nodeinfo('test','02e8c15f-6fee-4a52-8312-b2fd71b86c60')
# print info
# Deploy('dev','yjyg-service-yy')