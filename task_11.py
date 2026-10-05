import ast
import re


def guests_by_seat(seats):
    n = len(seats)
    res = [0] * n
    for guest_idx, seat_num in enumerate(seats):
        res[seat_num - 1] = guest_idx + 1
    return res


if __name__ == "__main__":
    user_input = input().strip()
    
    if "guests_by_seat" in user_input:
        match = re.search(r"guests_by_seat\(\s*(\[.*?\])\s*\)", user_input)
        if match:
            lst = ast.literal_eval(match.group(1))
            print(guests_by_seat(lst))
