# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaspiderItem(scrapy.Item):
    # ��ǩ  С��  ����   ���   ��ע����  �ۿ�����  ����ʱ��  �۸�   ����  ��������  ��γ�� ����
    title = scrapy.Field()
    community = scrapy.Field()
"""    
    model = scrapy.Field()
    area = scrapy.Field()
    focus_num = scrapy.Field()
    watch_num = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    average_price = scrapy.Field()
    link = scrapy.Field()
    Latitude = scrapy.Field()
    city = scrapy.Field()
"""