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

    def return_list(self):
        node = self.head
        output = []

        while node:
            output.append(node.value)
            node = node.next

        return output




class Node():

    def __init__(self, value):
        self.value = value
        self.next = None