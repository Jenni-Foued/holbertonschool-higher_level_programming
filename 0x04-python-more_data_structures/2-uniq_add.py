#!/usr/bin/python3


def uniq_add(my_list=[]):
    res = 0
    if my_list:
        my_list.sort()
        prev = my_list[0]
        res = prev
        for i in my_list:
            if i != prev:
                res += i
                prev = i
    return res
