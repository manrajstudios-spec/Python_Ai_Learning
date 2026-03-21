from Encryption_Decryption_Caesar_Ciphe import Encrypt ,Decrypt
from json import dump,load
from Hotel_Clases import RoomType,Simple,Plus,Luxury,Customer
from time import sleep

password_file = "Learning\Basic_Project\Password_Hotle.txt"
customer_file = "Learning/Basic_Project/Customer_Hotel.json"
rooms_file = "Learning/Basic_Project/Rooms.json"

prices = {"Luxury":10000,
          "Plus":7000,
          "Simple":2000}

extra_for_size = {"Group":5000,
                  "Double":2000,
                  "Single":0}

def LoadJson(file_name):
    try:
        with open(file_name,'r')as file:
            return load(file)
    except:return[]

def WriteJson(file_name,to_write):
    with open(file_name,'w') as file:
        dump(to_write,file,indent=4)

def LoadPassword():
    _pass = ""
    try:
        with open(password_file , 'r') as file:
            _pass = file.read()
    except:
        _pass = ""

    return _pass

def UpdatePass(_pass:str):
    with open(password_file , 'w') as file:
        file.write(_pass)


def NewCustomer():
    customer_name = ""
    cusomers = LoadJson(customer_file)
    while True:
        customer_input = input("Please :) Enter Your Name --> ")

        if customer_input:
            customer_name = customer_input
            break
    
def RegisteredCustomer():
    pass

def AskForCustomerID():
    booked = False

    while True:
        customer_input = input("Have You Already Booked A Room (Y/N) --> ")
        if customer_input:
            if customer_input.lower() == "y":booked = True
            elif  customer_input.lower() == "n":booked = False
            break

def ReturnRoomType(num:int):
    match num:
        case 1:
            return RoomType.Single
        case 2:
            return RoomType.Double
        case 3:
            return RoomType.Group
        
def ListRooms(num:int):
    rooms = LoadJson(rooms_file)
    luxury_rooms = []
    plus_rooms = []
    simple_rooms = []
    booked_rooms = []
    unbooked_rooms = []
    for r in rooms:
        if r["Booked"]:
            booked_rooms.append(r)
        else:
            unbooked_rooms.append(r)

        if r["Facility"] == "Luxury": luxury_rooms.append(r)
        elif r["Facility"] == "Plus": plus_rooms.append(r)
        elif r["Facility"] == "Simple":simple_rooms.append(r)

    match num:
        case 2:
            print(f"Number Of Booked Rooms {len(booked_rooms)}")
            return booked_rooms
        case 3:
            print(f"Number Of Un Booked Rooms {len(booked_rooms)}")
            return unbooked_rooms
        case 4:
            print(f"Number Of Lunxury Rooms {len(booked_rooms)}")
            return luxury_rooms
        case 5:
            print(f"Number Of Plus Rooms {len(booked_rooms)}")
            return plus_rooms
        case 6:
            print(f"Number Of Simple Rooms {len(booked_rooms)}")
            return simple_rooms
    
def AddNewRooms():
    number_of_Rooms = 0
    room_type = None
    while True:
        user_input = input("Enter Number Of Rooms To Add --> ")
        if user_input and user_input.isdigit():
            number_of_Rooms = int(user_input)
            break
    
    while True:
        sleep(0.5)
        user_input_type = input("Press 1 --> Single Room \nPress 2 --> Double Room \nPress 3 --> For Group \n")
        if user_input_type and user_input_type.isdigit():
            room_type = ReturnRoomType(int(user_input_type))
            break
    
    while True:
        user_input_facility = input("Press 1 --> Add Luxury Room \nPress 2 --> Add Plus Room \nPress 3 --> Add Simple Room \n")
        if user_input_facility and user_input_facility.isdigit() and int(user_input_facility) > 0 and int(user_input_facility) < 4:
            rooms = LoadJson(rooms_file)
            for i in range(0,number_of_Rooms):
                r = None
                match int(user_input_facility):
                    case 1:
                        r = Luxury(len(rooms) +i,room_type)
                    case 2:
                        r = Plus(len(rooms) + i,room_type)
                    case 3:
                        r = Simple(len(rooms) + i,room_type)
                rooms.append(r.ReturnInfo())
            WriteJson(rooms_file,rooms)
            print("Rooms Added :)")
            break
                                 
def OwnerMenu():
    sleep(1)
    while True:
        user_input = input("\nPress 1 -> Add New Rooms \nPress 2 --> See Booked Rooms \nPress 3 --> To See Unbooked Rooms \nPress 4 --> Change Prices Of Rooms \n")

        if user_input:
            if user_input == "1":
                AddNewRooms()
                sleep(1)
                break
            elif user_input in ["2","3"]:
                rooms = ListRooms(int(user_input))

                for r in rooms:
                    print(f"Room Number => {r["RoomNumber"]} \nRoom Type --> {r["RoomType"]}\nRoom Price --> {r["Price"]}\nFacility --> {r["Facility"]}\n")
                    if r["Booked"]:
                         print(f"Booker ID --> {r["Booker_ID"]}")
                break
            elif user_input == "4":
                pass

def AskForPassword():
    password = LoadPassword()
    
    if not password:
        while True:
            user_input = input("Make New Password --> ")

            if user_input:
                password = user_input
                password = Encrypt(password)
                UpdatePass(password)
                break

    if password:
        while True:
            user_input = input("Enter The Password --> ")

            if user_input:
                if user_input == Decrypt(password):
                    OwnerMenu()
                    break
                else:
                    print("Wrong Password :(")

while True:
    user_input = input("Press 1 If You Are Owner \nPress 2 If You Are Cutomer\n")

    if user_input:
        if user_input =="1":
            AskForPassword()
        elif user_input == "2":
            AskForCustomerID()
        elif user_input == "n":break