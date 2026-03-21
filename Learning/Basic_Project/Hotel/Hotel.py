from Learning.Basic_Project.PasswordManager.Encryption_Decryption_Caesar_Ciphe import Encrypt ,Decrypt
from json import dump,load
from Learning.Basic_Project.Hotel.Hotel_Clases import RoomType,Simple,Plus,Luxury,Customer
from time import sleep

password_file = "Learning/Basic_Project\Hotel/Password_Hotle.txt"
customer_file = "Learning/Basic_Project/Hotel/Customer_Hotel.json"
rooms_file = "Learning/Basic_Project/Hotel/Rooms/json"

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


def ReturnRoomType(num:int):
    match num:
        case 1:
            return RoomType.Single
        case 2:
            return RoomType.Double
        case 3:
            return RoomType.Group

def ReturnRoomFacility(num:int):
    match num:
        case 1:
            return "Luxury"
        case 2:
            return "Plus"
        case 3:
            return "Simple"


def UpdateRooms(room:dict):
    rooms = LoadJson(rooms_file)
    new = []
    for r in rooms:
        if r["RoomNumber"] == room["RoomNumber"]:
            new.append(room)
        else:
            new.append(r)

    WriteJson(rooms_file,new)

def ListSimilarOptions(room:dict,customer_name:str):
    rooms = LoadJson(rooms_file)
    rooms_small_size = []
    rooms_less_quality = []
    customers = LoadJson(customer_file)
    for r in rooms:
        if not r["Booked"]:
            if r["Facility"] == room["Facility"]:
                print("A Similar Room With Smaller Size Is Available")
                rooms_small_size.append(r)
            elif r["RoomType"] == room["RoomType"]:
                print("Same Sized Room is Available But with less Facilities")
                rooms_less_quality.append(r)
    want_continue = False

    while True:
        customer_input = input("Press Enter If You Other Options Will Work Or Press n to Quit")

        if not customer_input:
            want_continue = True
            break
        else:
            if customer_input == "n":
                break

    if want_continue:
        customer_input = input("\nPress 1 To List Less Facilities But Same Size \nPress 2 To List Rooms With Same Facilities But Smaller Size\n")
        founded_room = {}
        if customer_input:
            if customer_input == "1":
                if rooms_less_quality:
                    r = rooms_less_quality[0]
                    founded_room = r
                    print(f"Room Number => {r["RoomNumber"]} \nRoom Type --> {r["RoomType"]}\nRoom Price --> {r["Price"]}\nFacility --> {r["Facility"]}\n")
                else: print("No Rooms Found") 
            elif customer_input == "2":
                if rooms_small_size:
                    r = rooms_small_size[0]
                    founded_room = r
                    print(f"Room Number => {r["RoomNumber"]} \nRoom Type --> {r["RoomType"]}\nRoom Price --> {r["Price"]}\nFacility --> {r["Facility"]}\n")
                else: print("No Rooms Found") 

        if founded_room:
            while True:
                customer_input = input("Press Enter To Buy The Room or Press n To Quit --> ")

                if not customer_input:
                    customer = Customer(len(customers),customer_name,founded_room["RoomNumber"])  
                    customer_dict  = customer.ReturnInfo()
                    customers.append(customer_dict)
                    WriteJson(customer_file,customers)

                    founded_room["Booked"] = True
                    founded_room["Booker_ID"] = customer.i_d
                    UpdateRooms(founded_room)

                    break
                else:
                    if customer_input =="n":
                        break

def NewCustomer():
    customer_name = ""
    customers = LoadJson(customer_file)
    rooms = LoadJson(rooms_file)
    room_type: RoomType = None
    room = {}
    sleep(0.5)
    while True:
        customer_input = input("Please :) Enter Your Name")

        if customer_input:
            customer_name = customer_input
            break

    sleep(0.5)

    while True:
        customer_input = input("Press 1 --> Single Room \nPress 2 --> Double Room \nPress 3 --> For Group \n")

        if customer_input and customer_input.isdigit():
            room_type = ReturnRoomType(int(customer_input))
            break

    sleep(0.5)

    while True:
        customer_input = input("Press 1 --> Book Luxury Room \nPress 2 --> Book Plus Room \nPress 3 --> Book Simple Room \n")
        room_facility = ReturnRoomFacility(int(customer_input))

        if customer_input and customer_input.isdigit() and int(customer_input):
            for r in rooms:
                if not r["Booked"]:
                    if r["RoomType"] == str(room_type.name) and r["Facility"] == room_facility:
                        room = r
                        break
        break
    sleep(1)

    print("--------------------------------------------------------------------------------------\n")
    if room:
        print(f"Room Number => {room["RoomNumber"]} \nRoom Type --> {room["RoomType"]}\nRoom Price --> {room["Price"]}\nFacility --> {room["Facility"]}\n")
        sleep(0.5)
        while True:
            customer_input = input("Press Enter If You Want To Book Or Press n to Quit The Process --> ")

            if not customer_input:

                customer = Customer(len(customers),customer_name,room["RoomNumber"])  
                customer_dict  = customer.ReturnInfo()
                customers.append(customer_dict)
                WriteJson(customer_file,customers)

                room["Booked"] = True
                room["Booker_ID"] = customer.i_d
                UpdateRooms(room)

                break
            elif customer_input == "n":
                break
    else:
        print("No Rooms Found According To Your Preferance")
        ListSimilarOptions({"Facility":ReturnRoomFacility(int(customer_input)),
                           "RoomType":str(room_type.name)
                           },customer_name)

def RegisteredCustomer():
    while True:
        customers = LoadJson(customer_file)
        customer_input = input("Enter Your ID --> ")
        found = False
        if customer_input and customer_input.isdigit():
            for c in customers:
                if c["ID"] == int(customer_input):
                    print(f'Your Room Number --> {c["RoomNumber"]}')
                    found = True
                    break

        if not found:
            print("No Customer Found With This ID")

            while True:
                customer_input = input("Press Enter To Register or Type n to Quit --> ")

                if not customer_input:
                    NewCustomer()
                    break
                else:
                    if customer_input == "n":
                        break
def AskForCustomerID():
    have_booked = False

    while True:
        customer_input = input("Have You Already Booked A Room (Y/N) --> ")
        if customer_input:
            if customer_input.lower() == "y":have_booked = True
            elif  customer_input.lower() == "n":have_booked = False
            break
    
    if have_booked: RegisteredCustomer()   
    else: NewCustomer()
     
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
            print(f"Number Of UnBooked Rooms {len(unbooked_rooms)}")
            return unbooked_rooms
        case 4:
            print(f"Number Of Lunxury Rooms {len(luxury_rooms)}")
            return luxury_rooms
        case 5:
            print(f"Number Of Plus Rooms {len(
                plus_rooms
            )}")
            return plus_rooms
        case 6:
            print(f"Number Of Simple Rooms {len(simple_rooms)}")
            return simple_rooms
    
def AddNewRooms():
    number_of_Rooms = 0
    room_type = None
    sleep(0.5)
    while True:
        user_input = input("Enter Number Of Rooms To Add --> ")
        if user_input and user_input.isdigit():
            number_of_Rooms = int(user_input)
            break
    
    while True:
        sleep(0.5)
        user_input_type = input("\nPress 1 --> Single Room \nPress 2 --> Double Room \nPress 3 --> For Group \n")
        if user_input_type and user_input_type.isdigit():
            room_type = ReturnRoomType(int(user_input_type))
            
            break
    sleep(0.5)
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
        user_input = input("\nPress 1 -> Add New Rooms \nPress 2 --> See Booked Rooms \nPress 3 --> To See Unbooked Rooms\n")

        if user_input:
            if user_input == "1":
                AddNewRooms()
                sleep(1)
                break
            elif user_input in ["2","3"]:
                rooms = ListRooms(int(user_input))

                for r in rooms:
                    print("--------------------------------------------------------------------------------\n")
                    print(f"Room Number => {r["RoomNumber"]} \nRoom Type --> {r["RoomType"]}\nRoom Price --> {r["Price"]}\nFacility --> {r["Facility"]}\n")
                    if r["Booked"]:
                         print(f"Booker ID --> {r["Booker_ID"]}")
                break

def AskForPassword():
    password = LoadPassword()
    
    if not password:
        while True:
            sleep(0.5)
            user_input = input("Make New Password --> ")

            if user_input:
                password = user_input
                password = Encrypt(password)
                UpdatePass(password)
                break
    sleep(0.5)
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
    sleep(0.5)
    print("\n")
    if user_input:
        if user_input =="1":
            AskForPassword()
        elif user_input == "2":
            AskForCustomerID()
        elif user_input == "n":break