# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndexerItem(scrapy.Item):
    # The source URL
    url_from = scrapy.Field()
    # The destination URL
    # url_to = scrapy.Field()

    # Meta tags
    title = scrapy.Field()
    description = scrapy.Field()
    keywords = scrapy.Field()

    # Body tags
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    h3 = scrapy.Field()
    p = scrapy.Field()