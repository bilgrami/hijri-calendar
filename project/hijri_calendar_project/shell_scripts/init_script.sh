python ../manage.py makemigrations
python ../manage.py migrate

echo -----------------------------------------
echo creating superuser [$ADMIN_USER], please wait ..
ADMIN_USER="$ADMIN_USER";
ADMIN_EMAIL="$ADMIN_EMAIL";
ADMIN_PASSWD="$ADMIN_PASSWD";

echo    email=$ADMIN_EMAIL
 
__script="
from django.contrib.auth.models import User;
if (User.objects.filter(username = '$ADMIN_USER')): 
  print ('Warning: Username [$ADMIN_USER] aleady exists. ')
else:
  User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PASSWD')
"
echo "$__script" | python ../manage.py shell
echo finished!
echo ----------------------------------------- 
