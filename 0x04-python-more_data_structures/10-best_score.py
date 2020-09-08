#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    return max(i for i, pair in a_dictionary.items())
