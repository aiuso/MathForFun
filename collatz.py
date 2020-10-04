import random
global collatz_list
global count

"""
Collatz Conjecture
Let n equal a positive integer.
    -If the n is even, the next term is: n/2
    -If the n term is odd, the next term is: 3n+1.
After a number of steps you end with 1.
"""


# User input number test
def collatz_input():
    number = int(input('Choose a number: '))
    num = number
    steps = 0
    print(number)
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        steps += 1
        print(number)
    print(f'It took {steps} steps for {num} to each 1.')


# Iterate and add to list...
def collatz(number):

    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1

    if number == 1:
        collatz_list.append(count)
    #need elif time >> threshold
    else:
        print(f'Number {count} took too long to process!')


##### Run Tests

#collatz_input()


count = 1
collatz_list = []


while True:
    collatz(count)
    count += 1
