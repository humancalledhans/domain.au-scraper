# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter

from .items import Listing, Agency
from domain_au.singleton.all_listings import AllListings


class DomainAuPipeline:
    def process_item(self, item, spider):
        if isinstance(item, Listing):
            self.write_listing_to_csv(item)

        elif isinstance(item, Agency):
            self.write_agency_to_csv(item)
        return item

    def write_listing_to_csv(self, item):
        with open('listings.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            # for listing in listings_singleton.get_all_listings_list(self=listings_singleton):
            writer.writerow([item['title'], item['address'], item['num_of_residences'],
                             item['num_of_floors'], item['num_of_buildings'], item['listing_type'], item['property_features'],
                             item['property_additional_features'], item['full_highlights'], item['full_description'], item['agent_name'], item['agency_href']])

    def write_agency_to_csv(self, item):
        with open('agency.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            header = ['Agency Name', 'Agency Link']
            writer.writerow(header)

            writer.writerow([item['agency_name'], item['agency_link']])
