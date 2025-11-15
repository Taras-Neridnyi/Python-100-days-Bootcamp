print("""

Welcome to Treasure Island.
Your mission is to find the treasure.

""")
print("You're at a cross road. Where do you want to go?")
choice_side = str(input('Type "left" or "right"? '))
if choice_side == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = str(input('Type "wait" to wait for a boat. Type "swim" to swim across. '))
    if choice == "wait":
        print('You arrive at the island unharmed. There is a house with 3 doors.')
        choice = str(input('One red, one yellow and one blue. Which colour do you choose? '))
        if choice == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You don't found the treasure! You Lose!")
    else:
        print("You don't found the treasure! You Lose!")
else:
    print("You don't found the treasure! You lose!")