def compare(m, n):
    if m > n:
        return "Number m > n"
    elif m < n:
        return "Number m < n"
    else:
        return "The numbers are equal"


if __name__ == "__main__":
    import re
    
    user_input = input().strip()
    
    if "compare" in user_input:
        match = re.search(r"compare\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip()) if match.group(1).strip().isdigit() else float(match.group(1).strip())
            arg2 = int(match.group(2).strip()) if match.group(2).strip().isdigit() else float(match.group(2).strip())
            print(f"'{compare(arg1, arg2)}'")
