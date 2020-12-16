#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    res = 0
    if len(sys.argv) > 1:
        for idx in range(1, len(sys.argv)):
            res += int(sys.argv[idx])
    print("{:d}".format(res))
