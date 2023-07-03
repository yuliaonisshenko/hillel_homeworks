from pythonProject.tenthHW.building import Building


class School(Building):
    def __init__(self, name, height, num_classrooms):
        super().__init__(name, height)
        self.num_classrooms = num_classrooms

    def enroll_student(self, student_name):
        print(f"Enrolling {student_name} in {self.name}.")

    def organize_field_trip(self, destination):
        print(f"Organizing a field trip to {destination} for students of {self.name}.")
