def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


if __name__ == "__main__":
    import re
    
    user_input = input().strip()
    
    if "swap" in user_input:
        match = re.search(r"swap\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip()) if match.group(1).strip().isdigit() else float(match.group(1).strip())
            arg2 = int(match.group(2).strip()) if match.group(2).strip().isdigit() else float(match.group(2).strip())
            print(swap(arg1, arg2))
