import re
from datetime import date


def century_message(name, age, current_year):
    target_year = current_year + (100 - age)
    return f"{name}, тебе исполнится 100 лет в {target_year} году"


if __name__ == "__main__":
    user_input = input().strip()
    
    if "century_message" in user_input:
        match = re.search(r"century_message\([\"'](.*?)[\"'],\s*(\d+),\s*(\d+)\)", user_input)
        if match:
            name_arg = match.group(1)
            age_arg = int(match.group(2))
            year_arg = int(match.group(3))
            print(f"'{century_message(name_arg, age_arg, year_arg)}'")
