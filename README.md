# Restful API for Pakistani Holidays
This repo is created to display hijri calendar and Pakistani holidays via restful API. 
Data is obtained from official [pakmoonsighting.com.pk] government website. 

### Demo links
* [Pak Holidays Website] - Mooncalendar website is hosted on Azure Cloud Platform
* [Holidays API] - The Holiday API provides access to public holidays observed in Pakistan. API is public and require no authenticatation for read-only access.
* [Calendar API] - The Calendar API provides access to two years (Y2019 and Y2020) worth of hijri calendar data. API is public and require no authenticatation for read-only access.


### Installation

#### Pre-requisites: 

You need docker and docker-compose to run the website.

##### Method 1: Pull image from docker hub

```sh
docker pull -t bilgrami/hijricalendar:latest
```

##### Method 2: Build image on your local machine

```sh
git clone https://github.com/bilgrami/hijri-calendar.git
cd hijri-calendar
docker build -t bilgrami/hijricalendar:latest .
```

After building docker image, bring up the container:

```sh
docker-compose up
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:5000
```

----


[Pak Holidays Website]: <https://mooncalendar.azurewebsites.net>
[pakmoonSighting.com.pk]: <http://pakmoonsighting.pk> 
[Holidays API]: <https://mooncalendar.azurewebsites.net/api/v1/holiday/>
[Calendar API]: <https://mooncalendar.azurewebsites.net/api/v1/calendar/>
