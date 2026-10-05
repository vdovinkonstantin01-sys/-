import ast
import re


def team_weights(weights):
    return sum(weights[::2]), sum(weights[1::2])


if __name__ == "__main__":
    user_input = input().strip()
    
    if "team_weights" in user_input:
        match = re.search(r"team_weights\(\s*(\[.*?\])\s*\)", user_input)
        if match:
            lst = ast.literal_eval(match.group(1))
            print(team_weights(lst))
