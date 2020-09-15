import scrapy
from scrapy.loader import ItemLoader
from scraper.utils import get_filenames
from scraper.items import SplItem, ProductItem, PackageItem, InactiveIngredient


class JsonSpider(scrapy.Spider):
    name = 'json_extract'
    start_urls = get_filenames()

    def parse(self, response):
        response.selector.remove_namespaces()
        document = response.xpath('//document')
        manu_products = document.xpath('.//subject/manufacturedProduct')

        spl_il = ItemLoader(item=SplItem(), selector=document)
        spl_il.add_xpath('id', './id/@root')
        spl_il.add_xpath('set_id', './setId/@root')
        spl_il.add_xpath('labeler', './/representedOrganization/name/text()')

        for product in manu_products:
            product_il = ItemLoader(item=ProductItem(), selector=product)
            product_il.add_xpath('code', './manufacturedProduct/code/@code')
            product_il.add_xpath('name', './manufacturedProduct/name/text()')

            inactive_ingredients = product.xpath(
                './/ingredient[starts-with(@classCode, "IACT")]'
            )

            for inactive_ingredient in inactive_ingredients:
                inactive_il = ItemLoader(
                    item=InactiveIngredient(),
                    selector=inactive_ingredient,
                )
                inactive_il.add_xpath(
                    'name',
                    './ingredientSubstance/name/text()',
                )
                inactive_il.add_xpath(
                    'unii',
                    './ingredientSubstance/code/@code',
                )

                product_il.add_value(
                    'inactive_ingredients',
                    inactive_il.load_item(),
                )

            for package in product.xpath('.//containerPackagedProduct'):
                package_il = ItemLoader(item=PackageItem(), selector=package)
                package_il.add_xpath('code', './code/@code')

                if not package_il.load_item():
                    continue

                product_il.add_value('packages', package_il.load_item())

            spl_il.add_value('products', product_il.load_item())

        return spl_il.load_item()
