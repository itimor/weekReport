# -*- coding: utf-8 -*-
# author: itimor

from reports.models import WeekReport
from rest_framework import viewsets
from reports.serializers import WeekReportSerializer

class WeekReportViewSet(viewsets.ModelViewSet):
    queryset = WeekReport.objects.all().order_by('-date')
    serializer_class = WeekReportSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)