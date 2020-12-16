#!/usr/bin/python3


if __name__ == "__main__":
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
else:
    print("{:d} argument:".format(len(sys.argv) - 1) if (len(sys.argv) == 2)
          else "{:d} arguments:".format(len(sys.argv) - 1))
    for idx in range(1, len(sys.argv)):
        print("{:d}: {}".format(idx, sys.argv[idx]))
