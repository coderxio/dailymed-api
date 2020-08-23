import scrapy
from scrapy.loader import ItemLoader
from pathlib import Path

def get_filenames():
    cwd = Path(__file__)
    partial_dir = cwd.parent.parent.parent.parent.absolute() / 'data' / 'partial'
    adjusted_filenames = [ f'file://{path}' for path in list(partial_dir.iterdir()) ]
    return adjusted_filenames

class InactiveSpider(scrapy.Spider):
    name = 'inactive'
    start_urls = get_filenames()

    def parse(self, response):
        response.selector.remove_namespaces()
        document = response.xpath("//document")
        manu_products = document.xpath('.//subject/manufacturedProduct/manufacturedProduct')

        for manu_product in manu_products:
            for ndc in manu_product.xpath('.//containerPackagedProduct/code/@code').getall():
                data_dict = {
                    'set_id': document.xpath('./setId/@root').get(),
                    'spl_id': document.xpath('./id/@root').get(),
                    'org': document.xpath('.//representedOrganization/name/text()').get(),
                    'ndc': ndc,
                    'schedule': document.xpath('.//policy/code/@displayName').get(),
                    'name': manu_product.xpath('./name/text()').get(),
                    'active': manu_product.xpath('.//ingredient[starts-with(@classCode, "ACT")]//name/text()').get(),
                    'inactive': manu_product.xpath('.//ingredient[@classCode="IACT"]//name/text()').getall()
                }

                yield data_dict
