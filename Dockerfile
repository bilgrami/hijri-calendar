FROM bilgrami/python-base:latest
LABEL Name=hijri_calendar Version=0.0.1 maintainer="Syed Bilgrami <bilgrami@gmail.com>"


ARG PROJECT_ROOT=/usr/local/project
ARG CONFIG_ROOT=$PROJECT_ROOT/config
ENV VIRTUAL_ENV=$PROJECT_ROOT/.virtualenvs/myproject_env


# Copy files and configs
WORKDIR $PROJECT_ROOT
COPY /config/requirements.txt $CONFIG_ROOT/requirements.txt
ADD /project $PROJECT_ROOT


# Create virtual environment and install python packages
RUN mkdir -p $VIRTUAL_ENV;\ 
    python -m venv $VIRTUAL_ENV; 

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN  python -m pip install --upgrade pip && \
     pip install -r $CONFIG_ROOT/requirements.txt; 


# **** Server ****
ENV SERVER_PORT=5000
ENV UWSGI_INI=uwsgi.ini
ENV STATIC_URL=/app/static_collected
ENV LISTEN_PORT=5000
ENV PYTHONUNBUFFERED 1
EXPOSE $SERVER_PORT
STOPSIGNAL SIGINT
CMD python ./hijri_calendar_project/manage.py runserver 0.0.0.0:$SERVER_PORT
