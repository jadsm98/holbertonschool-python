#!/usr/bin/python3
"""
Script that takes a text and decomposes
it into lines with a new line in between
"""


def text_indentation(text):
    """ Function that takes a text as a string
        and prints it with 2 new lines when
        '.', '?' or ':' appear """

    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = list(text)
    for i in range(len(text)):
        if new_text[i] in ['.', '?', ':']:
            new_text.insert(i + 1, '\n\n')
        if new_text[i - 1] == '\n\n' and new_text[i] == ' ':
            while new_text[i] == ' ':
                new_text.pop(i)
    print(''.join(new_text), end='')
