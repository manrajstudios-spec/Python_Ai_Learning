import json

#to open any file
# just with open("FileName" , "Mode") as file


file_name = "Learning/Basics/TestFile.txt"
#overrite removes existing
with open(file_name,'w') as file: #forward slahes 
    file.write("Manraj Singh")

#read the data
with open(file_name,'r') as file:
    data = file.read()
    print(data)
#append
with open(file_name , 'a') as file:
    file.write("\nAge 17 years")

with open(file_name,'r') as file:
    data = file.read()
    print(data)


# jason file

file_Name_Json = "Learning/Basics/Test_Data.json"


data1 = {"User_Name":"Manraj",
        "Age":17,
        "Gender":"Male"}

data2 = {"User_Name":"Jay",
        "Age":17,
        "Gender":"Male"}

data = [data1,data2]

with open(file_Name_Json,'w') as file:
    json.dump(data,file,indent=5) 

with open(file_Name_Json,'r') as file:
    data = json.load(file) 
    #print(data)

#to append we need to aceess previous data andthen add new data to previous one and add all the data


#take previous file 

#extract datain a list

old_data = [] #make sure data stored in json is a list


with open(file_Name_Json , 'r') as file:
    old_data = json.load(file)

data_to_add = {"User_Name":"Jack",
               "Age":17,
               "Gender":"Male"}

old_data.append(data_to_add)

with open (file_Name_Json,'w') as file:
    json.dump(old_data,file,indent=4)

with open(file_Name_Json , 'r') as file:
    old_data = json.load(file)

print(old_data)