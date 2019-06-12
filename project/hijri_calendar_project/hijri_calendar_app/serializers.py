from rest_framework import serializers
from .models import DataFile, HijriCalendar


class DataFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataFile
        fields = ('url', 'file_name', 'file_type')


class HijriCalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HijriCalendar
        fields = ('url', 'date_value', 'lunar_day', 'lunar_month',
                  'lunar_year', 'day', 'month', 'year')
