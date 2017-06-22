import pymongo
from scrapy.conf import settings
from scrapy.utils.project import get_project_settings
from tutorial.spiders.fox import FoxNewsSpider
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

connection = pymongo.MongoClient(
settings['MONGODB_SERVER'],
settings['MONGODB_PORT']
)
db = connection[settings['FOX_MONGODB_DB']]
person_collection = db[settings['PERSON_COLLECTION']]
article_collection = db[settings['ARTICLE_COLLECTION']]

person_collection_result = person_collection.find({})
runner = CrawlerRunner(get_project_settings())

@defer.inlineCallbacks
def crawl():
    for person in person_collection_result:

        print(person)
        try:
            FoxNewsSpider.start_urls = person["url"]
            FoxNewsSpider.AUTHOR_FIRST_NAME = person["first_name"]
            FoxNewsSpider.AUTHOR_LAST_NAME = person["last_name"]
            yield runner.crawl(FoxNewsSpider)
        except Exception as e:
            print(e)
try:
    crawl()
    reactor.run()
    reactor.stop()
except Exception as e:
    print(e)




        