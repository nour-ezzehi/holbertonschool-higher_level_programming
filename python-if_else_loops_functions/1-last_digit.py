#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of "
if number < 0:
    x = -(-number % 10)
else:
    x = number % 10
if x > 5:
    print(f"{str}{number} is {x} and is greater than 5")
elif x == 0:
    print(f"{str}{number} is {x} and is 0")
else:
    print(f"{str}{number} is {x} and is less than 6 and not 0")
