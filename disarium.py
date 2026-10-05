import re


def is_disarium(n):
    s = str(n)
    return sum(int(digit) ** (i + 1) for i, digit in enumerate(s)) == n


if __name__ == "__main__":
    user_input = input().strip()
    
    if "is_disarium" in user_input:
        match = re.search(r"is_disarium\((.*?)\)", user_input)
        if match:
            arg = int(match.group(1).strip())
            print(is_disarium(arg))
