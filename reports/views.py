# -*- coding: utf-8 -*-
# author: itimor

from reports.models import WeekReport
from rest_framework import viewsets
from reports.serializers import WeekReportSerializer
from users.models import User

class WeekReportViewSet(viewsets.ModelViewSet):
    queryset = WeekReport.objects.all().order_by('-date')
    serializer_class = WeekReportSerializer

    def perform_create(self, serializer):
        userinfo = User.objects.get(username=self.request.user)
        serializer.save(owner=self.request.user, group=userinfo.group)