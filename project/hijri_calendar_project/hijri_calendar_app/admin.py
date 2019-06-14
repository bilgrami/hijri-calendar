from django.contrib import admin

# Register your models here.
from .models import DataFile, HijriCalendar

admin.site.register(DataFile)
# admin.site.register(HijriCalendar)


@admin.register(HijriCalendar)
class HijriCalendarAdmin(admin.ModelAdmin):
    list_display = ('date_value',
                    'hijri_date_value',
                    'day', 'hijri_day',
                    'month', 'hijri_month',
                    'year', 'hijri_year')
    list_filter = ('data_file', 'date_value', 'year', 'hijri_year',
                   'hijri_month')
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
              'hijri_date_value',)
    save_on_top = True
    # prepopulated_fields = {'hijri_month_name': ('hijri_month',)}
