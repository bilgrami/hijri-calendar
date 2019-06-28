from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
  url(r'^admin/shell/', include('django_admin_shell.urls')),
  path('admin/', admin.site.urls),
  url(r'^', include('hijri_calendar_app.urls')),
  url(r'^', include('hijri_calendar_api.urls')),
]
# https://stackoverflow.com/questions/9181047/django-static-files-development
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
