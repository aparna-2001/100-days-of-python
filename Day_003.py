
#day 003
#Treasure Island Project

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("you are in a jungle with two paths\n"
                      "would you go 'left' or 'right'?\n") #I could have used .lower()
if left_or_right == "left" or left_or_right == "Left" or left_or_right == "LEFT":
    print("you have reached the river.")
    swim_or_wait = input("you are in front of the river.\nwould you 'swim' or 'wait'?\n")
    if swim_or_wait == "wait" or swim_or_wait == "Wait" or swim_or_wait == "WAIT":
        print("you have reached the door to the treasure")

        door = input(
            "you are in front of the doors in which one of them opens to the treasure.\n"
            " would you choose 'yellow', 'red', 'blue'?\n")
        if door == "yellow" or door == "Yellow" or door == "YELLOW":
            print("you have reached the treasure! yoohooo")
        elif door == "blue" or door == "BLUE" or door == "Blue":
            print("you are eaten by the beast\n GAME OVER")
        elif door == "red" or door == "RED" or door == "Red":
            print("you are burned by fire\n GAME OVER")
        else:
            print("That's the wrong door\n GAME OVER")
    else:
        print("you are eaten by crocodiles\n GAME OVER")
else:
    print("You are eaten by bear\n GAME OVER")
