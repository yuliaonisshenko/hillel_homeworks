from pythonProject.tenthHW.building import Building
from pythonProject.tenthHW.skyscraper import Skyscraper


class Mall(Building, Skyscraper):
    def __init__(self, name, address, num_shops, num_floors):
        Building.__init__(self, name, address)
        Skyscraper.__init__(self, name, address, num_floors)
        self.num_shops = num_shops

    def display_shops(self):
        print("Number of shops: {}".format(self.num_shops))

    def add_shop(self, shop_name):
        print(f"Adding a new shop '{shop_name}' to {self.name}.")

    def extend_parking(self, num_spots):
        print(f"Extending parking area of {self.name} by {num_spots} spots.")
