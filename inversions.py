def count_inversions(arr):
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst, 0
        mid = len(lst) // 2
        left, inv_left = merge_sort(lst[:mid])
        right, inv_right = merge_sort(lst[mid:])
        merged = []
        i = j = 0
        inversions = inv_left + inv_right
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, total = merge_sort(arr)
    return total


if __name__ == "__main__":
    pass
