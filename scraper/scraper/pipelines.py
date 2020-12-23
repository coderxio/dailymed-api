# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from scraper.utils import get_rxnorm
from dailymed.models import Set, InactiveIngredient


class ScraperPipeline:
    def process_item(self, item, spider):
        set_id = item.pop('set_id')
        products_data = item.pop('products')
        set = Set.objects.create(id=set_id)
        spl = set.spls.create(**item)

        for product_data in products_data:
            packages_data = product_data.pop('packages')
            inactive_ingredients_list = []

            if 'inactive_ingredients' in product_data:
                inactive_ingredients_data = product_data.pop(
                    'inactive_ingredients'
                )
                for inactive_ingredient_data in inactive_ingredients_data:
                    try:
                        ingredient = InactiveIngredient.objects.get(
                            **inactive_ingredient_data
                        )
                        inactive_ingredients_list.append(ingredient)
                    except Exception:
                        ingredient = InactiveIngredient.objects.create(
                            **inactive_ingredient_data
                        )
                        inactive_ingredients_list.append(ingredient)

            product = spl.products.create(**product_data)

            product.inactive_ingredients.add(*inactive_ingredients_list)

            for package_data in packages_data:
                product.packages.create(**package_data)

        return item

    def close_spider(self, spider):
        print("loading rxnorm data")
        columns = ['setId', 'splVersion', 'rxcui', 'rxstring', 'rxtty']
        with open(get_rxnorm()[0], newline='') as csvfile:
            rxreader = csv.reader(csvfile, delimiter='|')
            for row in rxreader:
                data = dict(zip(columns, row))
                data.pop('splVersion')
                setId = data.pop('setId')
                try:
                    setObj = Set.objects.get(id=setId)
                except Exception:
                    continue
                setObj.rxnorms.create(**data)
