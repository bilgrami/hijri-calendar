from django.db import models
# from .models import HijriCalendar, HolidayCalendar


class HolidayCalendarManager(models.Manager):
    def get_queryset(self):
        return super(HolidayCalendarManager, self).get_queryset()\
                          .filter(is_holiday=True)
