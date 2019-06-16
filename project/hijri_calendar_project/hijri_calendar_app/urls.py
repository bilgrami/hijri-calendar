from django.conf.urls import url
from django.urls import include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register(r'datafiles', views.DataFileViewSet)
router.register('', views.HijriCalendarViewSet)

holiday_router = routers.DefaultRouter()
holiday_router.register('', views.HolidayViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^holiday/$', views.HolidayPageView.as_view(), name='holiday'),
    url(r'^calendar_detail/(?P<date_value>\d{4}-\d{2}-\d{2})/$',
        views.CalendarDetailPageView.as_view(),
        name='calendar_detail_url'),
    url(r'^api/v1/calendar/', include(router.urls)),
    url(r'^api/v1/holiday/', include(holiday_router.urls)),
    # path('api/v1/', include(router.urls)),
]
