#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    total = 0
    strr = roman_string
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(strr)):
        if i < len(strr) - 1 and roman[strr[i]] < roman[strr[i + 1]]:
            total -= roman[strr[i]]
        else:
            total += roman[strr[i]]
    return total
