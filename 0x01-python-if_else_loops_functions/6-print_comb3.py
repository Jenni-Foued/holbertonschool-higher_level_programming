#!/usr/bin/python3
for first_digit in range(0, 8):
    for second_digit in range(1 + first_digit, 10):
        print("{:d}{:d}".format(first_digit, second_digit), end=", ")
print("{:d}{:d}".format(first_digit + 1, second_digit))
