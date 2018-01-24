'''
This small script shows the basics of for loops, using the range() function, and then looping through a list we created.
'''

for number in range(100):
    print(number)

a_list = [1, 15, 23, -1, 2345, 23.0, 's', 15]

# screen seperator
print("-" * 40)

for thing in a_list:
    print(thing)