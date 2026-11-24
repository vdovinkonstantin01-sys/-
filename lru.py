class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = {}
        self._head = _Node(None, None)
        self._tail = _Node(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        prev_node = self._tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self._tail
        self._tail.prev = node

    def get(self, key):
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def put(self, key, value):
        if key in self._cache:
            node = self._cache[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if self._capacity <= 0:
                return
            if len(self._cache) >= self._capacity:
                lru = self._head.next
                self._remove(lru)
                del self._cache[lru.key]
            node = _Node(key, value)
            self._cache[key] = node
            self._add_to_tail(node)


if __name__ == "__main__":
    pass
