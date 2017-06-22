

from scrapy.spiders import Rule
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess





class FoxNewsSpider(Spider):
    name = "test"
    allowed_domains = ["foxnews.com"]
    start_urls = ["http://www.foxnews.com/person/a/keith.html"]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="button next"]',)), callback="parse_items",
             follow=True),
    )

    def parse(self, response):
        self.start_urls.append("http://api.foxnews.com/v2/person?site=fox-news&role=personality&rows=300&callback=fo")
        page = response.url.split("/")[-2]
        filename = 'test.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def parse_items(self, response):
            print('##############################################################################')
            page = response.url.split("/")[-2]
            filename = 'test.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)


#process = CrawlerProcess({
 #   'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#})

#process.crawl(FoxNewsSpider,start_urls = ["http://www.foxnews.com/person/a/keith-ablow.html"] )
#process.start()