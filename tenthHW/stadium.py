from pythonProject.tenthHW.building import Building
from pythonProject.tenthHW.hotel import Hotel


class Stadium(Building, Hotel):
    def __init__(self, name, address, capacity, num_rooms):
        Building.__init__(self, name, address)
        Hotel.__init__(self, name, address, num_rooms)
        self.capacity = capacity

    def display_capacity(self):
        print("Capacity: {} seats".format(self.capacity))

    def sell_tickets(self, num_tickets):
        print(f"Selling {num_tickets} tickets for the upcoming event at {self.name}.")

    def install_jumbotron(self):
        print(f"Installing a jumbotron screen in {self.name}.")
