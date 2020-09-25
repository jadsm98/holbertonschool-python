#!/usr/bin/python3
"""Module Lockboxes"""

def canUnlockAll(boxes):
    """ function to check if all
    boxes in a list are unlocked """

    boxesDict = {}
    boxesDict[0] = False  # unlocked
    for i in range(len(boxes) - 1):
        boxesDict[i + 1] = True  # locked

    while True:
        change = False
        for i, box in enumerate(boxes):
            if not boxesDict[i]:
                for key in box:
                    if boxesDict[key]:
                        boxesDict[key] = False
                        change = True
        if not change:
            break

    for box, lockStatus in boxesDict.items():
        if lockStatus:
            return False
    return True
