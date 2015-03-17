# -*- coding: utf-8 -*-
import scrapy
# from tourney_scrape.items import myDatabase
from tourney_scrape.items import *
import re


class EspnSpider(scrapy.Spider):
    name = "espn"
    allowed_domains = "espn.go.com"
    start_urls = []
    for i in range(0,8,1):
        start_urls.append('http://espn.go.com/mens-college-basketball/rpi/_/page/%(start)d/sort/RPI' % {"start":i})

    def chunks(self,l, n):
        n = max(1, n)
        return [l[i:i + n] for i in range(0, len(l), n)]

    def parse(self, response):
        for i in response.xpath("//table[@class='tablehead']//tr"):
            scrapy_record=ESPNcols()
            scrapy_record['rows']=i.xpath('.//td[position()>1]//text()').extract()
            scrapy_record['rank']=i.xpath('.//td[position()=1]//text()').extract()
            if i.xpath('.//td[position()=1]/text()').extract()==[]:
                scrapy_record['rank']=[-1]


            yield scrapy_record

