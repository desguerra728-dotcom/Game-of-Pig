import random

def summary(player, turn_tot, p_tot):
    print(player + "'s turn points: " + str(turn_tot))
    print("Points to 100: " + str(100-p_tot-turn_tot) +"\n")

def dice(player):
    roll = random.randint(1,6)
    print("\n" + player + " rolled a " + str(roll))
    return roll

def bank_or_roll():
    choice = random.randint(1,2)
    if choice == 1:
        return True
    else:
        return False

def ask():
    while True:
        choice = input("Bank or Roll?\n0:Bank\n1:Roll\n")
        if choice == "0":
            return True
        elif choice == "1":
            return False
        else:
            print("Enter 0 or 1: \n")


def player_turn(p_tot):
    turn_tot = 0
    isBanking = False
    print("PLAYER TURN:")
    while True:
        roll = dice("Player")
        if roll == 1:
            return 0
        turn_tot += roll
        summary("Player", turn_tot, p_tot)
        if (turn_tot + p_tot) >= 100:
            return turn_tot
        isBanking = ask()
        if isBanking == True:
            return turn_tot

def computer_turn(c_tot):
    turn_tot = 0
    print("COMPUTER TURN:")
    while True:
        roll = dice("Computer")
        if roll == 1:
            return 0
        turn_tot += roll
        summary("Computer", turn_tot, c_tot)
        if ((turn_tot + c_tot) >= 100):
            return turn_tot
        isBanking = bank_or_roll()
        if isBanking == True:
            return turn_tot

p_tot = 0
c_tot = 0
print("Game Of Pig")
while True:
    p_tot += player_turn(p_tot)
    print("Player total points: "+ str(p_tot) + "\n")
    if p_tot >= 100:
        print("Player wins.")
        break
    
    c_tot += computer_turn(c_tot)
    print("Computer total points: "+ str(c_tot) + "\n")
    if c_tot >= 100:
        print("Computer wins.")
        break