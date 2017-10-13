# -*- coding: utf-8 -*-
# author: itimor

from django.db.models import Q
from dry_rest_permissions.generics import DRYPermissionFiltersBase
from users.models import User
from django.shortcuts import get_object_or_404

class ReportFilterBackend(DRYPermissionFiltersBase):
    def filter_list_queryset(self, request, queryset, view):
        userinfo = get_object_or_404(User, username=request.user)
        role = userinfo.roles.name
        group = userinfo.group
        if request.user == 'admin' or role == 'admin':
            return queryset.all()
        elif role == 'groupadmin':
            return queryset.filter(Q(group=group))
        else:
            return queryset.filter(Q(owner=request.user))
