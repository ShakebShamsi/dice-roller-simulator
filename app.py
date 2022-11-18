import random

def roll_dice():

    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))

        roll = input("Roll again? (Yes/No): ")
    while roll.lower() == "no".lower():
        print("Good Bye!!!")
        quit()
        
roll_dice()
