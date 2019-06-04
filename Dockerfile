FROM bilgrami/python-base:latest
LABEL Name=hijri_calendar Version=0.0.1 maintainer="Syed Bilgrami <bilgrami@gmail.com>"


ARG PROJECT_ROOT=/usr/local/project
ARG CONFIG_ROOT=$PROJECT_ROOT/config
ENV VIRTUAL_ENV=$PROJECT_ROOT/.virtualenvs/myproject_env


# Create virtual environment
RUN mkdir -p $PROJECT_ROOT; \
    mkdir -p $VIRTUAL_ENV; \ 
    python -m venv $VIRTUAL_ENV; 

ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# install python packages
WORKDIR $PROJECT_ROOT
COPY /config/requirements.txt $CONFIG_ROOT/requirements.txt
RUN  python -m pip install --upgrade pip && \
     pip install -r $CONFIG_ROOT/requirements.txt; 
ADD ./project $PROJECT_ROOT 


# **** Server ****
ENV SERVER_PORT=5000
ENV iPYTHON_NOTEBOOK_PORT=8888
ENV UWSGI_INI=uwsgi.ini
ENV STATIC_URL=/static/
ENV LISTEN_PORT=5000
ENV PYTHONUNBUFFERED 1
EXPOSE $SERVER_PORT
EXPOSE $iPYTHON_NOTEBOOK_PORT
STOPSIGNAL SIGINT
CMD python ./hijri_calendar_project/manage.py runserver 0.0.0.0:$SERVER_PORT