from Encryption_Decryption_Caesar_Ciphe import Encrypt ,Decrypt
from json import dump,load
from Hotel_Clases import RoomType,Simple,Plus,Luxury
from time import sleep

password_file = "Learning\Basic_Project\Password_Hotle.txt"
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

def AskForCustomerID():
    pass

def ReturnRoomType(num:int):
    match num:
        case 1:
            return RoomType.Single
        case 2:
            return RoomType.Double
        case 3:
            return RoomType.Group
        
def RoomPrice(room_type:RoomType , num:int):
    if num > 3 : return
    match num:
        case 1 :
            if room_type == RoomType.Single: return prices["Luxury"]
            elif room_type == RoomType.Double:return prices["Luxury"] + extra_for_size["Double"]
            else : return prices["Luxury"] + extra_for_size["Group"]
        case 2:
            if room_type == RoomType.Single: return prices["Plus"]
            elif room_type == RoomType.Double:return prices["Plus"] + extra_for_size["Double"]
            else : return prices["Plus"] + extra_for_size["Group"]
        case 3:
            if room_type == RoomType.Single: return prices["Simple"]
            elif room_type == RoomType.Double:return prices["Simple"] + extra_for_size["Double"]
            else : return prices["Simple"] + extra_for_size["Group"]


def ListRooms(room_type:RoomType,num:int):
    rooms = LoadJson(rooms_file)
    match num:
        case 1:
            for r in rooms:
                pass
        case 2:
            pass
        case 3:
            pass

def AddNewRooms():
    added = False

    while not added:
        user_input = input("Enter Number Of Rooms To Add --> ")
        rooms:list = LoadJson(rooms_file)

        if user_input:
            if user_input.isdigit():
                while not added:
                    sleep(0.5)
                    user_input_type = input("Press 1 --> Single Room \nPress 2 --> Double Room \nPress 3 --> For Group \n")

                    if user_input_type:
                        if user_input_type.isdigit():
                            while not added:
                                sleep(0.5)
                                user_input_facility = input("Press 1 --> Add Luxury Room \nPress 2 --> Add Plus Room \nPress 3 --> Add Simple Room \n")

                                if user_input_facility:
                                    if user_input_facility.isdigit():
                                        room_type = ReturnRoomType(int(user_input_type))
                                        for i in range(0,int(user_input)):
                                            room = None
                                            room_dict = {}
                                            faclity = ""
                                            match int(user_input_facility):
                                                case 1:
                                                    price = RoomPrice(room_type=room_type ,num = 1)
                                                    room = Luxury(room_number=len(rooms) , room_type=room_type,price=price)
                                                    faclity = "Luxury"
                                                case 2:
                                                    price = RoomPrice(room_type=room_type ,num = 2)
                                                    room = Plus(room_number=len(rooms) , room_type=room_type,price=price)
                                                    faclity = "Plus"
                                                case 3:
                                                    price = RoomPrice(room_type=room_type ,num = 3)
                                                    room = Simple(room_number=len(rooms) , room_type=room_type,price=price)
                                                    faclity = "Simple"
                                                case _: 
                                                    print("Invalid") 
                                                    break
                                            r_type = str(room_type)[9:]
                                            room_dict = {"Room_ID":room.room_number,
                                                        "Room_Type":(r_type),
                                                        "Room_Facility":faclity,
                                                        "Room_Price":int(price),
                                                        "Room_Assigned":False,
                                                        "Assigned_To":0}
                                            
                                            rooms.append(room_dict)
                                        WriteJson(rooms_file,rooms)
                                        print("Rooms Added")
                                        added = True
    
def OwnerMenu():
    sleep(1)
    while True:
        user_input = input("\nPress 1 -> Add New Rooms \nPress 2 --> See Booked Rooms \nPress 3 --> To See Unbooked Rooms \nPress 4 --> Change Prices Of Rooms \n")

        if user_input :
            if user_input == "1":
                AddNewRooms()
                sleep(1)
                break
            elif user_input in ["2","3"]:
                pass
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
        break