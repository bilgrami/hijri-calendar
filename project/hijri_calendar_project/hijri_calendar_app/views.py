from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import HijriCalendar
from datetime import date
from helpers import cache_helper as ch


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


# Add this view
class HolidayPageView(TemplateView):

    @staticmethod
    def cache_key_prefix():
        return 'holiday-list:views'

    def get(self, request, **kwargs):
        self.cache = ch.CacheHelper(key_prefix=self.cache_key_prefix())
        m = HijriCalendar.holiday_calendar.all()
        holiday_calendars = m.filter(date_value__gte=date.today())  \
                             .order_by('date_value')
        data = 'Note: Holidays earlier than today are not displayed'
        key = ''
        total_views = self.cache.increment(key)
        return render(request, 'hijri_calendar_app/holiday.html',
                               {'holiday_calendars': holiday_calendars,
                                'data': data,
                                'cache_key': self.cache.get_key(key),
                                'cache_timeout': self.cache.get_timeout(),
                                'total_views': total_views})


class CalendarDetailPageView(TemplateView):

    @staticmethod
    def cache_key_prefix():
        return 'calendar-date'

    def get(self, request, date_value, **kwargs):
        self.cache = ch.CacheHelper(key_prefix=self.cache_key_prefix())
        data = get_object_or_404(HijriCalendar,
                                 date_value=date_value)
        key = f'{str(date_value)}:views'
        total_views = self.cache.increment(key=key)
        return render(request, 'hijri_calendar_app/calendar_detail.html',
                               {'data': data,
                                'cache_key': self.cache.get_key(key=key),
                                'cache_timeout': self.cache.get_timeout(),
                                'total_views': total_views})
