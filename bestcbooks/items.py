# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BestcbooksItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    url = Field()


class CatagoryItems(Item):
    catagory = Field()
    url = Field()


class BookPageItems(Item):
    name = Field()
    url = Field()


class BookItems(Item):
    name = Field()
    link = Field()
    password = Field()
    orig_url = Field()
