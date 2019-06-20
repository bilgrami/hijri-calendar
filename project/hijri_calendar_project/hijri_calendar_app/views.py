from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import HijriCalendar
from datetime import date
import redis
from django.conf import settings
# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


# Add this view
class HolidayPageView(TemplateView):
    def get(self, request, **kwargs):
        m = HijriCalendar.holiday_calendar.all()
        holiday_calendars = m.filter(date_value__gte=date.today())  \
                             .order_by('date_value')
        data = 'Note: Holidays earlier than today are not displayed'
        # increment total views by 1
        total_views = r.incr('holiday-list:views')
        return render(request, 'hijri_calendar_app/holiday.html',
                               {'holiday_calendars': holiday_calendars,
                                'data': data,
                                'cache_timeout': settings.VIEW_CACHE_TIMEOUT,
                                'total_views': total_views})


class CalendarDetailPageView(TemplateView):
    def get(self, request, date_value, **kwargs):
        data = get_object_or_404(HijriCalendar,
                                 date_value=date_value)
        # increment total date views by 1
        total_views = r.incr('calendar-date:{}:views'.format(str(date_value)))
        return render(request, 'hijri_calendar_app/calendar_detail.html',
                               {'data': data,
                                'cache_timeout': settings.VIEW_CACHE_TIMEOUT,
                                'total_views': total_views})
