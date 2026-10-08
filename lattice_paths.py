import re


def count_paths(n, k):
    MOD = 10**9 + 7
    max_steps = n + k

    fact = [1] * (max_steps + 1)
    inv = [1] * (max_steps + 1)
    for i in range(1, max_steps + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    inv[max_steps] = pow(fact[max_steps], MOD - 2, MOD)
    for i in range(max_steps - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD

    def nCr(total, horiz):
        if horiz < 0 or horiz > total:
            return 0
        return fact[total] * inv[horiz] % MOD * inv[total - horiz] % MOD

    total_paths = 0

    for dy in range(n):
        ways = n if dy == 0 else 2 * (n - dy)
        paths = nCr(k + dy, k)
        total_paths = (total_paths + ways * paths) % MOD

    return total_paths


if __name__ == "__main__":
    user_input = input().strip()

    if "count_paths" in user_input:
        match = re.search(r"count_paths\((.*?),\s*(.*?)\)", user_input)
        if match:
            arg1 = int(match.group(1).strip())
            arg2 = int(match.group(2).strip())
            print(count_paths(arg1, arg2))
