import re


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    user_input = input().strip()
    
    if "is_power_of_two" in user_input:
        match = re.search(r"is_power_of_two\((.*?)\)", user_input)
        if match:
            arg = int(match.group(1).strip())
            print(is_power_of_two(arg))
