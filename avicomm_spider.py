import scrapy
from ..items import AvicommItem


class AvicommSpider(scrapy.Spider):
    name = 'avicomm'
    start_urls = [

        'https://www.avicomm.co.ke/'
    ]

    def parse(self, response):

        items = AvicommItem()

        all_div = response.css("div.product-inner")
        for div in all_div:
            title = div.css("h3.woocommerce-loop-product__title::text").extract()
            try:
                amount = div.css("bdi::text").extract_first().replace(",", "")
            except:
                pass

            items['title'] = title
            items['amount'] = amount

            yield items