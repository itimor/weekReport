# -*- coding: utf-8 -*-
# author: itimor

from reports.models import WeekReport
from rest_framework import viewsets
from reports.serializers import WeekReportSerializer
# from permission.permissions import IsAdmin
# from permission.filters import ReportPermissionFilterBackend

class WeekReportViewSet(viewsets.ModelViewSet):
    queryset = WeekReport.objects.all().order_by('-date')
    serializer_class = WeekReportSerializer
    # filter_backends = (ReportPermissionFilterBackend,)
    # permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)