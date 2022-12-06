class ListingObject():
    def __init__(self, title, address, num_of_residences, num_of_floors, num_of_buildings, type, highlights_list, description_list) -> None:
        self.title = title
        self.address = address
        self.num_of_residences = num_of_residences
        self.num_of_floors = num_of_floors
        self.num_of_buildings = num_of_buildings
        self.type = type
        self.highlights_list = highlights_list
        self.description_list = description_list

    def get_title(self):
        return self.title

    def get_address(self):
        return self.address

    def get_num_of_residences(self):
        return self.num_of_residences

    def get_num_of_floors(self):
        return self.num_of_floors

    def get_num_of_buildings(self):
        return self.num_of_buildings

    def get_type(self):
        return self.type

    def get_highlights_list(self):
        return self.highlights_list

    def get_description_list(self):
        return self.description_list
