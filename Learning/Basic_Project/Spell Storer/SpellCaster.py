
from enum import Enum
import time
class SpellType(Enum):
    Fire = 1,
    Water = 2,
    Ice = 3,
    Earth = 4,
    Thunder = 5,
    Heal = 6,
    Air = 7


curQueue = []

combo_spells = [{"Spell":"Smoke","Reqs":["Fire","Water"],"Amount":[1,1]} , {"Spell":"Mud","Reqs":["Earth","Water"],"Nums":[1,2]}]


def CheckForCombo():
    cur_spells_dict = {}

    for s in (curQueue):
        cur_spells_dict[s] = cur_spells_dict.get(s,0) +1
    
    print(cur_spells_dict)


def UpdateQueue(spell_name:str):
    curQueue.append(spell_name)
    print(f"Spell Added {spell_name}")

def QueueManager():
    time.sleep(1)
    while True:
        user_input = input("Press 1 = Fire \nPress 2 = Water \nPress 3 = Ice \nPress 4 = Earth \nPress 5 = Thunder \nPress 6 = Heal \nPress 7 = Air \nPress 0 = To Delete Last Added Spell \nPress Enter To Shoot \n")
        
        if not user_input: 
            CheckForCombo()
            break

        for i in range(1,8):
            if str(i) == user_input:
                UpdateQueue(SpellType((i,)).name)
                time.sleep(1)
        

while True:
    user_input = input("Press Enter To Satrt Speel Queue OR Press n To Quit --> \n")

    if not user_input:
        QueueManager()
    elif user_input.lower() == 'n':
        break
