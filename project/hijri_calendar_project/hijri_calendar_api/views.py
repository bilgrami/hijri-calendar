from rest_framework import viewsets

from hijri_calendar_app.models import DataFile, HijriCalendar, Holiday
from hijri_calendar_api.serializers import (DataFileSerializer,
                                            HijriCalendarSerializer,
                                            HolidaySerializer)


class DataFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DataFile to be viewed or edited.
    """
    queryset = DataFile.objects.all().order_by('file_name')
    serializer_class = DataFileSerializer


class HijriCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows HijriCalendar to be viewed or edited.
    """
    queryset = HijriCalendar.objects.all().order_by('date_value')
    serializer_class = HijriCalendarSerializer


class HolidayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Holidays to be viewed or edited.
    """
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
