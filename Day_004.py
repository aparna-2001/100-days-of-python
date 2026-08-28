
#day 004
#Rock Paper Scissors

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

random_int_generator_for_player = int(input("What do you choose? "
                                        "Type 0 for Rock, "
                                            "1 for Paper or "
                                            "2 for Scissors.\n"))


if random_int_generator_for_player not in [0, 1, 2]:
    print("Invalid input! Please restart and enter 0, 1, or 2")
else:
    if random_int_generator_for_player == 0:
       print(f"you chose\n{rock}")
    elif random_int_generator_for_player == 1:
       print(f"you chose\n{paper}")
    elif random_int_generator_for_player == 2:
       print(f"you chose\n{scissors}")


    random_int_generator_for_computer = random.randint(0, 2)

    if random_int_generator_for_computer == 0:
       print(f"the computer chose\n{rock}")
    elif random_int_generator_for_computer == 1:
       print(f"the computer chose\n{paper}")
    elif random_int_generator_for_computer == 2:
       print(f"the computer chose\n{scissors}")


    if random_int_generator_for_player == 0 and random_int_generator_for_computer == 0:
      print("draw")
    elif random_int_generator_for_player == 1 and random_int_generator_for_computer == 1:
      print("draw")
    elif random_int_generator_for_player == 2 and random_int_generator_for_computer == 2:
      print("draw")

    elif random_int_generator_for_player == 0 and random_int_generator_for_computer == 1:
      print("paper beats rock\n you lose")
    elif random_int_generator_for_player == 1 and random_int_generator_for_computer == 0:
      print("paper beats rock\n you win")

    elif random_int_generator_for_player == 1 and random_int_generator_for_computer == 2:
      print("scissors beats paper\n you lose")
    elif random_int_generator_for_player == 2 and random_int_generator_for_computer == 1:
      print("scissors beats paper\n you win")

    elif random_int_generator_for_player == 0 and random_int_generator_for_computer == 2:
      print("rock beats scissors\n you win")
    elif random_int_generator_for_player == 2 and random_int_generator_for_computer == 0:
      print("rock beats scissors\n you lose")
