#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if alphabet == 'e' or alphabet == 'q':
        continue
    print("{:c}".format(alphabet), end="")
