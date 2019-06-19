from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page
from django.conf import settings

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', 
        cache_page(settings.VIEW_CACHE_TIMEOUT)(views.AboutPageView.as_view()),
        name='about'),
    url(r'^holiday/$', 
        cache_page(settings.VIEW_CACHE_TIMEOUT)(views.HolidayPageView.as_view()),
        name='holiday'),
    url(r'^calendar_detail/(?P<date_value>\d{4}-\d{2}-\d{2})/$',
        cache_page(settings.VIEW_CACHE_TIMEOUT)
        (views.CalendarDetailPageView.as_view()),
        name='calendar_detail_url'),
]
