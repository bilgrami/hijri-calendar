#!/bin/bash
python manage.py get_hijri_json_from_csv \
'../data/source/Y2019-hijri_calendar.csv' > \
./hijri_calendar_app/fixtures/hijri_calendar_Y2019.json

python manage.py get_hijri_json_from_csv \
    '../data/source/Y2020-hijri_calendar.csv' > \
    ./hijri_calendar_app/fixtures/hijri_calendar_Y2020.json
