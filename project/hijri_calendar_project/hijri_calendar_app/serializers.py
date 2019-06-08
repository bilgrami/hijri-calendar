from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import DataFile, HijriCalendar

class DataFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataFile
        fields = ('url', 'FileName', 'FileType')


class HijriCalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HijriCalendar
        fields = ('url', 'dateValue', 'lunarDay', 'lunarMonth', 'lunarYear', 'day', 'month', 'year')
        