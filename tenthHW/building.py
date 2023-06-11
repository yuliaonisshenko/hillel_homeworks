class Building:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def construct(self):
        print(f"The {self.name} is under construction.")

    def demolish(self):
        print(f"The {self.name} is being demolished.")
