from pathlib import Path
import scrapy

class OlxSpider(scrapy.Spider):
    name = 'olx'

    def start_requests(self):
        urls = [
            'https://www.olx.com.br/imoveis/aluguel/estado-mg/belo-horizonte-e-regiao/zona-centro-sul?pe=4500&ros=3&sf=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        pass