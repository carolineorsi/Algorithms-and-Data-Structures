class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


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
        node = self.head
        max = node.value

        while node:
            if node.value > max:
                max = node.value
            node = node.next

        return max


    def min(self):
        node = self.head
        min = node.value

        while node:
            if node.value < min:
                min = node.value
            node = node.next

        return min

    def return_node_by_index(self, index):
        count = 0
        node = self.head

        while count < index:
            node = node.next
            count += 1

        return node


    def find_kth_to_last(self, k):
        count = 1
        node = self.head

        while count < k:
            node = node.next
            count += 1

        pointer = self.head

        while node.next:
            node = node.next
            pointer = pointer.next

        return pointer



def remove_node(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        node.value = None

