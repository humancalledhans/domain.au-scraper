import time
from src.singleton.all_listings import AllListings
from src.objects_model.listing_object import ListingObject
from src.operations.pause_until_loaded import pause_until_loaded
from src.operations.driver_setup import driver_setup
from src.operations.gather_all_links_to_scrape import gather_all_links_to_scrape
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException


def get_listing_data(driver, a):
    # title works
    try:
        title = driver.find_element(
            By.XPATH, "//div[contains(@data-testid,'summary-title')]").text
    except NoSuchElementException:
        title = ''

    try:
        address = driver.find_element(
            By.XPATH, "//div[@data-testid='listing-details__button-copy-wrapper']").text
    except NoSuchElementException:
        address = ''

    # num of residences works
    try:
        num_of_residences = driver.find_element(
            By.XPATH, "//div[contains(@data-testid,'totalNumberOfResidences')]").text
    except NoSuchElementException:
        num_of_residences = ''

    try:
        num_of_floors = driver.find_element(
            By.XPATH, "//div[@data-testid='listing-details-feature-floorCount']//span").text
    except NoSuchElementException:
        num_of_floors = ''

    try:
        num_of_buildings = driver.find_element(
            By.XPATH, "//div[@data-testid='listing-details-feature-numberOfBuildings']//span").text
    except NoSuchElementException:
        num_of_buildings = ''

    try:
        type = driver.find_element(
            By.XPATH, "//div[@data-testid='listing-details-feature-propertyTypes']//span").text
    except NoSuchElementException:
        type = ''

    try:
        highlights = driver.find_elements(
            By.XPATH, "//div[@data-testid='listing-details__listing-summary-key-selling-points-list'][1]//div[@class='css-1dfcg0y']")
        full_highlights = ''
        for h in highlights:
            full_highlights = full_highlights + h.text + ' '

    except NoSuchElementException:
        full_highlights = ''

    try:
        read_more_btn = driver.find_element(
            By.XPATH, "//button[@type = 'button' and @data-testid = 'listing-details__description-button']")

        a.move_to_element(read_more_btn).click().perform()
        (driver, a) = pause_until_loaded(driver, a)

        # description works
        description = driver.find_elements(
            By.XPATH, "//div[@name='listing-details__description']//p")
        full_description = ""
        print("len of description" + str(len(description)))
        for d in description:
            if d.text != '':
                full_description = full_description + d.text + ' '

    except NoSuchElementException:
        full_description = ''

    print("title", title)
    print("address", address)
    print("num_of_residences", num_of_residences)
    print("num_of_floors", num_of_floors)
    print("num_of_buildings", num_of_buildings)
    print("type", type)
    print("highlights", full_highlights)
    print("description", full_description)

    all_listings_singleton = AllListings.get_instance()
    all_listings_singleton.add_to_all_listings_list(self=all_listings_singleton, listing=ListingObject(title, address, num_of_residences, num_of_floors,
                                                                                                       num_of_buildings, type, full_highlights.strip(), full_description.strip()))
