#!usr/bin/python
#coding=utf-8

import scrapy
class DmozSpider(scrapy.Spider): # 继承Spider类
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2] # 获取url，用”/”分段，获去倒数第二个字段
        print filename,22222222
        print response,111111111111
        with open(filename, 'a') as f:
            f.write(response.body) # 把访问的得到的网页源码写入文件
