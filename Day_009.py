# day 009
#Blind bidding

# from art import logo
# print(logo)


bidding_dict = {}

def find_highest_bidder(bidding_dict):
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a highest bid of {highest_bid}")

continue_bidding = True
while continue_bidding :
    bidder_name = input("What is your name?\n")
    bid_price = int(input("Enter your price?\n"))
    bidding_dict[bidder_name] = bid_price
    new_bidders = input("Are there any other bidders? type 'yes' or 'no'\n").lower()
    if new_bidders == "no":
        continue_bidding = False
        find_highest_bidder(bidding_dict)
    elif new_bidders == "yes":
        print("\n" * 100)

    else:
        print("invalid input")