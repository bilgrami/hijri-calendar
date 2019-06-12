from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class DataFile(models.Model):
    file_name = models.CharField(max_length=30, unique=True)
    file_type = models.CharField(max_length=20)
    date_loaded = models.DateField("File Load Date", default=timezone.now)
    loaded_by = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='blog_posts',
                                  default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "data_file"

    def __str__(self):
        return f"{self.FileName}.{self.FileType}"


class HijriCalendar(models.Model):
    islamic_month_choices = [
        (1, 'MUHARRAM'),
        (2, 'Safar'),
        (3, 'RABI-UL-AWWAL'),
        (4, 'Rabi-us-Sani'),
        (5, 'JAMADI-UL-AWWAL'),
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
    lunar_day = models.CharField("Lunar Day", max_length=30)
    lunar_month_label = models.CharField("Lunar Month Label",
                                         max_length=20, default=None)
    lunar_month = models.SmallIntegerField(
        "Lunar Month",
        choices=islamic_month_choices
        )
    lunar_year = models.SmallIntegerField("Lunar Year")
    day = models.SmallIntegerField("Gregorian Day")
    month_label = models.CharField("Month Label", max_length=20, default=None)
    month = models.SmallIntegerField(
        "Gregorian Month",
        choices=month_choices
    )
    year = models.SmallIntegerField("Gregorian Year", )

    data_file = models.ForeignKey(DataFile,
                                  on_delete=models.CASCADE,
                                  related_name='date_entries'
                                  )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = "date_value"
        ordering = ["-date_value"]
        unique_together = ("lunar_year", "lunar_month", "lunar_day")
        verbose_name = "Hijri Islamic Calendar"
        db_table = "calendar"

    def __str__(self):
        date_value = self.dateValue.strftime("%Y-%m-%d")
        return (
            f"{date_value} {self.lunarDay} - "
            f"{self.lunarMonth} {self.lunarYear} Hijri"
        )
