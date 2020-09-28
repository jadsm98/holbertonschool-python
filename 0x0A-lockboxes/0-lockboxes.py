#!/usr/bin/python3
"""Module Lockboxes"""


def canUnlockAll(boxes):
    """function that opens boxes"""

    if not all(type(i) is list for i in boxes) \
       and not type(boxes) is list:
        return False
    unlocked = [0]
    for loop in range(len(boxes)): 
        for i, box in enumerate(boxes):
            if i in unlocked:
                for key in box:
                    if key not in unlocked:
                        unlocked.append(key)
    if all(i in unlocked for i in range(len(boxes))):
        return True
    return False
