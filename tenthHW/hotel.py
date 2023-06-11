from pythonProject.tenthHW.building import Building


class Hotel(Building):
    def __init__(self, name, height, num_rooms):
        super().__init__(name, height)
        self.num_rooms = num_rooms

    def book_room(self, room_number):
        print(f"Booking room {room_number} in {self.name}.")

    def order_room_service(self, room_number, meal):
        print(f"Ordering {meal} for room {room_number} in {self.name}.")
