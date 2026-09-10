#Day_014
#Higher or lower game

# from art import logo, vs
# from game_data import data
import random

# print(logo)

correct_guessing = True
current_score = 0

while correct_guessing:
    def data_fetching(details):
        details_a = random.choice(details)
        details_b = random.choice(details)
        print(f"compare A: {details_a["name"]} , {details_a["description"]} , from {details_a["country"]}")
        # print(vs)
        print(f"against B: {details_b["name"]} , {details_b["description"]} , from {details_b["country"]}")

        def comparison(details_a, details_b):
            if details_a["follower_count"]  > details_b["follower_count"]:
                winner = details_a
                return winner
            else:
                winner = details_b
                return winner

        winner = comparison(details_a, details_b)
        guess = input("who has more followers? type A or B? ").lower()

        def score(guess, details_a, details_b, winner ):
            if (guess == "a" and winner == details_a) or (guess == "b" and winner == details_b):
                global correct_guessing, current_score
                current_score += 1
                print(f"you are right! current score = {current_score}")
            else:
                final_score = current_score
                print(f"you are wrong! final score = {final_score}")
                correct_guessing = False
                return

        score(guess, details_a, details_b, winner)


    # data_fetching(data)
