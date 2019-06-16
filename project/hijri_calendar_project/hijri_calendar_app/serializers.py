from rest_framework import serializers

from .models import (DataFile, HijriCalendar, Holiday,
                     HolidayAliasList, HolidayCountryList, HolidayOriginList)


class DataFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataFile
        fields = ('url', 'file_name', 'file_type')


class HolidayAliasListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HolidayAliasList
        fields = ('name',)


class HolidayCountryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HolidayCountryList
        # fields = ('url', 'name')
        fields = ('name',)


class HolidayOriginListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HolidayOriginList
        fields = ('name',)


class HolidaySerializer(serializers.HyperlinkedModelSerializer):
    cultural_origin = HolidayOriginListSerializer(source="origin",
                                                  read_only=True)
    alias = HolidayAliasListSerializer(source='alias_names',
                                       read_only=True, many=True)
    country_origin = HolidayCountryListSerializer(source='country',
                                                  read_only=True, many=True)

    class Meta:
        model = Holiday
        fields = ('url', 'holiday_name', 'description', 'day', 'month',
                  'hijri_day', 'hijri_month', 'cultural_origin',
                  'alias', 'country_origin', 'holiday_dates')


class HijriCalendarSerializer(serializers.HyperlinkedModelSerializer):
    holiday = HolidaySerializer(source="holiday_list", read_only=True,
                                many=True)

    class Meta:
        model = HijriCalendar
        fields = ('url', 'date_value', 'day', 'month', 'year',
                  'hijri_date_value', 'hijri_day', 'hijri_month',
                  'hijri_month_name', 'hijri_year',
                  'is_holiday', 'holiday')
