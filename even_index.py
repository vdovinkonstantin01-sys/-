def find_even_index(numbers):
    left_sum = 0
    right_sum = sum(numbers)
    for i, num in enumerate(numbers):
        right_sum -= num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1


if __name__ == "__main__":
    pass
