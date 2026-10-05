import re


def even_fib_sum(limit):
    a, b = 1, 2
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total


if __name__ == "__main__":
    user_input = input().strip()
    
    if "even_fib_sum" in user_input:
        match = re.search(r"even_fib_sum\((.*?)\)", user_input)
        if match:
            arg = int(match.group(1).strip())
            print(even_fib_sum(arg))
