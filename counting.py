import re


def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def arrangements(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    res = 1
    for i in range(n - k + 1, n + 1):
        res *= i
    return res


def combinations(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    k = min(k, n - k)
    if k == 0:
        return 1
    num = 1
    den = 1
    for i in range(1, k + 1):
        num *= n - i + 1
        den *= i
    return num // den


if __name__ == "__main__":
    user_input = input().strip()
    
    if "factorial" in user_input:
        match = re.search(r"factorial\((.*?)\)", user_input)
        if match:
            arg = int(match.group(1).strip())
            print(factorial(arg))
            
    elif "arrangements" in user_input:
        match = re.search(r"arrangements\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip())
            arg2 = int(match.group(2).strip())
            print(arrangements(arg1, arg2))
            
    elif "combinations" in user_input:
        match = re.search(r"combinations\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip())
            arg2 = int(match.group(2).strip())
            print(combinations(arg1, arg2))
