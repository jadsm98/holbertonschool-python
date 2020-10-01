#!/usr/bin/python3
"""module add_item"""


from sys import argv
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file


my_list = argv[1:]
save_to_json_file(my_list, "add_item.json")
load_from_json_file("add_item.json")
