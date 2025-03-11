
class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

    def book_room(self):
        self.is_available = False

    def cancel_booking(self):
        self.is_available = True

    def __str__(self):
        availability = "Available" if self.is_available else "Booked"
        return f"Room {self.room_number} ({self.room_type}) - {self.price_per_night} per night - {availability}"


class Booking:
    def __init__(self, guest_name, room, number_of_nights):
        self.guest_name = guest_name
        self.room = room
        self.number_of_nights = number_of_nights
        self.total_price = room.price_per_night * number_of_nights

    def __str__(self):
        return f"Booking for {self.guest_name} - Room {self.room.room_number} - {self.number_of_nights} night(s) - Total Price: {self.total_price}"


class Hotel:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_rooms(self):
        print(f"\nRooms available in {self.hotel_name}:")
        for room in self.rooms:
            print(room)

    def find_available_rooms(self):
        available_rooms = [room for room in self.rooms if room.is_available]
        return available_rooms

    def make_booking(self, guest_name, room_number, number_of_nights):
        room_to_book = None
        for room in self.rooms:
            if room.room_number == room_number and room.is_available:
                room_to_book = room
                break

        if room_to_book:
            room_to_book.book_room()
            booking = Booking(guest_name, room_to_book, number_of_nights)
            self.bookings.append(booking)
            print(f"\nBooking successful for {guest_name} in Room {room_number}.")
            print(booking)
        else:
            print("\nSorry, this room is either already booked or does not exist.")

    def cancel_booking(self, room_number):
        booking_to_cancel = None
        for booking in self.bookings:
            if booking.room.room_number == room_number:
                booking_to_cancel = booking
                break

        if booking_to_cancel:
            self.bookings.remove(booking_to_cancel)
            booking_to_cancel.room.cancel_booking()
            print(f"\nBooking for Room {room_number} has been canceled.")
        else:
            print("\nNo booking found for this room number.")

    def show_bookings(self):
        print(f"\nAll bookings in {self.hotel_name}:")
        for booking in self.bookings:
            print(booking)

    def available_rooms(self):
        available_rooms = self.find_available_rooms()
        if available_rooms:
            print("\nAvailable Rooms:")
            for room in available_rooms:
                print(room)
        else:
            print("\nNo rooms are available right now.")


def main():
    hotel = Hotel("Grand Plaza Hotel")

    # Adding rooms to the hotel
    hotel.add_room(Room(101, "Single", 100))
    hotel.add_room(Room(102, "Double", 150))
    hotel.add_room(Room(103, "Suite", 300))
    hotel.add_room(Room(104, "Single", 120))
    hotel.add_room(Room(105, "Double", 180))

    while True:
        print("\nWelcome to the Hotel Booking System")
        print("1. View Available Rooms")
        print("2. Make a Booking")
        print("3. Cancel a Booking")
        print("4. View All Bookings")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            hotel.available_rooms()

        elif choice == "2":
            guest_name = input("Enter your name: ")
            room_number = int(input("Enter the room number you want to book: "))
            number_of_nights = int(input("Enter the number of nights: "))
            hotel.make_booking(guest_name, room_number, number_of_nights)

        elif choice == "3":
            room_number = int(input("Enter the room number you want to cancel: "))
            hotel.cancel_booking(room_number)

        elif choice == "4":
            hotel.show_bookings()

        elif choice == "5":
            print("\nThank you for using the Hotel Booking System!")
            break

        else:
            print("\nInvalid choice, please try again.")


if __name__ == "__main__":
    main()














