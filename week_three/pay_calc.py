# Function Definition it takes two parameters
def calc_wages(hours_worked, hourly_rate):
    # declaring a new variable to hold our calculated pay - our plan is to return this after we calculate our pay
    pay = 0
    # calculates our pay by multiplying our two parameters together
    pay = hours_worked * hourly_rate
    # return the newly calculated pay
    return pay


# if this program is being run, run this code!
if __name__ == '__main__':
    # a variable that will hold the return value of our function
    # when we call our function we must send it two arguments!
    two_week_pay = calc_wages(75, 13.50)
    # print out the results of our function
    print("You made ${} over the last two weeks".format(two_week_pay))