import json

file_name = "Learning/Basic_Project/User_Password_Data.json"

def StoreData(data_to_store: dict):
    oldData = []
    try:
        with open(file_name , 'r') as file:
            oldData = json.load(file)
    except:
        oldData = []

    oldData.append(data_to_store)

    with open(file_name,'w') as file:
        json.dump(oldData , file , indent=4)

    print("Data Stored")

def AskForDataToStore():
    while True:
        User_Name = input("Enter User Name For Site --> ")

        if User_Name == "":
            pass
        else:
            Site_Name = input("Enter Name For Site --> ")

            if Site_Name == "":
                pass
            else:
                password = input("Enter password For Site --> ")

                if password == "":
                    pass
                else:
                    StoreData({"User_Name": User_Name , "Site_Name":Site_Name,"Password":password})
                    break

def AskForDataBasedOnSiteName():
    while True:
        data_found = False
        site_name = input("Enter Name Of Site --> ")
        data=[]
        if site_name == "":
            print("Plz Enter Something")
        else:
            with open(file_name,'r') as file:
                data = json.load(file)
        
            for d in data:
                if d["Site_Name"] == site_name:
                    print(f"Your Data is --> {d}")
                    data_found = True 
                    break
        
        if not data_found:
            print("No Site Found")
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
        
