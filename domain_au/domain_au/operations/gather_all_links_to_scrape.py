import threading
from src.singleton.all_links_to_scrape import AllLinksToScrape
from src.singleton.all_listings import AllListings
from src.assumptions.tabs_available import get_tabs_available
from src.operations.go_to_address import GetAllAddressLinksFromTab


def gather_all_links_to_scrape():
    tabs_available = get_tabs_available()

    get_all_address_links_from_tab_instance_one = GetAllAddressLinksFromTab(
        tabs_available[0])
    # get_all_address_links_from_tab_instance_two = GetAllAddressLinksFromTab(
    #     tabs_available[1])
    # get_all_address_links_from_tab_instance_three = GetAllAddressLinksFromTab(
    #     tabs_available[2])
    # get_all_address_links_from_tab_instance_four = GetAllAddressLinksFromTab(
    #     tabs_available[3])
    # get_all_address_links_from_tab_instance_five = GetAllAddressLinksFromTab(
    #     tabs_available[4])
    # get_all_address_links_from_tab_instance_six = GetAllAddressLinksFromTab(
    #     tabs_available[5])
    # get_all_address_links_from_tab_instance_seven = GetAllAddressLinksFromTab(
    #     tabs_available[6])

    threading.Thread(
        target=get_all_address_links_from_tab_instance_one.get_all_address_links_from_tab).start()
    # threading.Thread(
    #     target=get_all_address_links_from_tab_instance_two.get_all_address_links_from_tab).start()
    # threading.Thread(
    #     target=get_all_address_links_from_tab_instance_three.get_all_address_links_from_tab).start()
    # threading.Thread(
    #     target=get_all_address_links_from_tab_instance_four.get_all_address_links_from_tab).start()
    # threading.Thread(
    #     target=get_all_address_links_from_tab_instance_five.get_all_address_links_from_tab).start()
    # threading.Thread(
    #     target=get_all_address_links_from_tab_instance_six.get_all_address_links_from_tab).start()
    # threading.Thread(
    #     target=get_all_address_links_from_tab_instance_seven.get_all_address_links_from_tab).start()

    all_listings_instance = AllLinksToScrape.get_instance()
    print("all listings links", all_listings_instance.get_links_list(
        self=all_listings_instance))
