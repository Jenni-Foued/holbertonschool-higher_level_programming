#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
if last_digit == 0:
    msg = "and is 0"
elif last_digit > 5:
    msg = "and is greater than 5"
else:
    msg = "and is less than 6 and not 0"
print("Last digit of", number, "is", last_digit, "{}".format(msg))
