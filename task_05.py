def greet(username):
    return f"Hello, {username}"


if __name__ == "__main__":
    import re
    
    user_input = input().strip()
    
    if "greet" in user_input:
        match = re.search(r"greet\([\"'](.*?)[\"']\)", user_input)
        if match:
            arg = match.group(1)
            print(f"'{greet(arg)}'")
