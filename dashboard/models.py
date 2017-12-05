# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class sinaRank(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    rank = models.IntegerField()
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    rankNum = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

class biliBiliDate(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    date = models.CharField(max_length=255)
    date_ts = models.DateTimeField()
    day_of_week = models.IntegerField()
    is_today = models.IntegerField()

class biliBiliDetail(models.Model):
    pkid = models.CharField(max_length=128,primary_key=True)
    fkid = models.CharField(max_length=128)
    square_cover = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    pub_time = models.CharField(max_length=255)
    pub_index = models.CharField(max_length=255)