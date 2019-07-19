# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {
            'email':'xxx',
            'password':'xxxx'
        }

        # scrapy.FormRequest 处理post请求
        request = scrapy.FormRequest(url=url,formdata=data,callback=self.parse_page)
        yield request


    def parse_page(self,response):

        yield scrapy.Request(
            url='http://www.renren.com/880151247/profile',
            callback=self.parse_person
        )



    def parse_person(self,response):
        with open("dapen.txt",'w',encoding='utf-8') as f:
            f.write(response.text)