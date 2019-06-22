from rest_framework.test import APIRequestFactory, APIClient
from hijri_calendar_app.models import HijriCalendar
from django.test import TestCase
from .views import HijriCalendarViewSet
from rest_framework import status
from rest_framework.test import APIClient


class HijriCalendarAPITestCase(TestCase):
    """
        python manage.py test hijri_calendar_api.tests --keepdb
    """

    def setUp(self):
        self.client = APIClient()
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
        api_url = '/api/v1/calendar/2017-01-01/'
        response = self.client.get(api_url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['date_value'] == '2017-01-01'
        assert response.data['hijri_date_value'] == '1438-03-03'

    def test_get_invalid_calendar_date(self):
        """
        Test that we can get an error on invalid calendar date
        """
        # api_url = '/api/v1/calendar/2016-01-01/'
        api_url = '/api/v1/calendar/dummy/'
        response = self.client.get(api_url, format='json')
        # print("response: ", response)
        # print("response.data: ", response.data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
