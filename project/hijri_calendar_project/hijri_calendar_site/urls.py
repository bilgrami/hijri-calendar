from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
  url(r'^admin/shell/', include('django_admin_shell.urls')),
  path('admin/', admin.site.urls),
  url(r'^', include('hijri_calendar_app.urls')),

]
# https://stackoverflow.com/questions/9181047/django-static-files-development
urlpatterns += staticfiles_urlpatterns()
