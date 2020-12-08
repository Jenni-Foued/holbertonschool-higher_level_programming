#!/usr/bin/env python3
def uppercase(str):
    str1 = ""
    for index in range(0, len(str)):
        if ord(str[index]) > 96 and ord(str[index]) < 128:
            str1 += chr(ord(str[index]) -32)
        else:
            str1 += str[index]
    print(str1)
