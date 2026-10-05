import re


def race(v1, v2, g):
    if v1 >= v2:
        return None
    
    total_seconds = (g * 3600) // (v2 - v1)
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return [hours, minutes, seconds]


if __name__ == "__main__":
    user_input = input().strip()
    
    if "race" in user_input:
        match = re.search(r"race\((.*?)\)", user_input)
        if match:
            args = [int(x.strip()) for x in match.group(1).split(",")]
            if len(args) == 3:
                print(race(args[0], args[1], args[2]))
