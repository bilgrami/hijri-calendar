from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    loaded_by = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='data_file_dates',
                                  default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "hijri_calendar_data_file"

    def __str__(self):
        return f"{self.file_name}.{self.file_type}"


class HijriCalendar(models.Model):

    date_value = models.DateField("Gregorian Date", unique=True,
                                  primary_key=True)
    day = models.SmallIntegerField("Gregorian Day")
    month = models.SmallIntegerField(
        "Gregorian Month",
        choices=month_choices
    )
    year = models.SmallIntegerField("Gregorian Year", )
    month_name = models.CharField("Month Label", max_length=20,
                                  editable=False, default=None)

    hijri_day = models.SmallIntegerField("Hijri Day")
    hijri_month = models.SmallIntegerField(
        "Hijri Month", choices=hijri_month_choices)
    hijri_year = models.SmallIntegerField("Hijri Year")
    hijri_month_name = models.CharField("Hijri Month Name",
                                        max_length=20,
                                        editable=False,
                                        default=None)
    data_file = models.ForeignKey(DataFile,
                                  on_delete=models.CASCADE,
                                  related_name='date_entries'
                                  )
    hijri_date_value = models.CharField("Hijri Date",
                                        max_length=10,
                                        editable=False
                                        )
    is_holiday = models.BooleanField("Is Holiday", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hijri Islamic Calendar"
        db_table = "hijri_calendar"
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
        return self.date_value.strftime("%Y-%m-%d")

    def save(self, *args, **kwargs):
        self.hijri_date_value = (f"{self.hijri_year}-"
                                 f"{str(self.hijri_month).zfill(2)}"
                                 f"-{str(self.hijri_day).zfill(2)}")
        hijri_month_filtered_list = [item[1]
                                     for item in self.hijri_month_choices
                                     if item[0] == self.hijri_month]
        self.hijri_month_name = next(iter(hijri_month_filtered_list or []),
                                     None)
        super(HijriCalendar, self).save(*args, **kwargs)


class Holiday(models.Model):
    holiday_name = models.CharField(max_length=30,
                                    unique=True,
                                    primary_key=True)
    hijri_day = models.SmallIntegerField("Hijri Day")
    hijri_month = models.SmallIntegerField(
        "Hijri Month", choices=hijri_month_choices)

    class Meta:
        verbose_name = "Hijri Holiday"
        db_table = "hijri_holiday"

    def __str__(self):
        return self.holiday_name


class HolidayCalendar(models.Model):
    hijri_date = models.ForeignKey(HijriCalendar,
                                   on_delete=models.CASCADE,
                                   related_name='holiday_dates')
    holiday = models.ForeignKey(Holiday,
                                on_delete=models.CASCADE,
                                related_name='holidays')

    class Meta:
        verbose_name = "Hijri Holiday Calendar"
        db_table = "hijri_holiday_calendar"
        get_latest_by = "-hijri_date"
        ordering = ["-hijri_date"]
        constraints = [
            models.UniqueConstraint(fields=["hijri_date",
                                            "holiday"],
                                    name='unique_holiday_date')
        ]
        indexes = [
            models.Index(fields=["hijri_date",
                                 "holiday"],
                         name='hijri_holiday_idx')
        ]


# class IslamicEventsManager(models.Manager):
#     def get_queryset(self):
#         return super(IslamicEventsManager),
#         self).get_queryset().filter()
