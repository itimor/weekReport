# -*- coding: utf-8 -*-
# author: itimor

from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, GroupViewSet, RoleViewSet
from reports.views import WeekReportViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'reports', WeekReportViewSet)

