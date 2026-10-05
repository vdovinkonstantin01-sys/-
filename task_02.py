def bytes_to_kilobytes(value):
    return float(value / 1024)


def kilobytes_to_bytes(value):
    res = value * 1024
    return int(res) if isinstance(value, int) else float(res)


if __name__ == "__main__":
    import re
    
    user_input = input().strip()
    
    if "bytes_to_kilobytes" in user_input:
        match = re.search(r"bytes_to_kilobytes\((.*?)\)", user_input)
        if match:
            arg = match.group(1)
            val = int(arg) if arg.isdigit() else float(arg)
            print(bytes_to_kilobytes(val))
            
    elif "kilobytes_to_bytes" in user_input:
        match = re.search(r"kilobytes_to_bytes\((.*?)\)", user_input)
        if match:
            arg = match.group(1)
            val = int(arg) if arg.isdigit() else float(arg)
            print(kilobytes_to_bytes(val))
