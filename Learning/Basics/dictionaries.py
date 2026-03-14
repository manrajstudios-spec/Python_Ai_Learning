User_Data = {"Name": "Manraj Singh",
              "Age": 17,
               "Gender": "Male",
                "State": "Good"}

User_Data["Age"] = 18

name = User_Data["Name"]

if User_Data["Name"] == "Manraj Singh":
    print("true")

User_Data2 = {"Name": "Jay",
              "Age": 18,
               "Gender": "Male",
                "State": "Happy"}

if User_Data["Age"] == User_Data2["Age"]:
    print(True)


#-------dictionaries operations-------
Data = {"Name": "Manraj Singh",
              "Age": 17,
               "Gender": "Male",
                "State": "Good"}

#Acess
print(Data["Name"])

#add new key and value

Data["Grade"] = "A+" # note if grade already exits as key it updates its value

print(Data.items())

# changing value

Data["Grade"] = "A-"
print(Data["Grade"])



#remove item pop and pop item

#pop
Data.pop("Age") # here pop need key it does not remove by index
print(Data)

#popitem removes items with index and by default -1th

Data.popitem()
print(Data)

# key is in and not in

exists = "Age" in Data
print(exists)

# get keys items values

print(Data.keys())

print(Data.values())

print(Data.items())
#---------lopping through dictionaries---------
User_Data = {"Name": "Manraj",
             "Age":18,
             "Gender":"Male",
             "State": "Happy 🙃"}

for k,v in User_Data.items():#first key second value
    if(v == "Depressed 🙃"):
        print("You are fucked")
    print(k,v)

# we can also enumrate

for i , (k,v) in enumerate(User_Data.items()):
    print(i,k,v)