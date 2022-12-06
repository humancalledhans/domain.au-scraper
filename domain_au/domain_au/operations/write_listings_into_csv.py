import csv
import re
from selenium.webdriver import ActionChains
from src.singleton.all_links_to_scrape import AllLinksToScrape
from src.operations.get_listing_data import get_listing_data
from src.operations.driver_setup import driver_setup
from src.assumptions.rent_data import get_rent_data
from src.assumptions.sale_data import get_sale_data
from src.singleton.all_listings import AllListings
from src.operations.pause_until_loaded import pause_until_loaded


def write_listings_into_csv():
    LISTINGS_PAGE_REGEX = "https://www.domain.com.au/((\w+)(-\w+)*)"

    rent_data = get_rent_data()
    sale_data = get_sale_data()

    rent_links_match = re.findall(LISTINGS_PAGE_REGEX, rent_data)
    sale_links_match = re.findall(LISTINGS_PAGE_REGEX, sale_data)

    all_rent_links = []
    for match in rent_links_match:
        all_rent_links.append(match[0])
        all_links_to_scrape_instance = AllLinksToScrape.get_instance()
        all_links_to_scrape_instance.add_to_links_list(
            self=all_links_to_scrape_instance, link=f"https://domain.com.au/{match[0]}")

    print("len all result page", len(all_rent_links))

    # driver = driver_setup()
    # a = ActionChains(driver)
    # driver.get(f"https://domain.com.au/{match[0]}")
    # (driver, a) = pause_until_loaded(driver, a)
    # get_listing_data(driver, a)

    all_sale_links = []
    for match in sale_links_match:
        all_sale_links.append(match[0])
        all_links_to_scrape_instance = AllLinksToScrape.get_instance()
        all_links_to_scrape_instance.add_to_links_list(
            self=all_links_to_scrape_instance, link=f"https://domain.com.au/{match[0]}")

    print("len all result page", len(all_sale_links))

    all_links_to_scrape_instance = AllLinksToScrape.get_instance()
    print("len of all links", len(all_links_to_scrape_instance.get_links_list(
        self=all_links_to_scrape_instance)))
    # driver = driver_setup()
    # a = ActionChains(driver)
    # driver.get(f"https://domain.com.au/{match[0]}")
    # (driver, a) = pause_until_loaded(driver, a)
    # get_listing_data(driver, a)

    # listings_singleton = AllListings.get_instance()
    # with open('listings.csv', 'w') as csvfile:
    #     writer = csv.writer(csvfile)
    #     header = ['Title', 'Address', 'Number of Residences', 'Number of Floors',
    #               'Number of Buildings', 'Type', 'Highlights', 'Description']
    #     writer.writerow(header)
    #     for listing in listings_singleton.get_all_listings_list(self=listings_singleton):
    #         writer.writerow([listing.title, listing.address, listing.num_of_residences,
    #                          listing.num_of_floors, listing.num_of_buildings, listing.type, listing.highlights_list, listing.description_list])


if __name__ == '__main__':
    write_listings_into_csv()
