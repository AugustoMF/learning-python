# Rock papers sicsors game, completely random choices by the pc!

import random

winner = False
pc = random.randint(1,3)

if pc == 1:
    pc = "paper"
elif pc == 2:
    pc = "rock"
else:
    pc = "sisors"

user = input("Choose rock, paper or sisors ")

if pc == "scissors":
    if user.lower() == "rock":
        winner = "user"
    elif user.lower() == "paper":
        winner = "pc"
    elif user.lower() == "scissors":
        winner = "It is a tie"
elif pc == "rock":
    if user.lower() == "rock":
        winner = "It is a tie"
    elif user.lower() == "paper":
        winner = "user"
    elif user.lower() == "scissors":
        winner = "pc"
elif pc == "paper":
    if user.lower() == "rock":
        winner = "pc"
    elif user.lower() == "paper":
        winner = "It is a tie"
    elif user.lower() == "scissors":
        winner = "user"
    
print ("The pc played", pc)

if winner == "pc" or "user":
    print ("The winner is:", winner)
else:
    print (winner)