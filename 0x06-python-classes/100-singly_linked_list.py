#!/usr/bin/python3
"""Template a singly linked list and its node."""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Initialize Node class.
        Args:
            data (int): data attribute of a Node object
            node (:obj: Node, optional): Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            print(value)
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Template of a SinglyLinkedList object"""
    def __init__(self):
        """Initialize SinlgyLinkedList class."""
        self.head = None

    def __repr__(self):
        string = ''
        curr = self.head
        while curr:
            string += str(curr.data) + '\n'
            curr = curr.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Insert new Node into the correct sorted position."""
        new_node = Node(value)
        curr = self.head
        if curr is None:
            self.head = new_node
        elif curr.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            while curr.next_node is not None:
                if curr.next_node.data > value:
                    break
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node
