[<img src="https://img.shields.io/badge/slack-@CodeRx-blue.svg?logo=slack">](https://coderx.slack.com) [![Build Status](https://travis-ci.org/coderxio/dailymed-api.svg?branch=master)](https://travis-ci.org/coderxio/dailymed-api)

# DailyMed API

This project uses poetry but its not necessary to install. It does require scrapy and python > 3.6.  This is really more of an experimental repo, there are a lot of caveats and really bugs with how this works but can serve as a starting point!

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