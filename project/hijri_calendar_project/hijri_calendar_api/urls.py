from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from . import views

calendar_router = routers.DefaultRouter()
calendar_router.register('', views.HijriCalendarViewSet)

holiday_router = routers.DefaultRouter()
holiday_router.register('', views.HolidayViewSet)

urlpatterns = [
    url(r'^api/v1/calendar/', include(calendar_router.urls)),
    url(r'^api/v1/holiday/', include(holiday_router.urls)),
]
