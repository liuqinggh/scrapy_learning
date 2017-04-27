# -*- coding: utf-8 -*-


import MySQLdb 
import datetime
from scrapy.conf import settings
from .items import LianjiaspiderItem

class LianjiaspiderPipeline(object):
    def __init__(self):
        host = settings['MYSQL_HOST']
        db_name = settings['MYSQL_DBNAME']
        userid = settings['MYSQL_USER']
        pswd = settings['MYSQL_PASSWD']
        port = settings['MYSQL_PORT']
        self.conn = MySQLdb.connect(host=host, user=userid, passwd=pswd, db=db_name, port=port)
        self.conn.set_character_set('utf8')
        self.cur = self.conn.cursor()
    
    def process_item(self, item, spider): 
				curTime =  datetime.datetime.now()
				try:
				    self.cur.execute('insert into ershoufang_cd(title, community, ins_time, mod_time) values(%s,%s,%s,%s)'\
				    %(item["title"],item["community"], curTime, curTime))
				except MySQLdb.Error, e:
				    print "Error %d: %s" % (e.args[0], e.args[1])
				print item
				return item
				
