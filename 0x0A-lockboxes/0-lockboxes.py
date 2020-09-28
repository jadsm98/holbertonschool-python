#!/usr/bin/python3
"""Module Lockboxes"""


def canUnlockAll(boxes):
    """function that opens boxes"""

    if not all(type(j) is list for j in boxes) and not type(boxes) is list:
        return False
    unlocked = [0]
    while True:
        change = False
        for i, box in enumerate(boxes):
            if i in unlocked:
                for key in box:
                    if key not in unlocked:
                        unlocked.append(key)
                        change = True
        if not change:
            break
    if len(unlocked) == len(boxes):
        return True
    return False
