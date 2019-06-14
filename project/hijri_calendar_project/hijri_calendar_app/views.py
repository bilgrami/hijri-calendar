from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import viewsets

from .models import DataFile, HijriCalendar
from .serializers import DataFileSerializer, HijriCalendarSerializer


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


# Add this view
class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }

        return render(request, 'data.html', context)


class DataFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DataFile.objects.all().order_by('file_name')
    serializer_class = DataFileSerializer


class HijriCalendarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = HijriCalendar.objects.all().order_by('-date_value')
    serializer_class = HijriCalendarSerializer
