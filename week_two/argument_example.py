def are_you_paul(a_first_name, a_last_name):
    if a_first_name == 'Paul' and a_last_name == "Matthews":
        print("Welcome Paul")
    else:
        print("YOU ARE NOT PAUL GO AWAY!")




first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
are_you_paul("Paul", "Matthews")