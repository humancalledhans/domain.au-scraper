from abc import ABCMeta, abstractstaticmethod


class IAllLinksToScrape(metaclass=ABCMeta):

    @abstractstaticmethod
    def add_to_links_list():
        """ to implement in child class """

    @abstractstaticmethod
    def get_links_list():
        """ to implement in child class """


class AllLinksToScrape(IAllLinksToScrape):

    __instance = None

    @staticmethod
    def get_instance():
        if AllLinksToScrape.__instance == None:
            AllLinksToScrape()
        return AllLinksToScrape.__instance

    def __init__(self):

        if AllLinksToScrape.__instance != None:
            raise Exception(
                "AllLinksToScrape instance cannot be instantiated more than once!")
        else:
            self.links_list = []
            AllLinksToScrape.__instance = self

    @staticmethod
    def add_to_links_list(self, link):
        self.links_list.append(link)

    @staticmethod
    def get_links_list(self):
        return self.links_list
