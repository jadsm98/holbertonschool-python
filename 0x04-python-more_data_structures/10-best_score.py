#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    maximum = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v == maximum:
            return k
