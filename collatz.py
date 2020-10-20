import random
import time
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
    global most_steps
    prev_num = number - 1
    steps = 0
    while number != 1:

        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = number * 3 + 1

        steps += 1

        if number <= prev_num:
            x = list[number-1][1]
            steps += x
            if steps > list[n-2][1]:
                most_steps = n
            break



    return [n, steps]



##### Run Tests

n = 1
list = []

while True:
    list.append(collatz(n))
    n += 1
