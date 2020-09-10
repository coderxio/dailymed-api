# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from dailymed.models import Set


class ScraperPipeline:
    def process_item(self, item, spider):
        print('Item pipeline processing \n')
        set_id = item.pop('set_id')
        products_data = item.pop("products")
        set = Set.objects.create(id=set_id)
        spl = set.spls.create(**item)

        for product_data in products_data:
            packages_data = product_data.pop('packages')
            product = spl.products.create(**product_data)
            print('Product data\n', product_data)
            for package_data in packages_data:
                product.packages.create(**package_data)
                print('Package data\n', package_data)
        return item
