# -*- coding: utf-8 -*-

BOT_NAME = 'LianjiaSpider'

SPIDER_MODULES = ['lianjiaspider.spiders']
NEWSPIDER_MODULE = 'lianjiaspider.spiders'

ROBOTSTXT_OBEY = False   #True


MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'test'           
MYSQL_USER = 'root'             
MYSQL_PASSWD = '111111'         

MYSQL_PORT = 3306  

ITEM_PIPELINES = {
    'lianjiaspider.pipelines.LianjiaspiderPipeline': 300
}

