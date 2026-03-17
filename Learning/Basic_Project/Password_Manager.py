import json
import time
from Encryption_Decryption_Caesar_Ciphe import Encrypt,Decrypt
file_name = "Learning/Basic_Project/User_Password_Data.json"


def LoadData():
    data = []
    try:
        with open(file_name , 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def WriteData(data:list):
    with open(file_name,'w') as file:
        json.dump(data,file,indent=4)

def StoreData(data_to_store: dict):
    oldData = LoadData()

    oldData.append(data_to_store)

    WriteData(oldData)

    print("Data Stored")

def AskToChangePassword(data:list,index:int):
    while True:
        wanna_chnage = input("Want To Change Password Or Not (y|n) --> ")
        password_stored = False
        if wanna_chnage.lower() == "y":

            print(f'Your current Password is ---> {Decrypt(data[index]["Password"])}')
            while not password_stored:
                time.sleep(0.3)
                new_password = input("Enter The new Password --> or (Type n to stop) : ")

                if new_password == "n":
                    break
                else:
                    while not password_stored:
                        time.sleep(0.3)
                        re_type_new_password = input("Confirm Password --> ")

                        if new_password == re_type_new_password:
                            data[index]["Password"] = Encrypt(new_password)

                            WriteData(data)

                            print("New Password Is Stored")  
                            password_stored = True
                            break
                        else:
                            print("Password Did not matched Try Again")
                            time.sleep(1)
        elif wanna_chnage.lower() == "n":
            break
        else:
            print("plz Enter Valid Option")       
        if password_stored == True:
            break

def AskForDataToStore():
    while True:
        User_Name = input("Enter User Name For Site --> ")

        if User_Name != "":
            time.sleep(0.3)
            Site_Name = input("Enter Name For Site --> ")

            data = LoadData()

            if data:
                found = False
                index = 0
                for i,d in enumerate(data):
                    if d["Site_Name"] == Site_Name:
                        found = True
                        index = i
                        print("A Site Same As This Already Exists")
                if found:
                    AskToChangePassword(data,index)
                    break
            if Site_Name != "":
                time.sleep(0.3)
                password = input("Enter password For Site --> ")

                if password != "":
                    StoreData({"User_Name": User_Name , "Site_Name":Site_Name,"Password":Encrypt(password)})
                    break

def AskForDataBasedOnSiteName():
    while True:
        print("To Get Data Related To Particular Site Or Press n to quit")
        time.sleep(0.5)
        data_found = False
        site_name = input("Enter Name Of Site --> ")

        if site_name == "n":
            break
        else:
            data = LoadData()
            for d in data:
                if site_name.lower() in d["Site_Name"].lower():
                    print(f'Your User_Name is --> {d["User_Name"]} , Your Site_Name {d["Site_Name"]} , Your PassWord IS {Decrypt(d["Password"])} ')
                    data_found = True 
                    break     

        if not data_found:
            print("No Site Found")
            break
        else:
            break

while True:
    wanna_store_new_password = input("Want To Store Data (y/n): ")

    if wanna_store_new_password.lower() == "y":
        AskForDataToStore()
        break
    elif wanna_store_new_password.lower() == "n":
        AskForDataBasedOnSiteName()
        break 
    else:
        print("plz Enter Suitable Option")
        
