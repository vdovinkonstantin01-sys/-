import re


def month_calendar(start_weekday, days):
    weeks = []
    current_week = ["  "] * start_weekday
    
    for day in range(1, days + 1):
        current_week.append(f"{day:2}")
        if len(current_week) == 7:
            weeks.append(" ".join(current_week).rstrip())
            current_week = []
            
    if current_week:
        weeks.append(" ".join(current_week).rstrip())
        
    return "\n".join(weeks)


if __name__ == "__main__":
    user_input = input().strip()
    
    if "month_calendar" in user_input:
        match = re.search(r"month_calendar\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip())
            arg2 = int(match.group(2).strip())
            print(month_calendar(arg1, arg2))
