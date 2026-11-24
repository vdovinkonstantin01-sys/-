def quirky_numbers(k):
    base = 10**k
    limit = 10**(2 * k)
    max_s = int((limit - 1) ** 0.5)
    res = []
    for s in range(max_s + 1):
        n = s * s
        left, right = divmod(n, base)
        if left + right == s:
            res.append(f"{n:0{2 * k}d}")
    return res


if __name__ == "__main__":
    pass
