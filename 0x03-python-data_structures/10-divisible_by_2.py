#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b = list()
    for j in my_list:
        if j % 2 == 0:
            b.append(True)
        else:
            b.append(False)
    return b
