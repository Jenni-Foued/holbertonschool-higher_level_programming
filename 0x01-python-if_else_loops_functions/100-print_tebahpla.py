#!/usr/bin/python3
checker = 1
for c in range(ord('z'), ord('a') - 1, -1):
    print(chr(c) if checker else chr(c - 32), end="")
    if checker == 1:
        checker = 0
    else:
        checker = 1
