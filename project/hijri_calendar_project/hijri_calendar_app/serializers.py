from rest_framework import serializers
from .models import DataFile, HijriCalendar


class DataFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataFile
        fields = ('url', 'file_name', 'file_type')


class HijriCalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HijriCalendar
        fields = ('url', 'date_value', 'day', 'month', 'year',
        'hijri_date_value', 'hijri_day', 'hijri_month', 'hijri_year')
