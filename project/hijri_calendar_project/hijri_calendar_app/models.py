from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class DataFile(models.Model):
    file_name = models.CharField(max_length=30, unique=True)
    file_type = models.CharField(max_length=20)
    date_loaded = models.DateTimeField("File Load Date", default=timezone.now)
    loaded_by = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='data_file_dates',
                                  default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "data_file"

    def __str__(self):
        return f"{self.file_name}.{self.file_type}"


class HijriCalendar(models.Model):
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

    date_value = models.DateField("Gregorian Date", unique=True)
    day = models.SmallIntegerField("Gregorian Day")
    month = models.SmallIntegerField(
        "Gregorian Month",
        choices=month_choices
    )
    year = models.SmallIntegerField("Gregorian Year", )
    month_name = models.CharField("Month Label", max_length=20,
                                  editable=False, default=None)

    hijri_day = models.CharField("Hijri Day", max_length=30)
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    hijri_date_value = models.CharField("Hijri Date",
                                        max_length=30,
                                        editable=False
                                        )

    class Meta:
        get_latest_by = "date_value"
        ordering = ["-date_value"]
        unique_together = ("hijri_year", "hijri_month", "hijri_day")
        verbose_name = "Hijri Islamic Calendar"
        db_table = "calendar"

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
