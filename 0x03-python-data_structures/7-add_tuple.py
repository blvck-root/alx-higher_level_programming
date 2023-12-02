#!/usr/bin/python3
def fill_with_zero(tuple_):
    """Return tuple filled with zeros
    if tuple_ has fewer than 2 elements"""
    if len(tuple_) == 0:
        return (0, 0)
    elif len(tuple_) == 1:
        return (tuple_[0], 0)
    else:
        return tuple_

def add_tuple(tuple_a=(), tuple_b=()):
    a = fill_with_zero(tuple_a)
    b = fill_with_zero(tuple_b)
    return tuple([a[i] + b[i] for i in range(2)])
