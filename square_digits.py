import re


def square_digits(n):
    return int("".join(str(int(digit) ** 2) for digit in str(n)))


if __name__ == "__main__":
    user_input = input().strip()
    
    if "square_digits" in user_input:
        match = re.search(r"square_digits\((.*?)\)", user_input)
        if match:
            arg = int(match.group(1).strip())
            print(square_digits(arg))
