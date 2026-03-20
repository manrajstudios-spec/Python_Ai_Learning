from enum import Enum

class RoomType(Enum):
    Single = 1
    Double = 2
    Group = 3

class Room:
    def __init__(self,room_number,room_type:RoomType,price:int):
        self.room_number = room_number
        self.renter = None
        self.room_type = room_type
        self.price = price

class Simple(Room):
    def __init__(self, room_number, room_type,price):
        super().__init__(room_number, room_type,price)
        self.features = ["Bed","WiFi"]

class Plus(Room):
    def __init__(self, room_number, room_type,price):
        super().__init__(room_number, room_type,price)
        self.features = ["Bed","WiFi","Meals","Air conditioning","Heat"]

class Luxury(Room):
    def __init__(self, room_number, room_type,price):
        super().__init__(room_number, room_type,price)
        self.features = ["Bed","WiFi","Meals","Air Conditioning","Heat","Separate Living Room And Bed Room","Private Swimming Pool"]

class Customer:
    def __init__(self,i_d):
        self.i_d = i_d
        self.room_rented:Room = None
