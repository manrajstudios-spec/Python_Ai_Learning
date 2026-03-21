import random
import time
class player:

    def __init__(self , name:str , i_d:int,is_bot:bool):
        self.name = name
        self.i_d = i_d
        self.score = 0
        self.is_bot = is_bot

    def AddScore(self,points_to_add:int):
        self.score += points_to_add
        self.ShowScore()

    def ShowScore(self):
        print(f"Player {self.i_d} {self.name}'s score is {self.score}")
        
    def RollDice(self):
        return random.randrange(1,7)
    

    def BotTurn(self,max_:int):
        first = True
        cur_score = 0
        number_of_current_turn = 0
        will_roll = True

        while True:
            outcome = 0

            if first:

                print(f'Its Player {self.i_d} turn , name --> {self.name} ,Points --> {self.score}')
                time.sleep(1)
                number_of_current_turn += 1
                will_roll = True
                first = False
            else:
                number_of_current_turn += 1 
                match number_of_current_turn:
                    case 2: will_roll = True if random.random() < 0.7 else False
                    case 3: will_roll = True if random.random() < 0.5 else False
                    case 4: will_roll = True if random.random() < 0.35 else False
                    case 5: will_roll = True if random.random() < 0.2 else False
                    case 6: will_roll = True if random.random() < 0.1 else False
                    case _: will_roll = True 
            
            if not will_roll: 
                self.AddScore(cur_score)
                break
            else:
                outcome = self.RollDice()
                if outcome == 1:
                    print("Bot Rolls 1 :<")
                    print("Bot Loose")
                    time.sleep(2)
                    break
                print(f"Congrats You Rolled {outcome} , Keep Going And You'll Earn More")
                cur_score += outcome
                time.sleep(1)
                print(f"Your Score In This Turn Is {cur_score}")
                print("--------------------------------------------------------------------------------------------------\n")
                if self.score + cur_score >= max_:
                    break

                time.sleep(1)

    def MyTurn(self):
        cur_score = 0
        is_first_turn = True
        turn_done = False
        
        while True:
            if is_first_turn:
                print(f'Its Player {self.i_d} turn , name --> {self.name} , Points --> {self.score}')
                time.sleep(1)
                u = input("Press Enter To Roll The Dice : ")
                is_first_turn = False
            else:
                u = input(f"Press Enter To Roll Dice, Current Score => {self.score} , OR Type 0 To Quit : ")
            
            outcome = 0

            if u and u.isdigit() and int(u) == 0:
                print("Don't You Have More Guts To Gamble, You Can Earn More points :)")

                time.sleep(1)

                while True:
                    retry = input("Press 1 To Keep Playing You Have Chances Of Earning More :) or press 0 to quit Your turn : ")

                    if retry and retry.isdigit() :
                        match int(retry):
                            case 0:
                                self.AddScore(cur_score)
                                turn_done = True
                                time.sleep(1)
                                break
                            case 1:
                                outcome = self.RollDice()
                                break       
                        time.sleep(0.5)
            elif not  u:
                outcome = self.RollDice()

            if outcome:
                if outcome == 1:
                    print("You Rolled 1")
                    time.sleep(0.3)
                    print("You Loose :)")
                    turn_done = True
                    time.sleep(2)
                    break 
                else:
                    print(f"Congrats You Rolled {outcome} , Keep Going And You'll Earn More")
                    cur_score += outcome
                    time.sleep(0.5)
                    print(f"Your Score In This Turn Is {cur_score}")
                    print("--------------------------------------------------------------------------------------------------\n")
                    time.sleep(1)

            if turn_done: break




