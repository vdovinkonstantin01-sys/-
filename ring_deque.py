class Deque:
    def __init__(self):
        self._capacity = 4
        self._data = [None] * self._capacity
        self._head = 0
        self._size = 0

    @property
    def capacity(self):
        return self._capacity

    def _resize(self):
        new_cap = self._capacity * 2
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._capacity]
        self._data = new_data
        self._capacity = new_cap
        self._head = 0

    def push_back(self, item):
        if self._size == self._capacity:
            self._resize()
        idx = (self._head + self._size) % self._capacity
        self._data[idx] = item
        self._size += 1

    def push_front(self, item):
        if self._size == self._capacity:
            self._resize()
        self._head = (self._head - 1) % self._capacity
        self._data[self._head] = item
        self._size += 1

    def pop_back(self):
        if self._size == 0:
            raise IndexError("Дек пуст")
        idx = (self._head + self._size - 1) % self._capacity
        val = self._data[idx]
        self._data[idx] = None
        self._size -= 1
        return val

    def pop_front(self):
        if self._size == 0:
            raise IndexError("Дек пуст")
        val = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return val

    def back(self):
        if self._size == 0:
            raise IndexError("Дек пуст")
        return self._data[(self._head + self._size - 1) % self._capacity]

    def front(self):
        if self._size == 0:
            raise IndexError("Дек пуст")
        return self._data[self._head]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size


if __name__ == "__main__":
    pass
    
