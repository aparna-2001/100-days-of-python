#day 002
#Tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = (tip/100 * bill) + bill
each_to_pay = bill_with_tip/people
print(f"each should pay: {round(each_to_pay, 2)}")
