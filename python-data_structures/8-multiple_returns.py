#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return (0, None)
    if not sentence:
        return (0, None)
    f_c = sentence[0]
    return (len(sentence), f_c)
