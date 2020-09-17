#!/usr/bin/python3
"""
This script contains say_my_name
function
"""


def say_my_name(first_name, last_name=""):
    """ This function takes the first and last name
        as string and prints the full name """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
