from pythonProject.tenthHW.building import Building


class Hospital(Building):
    def __init__(self, name, height, num_rooms):
        super().__init__(name, height)
        self.num_rooms = num_rooms

    def admit_patient(self, patient_name):
        print(f"Admitting {patient_name} to {self.name}.")

    def perform_surgery(self):
        print(f"Performing surgery in the operation theater of {self.name}.")
