#day 012
#guess the number

from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess < actual_answer:
        print('too low')
        return turns - 1
    elif user_guess > actual_answer:
        print('too high')
        return turns - 1
    else:
        print(f'you got it right! the number is {actual_answer}')


def difficulty():
    level = input("choose the difficulty. type 'easy' or 'hard': ").lower()
    if level == "easy":
       return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print('welcome to the number guessing game')
    print('I am thinking of a number between 1 and 100')
    answer = randint(1,100)
    print(answer)

    turns = difficulty()


    guess = 0
    while guess != answer:
        print(f"you have {turns} remaining to guess the number")
        guess = int(input("make a guess: "))
        turns = check_answer(user_guess=guess, actual_answer=answer, turns=turns)
        if turns == 0:
            print("you are out of guesses, game over")
            return
        elif guess != answer:
            print("guess again")

game()
