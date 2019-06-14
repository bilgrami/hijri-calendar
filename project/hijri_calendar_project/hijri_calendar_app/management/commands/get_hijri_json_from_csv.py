from django.core.management.base import BaseCommand, CommandError
import json
import csv
import os
from django.utils import timezone


class Command(BaseCommand):
    """
    pre-requisite:
    sql:
        drop table hijri_calendar_data_file CASCADE;
        drop table hijri_calendar CASCADE;
        drop table hijri_holiday_calendar CASCADE;
        drop table hijri_holiday CASCADE;
        or
        truncate table hijri_calendar_data_file CASCADE;
    script
        python manage.py makemigrations
        python manage.py migrate --fake hijri_calendar_app zero
        python manage.py migrate
        python manage.py loaddata data_file

    Usage:
    python manage.py get_hijri_json_from_csv \
    '../data/source/Y2019-hijri_calendar.csv' > \
    ./hijri_calendar_app/fixtures/hijri_calendar_Y2019.json
    python manage.py loaddata hijri_calendar_Y2019

    python manage.py get_hijri_json_from_csv \
        '../data/source/Y2020-hijri_calendar.csv' > \
        ./hijri_calendar_app/fixtures/hijri_calendar_Y2020.json
    python manage.py loaddata hijri_calendar_Y2020

    """
    def add_arguments(self, parser):
        help_text = 'Converts a csv file containing Calendar data '
        'into Fixture JSON format'
        parser.add_argument('file_path', type=str, help=help_text)

    def handle(self, *args, **options):
        file_path = options['file_path']
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_file_path = os.path.join(BASE_DIR, file_path)

        if not os.path.exists(full_file_path):
            raise CommandError('File Path "%s" does not exist' % file_path)

        json = self.hijri_calendar_csv_to_fixture_json(
            file_full_path=full_file_path)
        self.stdout.write(json)

    def hijri_calendar_csv_to_fixture_json(self, file_full_path):
        total_lines = 0
        with open(file_full_path) as csvfile:
            total_lines = sum(1 for line in csvfile)
            total_data_rows = total_lines - 1  # totallines minus header

        result = '[\n'
        with open(file_full_path) as csvfile:
            reader = csv.reader(csvfile)
            for rid, row in enumerate(reader):
                # skipping first header row
                if rid == 0:
                    continue

                d = {
                    "model": "hijri_calendar_app.hijricalendar",
                    "pk": row[0],
                    "fields": {
                        # "date_value": pk,
                        "day": int(row[5]),
                        "month": int(row[7]),
                        "year": int(row[8]),
                        "month_name": row[6],
                        "hijri_day": int(row[1]),
                        "hijri_month": int(row[2]),
                        "hijri_year": int(row[4]),
                        "hijri_month_name": row[3],
                        "data_file": row[9],
                        "hijri_date_value": row[10],
                        "is_holiday": str(False),
                        "created": str(timezone.now()),
                        "updated": str(timezone.now()),
                        }
                        }
                result += str(d)

                # skip comma for last row
                if rid < total_data_rows:
                    result += ','

                result += '\n'

        result += ']\n'
        result = result.replace("'", '"')

        res = json.loads(result)
        json_data = json.dumps(res, indent=4)
        return json_data
