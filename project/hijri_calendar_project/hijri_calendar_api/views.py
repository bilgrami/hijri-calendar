from rest_framework import viewsets
from hijri_calendar_app.models import DataFile, HijriCalendar, Holiday
from hijri_calendar_api.serializers import (DataFileSerializer,
                                            HijriCalendarSerializer,
                                            HolidaySerializer)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings


class DataFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DataFile to be viewed or edited.
    """
    queryset = DataFile.objects.all().order_by('file_name')
    serializer_class = DataFileSerializer

    @method_decorator(cache_page(settings.API_CACHE_TIMEOUT))
    def dispatch(self, *args, **kwargs):
        return super(DataFileViewSet, self).dispatch(*args, **kwargs)


class HijriCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows HijriCalendar to be viewed or edited.
    """
    queryset = HijriCalendar.objects.all().order_by('date_value')
    serializer_class = HijriCalendarSerializer

    @method_decorator(cache_page(settings.API_CACHE_TIMEOUT))
    def dispatch(self, *args, **kwargs):
        return super(HijriCalendarViewSet, self).dispatch(*args, **kwargs)


class HolidayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Holidays to be viewed or edited.
    """
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer

    @method_decorator(cache_page(settings.API_CACHE_TIMEOUT))
    def dispatch(self, *args, **kwargs):
        return super(HolidayViewSet, self).dispatch(*args, **kwargs)
