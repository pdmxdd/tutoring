def return_the_number_five():
    return 5


def return_user_number():
    return_number = int(input("What is your favorite number? "))
    return return_number

'''
the_number = return_the_number_five()
print(the_number)
'''
the_number = return_user_number()
print("Your favorite number is " + str(the_number))




