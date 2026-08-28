#day 005
#PyPassword generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #easy version (letters, symbols, numbers in order)
# password = ""
#
# for char in range(1,nr_letters + 1):
#     random_characters = random.choice(letters)
#     password += random_characters
#
# for symbol in range(1, nr_symbols + 1):
#     random_symbols = random.choice(symbols)
#     password += random_symbols
#
# for number in range(1, nr_numbers + 1):
#     random_numbers = random.choice(numbers)
#     password += random_numbers
#
# print(f"your password is {password}")

#hard version (letters, symbols and numbers are shuffled)
password_list = []

for letter in range(0, nr_letters):
    random_letters = random.choice(letters)
    password_list.append(random_letters)

for symbol in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

for number in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    password_list.append(random_numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is: {password}")
