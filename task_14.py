import re


def circle_diameter(radius):
    res = radius * 2
    return int(res) if isinstance(res, (int, float)) and res.is_integer() else res


def sum_range(start, end):
    if start > end:
        return 0
    return (start + end) * (end - start + 1) // 2


if __name__ == "__main__":
    user_input = input().strip()
    
    if "circle_diameter" in user_input:
        match = re.search(r"circle_diameter\((.*?)\)", user_input)
        if match:
            arg = match.group(1).strip()
            val = int(arg) if arg.isdigit() else float(arg)
            print(circle_diameter(val))
            
    elif "sum_range" in user_input:
        match = re.search(r"sum_range\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip())
            arg2 = int(match.group(2).strip())
            print(sum_range(arg1, arg2))
