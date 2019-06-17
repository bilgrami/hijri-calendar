#!/bin/bash

# Get environment variables to show up in SSH session
eval $(printenv | sed -n "s/^\([^=]\+\)=\(.*\)$/export \1=\2/p" | sed 's/"/\\\"/g' | sed '/=/s//="/' | sed 's/$/"/' >> /etc/profile)

echo starting sshd process
sed -i "s/SSH_PORT/$SSH_PORT/g" /etc/ssh/sshd_config;
/usr/sbin/sshd

echo "python is located at:"
which python 

cd $PROJECT_ROOT/hijri_calendar_project/
echo "Running django server on port $SERVER_PORT"
python manage.py runserver 0.0.0.0:$SERVER_PORT
