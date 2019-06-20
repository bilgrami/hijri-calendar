#!/bin/bash
# BASE_URL=localhost
BASE_URL=https://mooncalendar.azurewebsites.net
echo Base URL: $BASE_URL
echo warming view cache 
curl -s -o nul $BASE_URL/calendar_detail/2019-06-05/
curl -s -o nul $BASE_URL/calendar_detail/2019-08-12/
curl -s -o nul $BASE_URL/calendar_detail/2019-08-12/
curl -s -o nul $BASE_URL/calendar_detail/2019-09-01/
curl -s -o nul $BASE_URL/calendar_detail/2019-09-10/
curl -s -o nul $BASE_URL/calendar_detail/2019-11-10/
curl -s -o nul $BASE_URL/calendar_detail/2019-12-25/
curl -s -o nul $BASE_URL/calendar_detail/2020-03-22/
curl -s -o nul $BASE_URL/calendar_detail/2020-04-09/
curl -s -o nul $BASE_URL/calendar_detail/2020-04-25/
curl -s -o nul $BASE_URL/calendar_detail/2020-05-01/
curl -s -o nul $BASE_URL/calendar_detail/2020-05-24/
curl -s -o nul $BASE_URL/calendar_detail/2020-07-31/
curl -s -o nul $BASE_URL/calendar_detail/2020-08-21/
curl -s -o nul $BASE_URL/calendar_detail/2020-08-30/
curl -s -o nul $BASE_URL/calendar_detail/2020-10-29/
curl -s -o nul $BASE_URL/calendar_detail/2020-12-25/
echo warming api cache
curl -s -o nul $BASE_URL/api/v1/calendar/2019-06-05/
curl -s -o nul $BASE_URL/api/v1/calendar/2019-08-12/
curl -s -o nul $BASE_URL/api/v1/calendar/2019-09-01/
curl -s -o nul $BASE_URL/api/v1/calendar/2019-09-10/
curl -s -o nul $BASE_URL/api/v1/calendar/2019-11-10/
curl -s -o nul $BASE_URL/api/v1/calendar/2019-12-25/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-03-22/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-04-09/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-04-25/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-05-01/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-05-24/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-07-31/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-08-21/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-08-30/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-10-29/
curl -s -o nul $BASE_URL/api/v1/calendar/2020-12-25/
