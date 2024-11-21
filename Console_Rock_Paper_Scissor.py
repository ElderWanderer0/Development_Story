#Basic rock paper scissor game.

import random

ListOfItems = ["rock", "paper", "scissor", "1", "2", "3"]
opList = ["rock", "paper", "scissor"]
opSelector = random.choice(opList)

while True:
    opChoice = str(input("Rock(1), paper(2), scissor(3) ? : "))
    Choice = opChoice.lower()

    if Choice in ListOfItems:
        pass
    else:
        print("Please choose one of them")
        break

    if Choice == '1' or Choice == 'rock':
        print(f"Rock against to {opSelector}")
        if opSelector == ListOfItems[0]:
            print("Again")
            pass
        elif opSelector == ListOfItems[1]:
            print("You lost")
            break
        else:
            print("You win!")
            break
    elif Choice == '2' or Choice == 'paper':
        print(f"Paper against to {opSelector}")
        if opSelector == ListOfItems[0]:
            print("You win!")
            break
        elif opSelector == ListOfItems[1]:
            print("Again")
            pass
        else:
            print("You lost")
            break
    else:
        print(f"Scissor against to {opSelector}")
        if opSelector == ListOfItems[0]:
            print("You lost")
            break
        elif opSelector == ListOfItems[1]:
            print("You win!")
            break
        else:
            print("Again")
            pass
