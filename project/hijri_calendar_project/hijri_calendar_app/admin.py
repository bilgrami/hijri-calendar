from django.contrib import admin

from .models import (DataFile, HolidayOriginList,
                     HolidayCountryList, HolidayAliasList,
                     Holiday, HijriCalendar)

# Register your models here.
admin.site.register(DataFile)
admin.site.register(HolidayOriginList)
admin.site.register(HolidayCountryList)
admin.site.register(HolidayAliasList)
admin.site.register(Holiday)


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
