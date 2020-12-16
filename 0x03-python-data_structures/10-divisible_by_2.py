#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    result_list = []
    if my_list:
        for idx in range(0, len(my_list)):
            if my_list[idx] % 2 == 0:
                result_list.append(True)
            else:
                result_list.append(False)
    return result_list
