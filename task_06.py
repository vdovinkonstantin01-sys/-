def echo_number(number):
    return f"Thats the number you entered {number}"


if __name__ == "__main__":
    import re
    
    user_input = input().strip()
    
    if "echo_number" in user_input:
        match = re.search(r"echo_number\((.*?)\)", user_input)
        if match:
            arg = match.group(1).strip()
            val = int(arg) if arg.isdigit() else float(arg)
            print(f"'{echo_number(val)}'")
