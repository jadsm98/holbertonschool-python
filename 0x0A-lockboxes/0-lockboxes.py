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

    boxesDict = {}
    boxesDict[0] = False
    for i in range(len(boxes) - 1):
        boxesDict[i + 1] = True
    unlocked_boxes = []
    while True:
        new_list = [i for i in unlocked_boxes]
        unlocked_boxes = []
        for box, lockStatus in boxesDict.items():
            unlocked_boxes.append(box)
        if new_list == unlocked_boxes:
            break
        for b in unlocked_boxes:
            for k in boxes[b]:
                boxesDict[k] = False
    for box, lockStatus in boxesDict.items():
        if lockStatus:
            return False
    return True
