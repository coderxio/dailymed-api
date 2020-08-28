# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SetItem(scrapy.Item):
    name = scrapy.Field()
    spls = scrapy.Field()

class SplItem(scrapy.Item):
    name = scrapy.Field()
    ndcs = scrapy.Field()

class NdcItem(scrapy.Item):
    value = scrapy.Field()
