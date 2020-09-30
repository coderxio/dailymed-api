[<img src="https://img.shields.io/badge/slack-@CodeRx-blue.svg?logo=slack">](https://coderx.slack.com) [![Build Status](https://travis-ci.org/coderxio/dailymed-api.svg?branch=master)](https://travis-ci.org/coderxio/dailymed-api)

# DailyMed API
## Available at [api.coderx.io](http://api.coderx.io)
### Endpoint(s)
- [/SPL](http://api.coderx.io/spl)  
   Filter by set_id, labeler, package_ndc, product_ndc, product_name, inactive_ingredient_name, inactive_ingredient_unii or schedule  
   Example filter by schedule: http://api.coderx.io/spl/?schedule=ciii

### Docker Containers
#### Docker Development Usage
**This method is intended for internal testing only.  It has not been secured for external access.**
##### Steps:
1. Create docker container `docker-compose up -d` to bring up the Django API
2. Optional: load the database `docker-compose exec -d api sh -c "cd /dailymed-api/scraper/ && scrapy crawl json_extract"`  
   An alternate command is `docker exec -d -it -w /dailymed-api/scraper dailymed-api scrapy crawl json_extract`

#### Docker Production Usage
**This method is for using docker-compose.prod.yml**
##### Prep:
- Update secret in Django settings.py
- Disable debug mode in Django settings.py
- Install & configure Nginx to serve static folder and proxy Gunicorn
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

### Dependencies
This project uses poetry but its not necessary to install. It does require scrapy and python >= 3.7.

#### Usage
1. Create data dir
2. download spl archive zip to data/
3. Run `extract_zips.py`, this will extract just the spl xml files into data/partial/
4. cd into scraper/
5. Run `scrapy crawl basic_extract -o basic_extract.csv -t csv`, to generate a csv

#### Scrapy Integration
In order to use django models within scrapy the `PYTHONPATH` env variable must be set. To set this env var use, run `export PYTHONPATH=/home/<your-user-name>/path/to/django/project`. As an example to set this on my ubuntu machine I would run `export PYTHONPATH=/home/yevgeny/workspace/dailymed-api/api`. In future iterations of this repo, this process will be automated. 

#### Django Usage

1. cd into the `api/` dir and execute `./manage.py migrate` to create a sqlite db.
2. cd into the `scraper/` dir and run `scrapy crawl json_extract` to populate the db.

### Django Rest Framework API Usage

1. cd into the `api/` dir and execute `./manage.py runserver 0.0.0.0:8000` to start the API server
2. In a web browser, open up `localhost:8000`
