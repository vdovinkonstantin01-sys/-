import re


def shortest_distance(kilometers, meters):
    km_to_m = kilometers * 1000
    res = min(km_to_m, meters)
    return int(res) if isinstance(res, (int, float)) and res.is_integer() else res


if __name__ == "__main__":
    user_input = input().strip()
    
    if "shortest_distance" in user_input:
        match = re.search(r"shortest_distance\((.*?),\s*(.*?)\)", user_input)
        if match:
            def parse_num(s):
                s = s.strip()
                return int(s) if s.isdigit() else float(s)
            
            arg1 = parse_num(match.group(1))
            arg2 = parse_num(match.group(2))
            print(shortest_distance(arg1, arg2))
