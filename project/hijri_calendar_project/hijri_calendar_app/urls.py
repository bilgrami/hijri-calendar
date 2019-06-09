from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
# router.register(r'datafiles', views.DataFileViewSet)
router.register(r'calendar', views.HijriCalendarViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^data/$', views.DataPageView.as_view(), name='data'),
    path('api/v1/', include(router.urls)),
]