# Rest API for Pakistan Holidays
This repo is created to display hijri calendar and Pakistani holidays via restful API. 
Data is obtained from official [pakmoonsighting.com.pk] government website. 

### Demo website
* [Moon calendar] - Mooncalendar Hosted on Azure Cloud Platform


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


 [Moon calendar]: <https://mooncalendar.azurewebsites.net>
[pakmoonSighting.com.pk]: <http://pakmoonsighting.pk> 