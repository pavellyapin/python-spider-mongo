# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class FoxPerson(Item):

    first_name = Field()
    last_name = Field()
    url = Field()

class FoxArticle(Item):

    author_first_name = Field()
    author_last_name = Field()
    url = Field()
    img_src = Field()
    img_alt = Field()
    date = Field()
    title = Field()
    desc = Field()
    tag = Field()




