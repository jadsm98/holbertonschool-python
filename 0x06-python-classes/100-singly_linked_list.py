#!/usr/bin/python3
"""singly linked"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data"""
        return self.__data

    @property
    def next_node(self):
        """getter for next_node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """setter for data"""
        if not type(value) is int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """setter for next_node"""
        if self.data != value or value != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """single link list"""
    def __init__(self):
        """initializing"""
        self.head = None
        self.nodes = []
        return

    def sorted_insert(self, value):
        """insert node"""
        node = Node(value, self.head)
        self.nodes.append(node)
        self.nodes.sort(key = lambda x: x.data)
        
    def __str__(self):
        result = ""
        for node in self.nodes:
            result += str(node.data) + "\n"
        return result
