from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError
        return self._items[0]

    def size(self):
        return len(self._items)


if __name__ == "__main__":
    pass
