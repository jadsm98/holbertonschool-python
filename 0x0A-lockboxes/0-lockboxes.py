#!/usr/bin/python3
"""Module Lockboxes"""


def canUnlockAll(boxes):
    """function that opens boxes"""

    if not all(type(i) is list for i in boxes) or not type(boxes) is list:
        raise TypeError("boxes must be a list of lists")
    unlocked = [0]
    while True:
        change = False
        for i, box in enumerate(boxes):
            if i in unlocked:
                for key in box:
                    if key not in unlocked:
                        unlocked.append(key)
                        change = True
        if not change or len(unlocked) == len(boxes):
            break
    if len(unlocked) == len(boxes):
        return True
    return False
