import re


def max_power(n, k):
    factors = {}
    temp_k = k
    d = 2
    while d * d <= temp_k:
        if temp_k % d == 0:
            count = 0
            while temp_k % d == 0:
                count += 1
                temp_k //= d
            factors[d] = count
        d += 1
    if temp_k > 1:
        factors[temp_k] = 1

    ans = float("inf")
    for p, e in factors.items():
        count_p = 0
        temp_n = n
        while temp_n > 0:
            count_p += temp_n // p
            temp_n //= p
        ans = min(ans, count_p // e)

    return ans


if __name__ == "__main__":
    user_input = input().strip()

    if "max_power" in user_input:
        match = re.search(r"max_power\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip())
            arg2 = int(match.group(2).strip())
            print(max_power(arg1, arg2))
