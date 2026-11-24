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


def merge_k_sorted(lists):
    pq = PriorityQueue()
    for list_idx, lst in enumerate(lists):
        if lst:
            pq.push((list_idx, 0), lst[0])

    result = []
    while not pq.is_empty():
        list_idx, elem_idx = pq.pop()
        result.append(lists[list_idx][elem_idx])
        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            pq.push((list_idx, next_idx), lists[list_idx][next_idx])

    return result


if __name__ == "__main__":
    pass
