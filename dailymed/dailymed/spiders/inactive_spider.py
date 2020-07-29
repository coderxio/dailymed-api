import scrapy
from scrapy.loader import ItemLoader
from pathlib import Path
from dailymed.items import InactiveItem

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

        il = ItemLoader(item=InactiveItem(), selector=document)
        il.add_value('spl_path', response.url)
        il.add_value('spl_file', Path(response.url).stem)
        il.add_xpath('text', '//paragraph[contains(text(), "inactive")]/text()')
        il.add_xpath('drug_name', '//manufacturedProduct/manufacturedProduct/name/text()')
        yield il.load_item()
