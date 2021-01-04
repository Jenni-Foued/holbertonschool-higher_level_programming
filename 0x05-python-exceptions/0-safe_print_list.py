#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        if x > 0:
            for elm in my_list:
                print("{}".format(elm), end="")
                i += 1
                if i == x:
                    break
            print("")
    except IndexError:
        print("Index out of range")
    return i
