import pymongo
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy.conf import settings
from tutorial.items import FoxPerson
from tutorial.items import FoxArticle

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item




class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['FOX_MONGODB_DB']]
        self.person_collection = db[settings['PERSON_COLLECTION']]
        self.article_collection = db[settings['ARTICLE_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        if isinstance(item, FoxPerson):
            person_exists = self.person_collection.find({'url': item['url']}, {"url": 1}).count()
            if person_exists == 0:
                self.person_collection.insert(dict(item))

        if isinstance(item, FoxArticle):
            article_exists = self.article_collection.find({'url': item['url']}, {"url": 1}).count()
            if article_exists == 0:
                self.article_collection.insert(dict(item))



        