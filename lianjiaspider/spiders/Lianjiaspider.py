# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import time
from lxml import etree
from ..items import LianjiaspiderItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjiaspider'
    allowed_domains = ["cd.lianjia.com"]
    start_urls = 'http://cd.lianjia.com/ershoufang/'

    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                         Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent}
        yield scrapy.Request(url=self.start_urls, headers=headers, method='GET', callback=self.parse)

    def parse(self, response):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                         Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent}
        lists = response.body.decode('utf-8')
        selector = etree.HTML(lists)
        area_list = selector.xpath('/html/body/div[3]/div[1]/dl[2]/dd/div[1]/div/a')
        for area in area_list:
            try:
                area_han = area.xpath('text()').pop()    # 地点
                area_pin = area.xpath('@href').pop().split('/')[2]   # 拼音
                area_url = 'http://cd.lianjia.com/ershoufang/{}/'.format(area_pin)
                yield scrapy.Request(url=area_url, headers=headers, callback=self.detail_url, meta={"id1":area_han,"id2":area_pin} )
            except Exception:
                pass

    def detail_url(self,response):
        for i in range(1, 3):
            url = 'http://cd.lianjia.com/ershoufang/{}/pg{}/'.format(response.meta["id2"],str(i))
            print 'url', url
            time.sleep(2)
            try:
                contents = requests.get(url)
                contents = etree.HTML(contents.content.decode('utf-8'))
                houselist = contents.xpath('/html/body/div[4]/div[1]/ul/li')
                for house in houselist:
                    try:
                        item = LianjiaspiderItem()
                        item['title'] = house.xpath('div[1]/div[1]/a/text()').pop()
                        item['community'] = house.xpath('div[1]/div[2]/div/a/text()').pop()
                    except Exception:
                        pass
                    yield item
            except Exception:
                pass



