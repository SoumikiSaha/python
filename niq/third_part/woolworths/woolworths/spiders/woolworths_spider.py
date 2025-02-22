import scrapy
from woolworths.items import WoolworthsItem

class WoolworthsSpider(scrapy.Spider):
    name = "woolworths"
    start_urls = [
        "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"
    ]

    def parse(self, response):
        # Extract and clean the breadcrumb text
        breadcrumbs = response.xpath('//ul[contains(@class, "breadcrumbs-linkList")]/li/a/span/text()').getall()
        breadcrumbs = [breadcrumb.strip() for breadcrumb in breadcrumbs if breadcrumb.strip()]  # Remove extra whitespace

        # Create a single item for the breadcrumbs
        item = WoolworthsItem()
        item['breadcrumb'] = breadcrumbs
        yield item