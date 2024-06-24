# Define a class for a Room
class Room:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length
        self.doors = []
        self.windows = []

    def add_door(self, door):
        self.doors.append(door)

    def add_window(self, window):
        self.windows.append(window)

    def __str__(self):
        return f"Room {self.name}: {self.width}x{self.length} with {len(self.doors)} doors and {len(self.windows)} windows"

# Define a class for a Door
class Door:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Door: {self.width}x{self.height}"

# Define a class for a Window
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Window: {self.width}x{self.height}"

# Define a class for a House
class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return f"House at {self.address} with {len(self.rooms)} rooms:\n" + "\n".join([str(room) for room in self.rooms])

# Create a house
house = House("123 Main St")

# Create rooms
living_room = Room("Living Room", 10, 15)
living_room.add_door(Door(3, 6))
living_room.add_window(Window(2, 4))

kitchen = Room("Kitchen", 8, 10)
kitchen.add_door(Door(2, 5))
kitchen.add_window(Window(1, 3))

bedroom = Room("Bedroom", 12, 12)
bedroom.add_door(Door(3, 6))
bedroom.add_window(Window(2, 4))

# Add rooms to the house
house.add_room(living_room)
house.add_room(kitchen)
house.add_room(bedroom)

# Print the house floor plan
print(house)
