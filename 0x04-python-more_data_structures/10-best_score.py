#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maximum = max(a_dictionary.values())
    result = list(filter(lambda x:x[1] == maximum, a_dictionary.items()))[0]
    return result[0]
