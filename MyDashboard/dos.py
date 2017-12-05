#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import os


def openfile1():
    cmd = 'explorer.exe   D:\\test.bat'
    result = os.system(cmd)
    # print cmd.encode('utf8')
    return result
# openfile1()