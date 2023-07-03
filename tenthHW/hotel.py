from pythonProject.tenthHW.mall import Mall
from pythonProject.tenthHW.hospital import Hospital
from pythonProject.tenthHW.building import Building


class Hotel(Mall, Hospital):
    def __init__(self, name, address, num_rooms, num_shops, num_beds):
        Building.__init__(self, name, address)
        Mall.__init__(self, name, address, num_shops)
        Hospital.__init__(self, name, address, num_beds)
        self.num_rooms = num_rooms

    def display_rooms(self):
        print("Number of rooms: {}".format(self.num_rooms))
