[<img src="https://img.shields.io/badge/slack-@CodeRx-blue.svg?logo=slack">](https://coderx.slack.com) [![Build Status](https://travis-ci.org/coderxio/dailymed-api.svg?branch=master)](https://travis-ci.org/coderxio/dailymed-api)

# DailyMed API
## Available at [api.coderx.io](http://api.coderx.io)
### Endpoint(s)
- [/SPL](http://api.coderx.io/spl)  
   Filter by set_id, labeler, package_ndc, product_ndc, product_name, inactive_ingredient_name, inactive_ingredient_unii or schedule  
   Example filter by schedule: http://api.coderx.io/spl/?schedule=CIII

### Docker Containers
#### Docker Development Usage
**This method is intended for internal testing only.  It has not been secured for external access.**
##### Prep:
- Download SPL zip files `python3 get_zips.py`  
   Example parameter to download SPL zip 4 and unpack 100 SPL files `python3 get_zips.py --select 4 --unzip 100`  
   For further assistance `python3 get_zips.py -h`
##### Steps:
1. Create docker container `docker-compose up -d` to bring up the Django API
2. Optional: load the database `docker-compose exec -d api sh -c "cd /dailymed-api/scraper/ && scrapy crawl json_extract"`  
   An alternative command is `docker exec -d -it -w /dailymed-api/scraper dailymed-api scrapy crawl json_extract`

#### Docker Production Usage
**This method is for using docker-compose.prod.yml**
##### Prep:
- Update secret in Django settings.py
- Disable debug mode in Django settings.py
- Install & configure Nginx to serve static folder and proxy Gunicorn
- Download SPL zip files `sudo -u www-data python3 get_zips.py`
##### Steps:
1. Create directory `mkdir /opt/dailymed`
2. Change owner `chown www-data:www-data /opt/dailymed`
3. Change directory `cd /opt/dailymed`
4. Clone repo `sudo -u www-data git clone https://github.com/coderxio/dailymed-api`  
   An alternative command is `git clone https://github.com/coderxio/dailymed-api && chown -R www-data:www-data /opt/dailymed`  
5. Change directory `cd dailymed-api`
6. Create docker container `docker-compose -f docker-compose.prod.yaml up --build -d`
7. Optional: load the database `docker-compose exec -d api sh -c "cd /dailymed-api/scraper/ && scrapy crawl json_extract"`  
   An alternative command is `docker exec -d -it -w /dailymed-api/scraper dailymed-api scrapy crawl json_extract`