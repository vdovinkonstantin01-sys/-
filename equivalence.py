import itertools
import re


def are_equivalent(f, g, n):
    for r in itertools.product([0, 1], repeat=n):
        if f(*r) != g(*r):
            return False
    return True


def implies(a, b):
    return (not a) or b


if __name__ == "__main__":
    def de_morgan_left(a, b): return not (a and b)
    def de_morgan_right(a, b): return (not a) or (not b)
    def wrong(a, b): return (not a) and (not b)
    
    def dm2_left(a, b): return not (a or b)
    def dm2_right(a, b): return (not a) and (not b)
    
    def imp_left(a, b): return implies(a, b)
    def imp_right(a, b): return (not a) or b
    
    def cp_left(a, b): return implies(a, b)
    def cp_right(a, b): return implies(not b, not a)
    
    def dist_left(a, b, c): return a and (b or c)
    def dist_right(a, b, c): return (a and b) or (a and c)

    funcs = {
        "de_morgan_left": de_morgan_left,
        "de_morgan_right": de_morgan_right,
        "wrong": wrong,
        "dm2_left": dm2_left,
        "dm2_right": dm2_right,
        "imp_left": imp_left,
        "imp_right": imp_right,
        "cp_left": cp_left,
        "cp_right": cp_right,
        "dist_left": dist_left,
        "dist_right": dist_right
    }

    user_input = input().strip()
    
    if "are_equivalent" in user_input:
        match = re.search(r"are_equivalent\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*(\d+)\s*\)", user_input)
        if match:
            f_name = match.group(1).strip()
            g_name = match.group(2).strip()
            n_val = int(match.group(3).strip())
            
            f_func = funcs.get(f_name)
            g_func = funcs.get(g_name)
            
            if f_func and g_func:
                print(are_equivalent(f_func, g_func, n_val))

