# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import SitemapSpider

from indexer.items import IndexerItem

class SiteindexSpider(SitemapSpider):
    name = 'siteIndex'
    allowed_domains = ['webact.com', 'www.webact.com']
    sitemap_urls = ['https://www.webact.com/sitemap.xml']
    id = 0

    # Method for parsing items
    def parse(self, response):
        self.id += 1
        # The list of items that are found on the particular page
        item = IndexerItem()
        # incrementId
        item['id'] = self.id
        item['url'] = response.url
        item['title'] = ' '.join(response.css('title::text').extract()).strip()

        desc = response.xpath("//meta[@name='description']/@content")
        if desc:
            item['description'] = ''.join(response.xpath("//meta[@name='description']/@content").extract()).strip()
        keys = response.xpath("//meta[@name='description']/@content")
        if keys:
            item['keywords'] = response.xpath("//meta[@name='keywords']/@content").extract()

        item['h1'] = ' '.join(response.css("h1 *::text").extract()).strip()
        item['h2'] = ' '.join(response.css("h2 *::text").extract()).strip()
        item['h3'] = ' '.join(response.css("h3 *::text").extract()).strip()
        item['p'] = ' '.join(response.css("p *::text").extract()).strip()
        yield item
