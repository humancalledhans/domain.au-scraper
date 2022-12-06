from abc import ABCMeta, abstractstaticmethod


class IAllListings(metaclass=ABCMeta):

    @abstractstaticmethod
    def add_to_all_listings_list():
        """ to implement in child class """

    @abstractstaticmethod
    def get_all_listings_list():
        """ to implement in child class """


class AllListings(IAllListings):

    __instance = None

    @staticmethod
    def get_instance():
        if AllListings.__instance == None:
            AllListings()
        return AllListings.__instance

    def __init__(self):

        if AllListings.__instance != None:
            raise Exception(
                "AllListings instance cannot be instantiated more than once!")
        else:
            self.all_listings_list = []
            AllListings.__instance = self

    @staticmethod
    def add_to_all_listings_list(self, listing):
        self.all_listings_list.append(listing)

    @staticmethod
    def get_all_listings_list(self):
        return self.all_listings_list