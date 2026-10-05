import re


def to_jaden_case(text):
    return " ".join(word[0].upper() + word[1:].lower() if word else "" for word in text.split(" "))


if __name__ == "__main__":
    user_input = input().strip()
    
    if "to_jaden_case" in user_input:
        match = re.search(r"to_jaden_case\([\"'](.*?)[\"']\)", user_input)
        if match:
            arg = match.group(1)
            print(f"'{to_jaden_case(arg)}'")
