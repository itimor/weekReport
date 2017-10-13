# -*- coding: utf-8 -*-
# author: itimor

from reports.models import WeekReport
from rest_framework import serializers

class WeekReportSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = WeekReport
        fields = ('url', 'title', 'content', 'owner', 'week_count', 'date')

    def get_owner(self, obj):
        return obj.owner.name