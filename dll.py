class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next is not None:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return
            curr = curr.next

    def to_list(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def to_list_reverse(self):
        result = []
        curr = self.tail
        while curr is not None:
            result.append(curr.data)
            curr = curr.prev
        return result


if __name__ == "__main__":
    pass
