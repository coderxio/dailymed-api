# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class InactiveItem(scrapy.Item):
    drug_name = scrapy.Field(
        output_processor = TakeFirst()
    )
    spl_file = scrapy.Field()
    spl_path = scrapy.Field()
    text = scrapy.Field()
