#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_weighted = sum([t[0] * t[1] for t in my_list if len(t) == 2])
    sum_weights = sum([t[1] for t in my_list if len(t) == 2])
    return 0 if sum_weights == 0 else sum_weighted / sum_weights
