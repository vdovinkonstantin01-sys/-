class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self._items[-1]

    def size(self):
        return len(self._items)


if __name__ == "__main__":
    pass
