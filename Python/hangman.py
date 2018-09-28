x = input("Player 1, what's the word?: ")

blanks = []
for letter in x:
    blanks.append("_")

print("\n" * 50)

print(blanks)
guess = str(input("Player 2, enter a letter: "))


def findMan():
    print("---|")
    print("   o")
    print("   |")
    print("  /|\ ")
    print("   |")
    print("  / \ ")

arr = ["---|", "   o", "   |", "  /|","  /|\\", "   |", "  /","  / \\"]

turns = 7
import sys

while turns > 0:
              
    for i, letter in enumerate(x):
        if letter == guess:
            blanks[i] = guess
            
    
    print(blanks)
    if "_" not in blanks:
        print("you won")
        sys.exit()

    if guess not in x:
        turns -= 1

        if turns == 6:
            print(arr[0])
            print(arr[1])
        if turns == 5:
            print(arr[0])
            print(arr[1])
            print(arr[2])
        if turns == 4:
            print(arr[0])
            print(arr[1])
            print(arr[2])
            print(arr[3])
        if turns == 3:
            print(arr[0])
            print(arr[1])
            print(arr[2])
            print(arr[4])
        if turns == 2:
            print(arr[0])
            print(arr[1])
            print(arr[2])
            print(arr[4])
            print(arr[5])
        if turns == 1:
            print(arr[0])
            print(arr[1])
            print(arr[2])
            print(arr[4])
            print(arr[5])
            print(arr[6])
        if turns == 0:
            print(arr[0])
            print(arr[1])
            print(arr[2])
            print(arr[4])
            print(arr[5])
            print(arr[7])
            print("Game over")

    if turns > 0:
        guess = input("Guess again: ")





