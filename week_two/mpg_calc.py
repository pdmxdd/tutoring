'''
We want to track our MPG on a very long road trip.
'''

def calculate_mpg():
    miles_drive = int(input("How many miles did you drive"))
    how_much_gas = int(input("How many gallons of gas did that take?"))
    mpg = miles_drive / how_much_gas
    #print("Your MPG is: " + str(mpg))
    return mpg
    

avg_mpg = 0
total_mpg = 0
for i in range(10):
    total_mpg += calculate_mpg()

avg_mpg = total_mpg / 10
print("Your average mpg is:" + str(avg_mpg))
    