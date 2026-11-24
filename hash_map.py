class HashMap:
    def __init__(self, size=10):
        self._size = size
        self._buckets = [[] for _ in range(size)]
        self._count = 0

    def _index(self, key):
        return hash(key) % self._size

    def put(self, key, value):
        bucket = self._buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._count += 1

    def get(self, key):
        bucket = self._buckets[self._index(key)]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        bucket = self._buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._count -= 1
                return
        raise KeyError(key)

    def contains(self, key):
        bucket = self._buckets[self._index(key)]
        return any(k == key for k, _ in bucket)

    def __len__(self):
        return self._count


if __name__ == "__main__":
    pass
