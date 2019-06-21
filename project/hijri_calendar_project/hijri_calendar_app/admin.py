from django.contrib import admin

from .models import (DataFile, HolidayOriginList,
                     HolidayCountryList, HolidayAliasList,
                     HolidayRegionList,
                     Holiday, HijriCalendar)

# Register your models here.
admin.site.register(DataFile)
admin.site.register(HolidayOriginList)
admin.site.register(HolidayCountryList)
admin.site.register(HolidayAliasList)
admin.site.register(HolidayRegionList)
# admin.site.register(Holiday)


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('holiday_name',
                    'day', 'month',
                    'hijri_day', 'hijri_month',
                    'is_official', 'is_birthday',
                    'is_religious', 'is_cultural'
                    )
    list_filter = ('month', 'is_official', 'is_birthday',
                   'is_religious', 'is_cultural')
    search_fields = ('holiday_name', 'day', 'month')
    ordering = ('holiday_name',)
    list_per_page = 30
    # fields = ('data_file',
    #           ('day', 'month', 'year'),
    #           'date_value',
    #           ('hijri_day', 'hijri_month', 'hijri_year'),
    #           'hijri_date_value',
    #           'is_holiday', 'holiday_list',)
    save_on_top = True


@admin.register(HijriCalendar)
class HijriCalendarAdmin(admin.ModelAdmin):
    list_display = ('date_value',
                    'hijri_date_value',
                    'day', 'month', 'year',
                    'hijri_day', 'hijri_month',
                    'hijri_year', 'is_holiday')
    list_filter = ('data_file', 'date_value', 'year', 'hijri_year',
                   'is_holiday')
    search_fields = ('date_value', 'hijri_date_value',
                     'month_name', 'hijri_month_name')
    date_hierarchy = 'date_value'
    ordering = ('date_value',)
    list_per_page = 30
    readonly_fields = ('date_value', 'hijri_date_value',)
    fields = ('data_file',
              ('day', 'month', 'year'),
              'date_value',
              ('hijri_day', 'hijri_month', 'hijri_year'),
              'hijri_date_value',
              'is_holiday', 'holiday_list',)
    save_on_top = True
    # prepopulated_fields = {'hijri_month_name': ('hijri_month',)}
