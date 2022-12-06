# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Listing(scrapy.Item):
    title = scrapy.Field()
    address = scrapy.Field()
    num_of_residences = scrapy.Field()
    num_of_floors = scrapy.Field()
    num_of_buildings = scrapy.Field()
    listing_type = scrapy.Field()
    property_additional_features = scrapy.Field()
    property_features = scrapy.Field()
    full_highlights = scrapy.Field()
    full_description = scrapy.Field()
    agent_name = scrapy.Field()
    agency_href = scrapy.Field()


class Agency(scrapy.Item):
    agency_name = scrapy.Field()
    agency_link = scrapy.Field()
