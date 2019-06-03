from django.db import models

# Create your models here.
class DataFile(models.Model):
    FileName = models.CharField(max_length = 30, unique = True),
    FileType= models.CharField(max_length = 20)

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

    dateValue = models.DateField("Gregorian Date", unique = True)
    dataFile =  models.ForeignKey(DataFile, on_delete = models.CASCADE)

    lunarDay = models.CharField("Lunar Day", max_length = 30)
    lunarMonth = models.CharField("Lunar Month", max_length = 2, choices = Islamic_month_choices)
    lunarYear = models.CharField("Lunar Year", max_length = 30)
    day = models.SmallIntegerField("Gregorian Day")
    month = models.CharField("Gregorian Month", max_length = 9)
    year = models.SmallIntegerField("Gregorian Year", )
