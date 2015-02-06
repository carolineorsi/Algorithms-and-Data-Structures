class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def remove_node(self, node):



class Node():

    def __init__(self, value):
        self.value = value
        self.next = None