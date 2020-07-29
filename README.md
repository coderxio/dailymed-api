# DailyMed Extracts

This project uses poetry but its not necessary to install. It does require scrapy and python > 3.6.  This is really more of an experimental repo, there are a lot of caveats and really bugs with how this works but can serve as a starting point!

#### Usage

1. Create data dir
2. download spl archive zip to data/
3. Run `extract_data.py`, this will extract just the spl xml files into data/partial/
4. cd into dailymed/
5. Run `scrapy crawl inactive -o inactive.csv -t csv`, to generate a csv
