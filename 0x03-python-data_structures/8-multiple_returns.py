#!/usr/bin/python3
def multiple_returns(sentence):
    len_ = len(sentence)
    if (len_ == 0):
        return (0, None)
    else:
        return (len_, sentence[0])
