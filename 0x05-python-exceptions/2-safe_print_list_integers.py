#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r_counter = 0
    for counter in range(x):
        try:
            print("{:d}".format(my_list[counter]), end="")
        except (TypeError, ValueError):
            continue
        else:
            r_counter += 1
    print()
    return r_counter
