import re


def max_of_three(a, b, c):
    return max(a, b, c)


if __name__ == "__main__":
    user_input = input().strip()
    
    if "max_of_three" in user_input:
        match = re.search(r"max_of_three\((.*?),\s*(.*?),\s*(.*?)\)", user_input)
        if match:
            def parse_num(s):
                s = s.strip()
                return int(s) if s.lstrip('-').isdigit() else float(s)
            
            arg1 = parse_num(match.group(1))
            arg2 = parse_num(match.group(2))
            arg3 = parse_num(match.group(3))
            print(max_of_three(arg1, arg2, arg3))
