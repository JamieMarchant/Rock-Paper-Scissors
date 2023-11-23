import random
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

#users make their choice here.
user_input = input("Type 1 for rock, 2 for paper, and 3 for scissors! ")
#each option is contained within this list
options = [rock, paper, scissors]
#This line indexes the input
user_input_index = int(user_input[0]) - 1
#This line links the index to the options list
user_choice = options[user_input_index]
#This line randomly generates 1 option from the options list. This is the computers choice
computer_choice = random.choice(options)
#variable concatenating both choices
final_choice = (user_choice + computer_choice)

if final_choice == rock + rock:
  print(f"{final_choice} You draw!")
if final_choice == rock + paper:
  print(f"{final_choice} You lose!")
if final_choice == rock + scissors:
  print(f"{final_choice} You win!")

if final_choice == paper + rock:
  print(f"{final_choice} You win!")
if final_choice == paper + paper:
  print(f"{final_choice} You draw!")
if final_choice == paper + scissors:
  print(f"{final_choice} You lose!")

if final_choice == scissors + rock:
  print(f"{final_choice} You lose!")
if final_choice == scissors + paper:
  print(f"{final_choice} You win!")
if final_choice == scissors + scissors:
  print(f"{final_choice} You lose!")