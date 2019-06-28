from django.core.management.base import BaseCommand
from django.db.models import Q

from helpers import cache_helper as ch
from hijri_calendar_app.models import HijriCalendar, Holiday
from hijri_calendar_app.views import CalendarDetailPageView, HolidayPageView


class Command(BaseCommand):
    """
    """
    def add_arguments(self, parser):
        parser.add_argument('--id')

    def populate_holiday(self, holiday_name):
        cache_key_prefix = HolidayPageView.cache_key_prefix()
        ch.CacheHelper(key_prefix=cache_key_prefix).clear()

        # cache_key_prefix = CalendarDetailPageView.cache_key_prefix()
        # ch.CacheHelper(key_prefix=cache_key_prefix).clear()

        holidays = Holiday.objects.all()
        h = Holiday.objects.get(holiday_name=holiday_name)
        print(f"{h}: day: {h.day}, month: {h.month}, "
              f"hijri_day: {h.hijri_day}, hijri_month: {h.hijri_month}")
        if h.day and h.month:
            q = ((Q(day=h.day) & Q(month=h.month)))
        elif h.hijri_day and h.hijri_month:
            q = ((Q(hijri_day=h.hijri_day) & Q(hijri_month=h.hijri_month)))

        dates = HijriCalendar.objects.filter(q)
        # first of all clear all existing holidays
        cal_detail_cache_key_prefix = CalendarDetailPageView.cache_key_prefix()
        for dt in dates:
            print(f"Clearing holiday data for [{dt}] [{dt.hijri_year}-"
                    f"{dt.hijri_month}-{dt.hijri_day} Hijri] ")
            dt.is_holiday = False
            dt.holiday_list.clear()
            # TODO: get this hard-coded value from source
            key = f'{str(dt.date_value)}:views'
            ch.CacheHelper(key_prefix=cal_detail_cache_key_prefix).delete(key)
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

    def populate_all_holidays(self):
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

    def handle(self, *args, **options):
        if options['id']:
            holiday_name = options['id']
            print(f"running for [{holiday_name}]")
            self.populate_holiday(holiday_name)
        else:
            print("running for all holidays")
            self.populate_all_holidays()
