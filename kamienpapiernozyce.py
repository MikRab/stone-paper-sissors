import random

listOfChoice = ["paper", "stone", "scissors"]
randomChoice = random.choice(listOfChoice)
gameLength = 3 

print("Hi, welcome to my game of paper stone scissors. Are we playing?")

gameAnswer = input("What do you choose - paper, stone or scissors?: ")


while (gameLength >= 0):
    gameLength = gameLength - 1
    if (gameAnswer == "paper"):
        print('paper is your choose, my choose is :' + str(randomChoice))
    elif (gameAnswer == "stone"):
        print('stone is your choose, my choose is :' + str(randomChoice))
    elif (gameAnswer == "scissors"):
        print('scissors is your choose, my choose is :' + str(randomChoice))
    else:
        print("You can choose only stone, scissors or paper")
        continue
    