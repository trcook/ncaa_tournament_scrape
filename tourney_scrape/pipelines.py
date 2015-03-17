# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import csv
import json

class EspnPipeline(object):
    def open_spider(self,spider):
        self.file = open('items.csv', 'wb')
        self.writer=csv.writer(self.file,quoting=csv.QUOTE_MINIMAL)

    def process_item(self, item, spider):
        if spider.name not in ['espn']:
            return item
        if item['rank']==[]:
            item['rank']=[-1]

        if item['rank']==['RK']:
            return

        if item['rank']==['2014-15 RPI']:
             item['rank']=[]
             item['rows']=[]

        tmp=[item['name'],item['year'],item['row']]
        self.writer.writerow([j for i in tmp for j in i])
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()


class ScorePipeline(object):
    def open_spider(self,spider):
        self.file = open('item_score.csv', 'wb')
        self.writer=csv.writer(self.file,quoting=csv.QUOTE_MINIMAL)

    def process_item(self, item, spider):
        if spider.name not in ['score']:
            return item

        flat_row=[j for i in item['row'] for j in i]
        flat_row.append( item['name'][0])
        # flat_row.append(item['year'])
        self.writer.writerow(flat_row)
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()