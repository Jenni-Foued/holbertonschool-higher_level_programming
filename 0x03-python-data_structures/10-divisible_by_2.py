#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    result_list = []
    if my_list:
        for idx in range(0, len(my_list)):
            result_list.append(False if my_list[idx] % 2 else True)
    return result_list
