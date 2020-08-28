import scrapy
from scrapy.loader import ItemLoader
from scraper.utils import get_filenames
from scraper.items import SetItem, SplItem, NdcItem
from dailymed.models import Set, Spl, Ndc


class JsonSpider(scrapy.Spider):
    """This class is really just a proof of concept to get models working in django. This needs to be redesigned and adjusted in the future"""
    name = 'json_extract'
    start_urls = get_filenames()

    def parse(self, response):
        response.selector.remove_namespaces()
        document = response.xpath("//document")
        manu_products = document.xpath('.//subject/manufacturedProduct/manufacturedProduct')

        set_item = SetItem()
        set_item['name'] = document.xpath('./setId/@root').get()

        spl_item = SplItem()
        spl_item['name'] = document.xpath('./id/@root').get()

        ndc_list = []

        for manu_product in manu_products:
            for ndc in manu_product.xpath('.//containerPackagedProduct/code/@code').getall():
                ndc_item = NdcItem()
                ndc_item['value'] = ndc
                ndc_list.append(dict(ndc_item))

        spl_item['ndcs'] = ndc_list

        set_item['spls'] = [dict(spl_item)]

        set = Set.objects.create(name=set_item['name'])

        for spl_data in set_item['spls']:
            ndcs = spl_data.pop('ndcs')
            spl = set.spls.create(**spl_data)

            for ndc_data in ndcs:
                spl.ndcs.create(**ndc_data)
