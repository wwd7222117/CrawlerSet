# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

class ChengfengPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        scrapy_db = client['chengfeng']
        self.coll = scrapy_db['price']

    def process_item(self, item, spider):
        self.coll.insert_one(dict(item))
        print('成功！！！！！！！！！！！！！！！！！！！！！！！！')
        #self.coll.update_one(dict(item),{'$set':(dict(item))},upsert=True)
        return item
    def close_spider(self,spider):
        self.client.close()