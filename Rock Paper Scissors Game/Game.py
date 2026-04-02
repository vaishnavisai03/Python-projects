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
choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)
else:
    print("you choose wrong number... run the game again and choose between 0 and 2")
    exit()

print("Computer choose: ")
list_of_3 = [rock,paper,scissors]
random_variable = random.randint(0,2)
print(list_of_3[random_variable])
1
if random_variable == choose:
    print("it's a draw")
elif (choose == 0 and random_variable == 1) or (choose == 1 and random_variable == 2) or (choose == 2 and random_variable == 0):
    print("you lose")
else:
    print("you win")
