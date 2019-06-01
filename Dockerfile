FROM bilgrami/python-base:latest
LABEL Name=hijri_calendar Version=0.0.1 maintainer="Syed Bilgrami <bilgrami@gmail.com>"

# set environment varibles
ENV PROJECT_ROOT /project
ENV CONFIG_ROOT /config
ENV DATA_ROOT /data
ENV VIRTUAL_ENV_ROOT /.virtualenvs

# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini
# Tell nginx where static files live (as typically collected using Django's
# collectstatic command.
ENV STATIC_URL /app/static_collected
ENV LISTEN_PORT=5000

WORKDIR $PROJECT_ROOT

EXPOSE 5000

COPY $CONFIG_ROOT/requirements.txt $CONFIG_ROOT/requirements.txt

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y 
RUN \
 apt-get update && \
 apt-get install -qy --no-install-recommends \
    libffi-dev \
    libssl-dev \
    python-mysqldb \
    default-libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim \
    tree

RUN mkdir -p $VIRTUAL_ENV_ROOT
RUN python -m venv $VIRTUAL_ENV_ROOT/myproject_env 
RUN . $VIRTUAL_ENV_ROOT/myproject_env/bin/activate
RUN $VIRTUAL_ENV_ROOT/myproject_env/bin/python -m pip install --upgrade pip
RUN $VIRTUAL_ENV_ROOT/myproject_env/bin/pip install -r $CONFIG_ROOT/requirements.txt

# Copy the app files to a folder and run it from there
ADD $PROJECT_ROOT $PROJECT_ROOT
# Make app folder writable for the sake of db.sqlite3, and make that file also writable.
# RUN chmod g+w $PROJECT_ROOT/app/db/db.sqlite3

CMD $VIRTUAL_ENV_ROOT/myproject_env/bin/python ./hijri_calendar_project/manage.py runserver 0.0.0.0:5000
