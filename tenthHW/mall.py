from pythonProject.tenthHW.building import Building


class Mall(Building):
    def __init__(self, name, height, num_shops):
        super().__init__(name, height)
        self.num_shops = num_shops

    def add_shop(self, shop_name):
        print(f"Adding a new shop '{shop_name}' to {self.name}.")

    def extend_parking(self, num_spots):
        print(f"Extending parking area of {self.name} by {num_spots} spots.")
