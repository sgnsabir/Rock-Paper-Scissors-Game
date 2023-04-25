rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# while(1):
#     choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#     if(choice>=0 and choice<3):
#         break
#     else:
#         print("Type in between 0 to 2 !\n")

while(1):
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if(choice>2 or choice<0):
        print("You lose! You chose wrong selection.\n")

    else:
        Computer_chose = random.randint(0, 2)

        if(choice == 0):
            print(f"\n{rock}\n")
        elif(choice == 1):
            print(f"\n{paper}\n")
        elif(choice == 2):
            print(f"\n{scissors}\n")
        if(Computer_chose == 0):
            print(f"Computer chose: {Computer_chose}\n{rock}\n")
        elif(Computer_chose == 1):
            print(f"Computer chose: {Computer_chose}\n{paper}\n")
        elif(Computer_chose == 2):
            print(f"Computer chose: {Computer_chose}\n{scissors}\n")
        #rock=0, paper=1, scissors=2
        if((choice == 0 and Computer_chose==2) or (choice == 2 and Computer_chose==1) or (choice == 1 and Computer_chose==0)):
            print("You win!\n")
        elif(choice == Computer_chose):
            print("It's a draw\n")
        else:
            print("You lose\n")
    breaking = (input("Do you want to continue the game? Press 1 "))
    if(breaking != "1"):
        print("You chose to exit the game!")
        break