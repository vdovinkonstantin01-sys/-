class PriorityQueue:
    def __init__(self):
        self._items = []

    def push(self, item, priority):
        idx = len(self._items)
        while idx > 0 and self._items[idx - 1][0] <= priority:
            idx -= 1
        self._items.insert(idx, (priority, item))

    def pop(self):
        if not self._items:
            raise IndexError("Очередь пуста")
        return self._items.pop()[1]

    def peek(self):
        if not self._items:
            raise IndexError("Очередь пуста")
        return self._items[-1][1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    pass
