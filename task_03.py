def is_divisor(a, b):
    if a == 0:
        return False
    return b % a == 0


if __name__ == "__main__":
    import re
    
    user_input = input().strip()
    
    if "is_divisor" in user_input:
        match = re.search(r"is_divisor\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip())
            arg2 = int(match.group(2).strip())
            print(is_divisor(arg1, arg2))
