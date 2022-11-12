from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return ''

        room.take_room(people)

    def free_room(self, room_number: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return ''

        room.free_room()

    def status(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        total_gusts = sum([r.guests for r in self.rooms])

        final_return = [f"Hotel {self.name} has {total_gusts} total guests",
                        f'Free rooms: {", ".join(map(str, free_rooms))}',
                        f'Taken rooms: {", ".join(map(str,taken_rooms))}']

        return '\n'.join(final_return)


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
