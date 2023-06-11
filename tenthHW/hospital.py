from pythonProject.tenthHW.building import Building


class Hospital(Building):
    def __init__(self, name, height, num_beds):
        super().__init__(name, height)
        self.num_beds = num_beds

    def admit_patient(self, patient_name):
        print(f"Admitting {patient_name} to {self.name}.")

    def perform_surgery(self):
        print(f"Performing surgery in the operation theater of {self.name}.")
    def display_rooms(self):
        print("Number of beds: {}".format(self.num_beds))
