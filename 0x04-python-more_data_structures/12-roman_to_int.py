#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if not roman_string or type(roman_string) != str:
        return 0
    roman_string = roman_string.upper()
    numerals = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    len_ = len(roman_string)
    i = 0
    while i < len_ - 1:
        reps = 1
        curr, next_ = roman_string[i], roman_string[i + 1]
        if curr not in numerals:
            return 0
        value = numerals[curr]  # value of current block of numerals
        while curr == next_:
            reps += 1
            if reps > 3:  # numerals only repeat thrice
                return 0
            elif curr in 'VLD':  # V, L, and D numerals do not repeat
                return 0
            elif i + reps == len_:
                next_ = None
            else:
                curr, next_ = next_, roman_string[i + reps]
            value += numerals[curr]
        if next_ and numerals[curr] < numerals[next_]:
            # enforce substraction rules of evaluating roman numerals
            if reps > 2 or numerals[next_] / numerals[curr] > 10 or\
              (reps > 1 and next_ in 'VLD') or curr in 'VLD':
                return 0
            value = numerals[next_] - value
            reps += 1
        total += value
        i += reps
    if i == len_ - 1:
        total += numerals.get(roman_string[i], 0)
    return total
