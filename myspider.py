import scrapy

class IKEASpider(scrapy.Spider):
    name = 'ikeaspider'

    def start_requests(self):
        urls = ['https://www.ikea.com/us/catalog/allproducts']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'allproducts.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('saved file allproducts.html')
