# -*- coding: utf-8 -*-
# author: itimor

from django.db import models
from users.models import User, Group
from reports.weekformat import *

COUNT = get_week_count()

class WeekReport(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'周报标题', blank=True)
    content = models.TextField(verbose_name=u'周报内容')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'所有者')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'所在部门')
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

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        userinfo = User.objects.get(username=request.user)
        role = userinfo.roles.name
        if request.user == self.owner or role == 'admin' or role == 'groupadmin':
            return True

    @staticmethod
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return False

    @staticmethod
    def has_publish_permission(request):
        return True

    def has_object_update_permission(self, request):
        return request.user == self.owner

    @staticmethod
    def has_publish_permission(request):
        return True

    def has_object_publish_permission(self, request):
        return request.user == self.owner