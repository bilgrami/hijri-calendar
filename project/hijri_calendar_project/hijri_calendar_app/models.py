from django.db import models


class DataFile(models.Model):
    FileName = models.CharField(max_length=30, unique=True)
    FileType = models.CharField(max_length=20)
    DateLoaded = models.DateField("File Load Date", default=None)

    def __str__(self):
        return f"{self.FileName}.{self.FileType}"


class HijriCalendar(models.Model):
    Islamic_month_choices = [
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

    dateValue = models.DateField("Gregorian Date", unique=True)
    lunarDay = models.CharField("Lunar Day", max_length=30)
    lunarMonthLabel = models.CharField("Lunar Month Label", max_length=20, default=None)
    lunarMonth = models.SmallIntegerField(
        "Lunar Month",
        choices=Islamic_month_choices
        )
    lunarYear = models.SmallIntegerField("Lunar Year")
    day = models.SmallIntegerField("Gregorian Day")
    monthLabel = models.CharField("Month Label", max_length=20, default=None)
    month = models.SmallIntegerField(
        "Gregorian Month",
        choices=month_choices
    )
    year = models.SmallIntegerField("Gregorian Year", )

    dataFile = models.ForeignKey(DataFile, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = "dateValue"
        ordering = ["-dateValue"]
        unique_together = ("lunarYear", "lunarMonth", "lunarDay")
        verbose_name = "Hijri Islamic Calendar"

    def __str__(self):
        date_value = self.dateValue.strftime("%Y-%m-%d")
        return (
            f"{date_value} {self.lunarDay} "
            f"{self.lunarMonth} {self.lunarYear} Hijri"
        )
