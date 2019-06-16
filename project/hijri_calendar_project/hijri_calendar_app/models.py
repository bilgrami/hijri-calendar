from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# from django.urls import reverse
from .managers import HolidayCalendarManager

hijri_month_choices = [
    (1, 'Muharram'),
    (2, 'Safar'),
    (3, 'Rabi-ul-Awwal'),
    (4, 'Rabi-us-Sani'),
    (5, 'Jamadi-ul-Awwal'),
    (6, 'Jamadi-us-Sani'),
    (7, 'Rajab'),
    (8, 'Shaaban'),
    (9, 'Ramazan'),
    (10, 'Shawwal'),
    (11, 'Ziquad'),
    (12, 'Zilhij')
]

month_choices = [
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'Novemeber'),
    (12, 'December')
]


class DataFile(models.Model):
    file_name = models.CharField(max_length=30, unique=True, primary_key=True)
    file_type = models.CharField(max_length=20)
    date_loaded = models.DateTimeField("File Load Date", default=timezone.now)
    loaded_by = models.ForeignKey(User, related_name='loaded_data_files',
                                  on_delete=models.SET_NULL,
                                  null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name


class HolidayOriginList(models.Model):
    name = models.CharField("Origin Name", max_length=30, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Holiday Origin"


class HolidayCountryList(models.Model):
    name = models.CharField("Country Name", max_length=100, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Holiday Country"


class HolidayAliasList(models.Model):
    name = models.CharField("Alias Name", max_length=100, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Holiday Alias"


class Holiday(models.Model):
    holiday_name = models.CharField(max_length=30, unique=True,
                                    primary_key=True)
    description = models.TextField("Description", blank=True, null=True)
    hijri_day = models.SmallIntegerField("Hijri Day", blank=True, null=True)
    hijri_month = models.SmallIntegerField("Hijri Month",
                                           choices=hijri_month_choices,
                                           blank=True, null=True)
    day = models.SmallIntegerField("Gregorian Day", blank=True, null=True)
    month = models.SmallIntegerField("Gregorian Month", choices=month_choices,
                                     blank=True, null=True)
    origin = models.ForeignKey(HolidayOriginList,
                               on_delete=models.CASCADE,
                               blank=True, null=True)
    alias_names = models.ManyToManyField(HolidayAliasList,
                                         blank=True, null=True)
    country = models.ManyToManyField(HolidayCountryList,
                                     blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Holiday"

    def __str__(self):
        if self.origin:
            return f"{self.holiday_name} ({self.origin})"
        else:
            return f"{self.holiday_name}"


class HijriCalendar(models.Model):

    date_value = models.DateField("Gregorian Date", unique=True,
                                  primary_key=True)
    day = models.SmallIntegerField("Gregorian Day")
    month = models.SmallIntegerField("Gregorian Month",
                                     choices=month_choices)
    year = models.SmallIntegerField("Gregorian Year", )
    month_name = models.CharField("Month Label", max_length=20,
                                  editable=False, default=None)
    hijri_day = models.SmallIntegerField("Hijri Day")
    hijri_month = models.SmallIntegerField("Hijri Month",
                                           choices=hijri_month_choices)
    hijri_year = models.SmallIntegerField("Hijri Year")
    hijri_month_name = models.CharField("Hijri Month Name",
                                        max_length=20,
                                        editable=False,
                                        default=None)
    data_file = models.ForeignKey(DataFile,
                                  related_name='date_entries',
                                  on_delete=models.SET_NULL,
                                  null=True, blank=True)
    hijri_date_value = models.CharField("Hijri Date",
                                        max_length=10,
                                        editable=False
                                        )
    is_holiday = models.BooleanField("Is Holiday", default=False)

    holiday_list = models.ManyToManyField(Holiday,
                                          related_name='holiday_dates')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    holiday_calendar = HolidayCalendarManager()

    class Meta:
        verbose_name = "Hijri Islamic Calendar"
        get_latest_by = "-date_value"
        ordering = ["-date_value"]
        constraints = [
            models.UniqueConstraint(fields=["hijri_year",
                                            "hijri_month",
                                            "hijri_day"],
                                    name='unique_hijri_date')
        ]
        indexes = [
            models.Index(fields=["hijri_month",
                                 "hijri_day"],
                         name='hijri_idx'),
            models.Index(fields=["month",
                                 "day"],
                         name='gregorian_idx'),
            models.Index(fields=["is_holiday"],
                         name='is_holiday_idx'),
        ]

    def __str__(self):
        return self.date_value.strftime("%Y%M-%D")

    def save(self, *args, **kwargs):
        self.hijri_date_value = (f"{self.hijri_year}-"
                                 f"{str(self.hijri_month).zfill(2)}"
                                 f"-{str(self.hijri_day).zfill(2)}")
        hijri_month_filtered_list = [item[1]
                                     for item in hijri_month_choices
                                     if item[0] == self.hijri_month]
        self.hijri_month_name = next(iter(hijri_month_filtered_list or []),
                                     None)
        super(HijriCalendar, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('calendar:calendar_detail_url',
        #                args=[{self.date_value}, ])
        return f"/calendar_detail/{self.date_value}"

    def get_api_url(self):
        return f"/api/v1/calendar/{self.date_value}"
