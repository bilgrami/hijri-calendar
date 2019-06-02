FROM bilgrami/python-base:latest
LABEL Name=hijri_calendar Version=0.0.1 maintainer="Syed Bilgrami <bilgrami@gmail.com>"


ARG PROJECT_ROOT=/project
ARG CONFIG_ROOT=/config
ARG DATA_ROOT=/data
ENV VIRTUAL_ENV_ROOT=/.virtualenvs/myproject_env


# Copy files and configs
WORKDIR $PROJECT_ROOT
COPY $CONFIG_ROOT/requirements.txt $CONFIG_ROOT/requirements.txt
ADD $PROJECT_ROOT $PROJECT_ROOT


# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y 
RUN \
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
RUN python -m venv $VIRTUAL_ENV_ROOT
RUN . $VIRTUAL_ENV_ROOT/bin/activate
RUN $VIRTUAL_ENV_ROOT/bin/python -m pip install --upgrade pip
RUN $VIRTUAL_ENV_ROOT/bin/pip install -r $CONFIG_ROOT/requirements.txt


# **** Server ****
ENV SERVER_PORT=5000
ENV UWSGI_INI=uwsgi.ini
ENV STATIC_URL=/app/static_collected
ENV LISTEN_PORT=5000
EXPOSE $SERVER_PORT
STOPSIGNAL SIGINT
CMD $VIRTUAL_ENV_ROOT/bin/python ./hijri_calendar_project/manage.py runserver 0.0.0.0:$SERVER_PORT
