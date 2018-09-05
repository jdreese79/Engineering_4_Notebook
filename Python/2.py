# Automatic Dice Roller
# Written by Jack and Elodie

from random import randint

print ("Automatic Dice Roller")

running = True

while running:
    rolled_num = randint(1,6)
    print("The dice rolled and you got: ", rolled_num)
    userInput = input("Roll again? (Y)es or (N)o")
    if userInput == "N":
        running = False
   
    
