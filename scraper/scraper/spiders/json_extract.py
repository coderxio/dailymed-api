import scrapy
from scrapy.loader import ItemLoader
from scraper.utils import get_filenames
from scraper.items import SplItem, ProductItem, PackageItem


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
            #  product_il.add_xpath('active_ing', './/ingredient[starts-with(@classCode, "ACT")]/ingredientSubstance/name/text()')
            #  product_il.add_xpath('inactive_ing', './/ingredient[starts-with(@classCode, "IACT")]/ingredientSubstance/name/text()')

            for package in product.xpath('.//containerPackagedProduct'):
                package_il = ItemLoader(item=PackageItem(), selector=package)
                package_il.add_xpath('code', './code/@code')

                if not package_il.load_item():
                    continue

                product_il.add_value('packages', package_il.load_item())


            spl_il.add_value('products', product_il.load_item())


        return spl_il.load_item()
