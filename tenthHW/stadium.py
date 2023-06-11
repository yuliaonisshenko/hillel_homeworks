from pythonProject.tenthHW.building import Building


class Stadium(Building):
    def __init__(self, name, height, seating_capacity):
        super().__init__(name, height)
        self.seating_capacity = seating_capacity

    def sell_tickets(self, num_tickets):
        print(f"Selling {num_tickets} tickets for the upcoming event at {self.name}.")

    def install_jumbotron(self):
        print(f"Installing a jumbotron screen in {self.name}.")
