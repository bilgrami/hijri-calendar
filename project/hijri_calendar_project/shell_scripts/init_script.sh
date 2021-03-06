#!/bin/bash

echo You are running script from $(pwd)
python manage.py sqlflush  #| python ./manage.py dbshell
python manage.py makemigrations
python manage.py migrate

echo -----------------------------------------
echo creating superuser [$ADMIN_USER], please wait ..
ADMIN_USER="$ADMIN_USER";
ADMIN_EMAIL="$ADMIN_EMAIL";
ADMIN_PASSWD="$ADMIN_PASSWD";

echo    email=$ADMIN_EMAIL

__script="
from django.contrib.auth.models import User;
if (User.objects.filter(username = '$ADMIN_USER')):
  # User.objects.get(username='$ADMIN_USER', is_superuser=True).delete()
  print ('Warning: Username [$ADMIN_USER] aleady exists. ')
else:
  User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PASSWD')
"
echo "$__script" | python manage.py shell
echo finished!
echo ----------------------------------------- 

python manage.py migrate --fake hijri_calendar_app zero
python manage.py migrate

echo -----------------------------------------
echo Loading Data
echo -----------------------------------------

python manage.py loaddata data_file;
python manage.py loaddata holidayaliaslist;
python manage.py loaddata holidaycountrylist;
python manage.py loaddata holidayoriginlist;
python manage.py loaddata holidayregionlist;
python manage.py loaddata holiday;
python manage.py loaddata hijri_calendar_Y2019
python manage.py loaddata hijri_calendar_Y2020;

echo -----------------------------------------
echo Populating Holidays
echo -----------------------------------------
python manage.py populate_holidays;
