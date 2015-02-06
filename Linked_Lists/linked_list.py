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


    def __len__(self):
        count = 0
        node = self.head

        while node:
            count += 1
            node = node.next

        return count


    def __contains__(self, value):
        node = self.head

        while node:
            if node.value == value:
                return True
            node = node.next

        return False


    def max(self):
        pass


    def min(self):
        pass


class Node():

    def __init__(self, value):
        self.value = value
        self.next = None