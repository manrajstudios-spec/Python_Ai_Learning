import json
from datetime import datetime,date
import time
import calendar

task_file = "Learning/Basic_Project/TaskManager/Tasks.json"

def LoadTask():
    data = []
    try:
        with open(task_file,'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
    data.sort(key = lambda task:(task["Priority"]) , reverse = True)
    return data
    
def UploadTask(data:dict):
    old_data = LoadTask()
        
    old_data.append(data)
    old_data.sort(key = lambda task:(task["Priority"]) ,reverse = True)

    with open(task_file,'w') as file:
        json.dump(old_data,file,indent=5)
def UpdateTasks(data:list):

    data.sort(key = lambda task:(task["Priority"]),reverse = True)

    with open(task_file,'w') as file:
        json.dump(data,file,indent=5)

def AddNewTask():
    while True:
        task_title = input("Enter Title For Task --> ")
        time.sleep(0.5)
        if task_title:
            task_discription = input("Enter Dicription For Task --> ") 

            time.sleep(0.5)
            if task_discription:
                task_priority = input("Enter Priority Of Task --> must be between 0 and 10 (0 is minimum and 10 is maximum) : ")
                
                if task_priority.isdigit() and task_priority:
                    if int(task_priority) >= 0 and int(task_priority) <= 10:
                        task_month = input("Enter number of month of Deadline --> ")

                        if  task_month.isdigit() and int(task_month) >0 and int(task_month) <= 12:
                            task_date = input("Enter Date of Deadline Of Task --> ")
                            days_in_task_month = calendar.monthrange(date.today().year , task_month)(1)
                            if task_date.isdigit() and int(task_date) > 0 and int(task_date) <= days_in_task_month:
                                task_time = input("Enter Time in 24hrs format only hour (integer) --> ")
                                if task_time.isdigit():
                                    days_left = (date(date.today().year, int(task_month),int(task_date)) - date.today()).days
                                    hours_left = (datetime(date.today().year,int(task_month),int(task_date),int(task_time)) - datetime.now()).total_seconds() // 3600 #only give left hours excluding days
                                    h = hours_left - 24 * days_left
                                    task = {"Title":task_title,
                                            "Discription":task_discription,
                                            "Priority":int(task_priority),
                                            "Deadline":[date.today().year,int(task_month),int(task_date),int(task_time)],
                                            "DaysLeft":[days_left,h]}
                                    UploadTask(task)
                                    print("Task Uploaded")
                                    break

def GetTasks(i:int):
    high_priority_tasks = []
    low_priority_tasks = []
    deadline_approaching_tasks = []
    deadline_passed_tasks = []
    all_tasks = []

    dict_to_return = []
    for t in LoadTask():
        all_tasks.append(t)
        if t["Priority"] > 5:
            high_priority_tasks.append(t)
        elif t["Priority"] <= 5:
            low_priority_tasks.append(t)

        deadline_date_time = t["Deadline"]

        days_left = (date(int(deadline_date_time[0]),int(deadline_date_time[1]),int(deadline_date_time[2])) - date.today()).days
        hours_left = (datetime(int(deadline_date_time[0]),int(deadline_date_time[1]),int(deadline_date_time[2]),int(deadline_date_time[3])) - datetime.now()).total_seconds() // 3600 #only give left hours excluding days
        h = hours_left - 24 * days_left
        t["DaysLeft"] = [days_left,h]

        if days_left <= 10 and days_left >= 0 : 
            deadline_approaching_tasks.append(t)
        elif days_left < 0 :
            t["DaysLeft"] = [abs(days_left),24-h]
            deadline_passed_tasks.append(t)

    match i:
        case 1: dict_to_return =  all_tasks
        case 2: dict_to_return =  high_priority_tasks
        case 3: dict_to_return = low_priority_tasks
        case 4: dict_to_return =  deadline_approaching_tasks
        case 5: dict_to_return =  deadline_passed_tasks
        case _: 
            print("Invalid Input ")
            return []
        
    dict_to_return.sort(key = lambda task:(task["Priority"]),reverse = True)       
    return dict_to_return 

def SeeOldTasks():
    while True:
        if not LoadTask():
            print("No Tasks Stored")
            break 
        user_input = input("Type y to list All optionsor Type n to Quit : ")
        asked_tasks=[]
        
        if user_input.lower() == "y":

            while True:
                _input_user = input("Press 1 for listing all Tasks \nPress 2 for listing high Priority Tasks \nPress 3 for lisitng lowe Priority Tasks \nPress 4 for listing Deadline Approaching Tasks \nPress 5 for lisiting Tasks Past Deadline: ")
                
                if _input_user.isdigit() and int(_input_user) >= 1 and int(_input_user) <= 5:
                    asked_tasks = GetTasks(int(_input_user))
                    break

            for i,t in enumerate(asked_tasks):
                print(f"{i+1}. Task Is {t['Title']} \n Discription is {t['Discription']} \n Priority is {t['Priority']} \n Deadline is {t['Deadline'][0]} , {t['DaysLeft'][0]} days , {t['DaysLeft'][1]} hours left \n")
            while True:
                user_i = input("Enter Task Number You Wanna Delete --> ")

                if user_i.isdigit() and int(user_i) - 1 < len(asked_tasks):
                    data = LoadTask()
                    if asked_tasks[int(user_i)-1] in data:
                        data.remove(asked_tasks[int(user_i)-1])
                        UpdateTasks(data)
                        print("Task Removed")
                        break
        elif user_input.lower() =="n":
            break        

            
while True:
    user_input = input("Press 1 To Add new Task Or 2 to see Old Tasks : ")

    if user_input == "1":
        AddNewTask()
    elif user_input == "2":
        SeeOldTasks()
    elif user_input == "n":
        print("Quitting")
    break