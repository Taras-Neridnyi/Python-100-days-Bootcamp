import random

kamin = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papir = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

nozytsi = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

varianty_art = [kamin, papir, nozytsi]

try:
    vybir_hratsia = int(input("Your move! (0=Rock, 1=Paper, 2=Scissors):\n"))

    if vybir_hratsia < 0 or vybir_hratsia >= 3:
        print("Invalid number. You lose!")
    else:
        print("\nYou chose:")
        print(varianty_art[vybir_hratsia])

        vybir_kompa = random.randint(0, 2)
        print("Computer chose:")
        print(varianty_art[vybir_kompa])

        if vybir_hratsia == vybir_kompa:
            print("--- It's a Draw! ---")
        elif (vybir_hratsia == 0 and vybir_kompa == 2) or \
                (vybir_hratsia == 1 and vybir_kompa == 0) or \
                (vybir_hratsia == 2 and vybir_kompa == 1):
            print("--- You Win! ---")
        else:
            print("--- You Lose. ---")
except ValueError:
    print("That wasn't a number. You lose!")