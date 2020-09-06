# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class SmzdmItem(scrapy.Item):
    name = scrapy.Field()
    input_time = scrapy.Field()
    comment = scrapy.Field()
    sentiments = scrapy.Field()