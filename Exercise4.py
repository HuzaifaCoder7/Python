
#!  Program of Rock, Paper and Scissor
import random as ran

game = ["r","p","s"]

print("You have 5 tries choose between r, p, s")
i = 0
comp = 0
user = 0
while i <= 5:
    choice = ran.choice(game)
    inp = input(f"Enter try {i}: ")
    i = i + 1
    if(inp == choice):
        print("Draw")
        user = user + 1
        comp = comp + 1
    elif(choice=="p" and inp=="s" or inp=="r" and choice=="s" or inp=="p" and choice=="r"):
        user = user + 1
        print("User point")
    elif(choice=="p" and inp=="r" or inp=="s" and choice=="r" or inp=="p" and choice=="s"):
        comp = comp + 1
        print("Computer point")
    else:
        print("Invalid input. Point deducted")
        user = user - 1

print(f"The points of user is : {user}")
print(f"The points of computer is : {comp}")
if(user > comp):
    print("User wins")
elif(comp > user):
    print("Computer wins")
else:
    print("Drawn")