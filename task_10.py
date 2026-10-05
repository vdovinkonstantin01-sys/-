import ast
import re


def index_of_min(values):
    if not values:
        return -1
    return values.index(min(values))


if __name__ == "__main__":
    user_input = input().strip()
    
    if "index_of_min" in user_input:
        match = re.search(r"index_of_min\(\s*(\[.*?\])\s*\)", user_input)
        if match:
            lst = ast.literal_eval(match.group(1))
            print(index_of_min(lst))
