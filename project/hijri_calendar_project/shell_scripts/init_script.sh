
echo You are running script from $(pwd)
python manage.py sqlflush
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
python manage.py loaddata data_file

python manage.py get_hijri_json_from_csv \
'../data/source/Y2019-hijri_calendar.csv' > \
./hijri_calendar_app/fixtures/hijri_calendar_Y2019.json
python manage.py loaddata hijri_calendar_Y2019

python manage.py get_hijri_json_from_csv \
    '../data/source/Y2020-hijri_calendar.csv' > \
    ./hijri_calendar_app/fixtures/hijri_calendar_Y2020.json
python manage.py loaddata hijri_calendar_Y2020
