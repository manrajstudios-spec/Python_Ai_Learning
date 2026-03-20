class Player:

    def __init__(self,name,i_d):
        self.name = name
        self.i_d = i_d
        self.turn_took = 0

    def MyGuess(self):
        while True:
            player_guess = input("Enter Your Guess (R G B Y W) => ")

            if player_guess:
                if not player_guess.isdigit() :
                    if len(player_guess) == 4:
                        self.turn_took += 1
                        return player_guess
                    else:
                        print("Wrong Input")