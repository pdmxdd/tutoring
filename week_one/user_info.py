'''
This small program is practice working with Variables, Data Types (int, float, string), input, and some basic functions (print(), type(), float(), int(), input())

This program also uses 2 things we haven't learned the .format() method, and multiplying strings. Feel free to ignore those for now.

'''

first_name = input("What is your name? ")
last_name = input("What is your last name? ")
age = input("What is your age? ")
wishful_bank_account = input("What do you wish your bank account was? ")

age = int(age)
wishful_bank_account = float(wishful_bank_account)


print("-" * 40)
print("Your first name is {}".format(first_name))
print("First name type: {}".format(type(first_name)))
print("-" * 40)
print("Your last name is {}".format(last_name))
print("Last name type: {}".format(type(last_name)))
print("-" * 40)
print("Your age is {}".format(age))
print("Age type: {}".format(type(age)))
print("-" * 40)
print("You wish your bank account was: {}".format(wishful_bank_account))
print("Bank account type: {}".format(type(wishful_bank_account)))
print("-" * 40)