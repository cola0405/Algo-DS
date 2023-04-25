class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = node

        # update tail
        self.tail = node

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def get_tail(self):
        return self.tail.data



linked_lst = LinkedList()
linked_lst.append(1)
linked_lst.append(2)
linked_lst.append(3)
print(linked_lst.get_tail())