#!/usr/bin/python3
"""Module Lockboxes"""


def canUnlockAll(boxes):
    """ function to check if all
    boxes in a list are unlocked:
    >>>canUnlockAll([[1], [2], [3], [4], []])
    True
    >>>canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
    False
    >>>canUnlockAll(45)
    Traceback (most recent call last):
    TypeError: boxes should be a list of lists
    """


    if not all(type(i) is list for i in boxes) or not type(boxes) is list:
        raise TypeError("boxes should be a list of lists")

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
