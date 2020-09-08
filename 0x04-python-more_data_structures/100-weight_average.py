#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    result, denum = 0, 0
    for i in my_list:
        weight = 1
        for j in i:
            weight *= j
        result += weight
        denum += i[1]
    return result/denum
