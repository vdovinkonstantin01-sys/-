

def meters_to_centimeters(meters):
    res = meters * 100
    return int(res) if isinstance(meters, int) else float(res)


if __name__ == "__main__":
    user_input = input().strip()
    
    if "meters_to_centimeters" in user_input:
        import re
        match = re.search(r"meters_to_centimeters\((.*?)\)", user_input)
        if match:
            arg = match.group(1)
            val = int(arg) if arg.isdigit() else float(arg)
    else:
        val = int(user_input) if user_input.isdigit() else float(user_input)
        
    result = meters_to_centimeters(val)
    print(result)

