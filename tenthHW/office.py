from pythonProject.tenthHW.building import Building


class Office(Building):
    def __init__(self, name, height, num_floors):
        super().__init__(name, height)
        self.num_floors = num_floors

    def rent_office_space(self, num_rooms):
        print(f"Renting {num_rooms} office rooms in {self.name}.")

    def set_up_conference_room(self):
        print(f"Setting up a conference room in {self.name}.")
