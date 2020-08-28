# DailyMed Extracts

This project uses poetry but its not necessary to install. It does require scrapy and python > 3.6.  This is really more of an experimental repo, there are a lot of caveats and really bugs with how this works but can serve as a starting point!

#### Usage

1. Create data dir
2. download spl archive zip to data/
3. Run `extract_zips.py`, this will extract just the spl xml files into data/partial/
4. cd into dailymed/
5. Run `scrapy crawl basic_extract -o basic_extract.csv -t csv`, to generate a csv

#### Scrapy Integration

In order to use django models within scrapy the `PYTHONPATH` env variable must be set. To set this env var use, run `export PYTHONPATH=/home/<your-user-name/path/to/django/project`. As an example to set this on my ubuntu machine I would run `export PYTHONPATH=/home/yevgeny/workspace/dm_extracts/api`. In future iterations of this repo, this process will be automated. 
