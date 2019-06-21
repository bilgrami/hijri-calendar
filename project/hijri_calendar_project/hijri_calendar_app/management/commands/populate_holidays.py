from django.core.management.base import BaseCommand
from hijri_calendar_app.models import HijriCalendar, Holiday
from hijri_calendar_app.views import HolidayPageView, CalendarDetailPageView
from helpers import cache_helper as ch


class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):
        cache_key_prefix = HolidayPageView.cache_key_prefix()
        ch.CacheHelper(key_prefix=cache_key_prefix).clear()

        cache_key_prefix = CalendarDetailPageView.cache_key_prefix()
        ch.CacheHelper(key_prefix=cache_key_prefix).clear()

        holidays = Holiday.objects.all()
        dates = HijriCalendar.objects.all()
        # first of all clear all existing holidays
        for dt in dates:
            dt.is_holiday = False
            dt.holiday_list.clear()
            dt.save()

        for dt in dates:
            for h in holidays:
                if ((dt.hijri_day == h.hijri_day and dt.hijri_month
                   == h.hijri_month) or
                   (dt.day == h.day and dt.month == h.month)):
                    print(f"[{dt}] [{dt.hijri_year}-"
                          f"{dt.hijri_month}-{dt.hijri_day} Hijri] "
                          f"is '{h.holiday_name}' holiday")
                    dt.is_holiday = True
                    dt.holiday_list.add(h)

            dt.save()
