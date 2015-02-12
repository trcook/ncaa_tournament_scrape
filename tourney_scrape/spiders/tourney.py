# -*- coding: utf-8 -*-
import scrapy
from tourney_scrape.items import myDatabase
import re


class TourneySpider(scrapy.Spider):
    name = "tourney"
    allowed_domains = "databasesports.com"
    start_urls = []
    for i in range(1975,2014,1):
        start_urls.append('http://www.databasesports.com/ncaab/tourney.htm?yr=%d' % i)

    def chunks(self,l, n):
        n = max(1, n)
        return [l[i:i + n] for i in range(0, len(l), n)]

    def parse(self, response):
        for i in response.xpath("//tr[@class='region']/ancestor::table|//td[@class='region']/ancestor::table"):
            for j in range(1, 5, 1):
                out = i.xpath(".//tr[@class='tourney']/td[@valign='middle'][%d]/a/text()" % j).extract()
                out=self.chunks(out,2)
                outscore = i.xpath(".//tr[@class='tourney']/td[@valign='middle'][%d]" % j).extract()
                outscore = re.findall(r'teamid.*?/a>.*?(\d{1,3})',str(outscore))
                outscore=self.chunks(outscore,2)
                for idx,m in enumerate(out):
                    if len(m)>1:
                        scrap_record = myDatabase()
                        scrap_record['year']=response.url[len(response.url)-4:len(response.url)]
                        scrap_record['round'] = j
                        scrap_record['team1'] = m[0]
                        scrap_record['team2'] = m[1]
                        scrap_record['team1score']=outscore[idx][0]
                        scrap_record['team2score']=outscore[idx][1]
                # out=list(chain.from_iterable(out))
                #   scrap_record['matchups']
                        scrap_record['region'] = i.xpath("./tr[@class='region']/td/text()|.//td[@class='region']/text()").extract()
                        yield scrap_record

