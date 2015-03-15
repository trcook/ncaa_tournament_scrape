# -*- coding: utf-8 -*-
import scrapy
from tourney_scrape.items import myDatabase
from tourney_scrape.items import *
import re


class ScoreSpider(scrapy.Spider):
    name = "score"
    allowed_domains = "databasesports.com"
    start_urls = []
    for i in range(2003,2010,1):
        start_urls.append('http://www.cbssports.com/collegebasketball/bracketology/sos/%(start)d-%(end)d' % {"start":i,"end":i+1})
        print(start_urls)

    def chunks(self,l, n):
        n = max(1, n)
        return [l[i:i + n] for i in range(0, len(l), n)]

    def parse(self, response):
        # yeild yr
        year =response.request.url[-9::]
        cols=Cbstablecols()
        cols['year']=year
        cols['rows']=response.xpath("//table[@class='data']//tr[position() < 4]").extract()
        for i in response.xpath("//table[@class='data']//tr[position()>3]"):
            scrapy_record=mycbstable()
            scrapy_record['year']=year
            scrapy_record['name']=i.xpath("./td/a/text()").extract()
            tab_row=[year]
            for j in i.xpath(".//td"):
                tab_row.append(j.xpath("./text()").extract())
            scrapy_record['row']=tab_row
            yield scrapy_record



class ScorenamesSpider(scrapy.Spider):
    name = "score_names"
    allowed_domains = "databasesports.com"
    start_urls = []
    for i in range(2003,2010,1):
        start_urls.append('http://www.cbssports.com/collegebasketball/bracketology/sos/%(start)d-%(end)d' % {"start":i,"end":i+1})
        print(start_urls)

    def chunks(self,l, n):
        n = max(1, n)
        return [l[i:i + n] for i in range(0, len(l), n)]

    def parse(self, response):
        # yeild yr
        year =response.request.url[-9::]
        cols=Cbstablecols()
        cols['year']=year
        cols['rows']=response.xpath("//table[@class='data']//tr[position() < 4]").extract()
        yield cols

        # for i in response.xpath("//tr[@class='region']/ancestor::table|//td[@class='region']/ancestor::table"):
        #     for j in range(1, 5, 1):
        #         out = i.xpath(".//tr[@class='tourney']/td[@valign='middle'][%d]/a/text()" % j).extract()
        #         out=self.chunks(out,2)
        #         outscore = i.xpath(".//tr[@class='tourney']/td[@valign='middle'][%d]" % j).extract()
        #         outscore = re.findall(r'teamid.*?/a>.*?(\d{1,3})',str(outscore))
        #         outscore=self.chunks(outscore,2)
        #         for idx,m in enumerate(out):
        #             if len(m)>1:
        #                 scrap_record = myDatabase()
        #                 scrap_record['year']=response.url[len(response.url)-4:len(response.url)]
        #                 scrap_record['round'] = j
        #                 scrap_record['team1'] = m[0]
        #                 scrap_record['team2'] = m[1]
        #                 scrap_record['team1score']=outscore[idx][0]
        #                 scrap_record['team2score']=outscore[idx][1]
        #         # out=list(chain.from_iterable(out))
        #         #   scrap_record['matchups']
        #                 scrap_record['region'] = i.xpath("./tr[@class='region']/td/text()|.//td[@class='region']/text()").extract()
        #                 yield scrap_record

