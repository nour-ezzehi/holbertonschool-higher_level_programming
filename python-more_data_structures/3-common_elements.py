#!/usr/bin/python3
def common_elements(set_1, set_2):
    s = set()
    for s1 in set_1:
        for s2 in set_2:
            if s1 == s2:
                s .add(s1)
    return s
