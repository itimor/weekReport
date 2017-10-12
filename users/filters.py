# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from users.models import User, Group

class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'id': ['gt'],
            'username': ['exact', 'contains'],
            'email': ['exact'],
            'name': ['exact'],
            'group__name': ['exact'],
            'is_active': ['exact'],
            'roles': ['exact'],
        }
