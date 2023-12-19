#!/usr/bin/python3
class Node:
    """The node class"""
    @property
    def data(self):
        """retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) == Node or value == None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

    def __init__(self, data, next_node=None):
        if type(data) != int or (type(next_node) != Node or next_node != None):
            raise TypeError
        else:
            self.__data = data
            self.__next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        current = self.__head
        prev = self.__head
        while current != None:
            if value < current.data:
                if prev == self.__head:
                    new_node = Node(value, current)
                    self.__head = new_node
                else:
                    new_node = Node(value, current)
                    prev.next_node = new_node
            else:
                prev = current
                current = current.next_node

    def __str__(self):
        if self.__head == None:
            return ""
        else:
            current = self.__head
            string = str("{}".format(current.data))
            current = current.next_node
            while current != None:
                string.append("\n{}".format(current.data))
                current = current.next_node
        return string
