import scrapy

class EdmmailwormSpider(scrapy.spiders.Spider):
    name = "edm" #这个命令用于scrapy crawl edm 启动爬虫
    allowed_domains = ["dmoz.org"]
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }