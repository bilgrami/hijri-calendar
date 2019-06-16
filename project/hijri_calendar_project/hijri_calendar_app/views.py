from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from rest_framework import viewsets

from .models import DataFile, HijriCalendar, Holiday
from .serializers import DataFileSerializer, HijriCalendarSerializer, HolidaySerializer
from datetime import date


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
        return render(request, 'hijri_calendar_app/holiday.html',
                               {'holiday_calendars': holiday_calendars,
                                'data': data})


class CalendarDetailPageView(TemplateView):
    def get(self, request, date_value, **kwargs):
        data = get_object_or_404(HijriCalendar,
                                 date_value=date_value)
        return render(request, 'hijri_calendar_app/calendar_detail.html',
                               {'data': data})


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
