import random
import re


def birthday_probability(people):
    if people > 365:
        return 1.0
    if people <= 1:
        return 0.0
    
    prob_no_match = 1.0
    for i in range(people):
        prob_no_match *= (365 - i) / 365
        
    return 1.0 - prob_no_match


def simulate_birthday(people, trials):
    if people > 365:
        return 1.0
    if people <= 1:
        return 0.0
        
    matches = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            matches += 1
            
    return matches / trials


if __name__ == "__main__":
    user_input = input().strip()
    
    if "birthday_probability" in user_input:
        match = re.search(r"birthday_probability\((.*?)\)", user_input)
        if match:
            arg = int(match.group(1).strip())
            print(birthday_probability(arg))
            
    elif "simulate_birthday" in user_input:
        match = re.search(r"simulate_birthday\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip())
            arg2 = int(match.group(2).strip())
            print(simulate_birthday(arg1, arg2))
    else:
        # Вывод таблицы при прямом запуске без конкретной команды
        for p in range(5, 61, 5):
            exact = birthday_probability(p)
            sim = simulate_birthday(p, 10000)
            print(f"People: {p:2} | Exact: {exact:.6f} | Simulation: {sim:.6f}")
