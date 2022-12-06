import time
from src.operations.interacting_and_scraping_links import interacting_and_scraping_links
from src.singleton.all_listings import AllListings
from src.singleton.all_links_to_scrape import AllLinksToScrape
from src.operations.driver_setup import driver_setup
from src.operations.pause_until_loaded import pause_until_loaded
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver


class GetAllAddressLinksFromTab:

    def __init__(self, tab_link):
        self.tab_link = tab_link

    def get_all_address_links_from_tab(self):
        driver = driver_setup()
        a = ActionChains(driver)
        driver.get(self.tab_link)

        (driver, a) = pause_until_loaded(driver, a)

        self.try_and_get_dream_homes_and_home_designs_to_inspire_you_links(
            driver, a)
        self.try_and_get_the_block_links(driver, a)

        self.try_and_get_newly_released_links(driver, a)
        self.try_and_get_new_developments(driver, a)
        self.try_and_get_home_designs_to_inspire_you_links(driver, a)

    def try_and_get_the_block_links(self, driver, a):
        base_xpath_for_right_click_arrow = "//div[@data-testid='domain-the-block']"
        base_xpath = "//div[@data-testid='the-block-listing-item']"
        print('scraping block links')
        interacting_and_scraping_links(
            driver, a, base_xpath, base_xpath_for_right_click_arrow)

    def try_and_get_dream_homes_and_home_designs_to_inspire_you_links(self, driver, a):
        # newly released has the same base x path too.
        base_xpath_for_right_click_arrow = "//div[@data-testid='domain-dream-homes']"
        base_xpath = "//div[@data-testid='domain-dream-homes']//div[contains(@class,'slick-slide slick-active')]"
        print('get dream homes and home designs')

        interacting_and_scraping_links(
            driver, a, base_xpath, base_xpath_for_right_click_arrow)

    def try_and_get_newly_released_links(self, driver, a):
        base_xpath = "//div[@data-testid='domain-newly-released']"

        print('get newly released')
        interacting_and_scraping_links(driver, a, base_xpath, base_xpath)

    def try_and_get_home_designs_to_inspire_you_links(self, driver, a):
        base_xpath = "//div[@data-testid='domain-home-designs']"

        print('get home designs')
        interacting_and_scraping_links(driver, a, base_xpath, base_xpath)

    def try_and_get_new_developments(self, driver, a):
        # base_xpath = "//div[@data-testid='featured-projects']"
        base_xpath = "//div[@data-testid='featured-projects-card']"

        print('get new developments')
        interacting_and_scraping_links(driver, a, base_xpath, base_xpath)


"""
for Dream Homes: //div[@class='css-fz49w8']
for The Block 2022 Properties: //div[@class='css-1t7a3eq']

Dream Homes right arrow: //div[@data-testid='domain-dream-homes']//button[@class='slick-arrow slick-next']
The Block 2022 Properties right arrow: //div[@data-testid='domain-the-block-wrapper']//button[@class='slick-arrow slick-next']
//div[starts-with(@class, “css-”)]

"""
