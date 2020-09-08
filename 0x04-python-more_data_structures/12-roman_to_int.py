#!/usr/bin/python3
roman_dict = {
  "M": 1000,
  "D": 500,
  "C": 100,
  "L": 50,
  "X": 10,
  "V": 5,
  "I": 1
}


def is_smaller(roman1, roman2):
    if roman_dict[roman1] >= roman_dict[roman2]:
        return True
    return False

    
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    total = 0
    for i, val in enumerate(roman_string):
        if i < (len(roman_string) - 1):
            if is_smaller(roman_string[i], roman_string[i + 1]):
                total += roman_dict[val]
            else:
                total -= roman_dict[val]
        else:
            total += roman_dict[val]
        
    return total
    
