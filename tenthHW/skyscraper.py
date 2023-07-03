from pythonProject.tenthHW.building import Building


class Skyscraper(Building):
    def __init__(self, name, height, num_floors):
        super().__init__(name, height)
        self.num_floors = num_floors

    def install_elevators(self):
        print(f"Installing elevators in the {self.name}.")

    def break_ground(self):
        print(f"Breaking ground for the construction of {self.name}.")
