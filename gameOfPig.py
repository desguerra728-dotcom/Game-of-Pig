'''
PLAYER TURN
while True
    roll
    if roll == 1:
        return 0
    turn_tot += roll
    if p_tot + turn_tot > 100:
        return turn_tot
    if choice == bank:
        return turn_tot
p_tot += turn_tot

COMPUTER TURN
while True
    roll
    if roll == 1:
        return 0
    turn_tot += roll
    if p_tot + turn_tot > 100:
        return turn_tot
    count += 1
    if count == 20:
        return turn_tot
c_tot += turn_tot

'''

import rnadom

def roll():
    return random.randint()

def player_turn(p_tot):
    while True:
        roll = roll()
        if roll = 1:
            return 0
        if 


While True:
    p_tot = player_turn(p_tot)
    