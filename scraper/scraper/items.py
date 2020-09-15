# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import TakeFirst


class SplItem(Item):
    id = Field(
        output_processor=TakeFirst()
    )
    set_id = Field(
        output_processor=TakeFirst()
    )
    labeler = Field(
        output_processor=TakeFirst()
    )
    schedule = Field(
        output_processor=TakeFirst()
    )
    products = Field()


class ProductItem(Item):
    code = Field(
        output_processor=TakeFirst()
    )
    name = Field(
        output_processor=TakeFirst()
    )
    active_ingredients = Field()
    inactive_ingredients = Field()
    packages = Field()


class InactiveIngredient(Item):
    name = Field(
        output_processor=TakeFirst()
    )
    unii = Field(
        output_processor=TakeFirst()
    )


class PackageItem(Item):
    code = Field(
        output_processor=TakeFirst()
    )
