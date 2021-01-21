#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    weight = 0
    for elm in my_list:
        res += elm[0] * elm[1]
        weight += elm[1]
    return res / weight
