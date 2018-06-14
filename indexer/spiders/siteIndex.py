# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import SitemapSpider

from indexer.items import IndexerItem

class SiteindexSpider(SitemapSpider):
    name = 'siteIndex'

    def __init__(self, domains, sitemap, *args, **kwargs):
        super(SiteindexSpider, self).__init__(*args, **kwargs)
        self.id = 0
        self.name = 'siteIndex'
        self.domains = domains.split(',')
        self.sitemap = sitemap.split(',')

        self.allowed_domains = self.domains
        self.sitemap_urls = self.sitemap
        # self.logger.info('DOMAIN self.domains: ', self.domains)
        # self.logger.info('SITEMAP self.sitemap: ', self.sitemap)

    # Method for parsing items
    def parse(self, response):
        # incrementId
        self.id += 1
        # The list of items that are found on the particular page
        item = IndexerItem()
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