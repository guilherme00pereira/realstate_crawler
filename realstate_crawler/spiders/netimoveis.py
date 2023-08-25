from pathlib import Path
import scrapy

class VivaRealSpider(scrapy.Spider):
    name = 'vivareal'

    def start_requests(self):
        urls = [
            ''
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        pass