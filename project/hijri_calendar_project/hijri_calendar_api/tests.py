from rest_framework.test import APIRequestFactory
from hijri_calendar_app.models import HijriCalendar
from django.test import TestCase
from .views import HijriCalendarViewSet
from rest_framework import status


class HijriCalendarAPITestCase(TestCase):
    """
        python manage.py test hijri_calendar_api.tests --keepdb
    """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.hijri_calendar_view = HijriCalendarViewSet.as_view(
                                    {'get': 'list'})

        self.new_year_2017 = HijriCalendar.objects.create(
                                     date_value='2017-01-01',
                                     day=1,
                                     month=1,
                                     year=2017,
                                     month_name='January',
                                     hijri_day=3,
                                     hijri_month=3,
                                     hijri_year=1438,
                                     hijri_date_value='1438-03-03')

    def test_get_calendar_date(self):
        """
        Test that we can get a calendar date
        """
        request = self.factory.get('/api/v1/calendar/2017-01-01')
        response = self.hijri_calendar_view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_calendar_date(self):
        """
        Test that we can get an error on invalid calendar date
        """
        request = self.factory.get('/api/v1/calendar/2016-01-01')
        response = self.hijri_calendar_view(request)
        print("response: ", response)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
