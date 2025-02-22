import scrapy
from edeka.items import EdekaItem

class EdekaSpider(scrapy.Spider):
    name = "edeka"
    start_urls = [
        "https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel/"
    ]

    def parse(self, response):
        product_names = response.xpath('//div[@class="product-details"]/a/h2/text()').getall()

        for product_name in product_names:
            item = EdekaItem()
            item['product_name'] = product_name
            yield item