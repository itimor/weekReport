# -*- coding: utf-8 -*-
# author: itimor

from django.db.models import Q
from dry_rest_permissions.generics import DRYPermissionFiltersBase
from users.models import User

class ReportFilterBackend(DRYPermissionFiltersBase):
    def filter_list_queryset(self, request, queryset, view):
        try:
            userinfo = User.objects.get(username=request.user)
            role = userinfo.roles.name
            group = userinfo.group
            if role == 'admin':
                return queryset.all()
            elif role == 'groupadmin':
                return queryset.filter(Q(group=group))
            else:
                return queryset.filter(Q(owner=request.user))
        except:
            pass