# A python file for the Random Game !

import random
n = random.randint(1,20)
flag = False
while flag!=True:
    guess= int(input("Guess your number: "))
    if(guess==n):
        print("You won the game !")
        flag=True
    else:
        print("You were wrong please try again !")
