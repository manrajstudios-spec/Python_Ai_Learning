from enum import Enum
import json

class RoomType(Enum):
    Single = 0
    Double = 5000
    Group = 7000

class Room:
    def __init__(self,room_number,room_type:RoomType):
        self.room_number = room_number
        self.renter = None
        self.room_type = room_type
        self.base_price = 0
        self.name = ""
        self.is_booked = False
        self.price = self.ReturnPrice()

    def ReturnPrice(self):
        self.price = self.base_price + self.room_type.value
        return self.price
    
    def ReturnInfo(self):
        return {"RoomNumber":self.room_number,
                "RoomType":str(self.room_type.name),
                "Facility":self.name,
                "Booked":self.is_booked,
                "Booker_ID":0,
                "Price":self.price
                }
    
class Simple(Room):
    def __init__(self, room_number, room_type):
        super().__init__(room_number, room_type)
        self.features = ["Bed","WiFi"]
        self.base_price = 5000
        self.name = "Simple"

class Plus(Room):
    def __init__(self, room_number, room_type):
        super().__init__(room_number, room_type)
        self.features = ["Bed","WiFi","Meals","Air conditioning","Heat"]
        self.base_price = 7000
        self.name = "Plus"

class Luxury(Room):
    def __init__(self, room_number, room_type):
        super().__init__(room_number, room_type)
        self.features = ["Bed","WiFi","Meals","Air Conditioning","Heat","Separate Living Room And Bed Room","Private Swimming Pool"]
        self.base_price = 10000
        self.name = "Luxury"

class Customer:
    def __init__(self,i_d,name,room_number):
        self.i_d = i_d
        self.booked_room_number = room_number
        self.name = name

    def ReturnInfo(self):
        return {"ID": self.i_d,
                "RoomNumber":self.booked_room_number}

