import random 
import time

question1 = {"Q": "Number Of Continents In World",
             "Options": [1,6,2,7],
             "Ans":"4"}
question2 = {"Q":"Whats is 91 + 19",
             "Options":[100,110,20,80],
             "Ans":"2"}

question3 ={"Q":"Is List And Touple Same",
            "Options": ["True (1)","False (2)"],
            "Ans":"2"}
question4 = {"Q": "Number of Elements in Given Set , Set = {1,2,3,4,4,4} ",
             "Options": [4,10,3,5],
             "Ans":"1"}

Questions = [question1,question2,question3,question4]

wannaPlay = ""

while wannaPlay =="":
    wannaPlay = input("Y/N: ")

    if(wannaPlay == "Y"):
        break
    elif wannaPlay == "N":
        quit()
    else:
        wannaPlay =""

options = [1,2,3,4]
Ans = 0

quest_not_asked = Questions.cpoy()

correct_answers = 0
wrong_answers = 0


def PrintCorrectAndWrongAns():
    print("You got " , correct_answers , " Answers Correct")
    time.sleep(0.5)
    print("You got " , wrong_answers, " Answers Wrong")

def AskQuestion():
    global correct_answers
    global wrong_answers
    randomQuestion = random.choice(quest_not_asked)

    print("Question found")
    quest_not_asked.remove(randomQuestion)
    time.sleep(1)
    print("Your Question is ---> " , randomQuestion["Q"])
    time.sleep(1)
    print("Your Opitions Are --> " , randomQuestion["Options"])
    print("Enter Number Of your Options (1, 2, 3, 4)")

    while True:
        user_ans = input("Enter Your Options Number here --> ")
        if not user_ans.isdigit() :
            if user_ans == "N" or user_ans == "n":
                quit()
            else:
                print("Plz Enter a Number")
        elif int(user_ans) not in options:
            print("Your Ans is Not in Options please choose appropriate option (┬┬﹏┬┬) ")
        else:
            if str(user_ans) == randomQuestion["Ans"]:
                print("Your Ans is Correct congractulations ^_____^ ")
                correct_answers += 1
            else:
                print("your Ans is wrong")
                wrong_answers += 1
            break
       
while True:
    if len(quest_not_asked) > 0:
        for i in range(5,0,-1):
            print(i)
            time.sleep(0.5)
        AskQuestion()
    else:
        PrintCorrectAndWrongAns()
        break
