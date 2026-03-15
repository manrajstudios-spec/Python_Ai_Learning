import random
import time

wannaPlay = ""

while wannaPlay =="":
    wannaPlay = input("Y/N: ")

    if(wannaPlay == "Y"):
        break
    elif wannaPlay == "N":
        quit()
    else:
        wannaPlay =""


winning_combos = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]
positions_occupied_by_player = []
positions_occupied_by_cpu  = []
possible_moves = [0,1,2,3,4,5,6,7,8]

count = 0 

is_player_turn = True


def DrawBoard():
    global count
    count = 0
    for i in range(0,5):
        for j in range(0,5):
            if i % 2 == 0: # print Numbers or | in this row 
                if j % 2 == 0: # print numbers or croses or O
                    if count in positions_occupied_by_player:
                        print("X"," " ,end="")
                    elif count in positions_occupied_by_cpu:
                        print("O"," " ,end="")
                    else:
                        print(count," " ,end="")
                    count += 1
                else:
                    print("|" , " ", end="")
            else:
                if j % 2 == 0:
                    print("--","" ,end="")
                else:
                    print("|"," ",end="")
        print()

def WinCheck(lst: list , isPlayer: bool):
    if len(lst) < 3 :return
    won = False
    for i,l in enumerate(winning_combos):
        moves_matching_combo = 0
        for pm in lst:
            if pm in l:
                moves_matching_combo += 1

        if moves_matching_combo == 3:
            if(isPlayer):
                print("Player Wins ☆*: .｡. o(≧▽≦)o .｡.:*☆☆*: .｡. o(≧▽≦)o .｡.:*☆☆*: .｡. o(≧▽≦)o")
            else:
                print("Cpu Wins ☆*: .｡. o(≧▽≦)o .｡.:*☆☆*: .｡. o(≧▽≦)o .｡.:*☆☆*: .｡. o(≧▽≦)o")
                won =  True
            DrawBoard()
            quit()
            return True
        else:
            continue
    
    if not won:
        return False

def GetPositionsNotOccupied():
    postions_not_occupied = []
    for i in possible_moves:
        if i not in positions_occupied_by_cpu and i not in positions_occupied_by_player:
            postions_not_occupied.append(i)
    return postions_not_occupied

def GetCpuMove():
    for i,l in enumerate(winning_combos):
        combo_position_matched = 0
        for cp in positions_occupied_by_cpu:
            if cp in l:
                combo_position_matched += 1
        if combo_position_matched == 2:
            for p in l:
                if p not in positions_occupied_by_cpu and p not in positions_occupied_by_player:
                    return p

def CanCpuWinInOneMove():
    matched_2 = False
    for lst in winning_combos:
        combo_position_matched = 0 
        for cp in positions_occupied_by_cpu:
            if cp in lst:
                combo_position_matched += 1

        if combo_position_matched == 2 :
            for l in lst:
                if l not in positions_occupied_by_player and l not in positions_occupied_by_cpu:
                    print(positions_occupied_by_cpu)
                    matched_2 = True
                    return True
                else:
                    matched_2 = False
        else:
            matched_2 = False
        
    if(not matched_2):
        return False
      
def GetCounterPlayerPosition():
    matched_2 = False
    matched_1 = False

    for lst in winning_combos:

        moves_matching_combo = 0

        for pm in positions_occupied_by_player:
            if pm in lst:
                moves_matching_combo += 1
        
        if(moves_matching_combo == 2):
            for p in lst:
                if p not in positions_occupied_by_cpu and p not in positions_occupied_by_player:
                    matched_2 = True
                    time.sleep(0.4)
                    print("2 Matched Countring Move")
                    time.sleep(0.4)
                    return p
    
    if not matched_2:
        for lst in (winning_combos):
            moves_matching_combo = 0
            for pm in positions_occupied_by_player:
                if pm in lst:
                    moves_matching_combo += 1
        
            if(moves_matching_combo == 1):       
                 for p in lst:
                    if p not in positions_occupied_by_cpu and p not in positions_occupied_by_player:
                        time.sleep(0.4)
                        print("1 Matched, Planning Countring Move")
                        time.sleep(0.4)
                        matched_1 = True
                        return p
                
    if not matched_1 and not matched_2:
        return random.choice(GetPositionsNotOccupied())
    
def CpuTurn():
    global is_player_turn
    place_to_move = 0
    if CanCpuWinInOneMove():
        place_to_move = GetCpuMove()
    else:
        place_to_move = GetCounterPlayerPosition()
    
    positions_occupied_by_cpu.append(place_to_move)
    print(place_to_move)
    print("Wait CPU is Making A Move")
    time.sleep(1)
    print("Cpu Move Is")
    DrawBoard()
    if(not WinCheck(positions_occupied_by_cpu , False)):
        is_player_turn = True

while True:
    moves_Available= 0
    for i in possible_moves:
        if i  not in positions_occupied_by_cpu and i not in positions_occupied_by_player:
            moves_Available += 1

    if moves_Available == 0 :
        print("Draw")
        break
    else:
        if is_player_turn:
            while is_player_turn:
                print("------------------------------------")
                DrawBoard()
                player_move = input("Enter Your Move --> ")

                if not player_move.isdigit():
                    if player_move.lower() == "n":
                        quit()
                    else:
                        print("Plz Enter Number (^///^)")

                elif int(player_move) not in possible_moves or int(player_move) in positions_occupied_by_cpu or int(player_move) in positions_occupied_by_player:
                    print("plz Enter A valid Move ^_^")

                else:
                    positions_occupied_by_player.append(int(player_move))
                    is_player_turn = False
                    time.sleep(0.3)
                    DrawBoard()
                    time.sleep(0.5)          
                    WinCheck(positions_occupied_by_player,True)
        else:
            CpuTurn()