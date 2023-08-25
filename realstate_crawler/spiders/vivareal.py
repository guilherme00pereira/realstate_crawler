from pathlib import Path
import scrapy

class VivaRealSpider(scrapy.Spider):
    name = 'vivareal'

    def start_requests(self):
        urls = [
            'https://www.vivareal.com.br/aluguel/minas-gerais/belo-horizonte/apartamento_residencial/#onde=,Minas%20Gerais,Belo%20Horizonte,,,,,city,BR%3EMinas%20Gerais%3ENULL%3EBelo%20Horizonte,,,&ordenar-por=preco-total:ASC&preco-ate=4500&quartos=4&tipos=apartamento_residencial,casa_residencial,condominio_residencial,cobertura_residencial',
            'https://www.vivareal.com.br/aluguel/minas-gerais/belo-horizonte/bairros/lourdes/apartamento_residencial/#area-desde=100&onde=,Minas%20Gerais,Belo%20Horizonte,Bairros,Lourdes,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EBelo%20Horizonte%3EBarrios%3ELourdes,,,;,Minas%20Gerais,Belo%20Horizonte,Bairros,Funcion%C3%A1rios,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EBelo%20Horizonte%3EBarrios%3EFuncionarios,,,&ordenar-por=preco-total:ASC&preco-ate=4500&quartos=3&tipos=apartamento_residencial,casa_residencial,condominio_residencial,cobertura_residencial'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        pass