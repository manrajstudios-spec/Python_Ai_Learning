import random
import time
from Player_Color import Player

number_of_players = 0
players = []
colors = ["B" , "W" , "R" , "G" , "Y"]

def RandomColorGenrator():
    random_color = []
    for i in range(0,len(colors) -1):
        random_color.append(random.choice(colors))
    return random_color

def MatchGuess(guess:str,color_seq:list):
    lst_guess = list(guess)
    new_seq = color_seq.copy()
    found_and_placed = []
    found_and_not_placed = []

    for i,s in enumerate(lst_guess):
        if s == new_seq[i]:
            found_and_placed.append(s)
            new_seq[i] = 0
        else:
            if s in new_seq:
                found_and_not_placed.append(s)
                new_seq[i] = 0

    
    print(f"\nCorrect And Well Placed => {len(found_and_placed)} \nCorrect But Wrongly Placed => {len(found_and_not_placed)} \n")
    return len(found_and_placed)

def TurnSelector():
    turn_number = 0
    color_seq = RandomColorGenrator()

    while True:
        turn_player:Player = players[turn_number]
        turn_number += 1
        if turn_number == number_of_players:
            turn_number = 0
        
        guess = turn_player.MyGuess()

        corrects = MatchGuess(guess,color_seq)

        if corrects == 4:
            print(f"Player {turn_player.i_d} , Name {turn_player.name} Wins ^_^ ^_^")
            break
        

def AskForNames():
    for i in range(1,number_of_players+1):
        while True:
            user_input = input(f"Player {i} Enter Your Name --> ")
            if user_input:
                if not user_input.isdigit():
                    p:Player = Player(user_input , i)
                    players.append(p) 
                    break
    TurnSelector()

while True:
    user_input = input("Enter Number OF Players Players --> ")

    if user_input:
        if user_input.isdigit():
            number_of_players = int(user_input)
            AskForNames()
            break
        elif user_input == "n":
            break