import time
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


def interacting_and_scraping_links(driver, a, base_xpath, base_xpath_for_right_click_arrow):
    try:

        homes_shown = driver.find_elements(By.XPATH, f"{base_xpath}")
        num_of_apartments_shown = len(homes_shown)

        displacement = 1
        num_of_times_right_click_arrow_disappeared = 0

        all_links_instance = AllLinksToScrape.get_instance()
        listing_list = []

        iterations = 0

        listings_index = 1

        while driver.find_element(
                By.XPATH, f"{base_xpath_for_right_click_arrow}//button[@class='slick-arrow slick-next']"):

            if driver.find_element(
                    By.XPATH, f"({base_xpath}//a)[{listings_index}]").get_attribute('href') not in listing_list:
                listing_list.append(driver.find_element(
                    By.XPATH, f"({base_xpath}//a)[{listings_index}]").get_attribute('href'))
            print("index", listings_index)
            print("listing list", listing_list)

            right_click_arrow = driver.find_element(
                By.XPATH, f"{base_xpath_for_right_click_arrow}//button[@class='slick-arrow slick-next']")
            a.move_to_element(right_click_arrow).click().perform()
            (driver, a) = pause_until_loaded(driver, a)

            listings_index = listings_index + 1

        for residual_idx in range(1, homes_shown+1):
            try:
                if driver.find_element(
                        By.XPATH, f"({base_xpath}//a)[{listings_index + residual_idx}]").get_attribute('href') not in listing_list:
                    listing_list.append(driver.find_element(
                        By.XPATH, f"({base_xpath}//a)[{listings_index + residual_idx}]").get_attribute('href'))
            except NoSuchElementException:
                continue

        for listing_link in listing_list:
            if listing_link not in all_links_instance.get_links_list(self=all_links_instance):
                all_links_instance.add_to_links_list(
                    self=all_links_instance, link=listing_link)
                print("LINKS LIST TOTAL", all_links_instance.get_links_list(
                    self=all_links_instance))

            # while True:

            #     for idx in range(num_of_apartments_shown):
            #         try:
            #             WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located(
            #                 (By.XPATH, f"({base_xpath}//a)[{idx+displacement}]")))
            #             # all_links_instance.add_to_all_listings_list(self=all_links_instance, listing=driver.find_element(
            #             #     By.XPATH, f"({base_xpath}//a)[{idx+displacement}]").get_attribute('href'))
            #             listing_list.append(driver.find_element(
            #                 By.XPATH, f"({base_xpath}//a)[{idx+displacement}]").get_attribute('href'))
            #             print("index", idx+displacement)
            #             print("listing list", listing_list)

            #         except NoSuchElementException:
            #             for i in range(1, idx+1):
            #                 if driver.find_element(
            #                         By.XPATH, f"({base_xpath}//a)[{i}]").get_attribute('href') not in listing_list:
            #                     listing_list.append(driver.find_element(
            #                         By.XPATH, f"({base_xpath}//a)[{i}]").get_attribute('href'))
            #             continue

            #         except TimeoutException:
            #             continue

            #     for _ in range(num_of_apartments_shown):

            #         try:
            #             right_click_arrow = driver.find_element(
            #                 By.XPATH, f"{base_xpath_for_right_click_arrow}//button[@class='slick-arrow slick-next']")
            #             a.move_to_element(right_click_arrow).click().perform()
            #             (driver, a) = pause_until_loaded(driver, a)

            #         except NoSuchElementException:
            #             print('found?')
            #             num_of_times_right_click_arrow_disappeared = num_of_times_right_click_arrow_disappeared + 1
            #             if num_of_times_right_click_arrow_disappeared >= 2:
            #                 break

            #     displacement += num_of_apartments_shown
            #     if num_of_times_right_click_arrow_disappeared >= 2:
            #         break
            #     iterations = iterations + 1
            #     if iterations >= 5:
            #         break

            # for listing_link in listing_list:
            #     if listing_link not in all_links_instance.get_links_list(self=all_links_instance):
            #         all_links_instance.add_to_links_list(
            #             self=all_links_instance, link=listing_link)
            #         print("LINKS LIST TOTAL", all_links_instance.get_links_list(
            #             self=all_links_instance))

    except NoSuchElementException:
        return
