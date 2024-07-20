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

user_choice=int(input("What is your choice ? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

game_image=[rock,paper,scissors]
if(user_choice>2 or  user_choice<0):
    print("You type invalid number! You Loss")
else:
    print(game_image[user_choice])
    pc_choice = random.randint(0, 2)
    print(f'Computer choice :{pc_choice}')
    print(game_image[pc_choice])
    if(user_choice==0 and pc_choice==2):
        print("You Win")
    elif(user_choice==2 and pc_choice==0):
        print("You Loss")
    elif(user_choice<pc_choice):
        print("You Loss")
    elif(user_choice>pc_choice):
        print("You Win")
    else:
        print("It Draw!")
