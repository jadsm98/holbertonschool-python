#!/usr/bin/python3
"""Module Lockboxes"""


def canUnlockAll(boxes):
    """function that opens boxes"""

    unlocked = [0]
    for loop in range(len(boxes)):
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
