# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno

class ClinicalPipeline(object):

    def __init__(self):
    	# try:
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db = '_chen',
            user = 'chensh',
            passwd = 'abc',
            host = 'localhost',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )
	    # except MySQLdb.Error as err:
	    # 	# print "Connection Failed!"
	    # 	log.err(err)
        
    def process_item(self, item, spider):
    	# HERE before insert, clean the item, for those attributes without any value,
    	# set to none
    	# item['CH'] = None;
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error) 
        return item

    def handle_error(self, e):
        log.err(e)

    def _conditional_insert(self, tx, item):
    	# print item['record_id'][0]


        # create record if doesn't exist. 
        # all this block run on it's own thread
        tx.execute("select * from test_record where id = %s", (item['record_id'], ))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
        else:
        	# tx.execute("insert into test_record (id, url) values (%s, %s)",('123',r'http//'))
                # "insert into test_record1 "
                # "values (%s,%s)",
                # (item['record_id'],item['url'],))            
            tx.execute(\
                "insert into test_record (id, url, FRD, LUD, SD, EPCD1, CPOM, "
                "OPOM, CH, CSOM, OSOM, COOM, OOOM, "
                "BT, OT, BS, DD, ST, SP, SDs, Co, Intv, SA, Pub, "
                "RS, EE, CD, EPCD2, EC, Gend, Age, AHV, Cont, LC, "
                "NCTN, OSID, HDMC, RP, SS, Coll, Inves, IPB, VD) " 
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (item['record_id'],
                 item['url'],
                 item['FRD'],
                 item['LUD'],
                 item['SD'],
                 item['EPCD1'],
                 item['CPOM'],
                 item['OPOM'],
                 item['CH'],
                 item['CSOM'],
                 item['OSOM'],
                 item['COOM'],
                 item['OOOM'],
                 item['BT'],
                 item['OT'],
                 item['BS'],
                 item['DD'],
                 item['ST'],
                 item['SP'],
                 item['SDs'],
                 item['Co'],
                 item['Intv'],
                 item['SA'],
                 item['Pub'],
                 item['RS'],
                 item['EE'],
                 item['CD'],
                 item['EPCD2'],
                 item['EC'],
                 item['Gend'],
                 item['Age'],
                 item['AHV'],
                 item['Cont'],
                 item['LC'],
                 item['NCTN'],
                 item['OSID'],
                 item['HDMC'],
                 item['RP'],
                 item['SS'],
                 item['Coll'],
                 item['Inves'],
                 item['IPB'],
                 item['VD'],
                 )
            )

            log.msg("Item stored in db: %s" % item, level=log.DEBUG)





