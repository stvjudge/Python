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


moves = rock, paper, scissors

r_move = random.randint(0, 2)

my_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("You move:\n", moves[my_choice])
print("Computer move:\n", moves[r_move])

if (my_choice == 0 and r_move == 1) or (my_choice == 1 and r_move == 2) or (my_choice == 2 and r_move == 0):
    print("You lose!")
elif (my_choice == r_move):
    print("It's a draw!")
else:
    print("You Win!")
