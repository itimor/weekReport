# -*- coding: utf-8 -*-
# author: itimor

from reports.models import WeekReport
from rest_framework import serializers
from users.models import Group

class WeekReportSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)
    group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='name')
    class Meta:
        model = WeekReport
        fields = ('url', 'title', 'content', 'owner', 'group', 'week_count', 'date')
        read_only_fields = ('group',)

    def get_owner(self, obj):
        return obj.owner.name