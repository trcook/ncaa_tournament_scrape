# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class myDatabase(scrapy.Item):
    region = scrapy.Field()
    round = scrapy.Field()
    team1 = scrapy.Field()
    team2 = scrapy.Field()
    year=scrapy.Field()
    team1score=scrapy.Field()
    team2score=scrapy.Field()