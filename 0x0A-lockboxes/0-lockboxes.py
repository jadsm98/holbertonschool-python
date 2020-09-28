#!/usr/bin/python3
"""Module Lockboxes"""


def canUnlockAll(boxes):
    """function that opens boxes"""

    boxesDict = {}
    boxesDict[0] = False
    for i in range(len(boxes) - 1):
        boxesDict[i + 1] = True
    while True:
        change = False
        for i in range(len(boxes)):
            if not boxesDict[i]:
                for key in boxes[i]:
                    if boxesDict[key]:
                        boxesDict[key] = False
                        change = True
        if not change:
            break
    for box, lockStatus in boxesDict.items():
        if lockStatus:
            return False
    return True
