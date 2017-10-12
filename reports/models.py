# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from users.models import User
from reports.weekformat import *

COUNT = get_week_count()

class WeekReport(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'周报标题', blank=True)
    content = models.TextField(verbose_name=u'周报内容')
    owner = models.ForeignKey(User, default='', verbose_name=u'所有者')
    week_count = models.IntegerField(default=COUNT, verbose_name=u'周次')
    date = models.DateField(auto_now_add=True, verbose_name=u'周报生成日期')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '周报'
        verbose_name_plural = '周报'

    def save(self, *args, **kwargs):
        # 设置周报标题和周次
        self.title = "第" + str(self.week_count) + "周(" + str(get_this_monday()) + "至" + str(get_this_sunday()) + ")周报"
        super(WeekReport, self).save()