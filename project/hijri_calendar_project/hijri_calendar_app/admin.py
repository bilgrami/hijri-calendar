from django.contrib import admin

# Register your models here.
from .models import DataFile, HijriCalendar

admin.site.register(DataFile)
admin.site.register(HijriCalendar)
