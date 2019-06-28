-- psql -U postgres
SELECT table_name
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE 'hijr_%';
/*  
DROP TABLE hijri_calendar_app_holiday CASCADE;
DROP TABLE hijri_calendar_app_datafile CASCADE;
DROP TABLE hijri_calendar_app_holidayaliaslist CASCADE;
DROP TABLE hijri_calendar_app_holidaycountrylist CASCADE;
DROP TABLE hijri_calendar_app_holidayoriginlist CASCADE;
DROP TABLE hijri_calendar_app_hijricalendar CASCADE;
DROP TABLE hijri_calendar_app_holiday_alias_names CASCADE;
DROP TABLE hijri_calendar_app_holiday_country CASCADE;
DROP TABLE hijri_calendar_app_hijricalendar_holiday_list CASCADE;
DROP TABLE hijri_calendar_app_holiday_region CASCADE;
DROP TABLE hijri_calendar_app_holidayregionlist CASCADE;
*/