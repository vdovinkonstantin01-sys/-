import re


def sum_interval(a, b):
    low = min(a, b)
    high = max(a, b)
    return (low + high) * (high - low + 1) // 2


if __name__ == "__main__":
    user_input = input().strip()
    
    if "sum_interval" in user_input:
        match = re.search(r"sum_interval\((.*?),\s*(.*?)\)", user_input)
        if match:
            def parse_num(s):
                s = s.strip()
                return int(s)
            
            arg1 = parse_num(match.group(1))
            arg2 = parse_num(match.group(2))
            print(sum_interval(arg1, arg2))
