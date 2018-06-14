# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urlparse import urljoin

from bestcbooks.items import CatagoryItems, BookPageItems, BookItems

class BooksSpider(Spider):
    name = 'books'
    start_urls = ['http://bestcbooks.com//']

    def parse(self, response):
        for sel in response.xpath('//ul[@id="category-list"]/li'):
            name = sel.xpath('a/text()').extract()[0]
            url = urljoin(response.url, sel.xpath('a/@href').extract()[0])

            yield response.follow(url, callback=self.parse_catagory)


    def parse_catagory(self, response):
        """Parse catagory page"""
        for sel in response.xpath('//div[@class="categorywell"]/h4'):
            name = sel.xpath('a/text()').extract()[0]
            url = urljoin(response.url, sel.xpath('a/@href').extract()[0])

            yield response.follow(url, callback=self.parse_book_page)

            item = BookPageItems()
            item['url'] = url
            item['name'] = name


    def parse_book_page(self, response):
        """parse detail book page"""
        orig_url = response.url
        name = response.xpath('//h1[@class="entry-title"]/text()').extract()
        for sel in response.xpath('//blockquote'):
            link = sel.xpath('p/a/@href').extract()
            try:
                password = sel.xpath('p/text()').extract()[-1].split()[-1][-4:]
            except:
                password = ""

            item = BookItems()
            item['name'] = name
            item['link'] = link
            item['password'] = password
            item['orig_url'] = orig_url

        yield item
