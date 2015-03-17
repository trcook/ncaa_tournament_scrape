# -*- coding: utf-8 -*-

# Scrapy settings for wto_scrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tourney_scrape'

SPIDER_MODULES = ['tourney_scrape.spiders']
NEWSPIDER_MODULE = 'tourney_scrape.spiders'
ITEM_PIPELINES=['tourney_scrape.pipelines.EspnPipeline','tourney_scrape.pipelines.ScorePipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wto_scrape (+http://www.yourdomain.com)'
