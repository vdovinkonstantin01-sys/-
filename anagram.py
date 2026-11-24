def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    counts = {}
    for ch in s1:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in s2:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return True


if __name__ == "__main__":
    pass
