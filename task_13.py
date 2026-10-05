import re


def multiplication_table(n):
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]


if __name__ == "__main__":
    user_input = input().strip()
    
    if "multiplication_table" in user_input:
        match = re.search(r"multiplication_table\((.*?)\)", user_input)
        if match:
            arg = int(match.group(1).strip())
            print(multiplication_table(arg))
