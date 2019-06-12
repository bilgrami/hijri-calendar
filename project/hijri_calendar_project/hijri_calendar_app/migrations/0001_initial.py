# Generated by Django 2.2.2 on 2019-06-12 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=30, unique=True)),
                ('file_type', models.CharField(max_length=20)),
                ('date_loaded', models.DateField(default=django.utils.timezone.now, verbose_name='File Load Date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('loaded_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'data_file',
            },
        ),
        migrations.CreateModel(
            name='HijriCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_value', models.DateField(unique=True, verbose_name='Gregorian Date')),
                ('lunar_day', models.CharField(max_length=30, verbose_name='Lunar Day')),
                ('lunar_month_label', models.CharField(default=None, max_length=20, verbose_name='Lunar Month Label')),
                ('lunar_month', models.SmallIntegerField(choices=[(1, 'MUHARRAM'), (2, 'Safar'), (3, 'RABI-UL-AWWAL'), (4, 'Rabi-us-Sani'), (5, 'JAMADI-UL-AWWAL'), (6, 'Jamadi-us-Sani'), (7, 'Rajab'), (8, 'Shaaban'), (9, 'Ramazan'), (10, 'Shawwal'), (11, 'Ziquad'), (12, 'Zilhij')], verbose_name='Lunar Month')),
                ('lunar_year', models.SmallIntegerField(verbose_name='Lunar Year')),
                ('day', models.SmallIntegerField(verbose_name='Gregorian Day')),
                ('month_label', models.CharField(default=None, max_length=20, verbose_name='Month Label')),
                ('month', models.SmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'Novemeber'), (12, 'December')], verbose_name='Gregorian Month')),
                ('year', models.SmallIntegerField(verbose_name='Gregorian Year')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('data_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date_entries', to='hijri_calendar_app.DataFile')),
            ],
            options={
                'verbose_name': 'Hijri Islamic Calendar',
                'db_table': 'calendar',
                'ordering': ['-date_value'],
                'get_latest_by': 'date_value',
                'unique_together': {('lunar_year', 'lunar_month', 'lunar_day')},
            },
        ),
    ]
