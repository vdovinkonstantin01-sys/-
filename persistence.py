import re


def persistence(num):
    steps = 0
    while num >= 10:
        prod = 1
        for digit in str(num):
            prod *= int(digit)
        num = prod
        steps += 1
    return steps


if __name__ == "__main__":
    user_input = input().strip()
    
    if "persistence" in user_input:
        match = re.search(r"persistence\((.*?)\)", user_input)
        if match:
            arg = int(match.group(1).strip())
            print(persistence(arg))
