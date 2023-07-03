from pythonProject.tenthHW.building import Building


class House(Building):
    def __init__(self, name, height, num_rooms):
        super().__init__(name, height)
        self.num_rooms = num_rooms

    def paint(self, color):
        print(f"Painting the {self.name} in {color}.")

    def landscape_garden(self):
        print(f"Landscape the garden of {self.name}.")
