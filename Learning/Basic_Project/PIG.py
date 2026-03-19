import time
from Player import player

number_of_players = 0
players:player = []
maximum_score:int = 0


def TurnSelector():
    global maximum_score
    turn_number = 0

    while True:
        turn_number += 1
        p:player = players[turn_number -1]

        if turn_number == number_of_players: 
            turn_number = 0


        if p.is_bot :
            p.BotTurn(maximum_score)
        else:
            p.MyTurn()

        if p.score >= maximum_score:
            print(f"Player {p.i_d}  name --> {p.name} , wins with socres --> {p.score}")

            print("Players Who Loose Are")
            for i in players:
                if i != p:
                    print(f"Score Player {i.i_d} Name --> {i.name} Score --> {i.score} \n") 
            break   

def AskForNamesOfPlayers():
    global maximum_score

    for i in range(1,number_of_players+1):
        while True:
            user_input = input(f"Player {i} Enter Your Name --> ")
            if user_input and not user_input.isdigit():
                i = len(players) + 1
                p = player(name=user_input , i_d=i,is_bot=False)
                players.append(p)
                time.sleep(0.5)
                break

    while True: 
        user_input =input("Enter Maximum Score --> ")
        if user_input and user_input =="n":
            break
        elif user_input and user_input.isdigit() and int(user_input) > 10: maximum_score = int(user_input)   
        else : print("invalid")
        break

    TurnSelector()

def PlayWithBot():
    global number_of_players
    global maximum_score
    number_of_players = 1

    for i in range(1,number_of_players+1):
        while True:
            user_input = input(f"Player {i} Enter Your Name --> ")
            if user_input and not user_input.isdigit():
                i = len(players) + 1
                p = player(name=user_input , i_d=i,is_bot=False)
                players.append(p)
                time.sleep(0.5)
                break

    while True: 
        user_input =input("Enter Maximum Score --> ")
        if user_input and user_input =="n":
            break
        elif user_input and user_input.isdigit() and int(user_input) > 10: maximum_score = int(user_input)   
        else : print("invalid")
        break

    bot = player("Bot" , 2,True)
    players.append(bot)
    number_of_players = 2
    TurnSelector()
    

while True:
    _number_of_players = input("Enter Numbers Of Player Wanting To Play Or Type B To Play with bot ---> ")
    if _number_of_players and _number_of_players =="n":
        break
    elif _number_of_players and _number_of_players.lower() =="b":
        PlayWithBot()
    elif _number_of_players and _number_of_players.isdigit() and int(_number_of_players) > 1:
        number_of_players = int(_number_of_players)
        AskForNamesOfPlayers(True)
        break