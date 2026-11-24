class Matrix:
    def __init__(self, rows):
        if not rows or not rows[0]:
            raise ValueError("Матрица не может быть пустой")
        cols = len(rows[0])
        if any(len(row) != cols for row in rows):
            raise ValueError("Строки матрицы должны быть одинаковой длины")
        self._rows = [list(row) for row in rows]

    @property
    def shape(self):
        return (len(self._rows), len(self._rows[0]))

    def __getitem__(self, index):
        i, j = index
        return self._rows[i][j]

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.shape != other.shape:
            raise ValueError("Размеры матриц не совпадают")
        r, c = self.shape
        return Matrix([
            [self._rows[i][j] + other._rows[i][j] for j in range(c)]
            for i in range(r)
        ])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([
                [val * other for val in row]
                for row in self._rows
            ])
        if isinstance(other, Matrix):
            r1, c1 = self.shape
            r2, c2 = other.shape
            if c1 != r2:
                raise ValueError("Несовместимые размеры матриц для умножения")
            return Matrix([
                [
                    sum(self._rows[i][k] * other._rows[k][j] for k in range(c1))
                    for j in range(c2)
                ]
                for i in range(r1)
            ])
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self * other
        return NotImplemented

    def transpose(self):
        r, c = self.shape
        return Matrix([
            [self._rows[i][j] for i in range(r)]
            for j in range(c)
        ])

    @classmethod
    def identity(cls, n):
        if n <= 0:
            raise ValueError("Размер единичной матрицы должен быть положительным")
        return cls([
            [1 if i == j else 0 for j in range(n)]
            for i in range(n)
        ])

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        return self._rows == other._rows

    def __repr__(self):
        return f"Matrix({self._rows!r})"


if __name__ == "__main__":
    pass
