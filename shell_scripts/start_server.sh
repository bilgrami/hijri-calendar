#!/bin/bash
SERVER_PORT=5000

echo -----------------------------------------
ADMIN_USER="admin";
ADMIN_EMAIL="admin@gmail.com";
ADMIN_PASSWD="admin123";

echo creating superuser [$ADMIN_USER], please wait ..
echo    email=$ADMIN_EMAIL

__script="
from django.contrib.auth.models import User;
if (User.objects.filter(username = '$ADMIN_USER')):
  # User.objects.get(username='$ADMIN_USER', is_superuser=True).delete()
  print ('Warning: Username [$ADMIN_USER] aleady exists. ')
else:
  User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PASSWD')
"
echo "$__script" | python ./project/hijri_calendar_project/manage.py shell
echo finished!
echo ----------------------------------------- 

echo "starting django server on port $SERVER_PORT"
python ./project/hijri_calendar_project/manage.py runserver 0.0.0.0:$SERVER_PORT
