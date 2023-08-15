from pathlib import Path

import scrapy

class ImobsSpider(scrapy.Spider):
    name = 'imobs'

    def start_requests(self):
        return super().start_requests()
    
    def parse(self, response):
        pass