from scrapy.spiders import Spider
from scrapy.selector import Selector
from tutorial.items import FoxArticle

class FoxNewsSpider(Spider):
    name = "fox"
    allowed_domains = ["foxnews.com"]
    start_urls = []
    AUTHOR_FIRST_NAME = ''
    AUTHOR_LAST_NAME = ''

    def parse(self, response):

        print("Start")
        hxs = Selector(response)
        article_nodes = hxs.xpath('//article')
        articles = []

        for article in article_nodes:

            new_article = FoxArticle()
            new_article['author_first_name'] = self.AUTHOR_FIRST_NAME
            new_article['author_last_name'] = self.AUTHOR_LAST_NAME
            new_article['url'] =  article.xpath('div[@class="m"]/a/@href')[0].extract() if len(article.xpath('div[@class="m"]/a/@href'))!=0 else "N/A"
            new_article['img_src'] = article.xpath('img/@src')[0].extract() if len(article.xpath('img/@src'))!=0 else "N/A"
            new_article['img_alt'] = article.xpath('img/@alt')[0].extract() if len(article.xpath('img/@alt'))!=0 else "N/A"
            new_article['date'] = article.xpath('div[@class="date"]/text()')[0].extract() if len(article.xpath('div[@class="date"]/text()'))!=0 else "N/A"
            new_article['title'] = article.xpath('h3/a/text()')[0].extract() if len(article.xpath('h3/a/text()'))!=0 else "N/A"
            new_article['desc'] = article.xpath('p/text()')[0].extract() if len(article.xpath('p/text()'))!=0 else "N/A"
            new_article['tag'] = article.xpath('meta/@content')[0].extract() if len(article.xpath('meta/@content'))!=0 else "N/A"

            articles.append(new_article)

        return articles




