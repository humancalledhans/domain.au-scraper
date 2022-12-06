import asyncio
from src.singleton.all_listings import AllListings
from src.operations.write_listings_into_csv import write_listings_into_csv
from src.operations.get_listing_data import get_listing_data
from src.operations.pause_until_loaded import pause_until_loaded
from src.operations.driver_setup import driver_setup
from src.operations.gather_all_links_to_scrape import gather_all_links_to_scrape
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def playing_around():
    gather_all_links_to_scrape()


    # # code to get eric his data
    # driver = driver_setup()
    # a = ActionChains(driver)
    # driver.get(
    #     "https://www.domain.com.au/34-willowie-road-castle-cove-nsw-2069-2018174971")
    # (driver, a) = pause_until_loaded(driver, a)

    # get_listing_data(driver, a)

    # write_listings_into_csv()

    # for link in links_to_scrape:
    # confirm_btn = driver.find_element(
    #     By.XPATH, "//button[@class='slick-arrow slick-next']")
    # a.move_to_element(confirm_btn).click(confirm_btn).perform()
    # (driver, a) = pause_until_loaded(driver, a)
    # //div[@class='css-sl94cg']//input
if __name__ == '__main__':
    # playing_around()
    write_listings_into_csv()
